# Evidence

What each claim rests on, and how what is missing is got. A scientist who returns with something new (a result, a plot, a provisional direction, a change of mind) is asked first what it is meant to establish, what about it is still provisional and what they want the writing to settle; it is then taken in below, as a claim with nothing under it, as findings, or as a change to a result the paper uses. Read it when a claim has nothing under it, when an investigation's findings arrive, when a result the paper uses has changed, before a section with a results role is planned, and when the author chooses which results the paper shows.

## Claims and what they rest on

`paper/claims.md` holds one row per claim the argument depends on, in the columns its header defines, each claim worded no stronger than its test (core rule 4). A **supportable** row rests on sources the `sources` block lets the paper cite, each openable in one step. An **open** row may name what it has so far, including a root marked `never` (an agent's report, a forward plan), and says so. The verdicts are *supportable*, *if narrowed* (with the narrower wording), *open*, *unsupported* and *withdrawn*. `paper/outline.md` cites rows by id; a claim changes status only in its row.

## A claim with nothing under it

It becomes a question with a declared test, written before anything is run, for the author or for an investigation run elsewhere (a campaign). `skills/frame/SKILL.md`, *The declared test*, says what the question states and who reads it before it goes out.

Until the answer arrives the manuscript carries the gap of the kind `skills/paper/workspace.md` gives (*Gap kinds*) (a missing value is a `\gap{number}` naming the test). The answer updates the row: supportable, if narrowed, unsupported, or still open with what remains missing. A claim is never reworded softer to avoid a test it failed or never had (core rule 4).

## Findings from an investigation

An investigation returns a findings report whose last section lists every file it cites. The workspace `AGENTS.md` says where its dossiers live and the command that copies one. To pin it:

1. Copy the findings, the ledger and every cited file into `campaign-findings/<id>/`, a root marked `fixed` and `cite`, never edited; record the dossier's head commit and the commit of the code it ran.
2. Check that every cited path arrived; a path given with a commit (`path @ <commit>`) is read from that repository at that commit. A missing file that a verdict rests on is named to the investigation's owner, and that verdict stays open until it arrives.
3. Check each verdict against its receipts, recomputing where a small read-only check can, kept under `paper/checks/` (core rule 6).
4. Run the challenger on each claim as the investigation worded it.
5. Add the rows to `paper/claims.md` with both verdicts, the investigation's and the paper's, and write the long reading in `paper/ingest/<id>.md`, which opens with the dossier's head, the code's commit and the date read, and closes with what the investigation did not test; if the subject is still moving, update `paper/ingest/subject-delta.md` (`skills/paper/techniques/subject-repository.md`). The challenger's `as worded` is *supportable*, and its `open` is *open*.
6. Bring the author the results, with a recommendation of which the paper uses.

An investigation may already have run the checker on its findings and the referee on its headline result (`skills/readers/SKILL.md`, *What a reader is given*). That surfaces problems earlier; the paper still checks each verdict against its receipts.

## When a result changes

A result the paper already uses can be replaced: a re-run, a corrected data set, a new release of the subject, a change of mind about which result to show. The tools cannot be relied on to notice. A replacement written to a new path changes no file that a trace names, an old receipt may still be a true record of what was measured then, and moving a pin says which version is read, not which result the paper now stands on. The change therefore comes in through its claim, before any prose is edited:

1. Say what arrived, which rows of `paper/claims.md` it answers and what it supersedes.
2. Pin the new evidence: an investigation's findings as above, the author's own output where the `sources` block reads it. A `fixed` file corrected in place has no pin to move, so record the date and what changed. Where a root's pin would have to move, note the proposed pin and leave the `sources` block alone until the author has decided: every trace under the root is read at the pin, not only those the change concerns.
3. Reopen each row it touches: the verdict is *open* until the new evidence has been read against the claim as it would now be worded, and the challenger reads any row whose wording changes.
4. List what rests on the old result: the traces that name what was superseded (search `tools/traces.py list` for its paths; for a root whose pin would move, `tools/traces.py moved --from <the old revision> --to <the proposed one> <root>`, each a bare revision without the `git:` prefix), the sections the outline says carry the claim, the framing sentences that repeat it, the figures made from it, and the promises (`\gap{todo}`) that depend on it. Mark the sections it reaches *draft* in `paper/STATE.md` now, and say why there: their check no longer covers what they will come to say, though `stale` still shows their stamps.
5. Bring the author the change and its consequences, with a recommendation: a number that moves, a claim that narrows, a section left without its result. The decision is theirs, and no prose changes before it. If they keep the old result, each row and each section returns to what it was, with one journal line, but only where its old evidence still stands: a file that was overwritten in place is no longer what was checked. A pin moves only then, and `skills/paper/revise.md` applies the change, measured against a commit or a copy made before the first edit.

## Before a results section

An inventory, before the paragraph plan: for each claim the section must carry, open what it rests on now and ask whether the wording still holds; the challenger reads any row no independent reader has. Corrections go into `paper/claims.md` first, because the drafter is bound to the rows.

## Choosing the results

The author chooses which results the paper shows. The session brings the candidates side by side, each with what it shows, its verdict and what more it would need, and a recommendation. The decision goes into `paper/outline.md`; the stylist's outline mode then proposes the narrative (`skills/readers/stylist.md`).
