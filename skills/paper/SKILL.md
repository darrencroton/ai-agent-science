---
name: paper
description: Write a journal paper with an agent so that every checkable sentence is verifiable, in a git-isolated workspace with durable memory, beside science that may still be developing. Stages - orient (start: ingest the material, ask why the work was done, propose the argument), position (literature and journal), evidence (test each claim against what it rests on, turn what is missing into questions, take in results as they arrive or change), draft (a sketch or a section from sources, tracing as it goes), verify (an independent reader re-opens every trace), style and shape, referee (simulated criticism), finish, respond (revise after any reader, including the journal's referee). Use for starting, writing, restructuring, checking or continuing a paper. Literature questions go to the literature skill; an idea with no paper yet goes to the frame skill; an independent read of any document goes to the readers skill.
---

# paper

A map of what a scientist does when writing a paper, with one file for each stage. Paths below are relative to the installation root. The paper skill composes three skills that also work alone: `literature`, `frame` (`skills/frame/SKILL.md`) and `readers` (`skills/readers/SKILL.md`).

Before any work, as the workspace `AGENTS.md` also says: read `paper/STATE.md` in the workspace, then `skills/_shared/core.md` and `skills/paper/workspace.md`. With no workspace yet, or one whose `paper/STATE.md` is still the scaffold's, begin at `skills/paper/start.md`. A scientist who returns with something new (a result, a plot, a change of mind) goes to `skills/paper/evidence.md`; comments from any reader go to `skills/paper/revise.md`.

| Stage | What the scientist is doing | Read |
|---|---|---|
| Orient | Deciding what the paper is for | `skills/paper/start.md`; `skills/frame/SKILL.md` |
| Position | Finding its place in the literature and its journal | the `literature` skill; `skills/paper/techniques/field.md`; `skills/paper/techniques/venue.md` |
| Evidence | Checking each claim has something under it; getting what is missing; taking in a result that has changed | `skills/paper/evidence.md`; `skills/readers/challenger.md` |
| Draft | Writing a section | `skills/paper/draft.md`, `skills/paper/sections.md`; `paper/style.md` and `paper/venue.md` in the workspace |
| Verify | Having every trace re-opened | `skills/readers/SKILL.md`, `skills/readers/checker.md` |
| Style and shape | Shaping how the paper reads, from its story to its sentences, while it is planned, written and revised | `skills/readers/stylist.md`, then `skills/paper/revise.md` |
| Referee | Having it attacked | `skills/readers/referee.md`, then `skills/paper/revise.md` |
| Finish | Submitting | `skills/paper/finish.md` |
| Respond | Answering the referee and co-authors | `skills/paper/revise.md` |

The stages are not in order and none is a gate. How much is spent on a piece of text follows how settled it is: a sketch, a draft, or checked before anything rests on it (`skills/paper/draft.md`). The agent may leave the map; `skills/_shared/core.md` still holds, and what the paper teaches goes into its own `AGENTS.md`.

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
