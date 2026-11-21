# <paper short name>

A paper workspace: its own git repository, and the working directory of every session that writes the paper. Every path below is relative to this directory, and the toolkit's own paths are relative to the installation root, `<install>` (replaced by `start`).

## First action, every session

A reader commissioned with a brief reads only what its brief allows and skips this. Every other session:

1. Read `paper/STATE.md` in full.
2. Read `<install>/skills/_shared/core.md`. It is the authority on how to behave here, and nothing in this file overrides it.

## Sources

What the paper may cite, at what version, and what it may not. `python3 <install>/tools/traces.py lint` reads this block and stops if it is missing or a line does not parse. One line per root: `<root>/  <pin>  <cite|never>  [# comment]`. The pin is `git:<rev>` (read that repository at that revision), `fixed` (the file as it is here) or `-` (only with `never`). The longest matching root wins. Each source is linked or copied inside this directory.

```sources
# One line per source the paper draws on, for example:
# code/               git:v1.0   cite    # the repository the paper describes, at its release
# code/docs/plans/    -          never   # forward plans are not delivered work
# data/               fixed      cite    # files the paper reads as they are
# campaign-findings/  fixed      cite    # pinned copies of investigations' findings (skills/paper/evidence.md)
notes/              fixed      cite    # the author's testimony
paper/lit/          fixed      cite    # a note records a reading; a trace names the location in the paper
paper/checks/       fixed      cite    # the agent's own read-only checks
paper/lit/reports/  -          never   # agent-written answers to literature questions
paper/              -          never   # agent-written memory and indexes, never a source
manuscript/         -          never   # the draft is never a source
```

## Commit policy

_Not yet set. The author's words go here at `start`, and only the author changes them. Where none is stated, ask._

## Conventions

_This paper's conventions as they are decided: file names, labels, units, notation, citation keys. The style itself is in `paper/style.md`._

## How we work here

_Who drafts and who checks, and on which model (the stylist on the strongest available); the panel's membership; anything this paper teaches. A standing instruction from the author goes here, with one journal line quoting it._

## Build

From this directory:

    (cd manuscript && latexmk -pdf -interaction=nonstopmode main.tex)

The PDF is `manuscript/main.pdf`. Keep `-interaction=nonstopmode`: without it a LaTeX error waits at the interactive `?` prompt and the build hangs instead of failing. Draft mode is the default. Final mode is the `[final]` option on `\usepackage{scipaper}` in `main.tex`; it fails the build while any `\gap` remains.

## Venue

Not yet chosen; `main.tex` uses a plain `article` class. To choose one, and to switch the manuscript to it, read `<install>/skills/paper/techniques/venue.md`. The journal's facts, its class fixes and its referee instructions go in `paper/venue.md`.

## Directory map

| Path | Holds |
|---|---|
| `paper/` | the memory files: `STATE.md`, `outline.md`, `claims.md`, `open-questions.md`, `journal.md`, and the reference files `style.md`, `venue.md` and `field.md` once built |
| `paper/lit/` | the literature notebook; `pdf/` holds fetched full texts and is gitignored |
| `paper/ingest/` | agent-written indexes of the sources: never a source |
| `paper/checks/` | the agent's own read-only checks, one directory each, with script, command and output |
| `paper/reviews/` | one directory per milestone review |
| `manuscript/` | `main.tex`, `sections/`, `refs.bib`, `scipaper.sty`, `figures/`; the author edits here directly and constantly |
| `notes/` | the author's testimony, in their own words, never edited |
| `.scratch/` | scratch only; gitignored |

Add a row marked **local** for anything else this paper keeps here.
