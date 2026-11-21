# Revise

The one loop for every reader's points: an independent reader's report, the author's own red pen, an email, a co-author's marked-up PDF, a journal's referee. Read it when any such input arrives. The readers and their protocol are in `skills/paper/review.md`.

## The loop

1. **Save the input verbatim** when it is a milestone review or comes from outside the session (a co-author, a journal): as a review record (`skills/paper/review.md`, step 8). The author's own reading, given in conversation, is saved in their words too. A routine check of one section needs no record: its dispositions table is kept in the session, and its counts go in one journal line.
2. **Split it into numbered points.** One point, one change or one decision. Keep the reader's numbering where it has one.
3. **Confirm each point at source before disposing of it** (core rule 3). Open the file, the paper or the count the point is about. A reader's wrong finding must not become a wrong fix: record what you found, even when it agrees.
4. **Dispose of every point in one table**, `dispositions.md`:

   | Point | What was found at source | Disposition | Change made | Re-checked |
   |---|---|---|---|---|
   | the reader's number and a few words | what the source says, with its location | `accept`, `accept, changed`, `decline` (with the reason), or `author` | the edit, or none | yes, no, or not needed |

   `accept, changed` means the reader was right about the problem and the session chose a different fix.
5. **Bring the author every point that touches the argument, the framing or their own prose** (core rule 5), each with a recommendation; for a journal's referee or a co-author, every disposition goes to the author to decide. A stylist's report is disposed of as its brief's *Modes* table says. Points the author has not decided stay `author`, and nothing is applied for them.
6. **Apply the accepted changes, and carry each one through** the places that depend on it: `paper/outline.md` where the shape or a budget moved; `paper/claims.md` where a claim's wording or evidence changed; the other sections that rest on or promise the changed text; and the promises between sections, each a `\gap{todo}` under the heading it binds. Say what each change orphans or leaves unsupported. A cut keeps every traced fact or names it as dropped in the dispositions, a merge is re-checked as new text, and a moved paragraph keeps its traces, which `lost` verifies (step 7). New prose follows `paper/style.md`; where the author rewrote a passage for its voice, update the sheet as `skills/paper/techniques/style-sheet.md`, *Testing it*, says.
Steps 7 and 8 apply where the manuscript changed; a paragraph plan or the outline has no traces.

7. **Run `tools/traces.py lost --rev <the commit the brief names>`** (bare `lost` compares `HEAD` and misses what was committed in the round) and name every trace that disappeared or moved to another file, with its new home or the reason it is gone. Nothing may be lost that a disposition does not name.
8. **Send the changes back to the checker** (`skills/paper/readers/checker.md`, the re-check form). It covers everything changed since the section's last stamp (`git diff <the commit that last changed the stamp line> -- <file>`; `tools/traces.py stale` prints that commit), not only this round's edits. A section with no committed stamp, or one whose pinned sources have moved (a pin changed in the `sources` block), gets a full check; a `fixed` source that has changed since the stamp gets the traces that name it re-checked. Confirm its findings as in step 3. Then write the check stamp (`% checked: <YYYY-MM-DD> <reader>`) near the top of each re-checked file that needs one (`main.tex`, every section file, and any other file with traces or citations, as `stale` reports), and commit it with the text under the commit policy. The new stamp line must differ from the old one: a second check on the same day adds a round (`% checked: <YYYY-MM-DD> r2 <reader>`). `tools/traces.py stale` then shows what has changed since.
9. **Record.** Rewrite `paper/STATE.md`; append the decisions and their reasons to `paper/journal.md`, quoting the author where they decided. Complete the record or journal line as `skills/paper/review.md`, step 8, says.

## A journal's referee

The reply is the dispositions table rendered for the editor, each point naming its change, with a `latexdiff` of the expanded manuscript (`latexpand`, as `skills/paper/finish.md` makes the bundle) against the one expanded at the commit recorded at submission, so that changes inside `\input` files show.
