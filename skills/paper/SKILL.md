---
name: paper
description: Write a journal paper with an agent so that every checkable sentence is verifiable, in a git-isolated workspace with durable memory. Stages - orient (start: ingest the material, ask why the work was done, propose the argument), position (literature and journal), evidence (test each claim against what it rests on), draft (one section from sources, tracing as it goes), verify (an independent reader re-opens every trace), style and shape, referee (simulated criticism), finish, respond (revise after any reader, including the journal's referee). Use for starting, writing, restructuring, checking or continuing a paper. Literature questions (novelty, prior work, what a paper says, BibTeX) go to the literature skill.
---

# paper

A map of what a scientist does when writing a paper, with one file for each stage. Paths below are relative to the installation root.

Before any work, as the workspace `AGENTS.md` also says: read `paper/STATE.md` in the workspace, then `skills/_shared/core.md`. With no workspace yet, begin at `skills/paper/start.md`. A scientist who returns with something new (a result, a plot, a change of mind) goes to `skills/paper/evidence.md`; comments from any reader go to `skills/paper/revise.md`.

| Stage | What the scientist is doing | Read |
|---|---|---|
| Orient | Deciding what the paper is for | `skills/paper/start.md` |
| Position | Finding its place in the literature and its journal | the `literature` skill; `skills/paper/techniques/field.md`; `skills/paper/techniques/venue.md` |
| Evidence | Checking each claim has something under it; getting what is missing; taking in a result that has changed | `skills/paper/evidence.md`; `skills/paper/readers/challenger.md` |
| Draft | Writing a section | `skills/paper/draft.md`, `skills/paper/sections.md`; `paper/style.md` and `paper/venue.md` in the workspace |
| Verify | Having every trace re-opened | `skills/paper/review.md`, `skills/paper/readers/checker.md` |
| Style and shape | Shaping how the paper reads, from its story to its sentences, while it is planned, written and revised | `skills/paper/readers/stylist.md`, then `skills/paper/revise.md` |
| Referee | Having it attacked | `skills/paper/readers/referee.md`, then `skills/paper/revise.md` |
| Finish | Submitting | `skills/paper/finish.md` |
| Respond | Answering the referee and co-authors | `skills/paper/revise.md` |

The stages are not in order and none is a gate. The agent may leave the map; `skills/_shared/core.md` still holds, and what the paper teaches goes into its own `AGENTS.md`.

## Techniques

Short notes, read only when the case arises.

| Read | When |
|---|---|
| `skills/paper/techniques/subject-repository.md` | the paper describes software or an instrument: pin its version, build the feature map, follow the code where a guide disagrees, keep the delta list, leave detail to the guides |
| `skills/paper/techniques/many-drafters.md` | several drafters write at once: one writer per file, shared files written by the owning session only |
| `skills/paper/techniques/style-sheet.md` | building `paper/style.md` from the author's past papers, once per paper |
| `skills/paper/techniques/field.md` | what papers of this kind contain and what the field accepts, written once per paper to `paper/field.md` |
| `skills/paper/techniques/venue.md` | choosing a journal and recording it, its class and its referee instructions in `paper/venue.md`; switching the manuscript to its class |

Commands such as `/paper draft` are shortcuts where a harness offers them; plain conversation works everywhere, and a session that was never given a command starts in the right place by reading `paper/STATE.md`.
