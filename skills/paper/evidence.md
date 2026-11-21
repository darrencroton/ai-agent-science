# Evidence

What each claim rests on, and how what is missing is got. Read it when a claim has nothing under it, when an investigation's findings arrive, before a section with a results role is planned, and when the author chooses which results the paper shows.

## Claims and what they rest on

`paper/claims.md` holds one row per claim the argument depends on: the claim as the paper may word it (no stronger than its test, core rule 4), what it rests on, and the verdict. A **supportable** row rests on sources the `sources` block lets the paper cite, each openable in one step. An **open** row may name what it has so far, including a root marked `never` (an agent's report, a forward plan), and says so. The verdicts are *supportable*, *if narrowed* (with the narrower wording), *open*, *unsupported* and *withdrawn*. `paper/outline.md` cites rows by id; a claim changes status only in its row.

## A claim with nothing under it

It becomes a question with a declared test, written before anything is run, for the author or for an investigation run elsewhere (a campaign). The question states: the claim as a question, and the headline result that would answer it; what is measured, on what, and what is held fixed; the effective size of the design; each threshold with its reason; the holdout, named before the first change; and what the literature already says (the `literature` skill: has this been done?). The challenger's attacks (`skills/paper/readers/challenger.md`) are its checklist: run the challenger on the question before it goes out.

Until the answer arrives the manuscript carries the gap of the kind core's table gives (a missing value is a `\gap{number}` naming the test). The answer updates the row: supportable, if narrowed, unsupported, or still open with what remains missing. A claim is never reworded softer to avoid a test it failed or never had (core rule 4).

## Findings from an investigation

An investigation returns a findings report whose last section lists every file it cites. The workspace `AGENTS.md` says where its dossiers live and the command that copies one. To pin it:

1. Copy the findings, the ledger and every cited file into `campaign-findings/<id>/`, a root marked `fixed` and `cite`, never edited; record the dossier's head commit and the commit of the code it ran.
2. Check that every cited path arrived; a path given with a commit (`path @ <commit>`) is read from that repository at that commit. A missing file that a verdict rests on is named to the investigation's owner, and that verdict stays open until it arrives.
3. Check each verdict against its receipts, recomputing where a small read-only check can, kept under `paper/checks/` (core rule 6).
4. Run the challenger on each claim as the investigation worded it.
5. Add the rows to `paper/claims.md` with both verdicts, the investigation's and the paper's, and write the long reading in `paper/ingest/<id>.md`, which opens with the dossier's head, the code's commit and the date read, and closes with what the investigation did not test. The *Checked by* cell names who checked the paper's verdict and against what. The challenger's `as worded` is *supportable*.
6. Bring the author the results, with a recommendation of which the paper uses.

## Before a results section

An inventory, before the paragraph plan: for each claim the section must carry, open what it rests on now and ask whether the wording still holds; the challenger reads any row no independent reader has. Corrections go into `paper/claims.md` first, because the drafter is bound to the rows.

## Choosing the results

The author chooses which results the paper shows. The session brings the candidates side by side, each with what it shows, its verdict and what more it would need, and a recommendation. The decision goes into `paper/outline.md`; the stylist's outline mode then proposes the narrative (`skills/paper/readers/stylist.md`).
