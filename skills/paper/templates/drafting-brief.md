# Drafting brief: <paper short name>, <sections>

<!-- Template. The main session copies this to <ws>/paper/drafting-brief.md, replaces every <placeholder> (each line says what goes there) and deletes these comments. Facts it cannot confirm are marked as leads, never stated. -->

**Revision <n>, <date>.** Re-read this file before you finish: it may have changed while you worked. <Bump the number and date at every change; a changed brief is also sent to running drafters as a message.>

You are drafting ONE section of a journal paper with the `paper` skill. The main session owns the paper, reviews your draft line by line, and does all bookkeeping. You write one `.tex` file and report back.

## The workspace and what to read first (in this order, in full)

Workspace root: `<absolute path>` (WR). Every path below is relative to it. <If the subject repository is reached through a link, say how to write paths into it.>

1. `<root>/skills/paper/modes/draft.md`: follow §1–§5. **Skip §6, §7 and §8**: the main session wires the file in, builds, and updates STATE and the journal.
2. `<root>/skills/_shared/house-rules.md`: the integrity rules and *Source comments*. Binding.
3. `<root>/skills/_shared/sections/<role>.md`: the rhetorical moves for your section's role.
4. `paper/voice.md`, if it exists: the author's voice; its notes for drafting are binding defaults.
5. `paper/STATE.md`; `paper/outline.md` (sole authority for the argument: find your row and what it carries); the open questions that touch your section (`<ids>`).
6. `<any ingest index>`: an index to find sources, never a source.
7. Sections already drafted in `manuscript/sections/`: for terminology and to avoid repetition, never as a source.

## The paper in one paragraph

<What the paper is, its shape, its readers, what it is not about, who writes it.> Your section's role is **<role>**: <what this role does, and what it does not do, which sections carry that instead; forward-reference them rather than doing their work>.

## Version

<The subject's release the anchors are pinned to (tag, commit, date) and any difference between it and the checkout.> If the subject can move, every section file starts with this block, per house-rules *pin a source that moves*:

```latex
% Anchors read against <subject> <version> (<commit>); <state of the checkout>.
% If <path> has moved since, re-read anchors with: <command that shows the pinned file>
```

## Sources

- **Cite:** <the primary sources, with the anchor form for each>.
- **Never cite:** <forward plans, archives, the ingest index, the manuscript itself>.
- **Where a guide and the code disagree,** follow *Found while reading* in the house rules; the ids come from your range below.
- **Never run code.** Where a number exists only as the output of a run, write `\gap{number}{... run: <exact command>}`.
- **Every fact stated in this brief is a lead until you confirm it at source;** the ones the main session has verified are marked **(verified)**. <Mark each.> Report any that were wrong.
- <Claims and limits that must be stated where they arise.>

## Conventions (so several drafters produce one paper)

- **Files:** <section: path>. **Headings** as the outline gives them.
- **Section labels (fixed; usable before the section exists):** <every label in the outline>. Subsection labels `sec:<yours>-<slug>`; figures `fig:<slug>`, tables `tab:<slug>`.
- **Code names:** <how names, files and keys are set>.
- **Citations:** `\citet{<key>}` / `\citep{<key>}`, where the key is the citekey the export produced (the bibcode for ADS records; arXiv and DOI exports key differently, per the literature skill); confirm each key exists before using it. **Never edit `manuscript/refs.bib`**: list each key with its identifier in your report. A scratch build may export them into its own scratch copy only.
- **Figures:** placeholders only, a `\gap{todo}` naming what the figure must show, with a real `\caption` and `\label`. <Tables you may build, and their rules.>
- **Defined terms:** <terms and where each is defined>; use the drafted wording.
- **Question ids:** <section: Qnn to Qnn, one range per drafter>. Do not edit `open-questions.md`; put each question's full text in your report.

## Only the main session writes

`manuscript/main.tex`, `manuscript/refs.bib`, `paper/STATE.md`, `paper/journal.md`, `paper/open-questions.md`. You write your one section file and nothing else.

## Test builds

Only in a fresh copy of `manuscript/` made outside the workspace, **made afresh for each build**: never inside `manuscript/`, and never a copy reused from an earlier build, which shows other agents' edits.

## Length

<Per section: pages and words.> A guide, not a limit: **for a first draft coverage wins over the word target.** <Name what may be compressed.> Count words with `<one counter, one command>`: counters differ by 10 to 25%.

## Style and venue

Match `paper/voice.md` and `<root>/skills/_shared/venues/<venue>.md`. Written here only: <decisions specific to this paper; nothing that is already in those files>.

## Before you finish

Do §5 of the draft mode in full. Re-read this brief.

## Report back (under <n> words)

1. The file written and roughly what it says.
2. **Every gap, by kind, with what would fill it.**
3. Proposed open questions, full text, with their ids and your recommendation for each.
4. Citation keys used, each with its bibcode, arXiv id or DOI.
5. Figures and tables proposed, one line each.
6. Anything the sources disagreed about, anything you could not read, and any statement in this brief that proved wrong.
7. **Toolkit lessons**: friction or gaps in the skills or this brief, one line each.
