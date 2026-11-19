# Many drafters

For a paper whose sections are drafted at the same time by fresh contexts (subagents, second sessions or another harness). Read it before commissioning the first drafter. The procedure each drafter follows is `skills/paper/draft.md`; this is what the session does around them.

## Who writes what

- **One writer per file.** A drafter writes its one section file and nothing else.
- The session alone writes `main.tex`, `refs.bib`, `paper/open-questions.md`, `paper/STATE.md` and `paper/journal.md`, and does the wiring, the bookkeeping and the commit. Nothing a drafter does needs a shared file to change.
- Questions are reported without ids. The session numbers them (`Q<n>`), merges the ones that overlap and writes `paper/open-questions.md`. Keys to export are collected the same way and exported once, verbatim (core rule 2).

## The contract

- It is three workspace files and the section's row, not a separate brief: `AGENTS.md` (sources, pins, the build), `paper/outline.md` (the intent and the row), `paper/style.md`, and the claim rows the section carries.
- A change made while drafters run goes into those files and is sent to each drafter as a message. Every drafter re-reads the files before it reports.
- Tell each drafter only what is particular to its section: the file it owns and its role; its claim ids; the labels it may refer to in other sections, fixed by the outline's slugs so that a forward reference works before the section exists; terms defined elsewhere, and where; promises other sections expect it to keep; which drafted sections to read for notation.
- Every fact the session states is a lead until the drafter has confirmed it at source (core rule 1), and the drafter reports any that were wrong.

## Builds

- Each test build is in a fresh copy of `manuscript/`, made outside the workspace for that build, with the section added to the copy's `main.tex`. A reused or in-place copy shows other drafters' edits mid-build.
- Before the first drafter starts, the session gives every undrafted row of the outline a placeholder heading with its fixed label and a `\gap{todo}`, replaced by the `\input` when that section is wired in. Otherwise the first section is numbered "1" and every forward reference prints `??`.

## Order and quality

- Ask each drafter for its paragraph plan first (`skills/paper/draft.md`, step 1); accept it or send it back, then let it write. An overrun is reported, not trimmed in the drafter.
- Match the model to the section: a dense section written from code gets a stronger model than a short one written from notes. The session reviews every draft either way.
- Each section then goes to an independent check (`skills/paper/review.md`); the session confirms each finding at source, wires the sections in order, builds the whole, and only then calls a section drafted.
