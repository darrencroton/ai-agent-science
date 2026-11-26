---
name: readers
description: Have a document, a claim or a result read by an independent reader that did not write it. Four briefs - checker (does each statement say what its source says), challenger (does a claim as worded follow from what it rests on), referee (would a journal accept this paper or this result, and what would it object to) and stylist (does it communicate to its reader). They work on a paper's sections and equally on a findings report, a plan, a proposal or a result before any paper exists. Use to commission a check, test a claim, simulate a referee or have a document edited for its reader, in a paper or in an investigation. Applying a reader's points to a manuscript is the paper skill (skills/paper/revise.md).
---

# readers

Four independent readers and the protocol they share. Each is a brief handed to a fresh context that did not write what it reads: this skill carries out core rule 3, and `skills/_shared/core.md` holds throughout. Paths are relative to the installation root. Read it when commissioning a reader, or when briefing one by hand.

| Reader | Brief | Asks | Reads |
|---|---|---|---|
| Checker | `skills/readers/checker.md` | does each statement say what its source says | a section of a paper, or any document whose statements cite their sources (a findings report, a ledger, a plan) |
| Challenger | `skills/readers/challenger.md` | does the claim as worded follow from what it rests on | claims with what each rests on, or a question with its declared test |
| Referee | `skills/readers/referee.md` | would a journal accept it, and what would it object to | a paper, excerpts of its outline and claims, or a result before any paper exists |
| Stylist | `skills/readers/stylist.md` | does it communicate to its reader | a paper at any stage, or any document written for someone other than its writer |

## What a reader is given

Whoever commissions a reader supplies these. A paper workspace already holds most of them; outside one (a Campaign Manager under its brief, a Project Manager under its frozen plan) the commissioner's brief or plan supplies them.

- The toolkit's path.
- What is to be read, at a version that cannot change under the reader, and its inputs, each at a pin.
- What may be cited: in a paper, the `sources` block of the workspace `AGENTS.md`; elsewhere, a source policy the commissioner states.
- For a referee, the field and venue material, pinned, since a reader in an investigation may have no network.
- What the read is for, and how long the report may be.
- Where the report goes: a path or, for a reader that cannot write files, returned whole and filed by the commissioner as it came.
- Who confirms each finding at source and disposes of it: in a paper, the session, through `skills/paper/revise.md`; elsewhere, the commissioner within its brief or plan, with what the brief reserves going to the owner.

The steps below that assume a manuscript (`tools/traces.py`, the check stamp, the record under `paper/reviews/`) apply only to one.

## The protocol

1. **A fresh context that did not write the text** (core rule 3). It is never the writer and never the session that owns the work. A reader launched in another harness is confirmed running before the session moves on: a tool can fail at once and say nothing.
2. **Read-only.** A reader edits no file of the work it reads and runs no code (reading, search and read-only git are fine). It writes one thing: its report.
3. **It reads the core, then only what its brief allows, and reads text that cannot change under it.** Each brief carries its own list; the stylist's is its *Modes* table. In a paper, the session commits the text the reader reads, or the PDF is built from (under the workspace's commit policy), and names that commit in the brief, so that `skills/paper/revise.md` can measure every later change against it. Where the policy does not yet allow that commit, the session copies the manuscript's `.tex` files (all of them, so that a trace moved between files is seen as moved), at their workspace paths, into `.scratch/review/<slug>/`, leaves the copy untouched until the round is closed, and names it in the brief in place of the commit, with the pin of each source the text cites; `revise` then measures against the copy. The exceptions are a paragraph plan or an outline read by the stylist, given as a named file that is not changed while it is read, and a seeded test's copy in `.scratch/` (below), which is never revised.
4. **It writes its report to disk as it goes**, to the path the session gives, so that a reader that runs out of room has still reported. A report held until the end is lost with the reader. A reader that cannot write files returns its report whole, and the session files it as it came.
5. **The report is numbered points.** Each has a location, the claim or sentence, the evidence (what the source says, opened and quoted), and the proposed change. Fewer, well-evidenced points beat many weak ones. The session states a length limit in the brief and the reader keeps to it.
6. **For a manuscript, `tools/traces.py lint` runs first**, by the session, and its findings are fixed or handed over, so the reader's effort goes on meaning and not on mechanics.
7. **At a milestone of a paper** (the first complete run of sections, before the author's read, before submission): readers in parallel. Which model takes which seat is written in the workspace `AGENTS.md`. At a milestone the author may also draw an audit sheet, `tools/traces.py sample <n>`: traces chosen by the tool, not the agent, to read beside their sources.
8. **The record, in a paper.** A milestone review, or input from outside the session (a co-author, a journal), leaves `paper/reviews/<YYYY-MM-DD>-<slug>/` holding `brief.md`, one report per reader (`<NN>-<reader>.md`) and `dispositions.md`. A routine check leaves one journal line: what was read (the file, or the passages), at which version (the commit, or for a copy each file's `git hash-object`), what it was for where that is less than the whole, the count of findings, and anything left unchecked.

## Testing a reader brief

Run this whenever the checker's or the challenger's brief, or the model it runs on, changes, in a live workspace, on its own text.

1. Copy a checked section to `.scratch/` (never to the manuscript).
2. Plant five errors, one of each kind: a changed number; a strengthened quantifier ("some" to "all"); a trace moved to the wrong line; a converted unit; a swapped citation. Keep a list of where each is.
3. Run the reader on the copy, exactly as it would be run on the real section.
4. Count how many of the five it found, and whether anything it reported was wrong.
5. A reader that misses a kind of error gets a stronger brief for that kind. The copy stays in `.scratch/`, which is gitignored.

This measures recall on mechanical errors, which is what the checker and challenger are for. It says nothing about the stylist's or referee's judgement, which is judged against the author's own reading.
