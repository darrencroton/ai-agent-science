# Appendix H: implementation record, branch `purpose-fit`

What was built from the reflection, how it was reviewed, and what was left out. Written 2026-11-27 by the session that implemented it, for the owner's review of the branch.

## What changed, by commit

| Commit | Step | What it does |
|---|---|---|
| `7ea6050` | Record | The reflection and the owner's decisions; nothing in the toolkit changes |
| `48785b2` | Vision | `docs/VISION.md` states the whole purpose: beside developing science, finding what is missing, parts that stand alone, no ranking of kinds of paper. The guarantees are worded as the code delivers them. |
| `ddb744b` | Version A | Text is a sketch, a draft or checked, and a check is due before anything rests on it. A reader can be given an untouched copy where no commit is allowed yet. |
| `99ea30c` | Version B | A changed result comes back in through its claim. The state file lists what the paper needs. The challenger gains an `open` verdict and an attack on one-sided evidence. |
| `dc4650b` | Version C | The readers move to `skills/readers/` (paths only) |
| `de06974` | Review | The independent review of A and B applied |
| `c1c3308` | Version C | Four skills that each work alone: `paper`, `literature`, `readers`, `frame`. The core holds the seven portable rules; `skills/paper/workspace.md` holds what a paper adds. |
| `0ee7fc7` | Tools | `traces.py quotes`; one file can be excluded; verbatim listings are skipped; `ads.py` falls back to one bibcode at a time. The review of C applied. The backlog brought up to date. |
| `1e78c71` | Trials | What three live trials showed |
| `15e35ac` | Final review | The whole-branch review applied, and this record |
| `66e6067`, `201e08e`, `a9a7a4b`, `4db28b4` | Confirmation | Faults the reviewer found in the fixes themselves, each fixed with a test |

The reflection's items map onto these as follows. A1 to A7: `ddb744b` and `de06974`. A8 (the quote check): `0ee7fc7`. B1 to B7: `99ea30c` and `de06974`. C1 to C6: `dc4650b`, `c1c3308` and `0ee7fc7`. The contract faults: `0ee7fc7`. The vision changes: `48785b2`.

## Names that differ from the reflection

- **The skill is `readers`, not `review`.** The main harness has a built-in review command, and a skill of the same name would collide with it.
- **The third state is *checked*.** The reflection called it "checked for a named use". The use is recorded in the check's journal line where it is less than the whole file, and a single claim checked ahead of its section is recorded in `paper/claims.md`.
- **The workspace contract is `skills/paper/workspace.md`.** The core keeps its path and its rule numbers 1 to 7, so every existing citation of a core rule still holds. The old rule 8 (memory) is now the opening of the workspace contract.

## Reviews

Each step was reviewed by Codex CLI on `gpt-6.2-sol` at high effort, in its read-only sandbox, reading committed objects. It is a different model provider from the implementer.

| Review | Commits read | Findings marked FIX | Applied | Declined |
|---|---|---|---|---|
| Vision and Version A | `48785b2`, `ddb744b` | 6 | 5 | 1 |
| Version B | `99ea30c` | 6 | 6 | 0 |
| Version C, and the fixes to A and B | `dc4650b`, `c1c3308`, `de06974` | 10 | 10 | 0 |
| The whole branch | `main..0ee7fc7` | 8 | 7 | 1 |
| Four confirmation passes on the fixes | `15e35ac` to `a9a7a4b` | 8 | 8 | 0 |

The reviewer's verdict after the fifth pass, on the whole branch at `4db28b4`: merge-ready, with no new faults.

Bugs the reviews found in new code, each now covered by a test:

- `lost --copy` could report a deleted trace as moved when the copy held only some files, and could compare a file with itself when given an absolute path.
- A commented-out `\begin{verbatim}` could hide real traces, and a check stamp printed inside a listing counted as a stamp.
- A file exclusion with no directory root around it could crash `lint`.
- The export fallback could join two entries on one line.
- Inline verbatim (`\verb`, `\lstinline`) could open a listing that hid the rest of a file, hide a citation after a literal `%`, or show a trace that was read as real.
- The changed-result procedure let a source pin move before the author had decided.

Declined, with the reason:

- **Showing in the built PDF which text is unchecked.** It needs a build mechanism. The PDF is handed over with `stale`'s report and the sections the state file marks draft, and submission is gated by `stale`. Recorded in `docs/BACKLOG.md`.
- **A declared-test checklist for each kind of question.** The owner's decision is that the toolkit favours no kind of paper and the agent supplies what one paper needs. Recorded in `docs/BACKLOG.md`, *Decided against*.

## Live trials

Three fresh agents used the branch as written, read-only.

| Trial | Model | Result |
|---|---|---|
| Frame an idea with no workspace | Sonnet 5.5 | Worked end to end: it read `frame`, ran the literature tool against ADS, commissioned its own challenger and returned a framing that recommended against starting the investigation as worded. |
| Act as a standalone challenger on two claims | Haiku 5.5 | Worked: it returned verdicts with narrowed wordings, and found two real weaknesses in the new tool code. |
| Walk through a paper started while the science is moving | Haiku 5.5 | It routed all four situations correctly: start, sketch, a changed result, one claim checked early. |

Their usability findings were applied in `1e78c71`. They are walk-throughs and single calls, not a paper: no real campaign has yet commissioned a reader from this branch.

## Checks run

- The tools' unit tests: 50 pass (39 on `main`), and several of the 50 gained cases during the confirmation passes.
- `traces.py lint` gives the same result as `main`'s on both real workspaces (no findings in either), so the changes to backticks and listings break no existing trace.
- `traces.py quotes` on the two real workspaces reports 2 of 759 and 11 of 1,057 quoted phrases as not found, and lists the phrases whose source it cannot read.
- Every toolkit path and section named in the toolkit's own text exists.

## Not done, and not tested

- No paper has been written with this branch. The trigger for a check ("before anything rests on the text") is new and is on the backlog to watch.
- The Mermaid diagrams in the README and the reflection have not been rendered.
- Co-authors, `finish.md` and the reply to a journal are as untested as before.
- The framework paper's own workspace is untouched, by the owner's decision. Its files cite the toolkit at the paths of `8bd48c0`.
