# Review

The protocol every reader follows, whichever brief it is given: how a fresh context is commissioned, what it may read, and the form of its report. Read it when commissioning a reader, or when briefing one by hand. What a reader does with the points afterwards is `skills/paper/revise.md`.

## The protocol

1. **A fresh context that did not write the text** (core rule 3). It is never the drafter and never the session that owns the paper. A reader launched in another harness is confirmed running before the session moves on: a tool can fail at once and say nothing.
2. **Read-only.** A reader edits no file of the paper and runs no code (reading, search and read-only git are fine). It writes one thing: its report.
3. **It reads the core, then only what its brief allows, and reads text that cannot change under it.** Each brief carries its own list; the stylist's is its *Modes* table. The session commits the text the reader reads, or the PDF is built from (under the workspace's commit policy), and names that commit in the brief, so that `skills/paper/revise.md` can measure every later change against it. Where the policy does not yet allow that commit, the session copies the files to be read, at their workspace paths, into `.scratch/review/<slug>/`, leaves the copy untouched until the round is closed, and names it in the brief with the pin of each source the text cites; `revise` then measures against the copy. The exceptions are a paragraph plan or an outline read by the stylist, given as a named file that is not changed while it is read, and a seeded test's copy in `.scratch/` (below), which is never revised.
4. **It writes its report to disk as it goes**, to the path the session gives, so that a reader that runs out of room has still reported. A report held until the end is lost with the reader. A reader that cannot write files returns its report whole, and the session files it as it came.
5. **The report is numbered points.** Each has a location, the claim or sentence, the evidence (what the source says, opened and quoted), and the proposed change. Fewer, well-evidenced points beat many weak ones. The session states a length limit in the brief and the reader keeps to it.
6. **`tools/traces.py lint` runs first**, by the session, and its findings are fixed or handed over, so the reader's effort goes on meaning and not on mechanics.
7. **At a milestone** (the first complete run of sections, before the author's read, before submission): readers in parallel. Which model takes which seat is written in the workspace `AGENTS.md`. At a milestone the author may also draw an audit sheet, `tools/traces.py sample <n>`: traces chosen by the tool, not the agent, to read beside their sources.
8. **The record.** A milestone review, or input from outside the session (a co-author, a journal), leaves `paper/reviews/<YYYY-MM-DD>-<slug>/` holding `brief.md`, one report per reader (`<NN>-<reader>.md`) and `dispositions.md`. A routine check of one section leaves one journal line with its count of findings.

## Outside a paper workspace

An investigation may commission a reader too: a Campaign Manager under its brief, a Project Manager under its frozen plan. The protocol is the same, and the binding (the brief or plan) supplies what a workspace would:

- the toolkit's path;
- the document and its inputs, each at a pin;
- what may be cited, which replaces the `sources` block;
- the field and venue material a referee needs, pinned, since a reader in an investigation may have no network;
- where the report goes, a path or, for a reader that cannot write files, returned whole and filed by the commissioner as it came;
- who confirms each finding at source and disposes of it, the commissioner within its brief or plan, with what the brief reserves going to the owner.

Steps that assume a manuscript (`tools/traces.py`, the check stamp, the record under `paper/reviews/`) apply only to one.

## The readers

| Reader | Brief | Asks |
|---|---|---|
| Checker | `skills/readers/checker.md` | does each sentence say what its source says |
| Challenger | `skills/readers/challenger.md` | does the claim as worded follow from its test |
| Stylist | `skills/readers/stylist.md` | how the paper reads, from its story to its sentences |
| Referee | `skills/readers/referee.md` | would a journal accept it, and what would it object to |

## Testing a reader brief

Run this whenever the checker's or the challenger's brief, or the model it runs on, changes, in a live workspace, on its own text.

1. Copy a checked section to `.scratch/` (never to the manuscript).
2. Plant five errors, one of each kind: a changed number; a strengthened quantifier ("some" to "all"); a trace moved to the wrong line; a converted unit; a swapped citation. Keep a list of where each is.
3. Run the reader on the copy, exactly as it would be run on the real section.
4. Count how many of the five it found, and whether anything it reported was wrong.
5. A reader that misses a kind of error gets a stronger brief for that kind. The copy stays in `.scratch/`, which is gitignored.

This measures recall on mechanical errors, which is what the checker and challenger are for. It says nothing about the stylist's or referee's judgement, which is judged against the author's own reading.
