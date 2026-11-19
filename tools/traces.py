#!/usr/bin/env python3
"""Trace inventory and lint for a paper workspace. Python standard library only.

Every checkable sentence of the paper carries a `% src:` comment naming its
primary source (a "trace") or a `\\gap{kind}{note}` marker. Four commands read
them, from the workspace root (the working directory):

    traces.py list  [--rev REV] [files...]   every trace and gap, one per line
    traces.py lost  [--rev REV] [files...]   traces and gaps at REV missing now
    traces.py lint  [files...]               anchors, pins, paths, lines, cites
    traces.py stale [files...]               sections changed since their check stamp

Files default to manuscript/main.tex, manuscript/sections/*.tex and
manuscript/figures/*.tex; a directory stands for its *.tex files (not its
subdirectories). With --rev the files are read from that git revision of the
workspace.

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
anchor is free text. It then checks that no path lies under a `never` root, that
each path exists at its pin (`git:` roots are read through one `git ls-tree`
per root, `fixed` roots on disk), that a given line is within the file, that
each commit resolves, that no trace begins `../`, and that each \\cite key is
in refs.bib.

The check stamp is one line, `% checked: <YYYY-MM-DD> <who checked>`. `stale`
compares the file with the version in the commit that last changed that line.

Exit codes: 0 fine; 1 a finding (lint), a lost trace (lost), a stale or
unchecked file (stale); 2 the request or the configuration failed.
"""

import argparse
import collections
import difflib
import glob
import os
import re
import subprocess
import sys

DEFAULTS = ("manuscript/main.tex", "manuscript/sections/*.tex", "manuscript/figures/*.tex")
BIB = "manuscript/refs.bib"
SRC_RE = re.compile(r"(?<!\\)%\s*src(?:\s*\(([^)]*)\))?\s*:(.*)$")
STAMP_RE = re.compile(r"^\s*%\s*checked:\s*(\d{4}-\d{2}-\d{2})")
CITE_RE = re.compile(r"\\(?:cite|citet|citep|citealt|citealp|citeauthor|citeyear|citeyearpar)"
                     r"\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}")
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
        p = subprocess.run(["git", "--no-optional-locks", *args], cwd=cwd, capture_output=True, check=False)
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
            while i + 1 < len(lines) and lines[i + 1].lstrip().startswith("%") \
                    and not SRC_RE.search(lines[i + 1]) and not STAMP_RE.match(lines[i + 1]):
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
            groups.append(code[pos + 1:j])
            pos = j + 1
        if len(groups) == 2:
            out.append((path, code.count("\n", 0, m.start()) + 1, norm(f"{groups[0]}: {groups[1]}")))
    return out


def parse_cites(text):
    code = strip_comments(text)
    return [(code.count("\n", 0, m.start()) + 1, k.strip())
            for m in CITE_RE.finditer(code) for k in m.group(1).split(",") if k.strip()]


def expand_braces(s):
    """`a/{x,y}/b` -> [`a/x/b`, `a/y/b`]; a brace group without a comma is left alone."""
    for m in re.finditer(r"\{([^{}]*)\}", s):
        if "," in m.group(1):
            return [r for alt in m.group(1).split(",")
                    for r in expand_braces(s[:m.start()] + alt + s[m.end():])]
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
        elif any(tok.startswith(r) for r in roots):
            m = PATH_RE.match(tok)
            lines = [int(n) for n in (m.group("a"), m.group("b")) if n]
            out.append(("path", m.group("p"), lines))
        elif (m := COMMIT_RE.match(tok)) and m.group(1) + "/" in roots:
            out.append(("commit", tok, []))
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
        spec = spec.rstrip("/") if specs else spec
        if rev:
            pats = [spec] if spec.endswith(".tex") else [spec + "/*.tex"]
            hits = [n for n in names if any(re.fullmatch(glob_rx(p).pattern, n) for p in pats)]
        else:
            hits = sorted(glob.glob(spec + "/*.tex") if os.path.isdir(spec) else glob.glob(spec))
        if specs and not hits and strict:
            raise Error(f"no such .tex file or directory: {spec}")
        out += [h for h in hits if h not in out]
    if not out and strict:
        raise Error("no .tex files found: run from the workspace root, or name the files")
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
        out[path] = (parse_traces(path, text), parse_gaps(path, text), parse_cites(text))
    return out


# ---------------------------------------------------------------- list, lost

def cmd_list(args):
    data = load(args.files, args.rev)
    n_t = n_g = 0
    for path, (traces, gaps, _) in data.items():
        rows = [(t.line, "src", t.text) for t in traces] + [(g[1], "gap", g[2]) for g in gaps]
        for line, kind, text in sorted(rows):
            print(f"{path}:{line}  {kind}  {text}")
        n_t, n_g = n_t + len(traces), n_g + len(gaps)
    print(f"{n_t} traces, {n_g} gaps in {len(data)} files")
    return 0


def compare(old, new):
    """Match (file, line, text) items old against new: (lost, moved)."""
    by_new = collections.defaultdict(list)
    for f, l, t in new:
        by_new[t].append((f, l))
    lost, moved = [], []
    for f, l, t in sorted(old):
        news = by_new[t]
        same = next((n for n in news if n[0] == f), None)
        if same:
            news.remove(same)
        elif news:
            moved.append((f, l, news.pop(0), t))
        else:
            lost.append((f, l, t))
    return lost, moved


def cmd_lost(args):
    rev = args.rev or "HEAD"
    old, new = load(args.files, rev, strict=False), load(args.files, None, strict=False)
    if not old:
        raise Error(f"no .tex files at revision {rev}")
    items = lambda d, i: [(t.file, t.line, t.text) if i == 0 else t for f, v in d.items() for t in v[i]]
    t_lost, t_moved = compare(items(old, 0), items(new, 0))
    g_lost, g_moved = compare(items(old, 1), items(new, 1))
    short = lambda s: s if len(s) <= 140 else s[:137] + "..."
    for f, l, t in t_lost:
        print(f"lost  {f}:{l}  {short(t)}")
    for f, l, (nf, nl), t in t_moved:
        print(f"moved  {f}:{l} -> {nf}:{nl}  {short(t)}")
    for f, l, t in g_lost:
        print(f"gap closed  {f}:{l}  {short(t)}")
    for f, l, (nf, nl), t in g_moved:
        print(f"gap moved  {f}:{l} -> {nf}:{nl}  {short(t)}")
    print(f"{len(t_lost)} lost, {len(t_moved)} moved, {len(g_lost)} gaps closed, "
          f"{len(g_moved)} gaps moved (against {rev})")
    return 1 if t_lost else 0


# ---------------------------------------------------------------- lint

Root = collections.namedtuple("Root", "name pin policy")


def parse_sources(path="AGENTS.md"):
    if not os.path.exists(path):
        raise Error(f"{path} not found: lint needs its `sources` block (run from the workspace root)")
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
        ok = (len(f) == 3 and f[0].endswith("/") and f[2] in ("cite", "never")
              and (f[1] in ("fixed", "-") or re.fullmatch(r"git:\S+", f[1]))
              and (f[1] != "-" or f[2] == "never") and (f[2] != "cite" or f[1] != "-"))
        if not ok:
            raise Error(f"{path}:{start + i}: cannot parse sources line: {raw.strip()!r}")
        roots.append(Root(*f))
    if not roots:
        raise Error(f"{path}: the `sources` block is empty")
    return roots


def glob_rx(pat):
    return re.compile("".join("[^/]*" if c == "*" else "[^/]" if c == "?" else re.escape(c) for c in pat))


class Pins:
    """Existence and length of a path at its root's pin, with every git call cached."""

    def __init__(self, roots):
        self.roots = {r.name: r for r in roots}
        self._trees = {}

    def _tree(self, root):
        if root.name not in self._trees:
            rc, top = git("rev-parse", "--show-toplevel", cwd=root.name)
            if rc:
                raise Error(f"{root.name} is not a git repository, but its pin is {root.pin}")
            top = os.path.realpath(top.strip())
            prefix = os.path.relpath(os.path.realpath(root.name), top)
            rev = root.pin[4:]
            rc, out = git("ls-tree", "-r", "-z", "--name-only", rev, cwd=top)
            if rc:
                raise Error(f"the pin {rev} does not resolve in {root.name}")
            files = set(out.split("\0")[:-1])
            dirs = {d for f in files for d in _parents(f)}
            self._trees[root.name] = (top, "" if prefix == "." else prefix + "/", files, dirs, rev)
        return self._trees[root.name]

    def matches(self, root, path):
        """Files or directories the path (maybe a glob) names at the pin."""
        if root.pin == "fixed":
            return glob.glob(path)
        _, prefix, files, dirs, _ = self._tree(root)
        inner = (prefix + path[len(root.name):]).rstrip("/")
        if "*" in inner or "?" in inner:
            rx = glob_rx(inner)
            return [n for n in files | dirs if rx.fullmatch(n)]
        return [inner] if inner in files | dirs else []

    def length(self, root, match):
        """Number of lines of a matched file, or None for a directory."""
        if root.pin == "fixed":
            if not os.path.isfile(match):
                return None
            with open(match, "rb") as f:
                data = f.read()
        else:
            top, _, files, _, rev = self._tree(root)
            if match not in files:
                return None
            _, out = git("cat-file", "blob", f"{rev}:{match}", cwd=top)
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


def lint_trace(t, roots, keys, pins):
    if t.body.lstrip(LEAD).startswith("../"):
        yield "parent-path", t.body[:70]
    for kind, tok, lines in (found := anchors(t.body, [r.name for r in roots], keys)):
        if kind == "commit":
            root, hex_ = tok.split("@")
            if not pins.commit_ok(root + "/", hex_):
                yield "unknown-commit", tok
        elif kind == "path":
            root = max((r for r in roots if tok.startswith(r.name)), key=lambda r: len(r.name))
            if root.policy == "never":
                yield "never-root", tok
                continue
            for path in expand_braces(tok):
                hits = pins.matches(root, path)
                if not hits:
                    yield "missing-at-pin", path
                elif lines and len(hits) == 1 and "*" not in path:
                    n = pins.length(root, hits[0])
                    if n is not None and max(lines) > n:
                        yield "line-beyond-end", f"{path}:{max(lines)} (file has {n} lines)"
    if not found:
        yield "no-anchor", t.body[:70]


def cmd_lint(args):
    roots, keys = parse_sources(), read_keys()
    pins, findings = Pins(roots), []
    for path, (traces, _, cites) in load(args.files).items():
        for t in traces:
            findings += [(path, t.line, p, tok) for p, tok in lint_trace(t, roots, keys, pins)]
        findings += [(path, l, "unknown-cite-key", k) for l, k in cites if k not in keys]
    for path, line, problem, tok in sorted(findings, key=lambda f: (f[0], f[1])):
        print(f"{path}:{line}  {problem}  {tok}")
    print(f"{len(findings)} findings")
    return 1 if findings else 0


# ---------------------------------------------------------------- stale

def cmd_stale(args):
    bad = 0
    for path in find_files(args.files):
        lines = read(path).splitlines()
        n = next((i for i, l in enumerate(lines, 1) if STAMP_RE.match(l)), None)
        if n is None:
            print(f"{path}: never checked")
            bad += 1
            continue
        date = STAMP_RE.match(lines[n - 1]).group(1)
        rc, out = git("blame", "--porcelain", "-L", f"{n},{n}", "--", path)
        sha = out.split()[0] if rc == 0 and out else "0" * 40
        if set(sha) == {"0"}:
            print(f"{path}: checked {date}, not yet committed")
            continue
        old_name = re.search(r"^filename (.*)$", out, re.MULTILINE).group(1)
        rc, old = git("show", f"{sha}:{old_name}")
        keep = lambda ls: [l for l in ls if not STAMP_RE.match(l)]
        ops = difflib.SequenceMatcher(None, keep(old.splitlines()), keep(lines), autojunk=False)
        k = sum(max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in ops.get_opcodes() if tag != "equal")
        if k:
            print(f"{path}: STALE: checked {date}, changed since ({k} lines)")
            bad += 1
        else:
            print(f"{path}: checked {date}, unchanged")
    return 1 if bad else 0


# ---------------------------------------------------------------- main

def main(argv=None):
    _CACHE.clear()
    ap = argparse.ArgumentParser(prog="traces.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn, rev in (("list", cmd_list, True), ("lost", cmd_lost, True),
                          ("lint", cmd_lint, False), ("stale", cmd_stale, False)):
        p = sub.add_parser(name)
        p.set_defaults(fn=fn)
        if rev:
            p.add_argument("--rev", help="git revision of the workspace to read")
        p.add_argument("files", nargs="*")
    args = ap.parse_args(argv)
    try:
        return args.fn(args)
    except Error as e:
        print(f"traces.py {args.cmd}: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
