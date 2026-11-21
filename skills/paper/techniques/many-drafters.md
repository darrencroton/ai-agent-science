# Many drafters

For a paper whose sections are drafted at the same time by fresh contexts (subagents, second sessions or another harness). Read it before commissioning the first drafter. The procedure each drafter follows is `skills/paper/draft.md`; this is what the session does around them.

## Who writes what

Each drafter follows `skills/paper/draft.md`, which says what it writes and reports; the session numbers and merges the questions (`Q<n>`) and exports the keys once (core rule 2).

## The contract

- Drafters get no separate brief: they read the workspace's own files (`skills/paper/draft.md`, *Read first*).
- A change made while drafters run goes into those files and is sent to each drafter as a message. Every drafter re-reads the files before it reports.
- Tell each drafter only what is particular to its section: the file it owns and its role; its claim ids; the labels it may refer to in other sections, fixed by the outline's slugs so that a forward reference works before the section exists; terms defined elsewhere, and where; promises other sections expect it to keep; which drafted sections to read for notation.
- Every fact the session states is a lead until the drafter has confirmed it at source (core rule 1), and the drafter reports any that were wrong.

## Builds

- Each test build follows `skills/paper/draft.md`, step 4. A reused or in-place copy shows other drafters' edits mid-build.
- Before the first drafter starts, the session gives every undrafted row of the outline a placeholder heading with its fixed label and a `\gap{todo}`, replaced by the `\input` when that section is wired in. Otherwise the first section is numbered "1" and every forward reference prints `??`.

## Order and quality

- Ask each drafter for its paragraph plan first (`skills/paper/draft.md`, step 1); the session takes it through the stylist's plan mode, accepts it or sends it back, then lets the drafter write.
- Match the model to the section: a dense section written from code gets a stronger model than a short one written from notes. The session reviews every draft either way.
- The session wires the sections in order, builds the whole, and only then calls a section drafted.
