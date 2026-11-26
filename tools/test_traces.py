"""Unit tests for traces.py, on small made-up workspaces in temporary directories.

Run from the repository root:

    python3 -m unittest discover -s tools -p 'test_*.py'
"""

import contextlib
import io
import os
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import traces

GIT_ENV = {
    "GIT_AUTHOR_NAME": "t",
    "GIT_AUTHOR_EMAIL": "t@example.org",
    "GIT_COMMITTER_NAME": "t",
    "GIT_COMMITTER_EMAIL": "t@example.org",
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_NOSYSTEM": "1",
}

SOURCES = """# Workspace

```sources
code/               git:v1     cite
code/docs/dev/      -          never     # forward plans
notes/               fixed      cite
manuscript/          -          never     # the draft is never a source
```
"""

BIB = "@article{good2020,\n  title={x}\n}\n@book{other21, title={y}}\n"


def git(cwd, *args):
    p = subprocess.run(
        ["git", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
        env={**os.environ, **GIT_ENV},
    )
    assert p.returncode == 0, p.stderr
    return p.stdout.strip()


class Workspace(unittest.TestCase):
    """A temporary workspace with a `code` repository tagged v1 and a workspace repository."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self._old = os.getcwd()
        self.addCleanup(os.chdir, self._old)
        self.root = os.path.realpath(self._tmp.name)
        os.chdir(self.root)
        env = mock.patch.dict(os.environ, GIT_ENV)
        env.start()
        self.addCleanup(env.stop)
        self.write("code/src/a.c", "one\ntwo\nthree\n")
        self.write("code/models/m1/props.yaml", "a: 1\n")
        self.write("code/models/m2/props.yaml", "a: 2\n")
        self.write("code/docs/dev/plan.md", "plan\n")
        git("code", "init", "-q")
        git("code", "add", ".")
        git("code", "commit", "-q", "-m", "first")
        git("code", "tag", "v1")
        self.commit_hex = git("code", "rev-parse", "--short=8", "HEAD")
        self.write("code/src/later.c", "later\n")  # after the pin
        git("code", "add", ".")
        git("code", "commit", "-q", "-m", "later")
        self.write("notes/n.md", "a\nb\n")
        self.write("AGENTS.md", SOURCES)
        self.write("manuscript/refs.bib", BIB)
        self.write("manuscript/main.tex", "\\documentclass{article}\n")
        git(".", "init", "-q")
        git(".", "config", "core.excludesfile", os.devnull)
        self.write(".gitignore", "code/\n")

    def write(self, path, text):
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w") as f:
            f.write(text)

    def commit(self, msg="c"):
        git(".", "add", "-A")
        git(".", "commit", "-q", "-m", msg)

    def run_cmd(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = traces.main(list(argv))
        return code, out.getvalue(), err.getvalue()

    def section(self, text, name="s.tex"):
        self.write(f"manuscript/sections/{name}", text)
        return f"manuscript/sections/{name}"


class TestParsing(unittest.TestCase):
    ROOTS = ("code/", "notes/")

    def kinds(self, body, keys=()):
        return [(k, t, l) for k, t, l in traces.anchors(body, self.ROOTS, set(keys))]

    def test_line_lists_ranges_and_brace_paths(self):
        got = self.kinds("code/a.c:156 (f), :162; code/b.c:3-7, code/{x,y}/r.md")
        self.assertEqual(
            got,
            [
                ("path", "code/a.c", [156, 162]),
                ("path", "code/b.c", [3, 7]),
                ("path", "code/{x,y}/r.md", []),
            ],
        )
        self.assertEqual(
            traces.expand_braces("code/{x,y}/r.md"), ["code/x/r.md", "code/y/r.md"]
        )

    def test_quoted_text_and_bare_names_are_free_text(self):
        got = self.kinds(
            "code/a.c:5 \"see code/zzz.c\" and ``code/qq.c'' in plain.h, search"
        )
        self.assertEqual([k for k, _, _ in got], ["path", "search"])

    def test_commit_and_key(self):
        got = self.kinds(
            "code@a654c228 (2026) 2021MNRAS.506.4210I Table 1", ["2021MNRAS.506.4210I"]
        )
        self.assertEqual([k for k, _, _ in got], ["commit", "key"])

    def test_gaps_with_nested_braces_and_comments_ignored(self):
        text = "a \\gap{q}{why \\texttt{x}?\n  really} b\n% \\gap{todo}{commented}\n"
        self.assertEqual(
            traces.parse_gaps("f", text), [("f", 1, "q: why \\texttt{x}? really")]
        )

    def test_continuation_qualifier_and_stamp(self):
        text = (
            "% checked: 2026-01-01 me\n% src (footnote): code/a.c:1\n%   and more\n"
            "% src: notes/n.md\nText % src: code/b.c\n"
        )
        got = traces.parse_traces("f", text)
        self.assertEqual(
            [t.text for t in got],
            ["(footnote) code/a.c:1 and more", "notes/n.md", "code/b.c"],
        )
        self.assertEqual([t.line for t in got], [2, 4, 5])


class TestLint(Workspace):
    def lint(self, text):
        self.section(text)
        return self.run_cmd("lint")

    def test_clean_manuscript_passes(self):
        code, out, _ = self.lint(
            "Text \\citet[p.~2]{good2020, other21}.\n"
            "% src: code/src/a.c:3 (f), :2; code/models/*/props.yaml; notes/n.md:2\n"
            f'% src (footnote): code@{self.commit_hex} "a message"; good2020 Table 1\n'
            "% src: search grep -c x code/src (2026-11-19) -> 0\n"
        )
        self.assertEqual((code, out.strip()), (0, "0 findings"))

    def test_missing_sources_block_exits_2(self):
        self.write("AGENTS.md", "# no block here\n")
        code, _, err = self.lint("% src: code/src/a.c\n")
        self.assertEqual(code, 2)
        self.assertIn("sources", err)

    def test_unparsable_sources_line_exits_2(self):
        self.write("AGENTS.md", "```sources\ncode/  v1  cite\n```\n")
        code, _, err = self.lint("% src: code/src/a.c\n")
        self.assertEqual(code, 2)
        self.assertIn("AGENTS.md:2", err)

    def test_never_root(self):
        for tok in ("code/docs/dev/plan.md", "manuscript/main.tex"):
            code, out, _ = self.lint(f"% src: {tok}\n")
            self.assertEqual(code, 1)
            self.assertIn(f"never-root  {tok}", out)

    def test_never_policy_is_applied_to_what_is_named(self):
        for tok, shown in (
            ("code/docs/{dev,public}/plan.md", "never-root  code/docs/dev/plan.md"),
            ("code/docs/*/plan.md", "never-root  code/docs/dev/plan.md"),
            ("code/docs/dev@0123abcd", "never-root  code/docs/dev@0123abcd"),
            ("notes/../manuscript/x.tex", "parent-path  notes/../manuscript/x.tex"),
            ("notes/./n.md", "unplain-path  notes/./n.md"),
            ("code//docs/dev@0123abcd", "unplain-path  code//docs/dev@0123abcd"),
        ):
            with self.subTest(tok=tok):
                code, out, _ = self.lint(f"% src: {tok}\n")
                self.assertEqual(code, 1)
                self.assertIn(shown, out)

    def test_glob_reaching_another_cited_root(self):
        self.write(
            "AGENTS.md",
            SOURCES.replace("notes/", "code/models/m2/  fixed  cite\nnotes/", 1),
        )
        code, out, _ = self.lint(
            "% src: code/models/*/props.yaml\n% src: code/models/m1/props.yaml\n"
        )
        shown = (
            "manuscript/sections/s.tex:1  glob-spans-roots  code/models/*/props.yaml"
        )
        self.assertEqual((code, out.strip()), (1, f"{shown}\n1 findings"))

    def test_path_absent_at_pin(self):
        # later.c exists in the working tree and at HEAD, but not at the pin v1
        code, out, _ = self.lint("% src: code/src/later.c\n% src: notes/missing.md\n")
        self.assertIn("missing-at-pin  code/src/later.c", out)
        self.assertIn("missing-at-pin  notes/missing.md", out)
        self.assertEqual(code, 1)

    def test_line_beyond_end_and_glob_matching_nothing(self):
        _, out, _ = self.lint(
            "% src: code/src/a.c:4\n% src: code/nope/*/props.yaml\n"
            "% src: code/src/a.c:3-3\n"
        )
        self.assertIn("s.tex:1  line-beyond-end  code/src/a.c:4", out)
        self.assertIn("s.tex:2  missing-at-pin  code/nope/*/props.yaml", out)
        self.assertNotIn("s.tex:3", out)

    def test_unknown_cite_key_and_commit(self):
        _, out, _ = self.lint("A \\cite{good2020,bad99}.\n% src: code@0123abcd\n")
        self.assertIn("unknown-cite-key  bad99", out)
        self.assertIn("unknown-commit  code@0123abcd", out)
        self.assertNotIn("good2020", out)

    def test_no_anchor_and_parent_path(self):
        _, out, _ = self.lint(
            "% src: grep somewhere for a thing\n% src: ../code/src/a.c\n"
        )
        self.assertIn("s.tex:1  no-anchor", out)
        self.assertIn("s.tex:2  parent-path", out)

    def test_pin_that_does_not_resolve_exits_2(self):
        self.write("AGENTS.md", SOURCES.replace("git:v1", "git:v9"))
        code, _, err = self.lint("% src: code/src/a.c\n")
        self.assertEqual(code, 2)
        self.assertIn("v9", err)


class TestListAndLost(Workspace):
    def test_list_counts_and_rev(self):
        p = self.section("A.\n% src: code/src/a.c:1\nB \\gap{todo}{later}\n")
        self.commit()
        self.section("")
        _, out, _ = self.run_cmd("list")
        self.assertEqual(out.strip().splitlines()[-1], "0 traces, 0 gaps in 2 files")
        _, out, _ = self.run_cmd("list", "--rev", "HEAD", p)
        self.assertIn(f"{p}:2  src  code/src/a.c:1", out)
        self.assertIn(f"{p}:3  gap  todo: later", out)
        self.assertEqual(out.strip().splitlines()[-1], "1 traces, 1 gaps in 1 files")
        self.assertEqual(out.strip().splitlines()[-2], "gaps by kind: todo 1")

    def test_lost_moved_and_gap_closed(self):
        self.section(
            "% src: code/src/a.c:1\n% src: notes/n.md\n% src: code/src/a.c:2\n"
            "\\gap{q}{open}\n",
            "a.tex",
        )
        self.write("manuscript/sections/b.tex", "")
        self.commit()
        self.section("% src: notes/n.md\n", "a.tex")  # the other two go
        self.write("manuscript/sections/b.tex", "% src: code/src/a.c:1\n")  # one moves
        code, out, _ = self.run_cmd("lost")
        self.assertEqual(code, 1)
        self.assertIn("lost  manuscript/sections/a.tex:3  code/src/a.c:2", out)
        self.assertIn(
            "moved  manuscript/sections/a.tex:1 -> manuscript/sections/b.tex:1", out
        )
        self.assertIn("gap closed  manuscript/sections/a.tex:4  q: open", out)
        self.assertNotIn("notes/n.md", out)

    def test_copy_left_in_place_is_not_reported_moved(self):
        self.section("% src: notes/n.md\n", "a.tex")
        self.section("\n\n% src: notes/n.md\n", "b.tex")
        self.commit()
        self.section("Text.\n", "a.tex")  # the copy in a.tex goes; b.tex is untouched
        code, out, _ = self.run_cmd("lost")
        self.assertEqual(code, 1)
        self.assertIn("lost  manuscript/sections/a.tex:1  notes/n.md", out)
        self.assertIn("1 lost, 0 moved", out)
        self.assertNotIn("b.tex", out)

    def test_lost_against_a_copy_of_uncommitted_text(self):
        p = self.section("% src: code/src/a.c:1\n% src: notes/n.md\n", "a.tex")
        self.commit()
        self.section(
            "% src: code/src/a.c:1\n% src: notes/n.md\n% src: code/src/a.c:2\n", "a.tex"
        )
        self.write(
            f".scratch/review/r1/{p}", open(p).read()
        )  # what the reader was given
        self.section("% src: code/src/a.c:1\n", "a.tex")  # the round drops two traces
        code, out, _ = self.run_cmd("lost", "--copy", ".scratch/review/r1")
        self.assertEqual(code, 1)
        self.assertIn(f"lost  {p}:2  notes/n.md", out)
        self.assertIn(
            f"lost  {p}:3  code/src/a.c:2", out
        )  # never committed, still seen
        self.assertIn("(against the copy .scratch/review/r1)", out)
        self.assertEqual(os.getcwd(), self.root)
        code, _, err = self.run_cmd("lost", "--copy", "nowhere")
        self.assertEqual(code, 2)
        self.assertIn("no such directory", err)
        code, _, err = self.run_cmd(
            "lost", "--rev", "HEAD", "--copy", ".scratch/review/r1"
        )
        self.assertEqual(code, 2)

    def test_nothing_lost_exits_0(self):
        self.section("% src: code/src/a.c:1\n")
        self.commit()
        self.section(
            "% src:   code/src/a.c:1\n\nExtra text.\n"
        )  # whitespace and line moves are not losses
        code, out, _ = self.run_cmd("lost")
        self.assertEqual(code, 0)
        self.assertIn("0 lost, 0 moved", out)


class TestMoved(Workspace):
    def code_commit(self, tag=None):
        git("code", "add", "-A")
        git("code", "commit", "-q", "-m", "change")
        if tag:
            git("code", "tag", tag)

    def test_repin_reports_traces_in_changed_files_only(self):
        self.section(
            "% src: code/src/a.c:2\n% src: code/models/m1/props.yaml\n% src: notes/n.md\n"
        )
        self.write("code/src/a.c", "one\nTWO\nthree\n")
        self.code_commit("v2")
        code, out, _ = self.run_cmd(
            "moved", "code/", "--to", "v2"
        )  # --from defaults to the pin v1
        self.assertEqual(code, 1)
        self.assertEqual(
            out.splitlines()[0], "manuscript/sections/s.tex:1  src  code/src/a.c:2"
        )
        self.assertEqual(
            out.splitlines()[-1], "1 traces anchor in 2 changed files of code/ (v1..v2)"
        )
        self.assertNotIn("props.yaml", out)
        self.assertNotIn("n.md", out)

    def test_renamed_file_is_reported_under_its_old_path(self):
        self.section(
            "% src: code/models/m1/props.yaml\n% src: code/models/m2/props.yaml\n"
        )
        git("code", "mv", "models/m1/props.yaml", "models/m1/renamed.yaml")
        self.code_commit()
        code, out, _ = self.run_cmd("moved", "code/", "--to", "HEAD")
        self.assertEqual(code, 1)
        self.assertIn("s.tex:1  src  code/models/m1/props.yaml", out)
        self.assertNotIn("s.tex:2", out)

    def test_glob_directory_and_brace_anchors(self):
        self.section(
            "% src: code/models/*/props.yaml\n% src: code/models/m2/\n"
            "% src: code/models/m1/\n% src: code/models/{m1,m2}/props.yaml\n"
        )
        self.write(
            "code/models/m2/props.yaml", "a: 3\n"
        )  # edited, not committed: the working tree counts
        code, out, _ = self.run_cmd("moved", "code", "manuscript/sections/s.tex")
        self.assertEqual(code, 1)
        lines = out.splitlines()
        self.assertEqual(
            [l.split()[0] for l in lines[:-1]],
            [f"manuscript/sections/s.tex:{n}" for n in (1, 2, 4)],
        )
        self.assertIn("changed files of code/ (v1..working tree)", lines[-1])

    def test_fixed_root_edited_in_the_working_tree(self):
        self.section(
            "% src: notes/n.md:2\n% src: code/src/a.c\n% src: notes/[n].md\n% src: notes/*p.md\n"
        )
        self.write(
            "notes/sub/deep.md", "d\n"
        )  # `*p.md` would reach it only by crossing a `/`
        self.commit()
        code, out, _ = self.run_cmd(
            "moved", "--from", "HEAD", "notes", "manuscript/sections/s.tex"
        )
        self.assertEqual(
            (code, out.strip()),
            (0, "0 traces anchor in 0 changed files of notes/ (HEAD..working tree)"),
        )
        self.write("notes/n.md", "a\nB\n")
        self.write("notes/sub/deep.md", "D\n")
        self.write("notes/untracked.md", "u\n")
        code, out, _ = self.run_cmd(
            "moved", "--from", "HEAD", "notes", "manuscript/sections/s.tex"
        )
        self.assertEqual(code, 1)
        self.assertIn("s.tex:1  src  notes/n.md:2", out)
        self.assertIn("s.tex:3  src  notes/[n].md", out)
        self.assertNotIn("s.tex:4", out)
        self.assertIn(
            "2 traces anchor in 2 changed files of notes/ (HEAD..working tree); "
            "1 untracked files not compared",
            out,
        )

    def test_configuration_and_git_failures_exit_2(self):
        self.section("% src: notes/n.md\n")
        for argv, word in (
            (("lib/",), "declared"),
            (("manuscript/",), "`-` root"),
            (("notes/",), "--from"),
            (("code/", "--from", "nosuchrev"), "nosuchrev"),
        ):
            with self.subTest(argv=argv):
                code, _, err = self.run_cmd("moved", *argv)
                self.assertEqual(code, 2)
                self.assertIn(word, err)


class TestSample(Workspace):
    def test_sample_is_reproducible_and_shows_the_tex(self):
        self.section(
            "% src: code/src/a.c:1\nFirst sentence.\n% src: notes/n.md\nSecond.\n% src: code/src/a.c:2\nThird.\n"
        )
        code, out, _ = self.run_cmd("sample", "2", "--seed", "7")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip().splitlines()[-1], "2 of 3 traces, seed 7")
        self.assertEqual(out, self.run_cmd("sample", "2", "--seed", "7")[1])
        first = out.splitlines()[0]
        line = int(first.split()[1].split(":")[1])
        self.assertIn(f"{line + 1:>5}  ", out)

    def test_sample_more_than_there_are_and_bad_n(self):
        self.section("% src: notes/n.md\nOnly.\n")
        _, out, _ = self.run_cmd("sample", "5", "--seed", "1")
        self.assertTrue(out.strip().endswith("1 of 1 traces, seed 1"))
        self.assertEqual(self.run_cmd("sample", "0")[0], 2)


class TestStale(Workspace):
    def stale(self):
        return self.run_cmd("stale", "manuscript/sections/s.tex")

    def test_never_checked_and_no_traces(self):
        self.section("Text.\n% src: notes/n.md\n")
        code, out, _ = self.stale()
        self.assertEqual(code, 1)
        self.assertIn("never checked", out)
        self.section("Text, no traces.\n")  # a section needs a stamp whatever it holds
        self.assertEqual(self.stale()[0], 1)
        self.assertIn(
            "never checked", self.run_cmd("stale", "manuscript/main.tex")[1]
        )  # the abstract
        self.write("manuscript/figures/style.tex", "\\tikzset{x/.style={}}\n")
        code, out, _ = self.run_cmd("stale", "manuscript/figures/style.tex")
        self.assertEqual(
            (code, out.strip()), (0, "manuscript/figures/style.tex: no traces")
        )

    def test_git_failure_is_an_error(self):
        self.section("% checked: 2026-11-19 a checker\nText.\n")
        self.commit()
        os.rename(".git", ".git-away")  # no longer a repository
        code, _, err = self.stale()
        self.assertEqual(code, 2)
        self.assertIn("git", err)

    def test_stamp_not_yet_committed(self):
        self.section("% checked: 2026-11-19 a checker\nText.\n")
        code, out, _ = self.stale()  # untracked
        self.assertIn("checked 2026-11-19, not yet committed", out)
        self.assertEqual(code, 1)
        self.commit()
        self.section(
            "% checked: 2026-11-20 a checker\nText.\n"
        )  # re-stamped, uncommitted
        self.assertIn("not yet committed", self.stale()[1])
        git(".", "rm", "-qf", "manuscript/sections/s.tex")
        self.commit()
        self.section(
            "% checked: 2026-11-20 a checker\nText.\n"
        )  # restored, in history but not HEAD
        self.assertEqual(
            self.stale()[:2],
            (1, "manuscript/sections/s.tex: checked 2026-11-20, not yet committed\n"),
        )

    def test_unchanged_then_stale(self):
        self.section("% checked: 2026-11-19 a checker\nText.\n")
        self.commit()
        sha = git(".", "rev-parse", "--short=8", "HEAD")
        code, out, _ = self.stale()
        self.assertEqual(
            (code, out.strip()),
            (
                0,
                f"manuscript/sections/s.tex: checked 2026-11-19, unchanged since {sha}",
            ),
        )
        self.section("% checked: 2026-11-19 a checker\nText, changed.\nMore.\n")
        code, out, _ = self.stale()
        self.assertEqual(code, 1)
        self.assertIn(f"STALE: checked 2026-11-19, changed since {sha} (2 lines)", out)

    def test_second_check_on_the_same_day_adds_a_round(self):
        self.section("% checked: 2026-11-19 a checker\nText.\n")
        self.commit()
        self.section("% checked: 2026-11-19 r2 a checker\nText, changed.\n")
        self.commit()
        self.assertIn("checked 2026-11-19, unchanged", self.stale()[1])

    def test_restamping_in_a_new_commit_resets(self):
        self.section("% checked: 2026-11-19 a checker\nText.\n")
        self.commit()
        self.section("% checked: 2026-11-20 a checker\nText, changed.\n")
        self.commit()
        self.assertIn("checked 2026-11-20, unchanged", self.stale()[1])


if __name__ == "__main__":
    unittest.main()
