# Revise

The one loop for every reader's points: an independent reader's report, the author's own red pen, an email, a co-author's marked-up PDF, a journal's referee. Read it when any such input arrives. The readers and their protocol are in `skills/paper/review.md`.

## The loop

1. **Save the input verbatim** when it is a milestone review or comes from outside the session (a co-author, a journal): as a review record (`skills/paper/review.md`, step 8). The author's own reading, given in conversation, is saved in their words too. A routine check of one section needs no record.
2. **Split it into numbered points.** One point, one change or one decision. Keep the reader's numbering where it has one.
3. **Confirm each point at source before disposing of it** (core rule 3). Open the file, the paper or the count the point is about. A reader's wrong finding must not become a wrong fix: record what you found, even when it agrees.
4. **Dispose of every point in one table**, `dispositions.md`:

   | Point | What was found at source | Disposition | Change made | Re-checked |
   |---|---|---|---|---|
   | the reader's number and a few words | what the source says, with its location | `accept`, `accept, changed`, `decline` (with the reason), or `author` | the edit, or none | yes, no, or not needed |

   `accept, changed` means the reader was right about the problem and the session chose a different fix.
5. **Bring the author every point that touches the argument, the framing or their own prose** (core rule 5), each with a recommendation; for a journal's referee or a co-author, every disposition goes to the author to decide. A stylist's report is advice to the author. Points the author has not decided stay `author`, and nothing is applied for them.
6. **Apply the accepted changes, and carry each one through** the places that depend on it: `paper/outline.md` where the shape or a budget moved; `paper/claims.md` where a claim's wording or evidence changed; the other sections that rest on or promise the changed text; and the promises between sections, each a `\gap{todo}` under the heading it binds. Say what each change orphans or leaves unsupported.
7. **Run `tools/traces.py lost --rev <the commit the brief names>`** (bare `lost` compares `HEAD` and misses what was committed in the round) and name every trace that disappeared or moved to another file, with its new home or the reason it is gone. Nothing may be lost that a disposition does not name.
8. **Send the changes back to the checker** (`skills/paper/readers/checker.md`, the re-check form). It covers everything changed since the section's last stamp (`git diff <the commit that last changed the stamp line> -- <file>`; `tools/traces.py stale` prints that commit), not only this round's edits. A section with no committed stamp, or one whose pinned sources have moved (a pin changed in the `sources` block), gets a full check; a `fixed` source that has changed since the stamp gets the traces that name it re-checked. Confirm its findings as in step 3. Then write the check stamp (`% checked: <YYYY-MM-DD> <reader>`) near the top of each manuscript file that holds traces (sections and figure files) whose changes were re-checked, and commit it with the text under the commit policy. The new stamp line must differ from the old one: a second check on the same day adds a round (`% checked: <YYYY-MM-DD> r2 <reader>`). `tools/traces.py stale` then shows what has changed since.
9. **Record.** Rewrite `paper/STATE.md`; append the decisions and their reasons to `paper/journal.md`, quoting the author where they decided. Complete the record or journal line as `skills/paper/review.md`, step 8, says.

## Compression is where errors come in

A cut, a merge or a move changes sentences that were checked. So a cut keeps every traced fact, or names the fact as dropped in the dispositions (core rule 7); a merge is re-checked as new text; a moved paragraph keeps its traces, which `lost` verifies. Never accept "shorter" as the reason a fact leaves.

## A journal's referee

The report is saved verbatim in a review record and taken through the same loop, point by point. The reply adds two things: a letter rendered from `dispositions.md`, in which every point names its change, and a `latexdiff` PDF of the manuscript against the submitted version. The procedure for the letter is written at the first real report, from what it needs.
