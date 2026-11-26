# Evidence

What each claim rests on, and how what is missing is got. Read it when a claim has nothing under it, when an investigation's findings arrive, when a result the paper uses has changed, before a section with a results role is planned, and when the author chooses which results the paper shows.

## Claims and what they rest on

`paper/claims.md` holds one row per claim the argument depends on, in the columns its header defines, each claim worded no stronger than its test (core rule 4). A **supportable** row rests on sources the `sources` block lets the paper cite, each openable in one step. An **open** row may name what it has so far, including a root marked `never` (an agent's report, a forward plan), and says so. The verdicts are *supportable*, *if narrowed* (with the narrower wording), *open*, *unsupported* and *withdrawn*. `paper/outline.md` cites rows by id; a claim changes status only in its row.

## A claim with nothing under it

It becomes a question with a declared test, written before anything is run, for the author or for an investigation run elsewhere (a campaign). The question states the claim as a question, the headline result that would answer it and what would count against it; what the literature already says (the `literature` skill: has this been done?); and what its kind of test needs. For a measurement that is what is measured, on what, and what is held fixed; the effective size of the design; each threshold with its reason; and the holdout, named before the first change. A derivation, a check of what a data release covers or a question of provenance has its own equivalents: choose what applies. The challenger's attacks (`skills/paper/readers/challenger.md`) are its checklist: run the challenger on the question before it goes out.

Until the answer arrives the manuscript carries the gap of the kind core's table gives (a missing value is a `\gap{number}` naming the test). The answer updates the row: supportable, if narrowed, unsupported, or still open with what remains missing. A claim is never reworded softer to avoid a test it failed or never had (core rule 4).

## Findings from an investigation

An investigation returns a findings report whose last section lists every file it cites. The workspace `AGENTS.md` says where its dossiers live and the command that copies one. To pin it:

1. Copy the findings, the ledger and every cited file into `campaign-findings/<id>/`, a root marked `fixed` and `cite`, never edited; record the dossier's head commit and the commit of the code it ran.
2. Check that every cited path arrived; a path given with a commit (`path @ <commit>`) is read from that repository at that commit. A missing file that a verdict rests on is named to the investigation's owner, and that verdict stays open until it arrives.
3. Check each verdict against its receipts, recomputing where a small read-only check can, kept under `paper/checks/` (core rule 6).
4. Run the challenger on each claim as the investigation worded it.
5. Add the rows to `paper/claims.md` with both verdicts, the investigation's and the paper's, and write the long reading in `paper/ingest/<id>.md`, which opens with the dossier's head, the code's commit and the date read, and closes with what the investigation did not test; if the subject is still moving, update `paper/ingest/subject-delta.md` (`skills/paper/techniques/subject-repository.md`). The challenger's `as worded` is *supportable*, and its `open` is *open*.
6. Bring the author the results, with a recommendation of which the paper uses.

An investigation may already have run the checker on its findings and the referee on its headline result (`skills/paper/review.md`, *Outside a paper workspace*). That surfaces problems earlier; the paper still checks each verdict against its receipts.

## When a result changes

A result the paper already uses can be replaced: a re-run, a corrected data set, a new release of the subject, a change of mind about which result to show. The old receipt is still valid at its pin, since it records what was measured then, and a replacement at a new path changes no file that a trace names. So no tool reports it, and a new pin says which version is read, not which result now stands. The change therefore comes in through its claim, before any prose is edited:

1. Say what arrived, which rows of `paper/claims.md` it answers and what it supersedes.
2. Pin the new evidence as above, or move the pin in the `sources` block.
3. Reopen each row it touches: the verdict is *open* until the new evidence has been read against the claim as it would now be worded, and the challenger reads any row whose wording changes.
4. List what rests on the old result: the traces that name what was superseded (search `tools/traces.py list` for its paths; `moved` for a root whose pin moved), the sections the outline says carry the claim, the framing sentences that repeat it, the figures made from it, and the promises (`\gap{todo}`) that depend on it.
5. Bring the author the change and its consequences, with a recommendation: a number that moves, a claim that narrows, a section left without its result. The decision is theirs. `skills/paper/revise.md` then applies it, and the text it touches is a draft again (`skills/paper/draft.md`, *How settled the text is*).

## Before a results section

An inventory, before the paragraph plan: for each claim the section must carry, open what it rests on now and ask whether the wording still holds; the challenger reads any row no independent reader has. Corrections go into `paper/claims.md` first, because the drafter is bound to the rows.

## Choosing the results

The author chooses which results the paper shows. The session brings the candidates side by side, each with what it shows, its verdict and what more it would need, and a recommendation. The decision goes into `paper/outline.md`; the stylist's outline mode then proposes the narrative (`skills/paper/readers/stylist.md`).
