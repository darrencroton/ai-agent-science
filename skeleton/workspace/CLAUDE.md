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

Author-owned paths are the ones this paper actually uses --- edit the rows below
to match, and delete any that do not exist.

| Path | Owner | |
|---|---|---|
| `../notes/` | author | free-form markdown; never modified |
| `notes/` | author (written by the agent) | the author's captured words, as new dated notes; created on first capture (where the paper's subject is the project itself, this is the paper's notes directory) |
| `../figures/` | author | looked at, never regenerated |
| `../code/` | author | read, never run |
| `paper-voice/` | author | optional, for ai-agent-science's use only: past papers / style notes — see its own `README.md` |
| `paper/` | agent | this workspace's memory: `STATE.md`, `journal.md`, `outline.md`, `open-questions.md`, `voice.md` (only if `paper-voice/` is used), `lit/` |
| `manuscript/` | shared | the author edits this directly and constantly |
| `.build/` | build | gitignored |

`paper-voice/`, `paper/`, `manuscript/` and `.build/` are always directly
inside this workspace root. The author's own `notes/`, `figures/` and `code/`
are found wherever the author's project already keeps them, which is normally
one level up or deeper — the `../notes/` row above is the common case, not a
fixed path; edit it to match wherever the survey actually found them. For a paper whose subject is the project itself, the paper's `notes/` and `figures/` are inside this workspace instead; delete the `../` rows.

Everything except `.build/` is committed **to this workspace's own
repository**. The diffs of `paper/` are the record of how the paper was
thought through.

## Subject version

Only for a paper whose subject is a repository (a software or instrument paper): the version the paper describes, which every `% src:` anchor into it is pinned to — `<tag>` (`<commit>`) — and the command that re-reads a file at it (`git -C <subject> show <tag>:<path>`). See house-rules *Pin a source that moves*. Delete this section otherwise.

## Venue

Not yet chosen --- `main.tex` uses a plain `article` class. Choosing one means
switching the manuscript to it: see `<root>/skills/paper/modes/venue.md`, *Switching the manuscript to a venue*.

## Build

From this workspace root:

    (cd manuscript && latexmk -pdf -interaction=nonstopmode -outdir=../.build main.tex)

Keep `-interaction=nonstopmode`. Without it a LaTeX error waits at the
interactive `?` prompt and the build hangs instead of failing.

Draft mode is the default. Final mode is the `[final]` option on
\usepackage{scipaper} in `main.tex`; it fails the build while any `\gap`
remains.
