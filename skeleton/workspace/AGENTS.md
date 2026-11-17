# <paper short name>

A paper workspace. Sessions here work under the ai-agent-science skills.

**This directory is the workspace root** — every path below, and every path any
ai-agent-science skill uses, is relative to it. It is its own git repository,
deliberately isolated from the project above it: nothing ai-agent-science creates or
touches (drafts, memory, fetched PDFs, build output) ever reaches that
project's own git history. The project's own `.gitignore` (for a paper whose subject is the project itself, its `.git/info/exclude`) excludes this whole
directory (`sci-paper-workspace*/`) so that isolation holds even before this
repository exists.

## First action, every session

1. Read `paper/STATE.md` in full. It is capped at two pages so that it can be
   read whole, every time, without deciding whether to.
2. Read `<root>/skills/_shared/memory.md` and
   `<root>/skills/_shared/house-rules.md`.

Those two files are the authority on how to behave here. They are deliberately
not restated in this file, and nothing in this file overrides them. They apply
to ordinary conversation exactly as they apply to a `/paper` or `/literature` command — the
commands are shortcuts, not an interface anyone has to learn.

## Directory map

The **Kind** column marks each row **core** (what the skills create and name) or
**local** (this paper's own addition; no skill assumes a local item exists). Edit
the author-owned rows to match what this paper actually uses, delete any that do
not exist, and add a `local` row for anything else this paper keeps here.

| Path | Owner | Kind | |
|---|---|---|---|
| `../notes/` | author | core | free-form markdown; never modified |
| `notes/` | author (written by the agent) | core | the author's captured words, as new dated notes; created on first capture (where the paper's subject is the project itself, this is the paper's notes directory) |
| `../figures/` | author | core | looked at, never regenerated |
| `../code/` | author | core | read, never run |
| `paper-voice/` | author | core | optional, for ai-agent-science's use only: past papers / style notes — see its own `README.md` |
| `paper/` | agent | core | this workspace's memory: `STATE.md`, `journal.md`, `outline.md`, `open-questions.md`, `voice.md` (only if `paper-voice/` is used), `lit/` (`index.md`, notes, `reports/`, and `pdf/`, the fetched full texts, gitignored) |
| `manuscript/` | shared | core | the author edits this directly and constantly; `main.tex`, `sections/`, `refs.bib`, `scipaper.sty`, `figures/` (figures made for the paper, created when first needed) and the built `main.pdf` (gitignored) |
| `.scratch/` | scratch | core | gitignored, scratch only: conversions to look at, rendered pages, raw replies |

`paper-voice/`, `paper/`, `manuscript/` and `.scratch/` are always directly
inside this workspace root. The author's own `notes/`, `figures/` and `code/`
are found wherever the author's project already keeps them, which is normally
one level up or deeper — the `../notes/` row above is the common case, not a
fixed path; edit it to match wherever the survey actually found them. For a paper whose subject is the project itself, the paper's own notes are in `notes/` here and its figures are in `manuscript/figures/`; delete the `../` rows.

Everything `.gitignore` does not name is committed **to this workspace's own
repository**. The diffs of `paper/` are the record of how the paper was
thought through.

`paper/STATE.md` is the only handoff (`memory.md`, *Last action of every session*).

## Subject version

Only for a paper whose subject is a repository (a software or instrument paper): the version the paper describes, which every `% src:` anchor into it is pinned to — `<tag>` (`<commit>`) — and the command that re-reads a file at it (`git -C <subject> show <tag>:<path>`). See house-rules *Pin a source that moves*. Delete this section otherwise.

## Venue

Not yet chosen --- `main.tex` uses a plain `article` class. Choosing one means
switching the manuscript to it: see `<root>/skills/paper/modes/venue.md`, *Switching the manuscript to a venue*.

## Build

From this workspace root:

    (cd manuscript && latexmk -pdf -interaction=nonstopmode main.tex)

The PDF is `manuscript/main.pdf`. Keep `-interaction=nonstopmode`. Without it a LaTeX error waits at the
interactive `?` prompt and the build hangs instead of failing.

Draft mode is the default. Final mode is the `[final]` option on
\usepackage{scipaper} in `main.tex`; it fails the build while any `\gap`
remains.

## Local additions

Local procedures this paper adds go here. Delete this section if there are none.
