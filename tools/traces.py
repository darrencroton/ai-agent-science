#!/usr/bin/env python3
"""Trace inventory and lint for a paper workspace. Python standard library only.

Every checkable sentence of the paper carries a `% src:` comment naming its
primary source (a "trace") or a `\\gap{kind}{note}` marker. Six commands read
them, from the workspace root (the working directory):

    traces.py list  [--rev REV] [files...]   every trace and gap, one per line, and the gaps counted by kind
    traces.py lost  [--rev REV | --copy DIR] [files...]
                                             traces and gaps at REV, or in the copy DIR, missing now
    traces.py lint  [files...]               anchors, pins, paths, lines, cites
    traces.py stale [files...]               sections changed since their check stamp
    traces.py moved [--from OLD] [--to NEW] ROOT [files...]
                                             traces anchored in files of ROOT that changed
    traces.py sample [--seed S] N [files...] N traces drawn at random, with their TeX

Files default to manuscript/main.tex, manuscript/sections/*.tex and
manuscript/figures/*.tex; a directory stands for its *.tex files (not its
subdirectories). With --rev the files are read from that git revision of the
workspace. `lost --copy DIR` compares instead with a copy of those files kept
at the same paths under DIR, for text a reader was given before it could be
committed. Only the files the copy holds are compared, so a trace that moved
to a file outside the copy is reported lost: copy every file.

A trace is a comment `% src: ...` or `% src (qualifier): ...`, on its own line
or beside a sentence. On its own line it continues over the following comment
lines that are not themselves a `% src` or `% checked:` line. Its identity,
for `lost`, is its whitespace-normalised text, qualifier included.

`lint` needs a fenced block labelled `sources` in AGENTS.md, one line per root:

    <root>/  <git:REV | fixed | ->  <cite | never>  [# comment]

and checks that each trace holds an anchor it can recognise: a path that begins
with a declared root (optionally `:<line>`, `:<a>-<b>`, further `:<line>`
tokens, and globs or `{a,b}` alternatives); a commit `<root>@<hex>`; a key of
manuscript/refs.bib; or the word `search`. Text inside double quotes, backticks
and TeX quotes is never read for anchors, and any token that is not clearly an
anchor is free text. It then checks that no path lies under a `never` root,
that each path exists at its pin (`git:` roots are read through one
`git ls-tree` per root, `fixed` roots on disk), that a given line is within the
file, that each commit resolves, that every path is written plainly (no `.`,
`..` or empty segment), and that each \\cite key is in refs.bib. The `never`
policy is applied to what a trace names, not to what it is written as: each
`{a,b}` alternative is expanded first and judged under its own longest-matching
root, each file a glob matches is judged likewise and must exist at its own
root's pin, a glob that can reach another cited root is refused (write one
anchor per root), and a commit anchor `<root>@<hex>` is judged under its root.

The check stamp is one line, `% checked: <YYYY-MM-DD> <who checked>`. `stale`
compares the file with the version in the commit that last changed that line,
so the stamp line must differ from the one it replaces at every check: a second
check on the same day adds a round, e.g.
`% checked: 2026-11-19 r2 checker (Sonnet)`. A changed file is reported with
that commit, the baseline for its re-check, as is an unchanged one (a changed
`fixed` source still needs one). main.tex and each section file need a stamp
whatever they hold; any other file needs one only when it holds traces or
citations, and is otherwise `no traces` and not counted. A stamp whose line is
not yet committed is reported as such and counts as not clean, since the
section can still change under it; `stale` is a submission gate.

`moved` is for a source that changes under a checked trace, which `stale`
cannot see. ROOT is one declared in AGENTS.md. It takes the files that
`git diff --name-only OLD [NEW]` names in the repository holding ROOT (a
renamed or deleted file under its old path too), and reports every trace with a
path anchor in ROOT that names one of them: exactly, by glob, or as a directory
holding one. OLD defaults to a `git:` root's pin; a `fixed` root needs --from.
NEW defaults to the working tree, so an uncommitted edit counts. A root is
compared only as far as git tracks it: against the working tree, untracked
files are counted, not compared. Commit anchors never move and are not
reported. It narrows attention only: a section whose sources moved still gets
its full check.

Exit codes: 0 fine; 1 a finding (lint), a lost trace (lost), a stale, unchecked
or uncommitted file (stale), a trace anchored in a changed file (moved); 2 the
request, the configuration or git failed.
"""

import argparse
import collections
import difflib
import fnmatch
import glob
import os
import random
import re
import subprocess
import sys

MAIN, SECTIONS = "manuscript/main.tex", "manuscript/sections/"
DEFAULTS = (MAIN, SECTIONS + "*.tex", "manuscript/figures/*.tex")
BIB = "manuscript/refs.bib"
SRC_RE = re.compile(r"(?<!\\)%\s*src(?:\s*\(([^)]*)\))?\s*:(.*)$")
STAMP_RE = re.compile(r"^\s*%\s*checked:\s*(\d{4}-\d{2}-\d{2})")
CITE_RE = re.compile(
    r"\\(?:cite|citet|citep|citealt|citealp|citeauthor|citeyear|citeyearpar)"
    r"\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}"
)
PATH_RE = re.compile(r"^(?P<p>.+?)(?::(?P<a>\d+)(?:[-\u2013]:?(?P<b>\d+))?)?$")
LINE_RE = re.compile(r"^:(\d+)(?:[-\u2013]:?(\d+))?$")
COMMIT_RE = re.compile(r"^([\w./-]+)@([0-9a-f]{7,40})$")
QUOTED_RE = re.compile(r'"[^"]*"|``.*?\'\'|\u201c[^\u201d]*\u201d')
LEAD, TRAIL = "([\"'`\u201c\u2018", ")]\"'`\u201d\u2019.,:;!?"

Trace = collections.namedtuple("Trace", "file line text body")


class Error(Exception):
    """A request or configuration failure; reaches the user as a message, exit 2."""


_CACHE = {}


def git(*args, cwd=None):
    """Run git, caching by arguments; returns (exit code, stdout text)."""
    key = (cwd, args)
    if key not in _CACHE:
        p = subprocess.run(
            ["git", "--no-optional-locks", *args],
            cwd=cwd,
            capture_output=True,
            check=False,
        )
        _CACHE[key] = (p.returncode, p.stdout.decode("utf-8", "replace"))
    return _CACHE[key]


def norm(s):
    return " ".join(s.split())


# ---------------------------------------------------------------- parsing


def strip_comments(text):
    """The text with every comment removed, keeping line numbers."""
    return re.sub(r"(?<!\\)%.*", "", text)


def parse_traces(path, text):
    lines = text.splitlines()
    out, i = [], 0
    while i < len(lines):
        m = SRC_RE.search(lines[i])
        if not m:
            i += 1
            continue
        body, start = m.group(2), i
        if lines[i].lstrip().startswith("%"):
            while (
                i + 1 < len(lines)
                and lines[i + 1].lstrip().startswith("%")
                and not SRC_RE.search(lines[i + 1])
                and not STAMP_RE.match(lines[i + 1])
            ):
                i += 1
                body += " " + lines[i].lstrip().lstrip("%")
        body = norm(body)
        qual = norm(m.group(1) or "")
        out.append(Trace(path, start + 1, (f"({qual}) " if qual else "") + body, body))
        i += 1
    return out


def parse_gaps(path, text):
    """Each \\gap{kind}{note} (nested braces allowed) as (file, line, 'kind: note')."""
    code, out = strip_comments(text), []
    for m in re.finditer(r"\\gap(?=\s*\{)", code):
        groups, pos = [], m.end()
        for _ in range(2):
            while pos < len(code) and code[pos].isspace():
                pos += 1
            if pos >= len(code) or code[pos] != "{":
                break
            depth, j = 0, pos
            while j < len(code):
                if code[j] == "\\":
                    j += 1
                elif code[j] == "{":
                    depth += 1
                elif code[j] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            groups.append(code[pos + 1 : j])
            pos = j + 1
        if len(groups) == 2:
            out.append(
                (
                    path,
                    code.count("\n", 0, m.start()) + 1,
                    norm(f"{groups[0]}: {groups[1]}"),
                )
            )
    return out


def parse_cites(text):
    code = strip_comments(text)
    return [
        (code.count("\n", 0, m.start()) + 1, k.strip())
        for m in CITE_RE.finditer(code)
        for k in m.group(1).split(",")
        if k.strip()
    ]


def expand_braces(s):
    """`a/{x,y}/b` -> [`a/x/b`, `a/y/b`]; a brace group without a comma is left alone."""
    for m in re.finditer(r"\{([^{}]*)\}", s):
        if "," in m.group(1):
            return [
                r
                for alt in m.group(1).split(",")
                for r in expand_braces(s[: m.start()] + alt + s[m.end() :])
            ]
    return [s]


def anchors(body, roots, keys):
    """Recognised anchors of a trace body as (kind, token, lines) tuples.

    Kinds are path (lines: the line numbers given), commit, key and search.
    Everything else is free text."""
    body = QUOTED_RE.sub(" ", body)
    body = re.sub(r"\{[^{}]*\}", lambda m: m.group(0).replace(",", "\0"), body)
    out = []
    for raw in re.split(r"[\s;,]+", body):
        if not raw:
            continue
        tok = raw.replace("\0", ",").lstrip(LEAD).split("(")[0].rstrip(TRAIL)
        m = LINE_RE.match(tok)
        if m and out and out[-1][0] == "path":
            out[-1][2].extend(int(n) for n in m.groups() if n)
        elif (m := COMMIT_RE.match(tok)) and m.group(1) + "/" in roots:
            out.append(("commit", tok, []))
        elif any(tok.startswith(r) for r in roots):
            m = PATH_RE.match(tok)
            lines = [int(n) for n in (m.group("a"), m.group("b")) if n]
            out.append(("path", m.group("p"), lines))
        elif tok in keys:
            out.append(("key", tok, []))
        elif tok == "search":
            out.append(("search", tok, []))
    return out


# ---------------------------------------------------------------- files


def tree_at(rev):
    rc, out = git("ls-tree", "-r", "-z", "--name-only", rev)
    if rc:
        raise Error(f"cannot read revision {rev} of the workspace repository")
    return sorted(out.split("\0")[:-1])


def find_files(specs, rev=None, strict=True):
    """The .tex files named by `specs` (the defaults if none), now or at `rev`."""
    names = tree_at(rev) if rev else None
    out = []
    for spec in specs or DEFAULTS:
        spec = spec.rstrip("/")
        if rev:
            rx = glob_rx(spec if spec.endswith(".tex") else spec + "/*.tex")
            hits = [n for n in names if rx.fullmatch(n)]
        else:
            hits = sorted(
                glob.glob(spec + "/*.tex") if os.path.isdir(spec) else glob.glob(spec)
            )
        if specs and not hits and strict:
            raise Error(f"no such .tex file or directory: {spec}")
        out += [h for h in hits if h not in out]
    if not out and strict:
        raise Error(
            "no .tex files found: run from the workspace root, or name the files"
        )
    return out


def read(path, rev=None):
    if rev:
        rc, text = git("show", f"{rev}:./{path}")
        if rc:
            raise Error(f"{path} is not in revision {rev}")
        return text
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def load(specs, rev=None, strict=True):
    """{file: (traces, gaps, cites)} for the named files."""
    out = {}
    for path in find_files(specs, rev, strict):
        text = read(path, rev)
        out[path] = (
            parse_traces(path, text),
            parse_gaps(path, text),
            parse_cites(text),
        )
    return out


# ---------------------------------------------------------------- list, lost


def cmd_list(args):
    data = load(args.files, args.rev)
    n_t, n_g, kinds = 0, 0, collections.Counter()
    for path, (traces, gaps, _) in data.items():
        rows = [(t.line, "src", t.text) for t in traces] + [
            (g[1], "gap", g[2]) for g in gaps
        ]
        for line, kind, text in sorted(rows):
            print(f"{path}:{line}  {kind}  {text}")
        n_t, n_g = n_t + len(traces), n_g + len(gaps)
        kinds.update(g[2].split(":")[0] for g in gaps)
    if kinds:
        print(
            "gaps by kind: " + ", ".join(f"{k} {n}" for k, n in sorted(kinds.items()))
        )
    print(f"{n_t} traces, {n_g} gaps in {len(data)} files")
    return 0


def compare(old, new):
    """Match (file, line, text) items old against new: (lost, moved).

    Same-file matches come first, so a copy of a text left in place is never
    reported moved or lost because another copy elsewhere went."""
    pool = collections.defaultdict(list)
    for f, l, t in sorted(new):
        pool[t].append((f, l))
    rest, lost, moved = [], [], []
    for f, l, t in sorted(old):
        same = next((n for n in pool[t] if n[0] == f), None)
        if same:
            pool[t].remove(same)
        else:
            rest.append((f, l, t))
    for f, l, t in rest:
        if pool[t]:
            moved.append((f, l, pool[t].pop(0), t))
        else:
            lost.append((f, l, t))
    return lost, moved


def load_copy(specs, base):
    """`load` on the copy of the workspace's files kept under the directory `base`."""
    if not os.path.isdir(base):
        raise Error(f"no such directory: {base}")
    here = os.getcwd()
    os.chdir(base)
    try:
        return load(specs, None, strict=False)
    finally:
        os.chdir(here)


def cmd_lost(args):
    if args.rev and args.copy:
        raise Error("give --rev or --copy, not both")
    if args.copy:
        # Only the files the copy holds: an identical trace in a file it lacks
        # must not make a deleted one look moved.
        rev, old = f"the copy {args.copy}", load_copy(args.files, args.copy)
        new = load(sorted(old), None, strict=False) if old else {}
    else:
        rev = args.rev or "HEAD"
        old = load(args.files, rev, strict=False)
        new = load(args.files, None, strict=False)
    if not old:
        raise Error(f"no .tex files at {rev}")
    traces = lambda d: [(t.file, t.line, t.text) for v in d.values() for t in v[0]]
    gaps = lambda d: [g for v in d.values() for g in v[1]]
    t_lost, t_moved = compare(traces(old), traces(new))
    g_lost, g_moved = compare(gaps(old), gaps(new))
    short = lambda s: s if len(s) <= 140 else s[:137] + "..."
    for f, l, t in t_lost:
        print(f"lost  {f}:{l}  {short(t)}")
    for f, l, (nf, nl), t in t_moved:
        print(f"moved  {f}:{l} -> {nf}:{nl}  {short(t)}")
    for f, l, t in g_lost:
        print(f"gap closed  {f}:{l}  {short(t)}")
    for f, l, (nf, nl), t in g_moved:
        print(f"gap moved  {f}:{l} -> {nf}:{nl}  {short(t)}")
    print(
        f"{len(t_lost)} lost, {len(t_moved)} moved, {len(g_lost)} gaps closed, "
        f"{len(g_moved)} gaps moved (against {rev})"
    )
    return 1 if t_lost else 0


# ---------------------------------------------------------------- lint

Root = collections.namedtuple("Root", "name pin policy")


def parse_sources(path="AGENTS.md"):
    if not os.path.exists(path):
        raise Error(
            f"{path} not found: lint needs its `sources` block (run from the workspace root)"
        )
    text = read(path)
    m = re.search(r"^```sources[ \t]*\n(.*?)^```", text, re.MULTILINE | re.DOTALL)
    if not m:
        raise Error(f"{path} has no fenced block labelled `sources`")
    start = text.count("\n", 0, m.start(1)) + 1
    roots = []
    for i, raw in enumerate(m.group(1).splitlines()):
        line = re.sub(r"(^|\s)#.*", "", raw).strip()
        if not line:
            continue
        f = line.split()
        ok = (
            len(f) == 3
            and f[0].endswith("/")
            and f[2] in ("cite", "never")
            and (f[1] in ("fixed", "-") or re.fullmatch(r"git:\S+", f[1]))
            and (f[1] != "-" or f[2] == "never")
        )
        if not ok:
            raise Error(
                f"{path}:{start + i}: cannot parse sources line: {raw.strip()!r}"
            )
        roots.append(Root(*f))
    if not roots:
        raise Error(f"{path}: the `sources` block is empty")
    return roots


def glob_rx(pat):
    return re.compile(
        "".join(
            "[^/]*" if c == "*" else "[^/]" if c == "?" else re.escape(c) for c in pat
        )
    )


def repo_of(name):
    """(top level, the root's path within it as '' or 'dir/') of the git repository
    holding the directory `name`, or None if it is in none."""
    if not os.path.isdir(name):
        return None
    rc, top = git("rev-parse", "--show-toplevel", cwd=name)
    if rc:
        return None
    top = os.path.realpath(top.strip())
    prefix = os.path.relpath(os.path.realpath(name), top)
    return top, "" if prefix == "." else prefix + "/"


class Pins:
    """Existence and length of a path at its root's pin, with every git call cached."""

    def __init__(self):
        self._trees = {}

    def _tree(self, root):
        if root.name not in self._trees:
            if not (repo := repo_of(root.name)):
                raise Error(
                    f"{root.name} is not a git repository, but its pin is {root.pin}"
                )
            top, prefix = repo
            rev = root.pin[4:]
            rc, out = git("ls-tree", "-r", "-z", "--name-only", rev, cwd=top)
            if rc:
                raise Error(f"the pin {rev} does not resolve in {root.name}")
            files = set(out.split("\0")[:-1])
            dirs = {d for f in files for d in _parents(f)}
            self._trees[root.name] = (top, prefix, files, dirs, rev)
        return self._trees[root.name]

    def matches(self, root, path):
        """Files or directories the path (maybe a glob) names at the pin, as workspace paths."""
        if root.pin == "fixed":
            return glob.glob(path)
        _, prefix, files, dirs, _ = self._tree(root)
        inner = (prefix + path[len(root.name) :]).rstrip("/")
        if "*" in inner or "?" in inner:
            rx = glob_rx(inner)
            return [
                root.name + n[len(prefix) :] for n in files | dirs if rx.fullmatch(n)
            ]
        return [path.rstrip("/")] if inner in files | dirs else []

    def length(self, root, match):
        """Number of lines of a matched file, or None for a directory."""
        if root.pin == "fixed":
            if not os.path.isfile(match):
                return None
            with open(match, "rb") as f:
                data = f.read()
        else:
            top, prefix, files, _, rev = self._tree(root)
            inner = prefix + match[len(root.name) :]
            if inner not in files:
                return None
            _, out = git("cat-file", "blob", f"{rev}:{inner}", cwd=top)
            data = out.encode()
        return data.count(b"\n") + (0 if data.endswith(b"\n") or not data else 1)

    def commit_ok(self, root_name, hex_):
        return git("cat-file", "-e", f"{hex_}^{{commit}}", cwd=root_name)[0] == 0


def _parents(path):
    while "/" in path:
        path = path.rsplit("/", 1)[0]
        yield path


def read_keys():
    if not os.path.exists(BIB):
        return set()
    return set(re.findall(r"^\s*@\w+\s*\{\s*([^,\s]+)\s*,", read(BIB), re.MULTILINE))


def root_of(path, roots):
    """The declared root with the longest name that `path` lies under, or None."""
    p = path.rstrip("/") + "/"
    return max(
        (r for r in roots if p.startswith(r.name)),
        key=lambda r: len(r.name),
        default=None,
    )


def spans_roots(path, root, roots):
    """Whether a glob under `root` can reach another cited root (any pin, any repository)."""
    if not any(c in path for c in "*?["):
        return False
    segs = path.rstrip("/").split("/")
    for r in roots:
        cs = r.name.rstrip("/").split("/")
        if (
            r is not root
            and r.name.startswith(root.name)
            and r.policy != "never"
            and len(segs) >= len(cs)
            and all(fnmatch.fnmatchcase(c, p) for p, c in zip(segs, cs))
        ):
            return True
    return False


def plain(path):
    """Whether a path has no `.`, `..` or empty segment (a trailing slash is allowed)."""
    return os.path.normpath(path) == path.rstrip("/") and not path.startswith("..")


def lint_commit(tok, roots, pins):
    """Findings for one commit anchor `<root>@<hex>`."""
    root, hex_ = tok.split("@")
    if not plain(root):
        yield "unplain-path", tok
    elif root_of(root, roots).policy == "never":
        yield "never-root", tok
    elif not pins.commit_ok(root + "/", hex_):
        yield "unknown-commit", tok


def lint_path(path, lines, roots, pins):
    """Findings for one expanded path anchor and the line numbers given for it."""
    root = root_of(path, roots)
    if ".." in path.split("/"):
        yield "parent-path", path
    elif not plain(path):
        yield "unplain-path", path
    elif root.policy == "never":
        yield "never-root", path
    elif spans_roots(path, root, roots):
        yield "glob-spans-roots", path
    elif not (hits := pins.matches(root, path)):
        yield "missing-at-pin", path
    else:
        forbidden = False
        for h in hits:
            own = root_of(h, roots)
            if own.policy == "never":
                forbidden = True
                yield "never-root", h
            elif own is not root and not pins.matches(own, h):
                yield "missing-at-pin", h
        if lines and len(hits) == 1 and not forbidden:
            n = pins.length(root_of(hits[0], roots), hits[0])
            if n is not None and max(lines) > n:
                yield (
                    "line-beyond-end",
                    f"{path}:{max(lines)} (file has {n} lines)",
                )


def lint_trace(t, roots, keys, pins):
    if t.body.lstrip(LEAD).startswith("../"):
        yield "parent-path", t.body[:70]
    for kind, tok, lines in (found := anchors(t.body, [r.name for r in roots], keys)):
        if kind == "commit":
            yield from lint_commit(tok, roots, pins)
        elif kind == "path":
            for path in expand_braces(tok):
                yield from lint_path(path, lines, roots, pins)
    if not found:
        yield "no-anchor", t.body[:70]


def cmd_lint(args):
    roots, keys = parse_sources(), read_keys()
    pins, findings = Pins(), []
    for path, (traces, _, cites) in load(args.files).items():
        for t in traces:
            findings += [
                (path, t.line, p, tok) for p, tok in lint_trace(t, roots, keys, pins)
            ]
        findings += [
            (path, l, "unknown-cite-key", k) for l, k in cites if k not in keys
        ]
    for path, line, problem, tok in sorted(findings, key=lambda f: (f[0], f[1])):
        print(f"{path}:{line}  {problem}  {tok}")
    print(f"{len(findings)} findings")
    return 1 if findings else 0


# ---------------------------------------------------------------- stale


def stamp_origin(path, n):
    """(commit, the file's name in it) that last changed line `n` of `path`, or None
    if the file is not in HEAD or the line is not yet committed."""
    # Blame can date the stamp line only for a file that is in HEAD.
    in_head = git("cat-file", "-e", f"HEAD:./{path}")[0] == 0
    if not in_head:
        return None
    rc, out = git("blame", "--porcelain", "-L", f"{n},{n}", "--", path)
    if rc:
        raise Error(f"git blame failed for {path}")
    sha = out.split()[0]
    if set(sha) == {"0"}:
        return None
    return sha, re.search(r"^filename (.*)$", out, re.MULTILINE).group(1)


def lines_changed_since(sha, old_name, lines):
    """How many lines of `lines` differ from the file as it was in commit `sha`,
    not counting stamp lines."""
    rc, old = git("show", f"{sha}:{old_name}")
    if rc:
        raise Error(f"git show {sha}:{old_name} failed")
    keep = lambda ls: [l for l in ls if not STAMP_RE.match(l)]
    ops = difflib.SequenceMatcher(
        None, keep(old.splitlines()), keep(lines), autojunk=False
    )
    return sum(
        max(i2 - i1, j2 - j1)
        for tag, i1, i2, j1, j2 in ops.get_opcodes()
        if tag != "equal"
    )


def cmd_stale(args):
    if git("rev-parse", "--git-dir")[0]:
        raise Error("git failed: is this a git repository?")
    bad = 0
    for path in find_files(args.files):
        text = read(path)
        lines = text.splitlines()
        n = next((i for i, l in enumerate(lines, 1) if STAMP_RE.match(l)), None)
        if n is None:
            p = os.path.normpath(path)
            if (
                p == MAIN
                or p.startswith(SECTIONS)
                or parse_traces(path, text)
                or parse_cites(text)
            ):
                print(f"{path}: never checked")
                bad += 1
            else:
                print(f"{path}: no traces")
            continue
        date = STAMP_RE.match(lines[n - 1]).group(1)
        if not (origin := stamp_origin(path, n)):
            print(f"{path}: checked {date}, not yet committed")
            bad += 1
            continue
        sha, old_name = origin
        if k := lines_changed_since(sha, old_name, lines):
            print(f"{path}: STALE: checked {date}, changed since {sha[:8]} ({k} lines)")
            bad += 1
        else:
            print(f"{path}: checked {date}, unchanged since {sha[:8]}")
    return 1 if bad else 0


# ---------------------------------------------------------------- moved


def fnmatch_segments(name, pat):
    """Whether `name` matches the glob `pat` with no `*` or `?` reaching across a `/`."""
    ns, ps = name.split("/"), pat.split("/")
    # No zip(strict=): the lengths are equal by the first test, and strict= needs Python 3.10.
    return len(ns) == len(ps) and all(fnmatch.fnmatchcase(n, p) for n, p in zip(ns, ps))  # noqa: B905


def anchors_changed(t, root, roots, keys, changed):
    """Whether trace `t` has a path anchor in `root` naming a changed file, a glob matching
    one, or a directory holding one. `changed` holds files and their parent directories."""
    paths = [
        tok
        for kind, tok, _ in anchors(t.body, [r.name for r in roots], keys)
        if kind == "path"
    ]
    for path in (p for tok in paths for p in expand_braces(tok)):
        if root_of(path, roots) == root:
            rx, pat = glob_rx(path.rstrip("/")), path.rstrip("/")
            if any(
                rx.fullmatch(n) or (root.pin == "fixed" and fnmatch_segments(n, pat))
                for n in changed
            ):
                return True
    return False


def changed_names(top, prefix, old, new):
    """Paths, relative to repository `top`, that differ under `prefix` between
    revision `old` and `new` (None: the working tree); None if git fails."""
    rc, out = git(
        "--literal-pathspecs",
        "diff",
        "--name-only",
        "--no-renames",
        "-z",
        old,
        *([new] if new else []),
        "--",
        prefix or ".",
        cwd=top,
    )
    return None if rc else out.split("\0")[:-1]


def untracked_count(top, prefix):
    """Number of untracked files under `prefix` in repo `top`; None if git fails."""
    rc, out = git(
        "--literal-pathspecs",
        "ls-files",
        "--others",
        "-z",
        "--",
        prefix or ".",
        cwd=top,
    )
    return None if rc else len(out.split("\0")[:-1])


def cmd_moved(args):
    roots, keys = parse_sources(), read_keys()
    name = args.root.rstrip("/") + "/"
    root = next((r for r in roots if r.name == name), None)
    if not root:
        raise Error(
            f"{name} is not a root declared in the `sources` block of AGENTS.md"
        )
    if root.pin == "-":
        raise Error(f"{name} is a `-` root: nothing may cite it")
    old = args.old or (root.pin[4:] if root.pin != "fixed" else None)
    if not old:
        raise Error(
            f"{name} is `fixed`: say which revision to compare from with --from"
        )
    if old.startswith("-") or (args.to or "").startswith("-"):
        raise Error("a revision may not begin with '-'")
    if not (repo := repo_of(name)):
        raise Error(f"{name} is missing or not in a git repository")
    top, prefix = repo
    span = f"{old}..{args.to}" if args.to else f"{old}..working tree"
    if (names := changed_names(top, prefix, old, args.to)) is None:
        which = f"do {old} and {args.to}" if args.to else f"does {old}"
        raise Error(
            f"git diff {span} failed in {name}: "
            f"{which} exist in the repository holding it?"
        )
    files = sorted(name + f[len(prefix) :] for f in names)
    changed = {n for f in files for n in (f, *_parents(f))}
    hits = [
        t
        for v in load(args.files).values()
        for t in v[0]
        if anchors_changed(t, root, roots, keys, changed)
    ]
    untracked = ""
    if not args.to:
        if (k := untracked_count(top, prefix)) is None:
            raise Error(
                f"git ls-files failed in {name}: the untracked files were not scanned"
            )
        if k:
            untracked = f"; {k} untracked files not compared"
    for t in hits:
        print(f"{t.file}:{t.line}  src  {t.text}")
    print(
        f"{len(hits)} traces anchor in {len(files)} changed files of {name} ({span}){untracked}"
    )
    return 1 if hits else 0


# ---------------------------------------------------------------- sample


def cmd_sample(args):
    """An audit sheet: traces chosen by the tool, not the agent, each with the
    TeX it stands in (its own lines and the next few), so that the author can
    read each beside its source. The seed is printed so that a sheet can be
    drawn again."""
    if args.n < 1:
        raise Error("N must be at least 1")
    data = load(args.files)
    pool = [t for traces_, _, _ in data.values() for t in traces_]
    seed = (
        args.seed if args.seed is not None else random.SystemRandom().randrange(10**6)
    )
    chosen = sorted(random.Random(seed).sample(pool, min(args.n, len(pool))))
    lines = {path: read(path).splitlines() for path in {t.file for t in chosen}}
    for k, t in enumerate(chosen, 1):
        print(f"[{k}] {t.file}:{t.line}  {t.text}")
        for i in range(t.line - 1, min(t.line + 4, len(lines[t.file]))):
            print(f"    {i + 1:>5}  {lines[t.file][i]}")
    print(f"{len(chosen)} of {len(pool)} traces, seed {seed}")
    return 0


# ---------------------------------------------------------------- main


def main(argv=None):
    _CACHE.clear()
    summary, spec = __doc__.split("\n\n", 1)
    ap = argparse.ArgumentParser(
        prog="traces.py",
        description=summary,
        epilog=spec,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn, rev in (
        ("list", cmd_list, True),
        ("lost", cmd_lost, True),
        ("lint", cmd_lint, False),
        ("stale", cmd_stale, False),
    ):
        p = sub.add_parser(name)
        p.set_defaults(fn=fn)
        if rev:
            p.add_argument("--rev", help="git revision of the workspace to read")
        if name == "lost":
            p.add_argument(
                "--copy", help="a directory holding a copy of the files to compare with"
            )
        p.add_argument("files", nargs="*")
    p = sub.add_parser("moved")
    p.set_defaults(fn=cmd_moved)
    p.add_argument("root", help="a root declared in AGENTS.md")
    p.add_argument(
        "--from", dest="old", help="revision to compare from (default: the root's pin)"
    )
    p.add_argument("--to", help="revision to compare to (default: the working tree)")
    p.add_argument("files", nargs="*")
    p = sub.add_parser("sample")
    p.set_defaults(fn=cmd_sample)
    p.add_argument("n", type=int, help="how many traces to draw")
    p.add_argument("--seed", type=int, help="draw the same sheet again")
    p.add_argument("files", nargs="*")
    args = ap.parse_args(argv)
    try:
        return args.fn(args)
    except Error as e:
        print(f"traces.py {args.cmd}: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
