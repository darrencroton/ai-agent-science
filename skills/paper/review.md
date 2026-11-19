# Review

The protocol every reader follows, whichever brief it is given: how a fresh context is commissioned, what it may read, and the form of its report. Read it when commissioning a reader, or when running one by hand. What a reader does with the points afterwards is `skills/paper/revise.md`.

## The protocol

1. **A fresh context that did not write the text** (core rule 3): a subagent, a second session, or another harness. It is never the drafter and never the session that owns the paper.
2. **Read-only.** A reader edits no file of the paper and runs no code (reading, search and read-only git are fine). It writes one thing: its report.
3. **It reads only what its brief allows.**

   | Reader | May read |
   |---|---|
   | Checker | the section, the sources its traces name, `refs.bib`, the papers cited |
   | Challenger | the claims as worded and the sources they rest on |
   | Stylist | the built PDF, `paper/outline.md`, `paper/style.md`, `paper/lit/` and the author's notes |
   | Referee | the PDF, the venue file and genre exemplars; **nothing from `paper/`** |

4. **It writes its report to disk as it goes**, to the path the session gives, so that a reader that runs out of room has still reported. A report held until the end is lost with the reader.
5. **The report is numbered points.** Each has a location, the claim or sentence, the evidence (what the source says, opened and quoted), and the proposed change. Fewer, well-evidenced points beat many weak ones. The session states a length limit in the brief and the reader keeps to it.
6. **`tools/traces.py lint` runs first**, by the session, and its findings are fixed or handed over, so the reader's effort goes on meaning and not on mechanics.
7. **At a milestone** (the first complete run of sections, before the author's read, before submission): a different model from the writer's where one is available, and readers in parallel with staggered starts. Which model takes which seat is written in the workspace `AGENTS.md`.
8. **The record.** A milestone review leaves `paper/reviews/<YYYY-MM-DD>-<slug>/` holding `brief.md`, one report per reader (`<NN>-<reader>.md`) and `dispositions.md`. A routine check of one section leaves one journal line with its count of findings.

## The readers

| Reader | Brief | Asks |
|---|---|---|
| Checker | `skills/paper/readers/checker.md` | does each sentence say what its source says |
| Challenger | `skills/paper/readers/challenger.md` | does the claim as worded follow from its test |
| Stylist | below | is the paper the shape its author intends |
| Referee | below | would a journal accept it, and what would it object to |

**The stylist** (no brief file yet; run it by hand from this paragraph) reads the built PDF as an editor would, against the outline's intent, the section budgets and `paper/style.md`. It starts with a reverse outline: one line per paragraph, giving its point and its length, so that the paper's shape can be read in two pages. It then reports, in at most two pages, what to cut, merge, move and rebalance; where the text has drifted from the intent; what is said twice; what the author's notes hold that the draft lacks; and where the voice slips. It changes nothing, and its report is advice to the author, not an instruction to the agent. Run it at the first complete draft, before the author's own read.

**The referee** (no brief file yet; run it by hand from this paragraph) gets only the PDF, the venue file and a few exemplar papers of the same genre, and nothing from `paper/`. It runs once per angle: the specialist (methods, controls, what is missing); the sceptical generalist (novelty, significance, place in the literature); the journal's editor (scope, length, the norms of the venue and genre); and one chosen for the paper (a statistician, a user of the code, a competitor). It writes in the journal's report form, beginning with a summary of what the paper claims: a referee who summarises it wrongly has found a clarity problem. Then major points, minor points and a recommendation. It can be run early, on the outline and `paper/claims.md` alone, to get the report before the paper is written.

Once a hand run has produced substantive criticism, write the brief for that reader from what worked.

## Testing a reader brief

Run this whenever a reader brief or the model changes, in a live workspace, on its own text.

1. Copy a checked section to `.scratch/` (never to the manuscript).
2. Plant five errors, one of each kind: a changed number; a strengthened quantifier ("some" to "all"); a trace moved to the wrong line; a converted unit; a swapped citation. Keep a list of where each is.
3. Run the reader on the copy, exactly as it would be run on the real section.
4. Count how many of the five it found, and whether anything it reported was wrong.
5. A reader that misses a kind of error gets a stronger brief for that kind. The copy stays in `.scratch/`, which is gitignored.

This measures recall on mechanical errors, which is what the checker and challenger are for. It says nothing about the stylist's or referee's judgement, which is judged against the author's own reading.
