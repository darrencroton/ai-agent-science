# ai-agent-science

Agent skills for writing a journal paper with an AI agent so that every checkable sentence is verifiable. They are plain Markdown, one small Python tool for the literature and one for the traces, and one LaTeX package, and they work in any agent harness that reads `SKILL.md` skills.

## The idea

A paper is verifiable when every checkable sentence has its source beside it, or a visible gap where the source is missing, and when someone other than the writer has opened those pointers. An agent writes fast and cannot see its own errors; the author's attention is the scarce resource. So the toolkit makes the unverified visible, keeps what the author must read short, and never certifies anything itself. The author is the gate.

The mechanism is one comment per sentence in the manuscript source, `% src: <path>:<line>`, or a `\gap{kind}{note}` that prints loudly in a draft and fails the build in final mode. Everything else serves that, or serves the author's attention.

## The map

- **Core.** `skills/_shared/core.md`: eight rules, the trace forms and gap kinds, and the memory files. Every session and every subagent reads it.
- **Five procedures** in `skills/paper/`: `start`, `draft`, `review`, `revise`, and `finish` (submission).
- **Four reader briefs** in `skills/paper/readers/`, each handed to a fresh context that did not write the text: the checker (does each sentence say what its source says), the challenger (does the claim as worded follow from its test), the stylist and the referee.
- **One loop.** Every reader's report, the author's own red pen and a journal's referee all go through `revise`: numbered points, a disposition for each confirmed at source, the changes, and a re-check of only what changed.
- **Techniques**, short notes read when the case arises: a software or instrument subject, many drafters at once, a style sheet, choosing a venue; and one file per journal in `skills/paper/venues/`.
- **The workspace contract.** A paper lives in its own git repository, the working directory of every session, with three files every drafter reads: `AGENTS.md` (how we work here, and the `sources` block of what may be cited at which version), `paper/outline.md` (the intent, the argument and the section budgets) and `paper/style.md`. The memory files are `STATE.md`, `outline.md`, `claims.md`, `open-questions.md` and `journal.md`. `skeleton/workspace/` is the scaffold.

## The skills

- **`paper`** (`skills/paper/SKILL.md`) is a map of what a scientist does when writing a paper, with one file per stage. The stages are not in order and none is a gate.
- **`literature`** (`skills/literature/SKILL.md`) searches the astronomical literature through ADS/SciX: novelty, closest prior work, support or contradiction for one claim, comparison values with their conventions, and provenance. It keeps a notebook and exports BibTeX verbatim.

Not yet written, and each built when its case arrives: `skills/paper/finish.md` (at submission); the stylist and referee briefs (briefed by hand first, then written from what produced substantive criticism); and the `evidence` skill (how a claim with nothing under it becomes a question with a declared test, and the form in which findings come back from a campaign).

## The tools

- `tools/ads.py` searches ADS/SciX and exports BibTeX byte for byte. Python standard library only; it needs an [ADS/SciX API token](https://ui.adsabs.harvard.edu/user/settings/token).
- `tools/traces.py` is run from the workspace root: `list` collects every trace and gap; `lost` names each trace that disappeared or moved in a change; `lint` checks anchors, pins, paths and citation keys; `stale` reports sections changed since their last independent check. Python standard library only.
- `skeleton/workspace/manuscript/scipaper.sty` is the gap macro.

A paper also needs `latexmk` and a git installation. No third-party Python packages, no node, no MCP client.

## Installation

Install once, globally. Clone this repository, and link each `skills/<name>/` that holds a `SKILL.md` into the harness's skills directory (a catalogue script may do the linking); `skills/_shared/` is data the skills read and is not linked. The installation root, which holds `skills/`, `skeleton/` and `tools/`, is written once in each workspace's `AGENTS.md`, which is the only instruction file and is harness-agnostic. To develop, edit, commit and push in a separate clone, then bring the installed copy forward with `git pull --ff-only` in it; never edit the installed copy.

To begin a paper, ask the agent to start one (the `paper` skill's `start` procedure). It copies the scaffold to a new directory, makes it a git repository, links the sources in, and asks why the work was done and who the paper is for. Commands such as `/paper draft` are shortcuts where a harness offers them; plain conversation works everywhere.

## Design

The reasons for the shape, what is deliberately left out, how components are tested and the decisions settled so far are in [`docs/design.md`](docs/design.md).

## Licence

MIT
