# House rules

Read this once per session. It applies to every skill and to ordinary
conversation alike. It is written here and nowhere else; skills reference it
and do not restate it.

---

## Locating the installation

Most of what a skill needs is beside it: `_shared/` is `../_shared/` relative to
the running `SKILL.md`, and that resolves whether the skill is being read in
this repo or through the symlinked skill catalogue of an installed agent home.

**`skeleton/` and `tools/ads.py` are not.** They sit one level above `skills/`,
so they need the installation root, which is written `<root>` wherever a
skill refers to it. Resolve it once, at the start of the session that needs it:

```sh
# <skill dir> is the directory holding the running SKILL.md
SCIENCE_ROOT=$(cd -P "<skill dir>/../.." && pwd -P)
[ -f "$SCIENCE_ROOT/tools/ads.py" ] && printf 'installation root: %s\n' "$SCIENCE_ROOT" \
  || printf 'installation root not found from the skill path\n'
```

**`cd -P` is not optional and plain `cd` is actively wrong here.** A skill is
reached through a symlink, and `cd` resolves `..` against the *path you typed*
rather than against where the symlink points — so `cd <skill dir>/../..` lands
two levels above the catalogue instead of two above the real `skills/`. Verified:
it returns a directory that exists and has no `tools/` in it. `-P` resolves each
component physically; `pwd -P` then prints the real path.

That is also why **the `ads.py` test is the confirmation, not a formality** — the
failure it catches returns a plausible directory rather than an error. Do not
proceed on an unconfirmed root, and never guess a path.

**Two shortcuts before resolving anything.** A paper repo's own `CLAUDE.md`
records the absolute install path, so in an existing workspace read it from
there. And if `$SCIENCE_ROOT` is already set in the environment, trust it after
the same `ads.py` test.

**The one moment this genuinely matters** is the first `/paper start` in a
brand-new paper directory: there is no `CLAUDE.md` yet, because the scaffold is
what writes it. If the root cannot be confirmed, say so and ask for the path
rather than copying a partial skeleton or inventing a location (AQ15).

**The installed copy is a managed clone that the agent home's setup updates.** Changes to the system are made in a development clone and reach the installed copy only through commit, push and setup — an edit made in the installed copy either stops the next update or is reverted by it.

---

## The workspace root

A paper is rarely written in an empty directory. The usual case is an existing
science project — data, analysis code, its own git repo, often its own
`CLAUDE.md` — with the paper as one part of it, and that project is different
from one paper to the next. So the paper's workspace is **`sci-paper-workspace/`
(or `sci-paper-workspace-<suffix>/` where a second paper shares the project),
its own git repository, isolated from the project around it** — and every path
in this file and in every skill is relative to it: the **workspace root**.

**Find it before doing anything else.** Resolution is a short ladder, cheapest
first:

1. If you are already working inside a `sci-paper-workspace*/` directory, that
   is the workspace root. Its own `CLAUDE.md` confirms it.
2. Otherwise, read the working directory's **agent-instruction file** — its
   `AGENTS.md`, or its `CLAUDE.md` where that is what the project uses; the
   project's own convention decides which, and `/paper start` §5b resolves it.
   Look for the index block `/paper start` appends there, under *sci-paper
   workspaces in this project*, and match the paper being discussed by its
   **short name**, never by directory name — the directory can be renamed by hand at any time
   (nothing inside a workspace depends on its own directory name to function),
   **provided the rename keeps the `sci-paper-workspace` prefix** — the glob
   below and the working directory's own `.gitignore` both match on it, and a
   rename that drops it falls out of both at once.
3. If the index has no match, or looks stale, **glob for `sci-paper-workspace*/`
   and confirm each candidate structurally** — `paper/STATE.md` and
   `manuscript/` both present, the same "confirm by fingerprint, not by a
   recorded string" approach used to locate the installation above — then read
   each candidate's `STATE.md` header for its short name.
4. Once resolved, **upsert only that one row of the index** if it was missing
   or wrong, **where the index lives**: the project's agent-instruction file, or `<ws>/paper/CLAUDE-sci-paper.md` where the author declined that file (AQ3) or the subject is the project itself. Never create an index in the project's file that was deliberately kept out of it. Never rewrite the whole block: a second paper's row must survive
   the first paper's session touching the file.

Work from the workspace root once found — `cd` into it, or prefix paths with
it, but do not half-do one and half-do the other. `paper-voice/`, `paper/`,
`manuscript/` and `.build/` are always directly inside it.

**It is never `.` and never the working directory itself.** Isolation is the
point: the workspace is always its own repository and always one directory below
the project it draws from (or, where the workspace is reached through a symbolic link, with the project linked inside it; see below), and the project's own `.gitignore` (for a subject repository, its `.git/info/exclude`) excludes it by a
glob (`sci-paper-workspace*/`) so that holds regardless of a later rename —
**provided the rename keeps the prefix**, per the resolution ladder above.
Nothing about the working directory's own git history is ever touched by
anything ai-agent-science does.

**The author's directories are found, not placed, and live outside the
workspace root** (except where the paper's subject is the project itself, below). `notes/`, `figures/` and `code/` are the author's project
material, not ai-agent-science's, so they stay wherever the project already keeps
them and under whatever they are already called — `analysis/`, `plots/`, a
`notes/` at the project root. The workspace's own `CLAUDE.md` records the
resolved paths. A `% src:` anchor is written relative to the workspace root and
normally points outside it now, so `% src: ../analysis/plot_lf.py:88
(fit_break)` is the ordinary case, not the exception. The workspace's own `<ws>/notes/` (created on first capture) holds the author's captured words and, where the subject is the project, the paper's own notes; the author's project `notes/` stays read-only and untouched.

**`paper-voice/` is different: it is author-supplied, but for ai-agent-science's use,
so it lives inside the workspace root, beside `paper/` rather than inside it.**
It has nowhere else to be found, unlike `notes/`/`figures/`/`code/` — the
author assembles it specifically for `/paper voice` (see that skill), and
where it exists, `paper/voice.md` — the profile distilled from it — is
consulted by `/paper draft` and `/paper frame` by default. Its absence changes
nothing.

**Nothing the author owns is ever moved to tidy the layout.** Not a note, not a
figure, not a script. If the material sits somewhere awkward, say so and use it
where it is.

**When the paper's subject is the project itself** — a software or instrument repository that should hold nothing about a paper — the paper's own notes and figures live inside the workspace (`notes/`, `figures/`), and nothing is written into the subject's tracked files: the exclusion goes in its `.git/info/exclude`, and the index entry in `<ws>/paper/CLAUDE-sci-paper.md` (`start` §1a, §5b).

**A workspace reached through a symbolic link** (kept on a synced volume, say) cannot reach the project by `../`, because `..` is the link target's parent. Link the project inside the workspace and write every path into it through that link; the exclude pattern then drops its trailing slash (`sci-paper-workspace*`) so that it matches a link.

**These names belong to the workspace format, not to the toolkit, and keep their `sci-paper` spelling:** `sci-paper-workspace` (and `sci-paper-workspace*/`), `scipaper.sty`, the `<!-- sci-paper: begin -->`/`end` markers and the heading inside that block, `paper/CLAUDE-sci-paper.md`, and `SCI_PAPER_ADS_BASE`. They are written into live workspaces.

---

## Division of labour

**The author owns** the science, the notes, the figures, the analysis code,
every claim, every number, every interpretation, and the final text. The author
is the verifier and reads the paper in detail, repeatedly.

**The agent owns** turning notes into prose; literature legwork; keeping the
record of what was discussed and decided; suggesting connections and tensions
the author cannot see from inside the draft; drafting the framing sections from
the established body; assembling the bibliography.

**Never:**

- modify anything already in `notes/`
- run or modify analysis code
- regenerate figures
- silently change the strength of a claim while rewriting prose

**Capture the author's words.** When the author states the paper's direction, decides something, or answers a question, write it **verbatim and dated** into a **new** note in the workspace's `notes/` (`<ws>/notes/`), without being asked, and point each file changed because of it at that note. Existing notes are still never edited. If the author says not to, don't. Decisions arrive in one line mid-turn, and a decision recorded only in the agent's paraphrase is the agent's, not the author's.

**The other half of "never run it": say what to run.** On its own the
prohibition turns "this number does not exist yet" into a dead end. So where a
value can only come from executing something, write the **exact command** that
would produce it, mark the value `\gap{number}`, and note the command with the
question in `paper/open-questions.md`. When the author runs it and records the
output, that record is an ordinary `% src:` source like any other.

### Found while reading

**Writing from a repository audits its documentation.** Where a guide, comment or docstring disagrees with the code, the prose follows the code. The disagreement earns a `\gap{q}` in the manuscript only when it changes what the sentence says; otherwise it is an open question with no marker, still recorded, because it is real and it is the subject owner's to fix, not the paper's. The same goes for a quirk that is neither a disagreement nor a hole in the draft, such as a configuration key nothing reads. This concerns the subject's own documentation; a disagreement between the code and the **author's** notes keeps `draft`'s rule (always a `\gap{q}`).

---

## Gap markers

The draft is allowed to be incomplete. It is not allowed to hide a hole it
knows about.

One macro, five kinds:

```latex
\gap{number}{cooling threshold — need the value from run 3}
\gap{cite}{who first showed the bright-end cutoff?}
\gap{q}{is this the right sample cut? see paper/open-questions.md (Q7)}
\gap{logic}{this does not yet follow from Fig 4}
\gap{todo}{expand once the z=2 run finishes}
```

The note is typeset, so LaTeX's special characters in it (`_`, `%`, `&`, `#`, `^`) are escaped, or the build fails on the marker meant to report a hole.

Mode is a package option in `main.tex`:

- `\usepackage{scipaper}` — **draft** (the default). Markers render loudly
  inline and in the margin.
- `\usepackage[final]{scipaper}` — **final**. Every `\gap` invocation raises a
  package error and the build fails. A gap-free manuscript builds cleanly.

Switching is a one-word edit and it is visible in the diff.

**Collecting the gaps is a grep, not a tool.** Available at any time, not only
at `/paper finish`:

```sh
grep -rn '\\gap{' manuscript --include='*.tex'
```

Restricted to `.tex`, because `scipaper.sty` contains the macro's own
definition. Recursive, so it works before `sections/` exists.

**What this guarantees, and what it does not.** It guarantees a *marked* gap
cannot reach a submitted manuscript. It does not catch a free-text `TODO`,
`TBD` or `XXX`, and it cannot catch a number written instead of marked — that
is what the integrity rules below are for.

---

## The two integrity rules

Everything else about verification is the author's. These two are kept because
they are nearly free and they protect the author at the moment they are reading
fast.

### Rule 1 — every quantitative statement is either traced or marked

A number, range, threshold or uncertainty in the manuscript carries exactly one
of:

- a `% src:` comment naming where it came from, or
- a `\gap{number}` marker, if it has no source yet.

There is no third option. **Never write a number that cannot be traced.** The
same applies to a citation: found and cited, or `\gap{cite}`.

**A citation the paper adds for context**, beyond what its source cites, is welcome when confirmed to exist (ADS, or Rule 2's other paths). It is the paper's own choice and does not borrow the source's trace.

**The legitimate sources are wider than the notes**, because in practice a
result lives wherever the author put it. (Anchors are written relative to the workspace root; the examples leave out the `../` that usually leads out of it to the author's own directories.)

| Source | Anchor |
|---|---|
| a note | `% src: notes/methods.md "cooling threshold"` |
| a figure the agent looked at | `% src: figures/fig3.pdf` |
| a line in the analysis code | `% src: code/plot_lf.py:88 (fit_break)` |
| a module-level constant in that code | `% src: code/plot_lf.py:12 (MSTAR_MIN)` |
| a literature note | `% src: paper/lit/2020MNRAS.499.5732S.md table 2` |
| an absence claim or a search | `% src: search <exact command> (<date>, <version>) -> none` |
| a count made from a file | `% src: code/run.cfg (grep -c '^model_' -> 64)` |

An absence claim ("no shipped module does X") rests on a search, not a line, so the search is written out and can be re-run. A count is a trace only when the anchor says how it was made and the items counted can be named; a count without its items cannot be checked and silently goes stale.

A figure or a line of code is a first-class source. Marking the author's own
figure-derived result as unknown because it is not written down in a note is a
worse failure than any it prevents.

**The draft is never a source.** `notes/` (including `<ws>/notes/`), `figures/`, `code/`, the author's
tables, the subject repository at its pinned version and `paper/lit/` are where science comes from. A number or claim already
in the manuscript is never evidence for another one: that is circular, and it is
how a transcription error propagates. **Nor is anything an agent wrote about the sources** — a survey report, an ingest index, a brief's summary. These are indexes for finding a source; the `% src:` points at the file, commit or paper itself.

**A value read off a figure is an estimate and is labelled as one** — the
author's own figures as much as published ones. An exact value must trace to a
note, a table, an explicit annotation, or the code or data behind the plot.
Prose that quotes a point read off a plot to three significant figures is false
precision no matter how good the trace looks.

**Copy units and $h$-scalings exactly as the source writes them, and record
which convention the source used. Never convert.** A comparison silently made
between $h^{-1}M_\odot$ and $M_\odot$ is the commonest way a comparison goes
wrong, and it survives every proofread because both numbers are correct. The
same holds for an IMF, a cosmology and an aperture: they travel with the
number or the number is not usable. The rule is about **values and conventions, not notation**: typesetting `Mpc/h` as $h^{-1}\,\mathrm{Mpc}$ is the same unit, and notation follows the paper's voice.

**An inherited measurement keeps its version.** A tracked number measured on an earlier version than the one the paper describes is quoted with the version or date it was measured at, or is a `\gap{number}` with the command that would re-measure it; it is never presented as a property of the later version.

**Code is read, never run.** A `% src:` anchor into `code/` points at a
definition or a literal in the source; it never means anything was executed. A
result that exists only as the *output* of a run, written down nowhere, has no
source yet — it is a `\gap{number}` until the author records it. **Write the command that
would produce it** — see *the other half of "never run it"* under **Division
of labour** above.

### Rule 2 — BibTeX is exported verbatim, never composed

**Never hand-written, never adjusted, never "corrected."** An entry someone
typed out looks exactly like one a machine exported, right up until the volume
number is wrong.

**Three exporting paths**, because a real bibliography contains work ADS does
not hold — arXiv preprints never published, proceedings, the computer-science
literature an AI- or methods-adjacent paper has to cite. Leaving those with no
legal path does not prevent a composed entry; it guarantees one.

| The work | Path |
|---|---|
| anything ADS holds | `python3 <root>/tools/ads.py export '<bibcode>'` |
| an arXiv-only preprint | `curl -sfL 'https://arxiv.org/bibtex/<arxiv id>'` |
| anything else with a DOI | `curl -sfLH 'Accept: application/x-bibtex' 'https://doi.org/<doi>'` |

All three return archive- or publisher-supplied BibTeX. A work with none of
the three is a `\gap{cite}` until the author supplies one — it is not typed
out.

**The author may direct which record is used, and often should.** Published
version or the preprint the community reads; the journal version or the arXiv
one whose section numbering the prose refers to; a specific revision. That is
an editorial choice and it is theirs. Where they name it, use it; otherwise
take the table's order and say in one line which record was used (AQ14). Directing
*which* record is exported says nothing about *what it says*, which is not a
decision at all.

**A record that will not render is fixed in the preamble, never in `refs.bib`** — a `\DeclareUnicodeCharacter` or `\providecommand`, with a comment naming the record. A journal's own `.bst` or class fix is a venue fact and lives in `_shared/venues/<venue>.md`.

### Both rules are hard instructions, not gates

Nothing structurally prevents an agent with write access to `refs.bib` from
composing an entry, or from writing an untraced number. These rules make the
wrong thing visible; they do not make it impossible. That is the honest
description and it is the right one — the author is the verifier.

---

## Source comments

The `% src:` comment is the entire traceability mechanism. There is no
registry, no database, no index.

```latex
% src: notes/methods.md "cooling threshold"
```

Invisible in output, greppable, zero ceremony. Two rules about form and scope:

**Anchor by name, not by line number.** `notes/` is author-owned and edited
constantly; inserting one paragraph invalidates every line pointer below it,
and a link known to be stale is a link that gets ignored. Anchor on a heading
or a short distinctive quoted phrase. Code is the one exception where a line
number is useful, and it carries alongside it the **symbol that owns the line**
— the enclosing function where there is one, and the constant's own name where
the line is a module-level literal, which is where analysis scripts keep their
load-bearing cuts more often than not. The symbol is what survives the edit that
moves the line.

**Write a code line number by looking at the file, never from memory of it.**
Adding an import or a docstring line shifts every anchor below it silently, and
an anchor that is off by two points at real code, which is exactly why nobody
catches it.

**Comment what is load-bearing, not everything.** Every quantitative statement
(required by rule 1), plus method and sample definitions and any unusually
load-bearing claim. Connective and qualitative prose gets nothing — commenting
every sentence buries the section diffs and devalues the marks that matter.

**Pin a source that moves.** When the source is a repository that keeps changing — the paper's own subject — anchors are written against the version the paper describes: the workspace `CLAUDE.md` records that version (tag and commit), and each section file opens with a comment naming the version its anchors were read at and how to re-read them (`git -C <repo> show <tag>:<path>`). A session that finds the checkout has moved past it re-reads anchors at the tag.

---

## Voice

**Where `paper/voice.md` exists, drafted and framed prose matches it.** It is
written by `/paper voice`, from whatever the author has put in `paper-voice/`,
and it is opt-in by existence rather than a default every paper gets: no
`paper-voice/`, no change in behaviour. Where it does exist, treat it the same
way a `_shared/sections/<role>.md` rhetorical-moves file is treated — read
before writing, not restated here.

This is a per-paper setting, never a system-wide one. Do not generalise a
voice profile from one paper into how prose is drafted for a different one.

---

## Non-destructive editing

The author edits `manuscript/` directly and constantly. That is the point of
the project.

**Edit in place and preserve author prose.** Never regenerate a section
wholesale over existing text without showing what would be replaced and being
told to go ahead (AQ8).

A single silent overwrite of a day's hand-editing ends the author's trust in
the system permanently, and git making it *recoverable* does not make it
acceptable.

The same applies to `paper/`: `journal.md` is append-only, and `STATE.md` is
rewritten deliberately, not clobbered.

It also applies to the index block in the working directory's
agent-instruction file (**The workspace root**, above): a second paper's row
in that index is exactly like another author's paragraph — upsert your own
workspace's row, never rewrite the whole block. And where that file is a
checked-in contract for the project rather than personal notes, it is someone
else's document twice over.
