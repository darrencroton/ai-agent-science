# The venue

Choosing a journal, recording it in `paper/venue.md`, and switching the manuscript to its class. Read it when the author has no journal yet, and again when one is chosen: `paper/venue.md` is written then, once, so that it is current for this paper. Choosing a journal needs no workspace: given what the work does and the closest papers, it returns the shortlist with each journal's facts. Switching a manuscript to a class is the paper's.

## Choosing

Ask the `literature` skill where the closest papers (the build-on question) were published, or use `paper/field.md` if it exists, then read each candidate journal's own pages. Policy pages drift as class files do, so every fact is recorded with its URL and the date fetched.

For each journal quote its scope rather than characterising it, and record what discriminates: length norms; spelling; code and data requirements; the review model, **including anonymity** (a double-anonymous journal can be impossible for a software paper that names its package); cost; the **policy on AI use**, which for a paper where a model is part of the method can outweigh scope and prestige; and turnaround if it can be found. Name the journals ruled out and why, including any archived or closed: a journal that published an obvious precedent may no longer take submissions.

Publisher sites refuse automated readers. Expect `403`; where text was recovered only through a search index, say so and mark it lower confidence; treat a redirect off the publisher's own domain as a failed fetch.

**Return** a short list, each journal with its norms and the papers it published that are closest in kind. **The author decides.** Record the decision and its reason in the journal (a later referee or co-author reopens it), and propose any structural change to `paper/outline.md` for the author.

## Recording it

Once a journal is chosen, write `paper/venue.md` (agent-written, never cited). It holds, for that journal only:

- the facts above, each with its URL and the date fetched;
- its instructions to referees: the criteria referees are asked to judge, the report form, the recommendation categories, and its rules for referees (confidentiality, use of AI), each quoted with its URL and date; where the journal gives no criteria, no form or no categories, the file says so, for the referee brief (`skills/readers/referee.md`);
- after the switch below, the template and the date fetched, each preamble fix, the bibliography style's fix, characters the class cannot print, the class's baseline warnings, the rules for tables, listings and citations, and greps that check conformance.

Its contents are fetched again when the venue changes, and checked for drift before submission. Record the switch in `paper/STATE.md` and the journal as for any decision.

## Switching to the journal's class


1. **Fetch the official bundle** (class, bibliography style, style files) and record the URL and date in the preamble comment and `paper/venue.md`.
2. **Build the bundle's own sample first**, in a scratch directory, before any manuscript text goes near it. A class can fail on a current TeX and the failure then looks like the author's error. Test the bibliography style with a citation: a broken one shows only when the first reference goes in. Record every fix and the class's **baseline warnings** (those the sample itself produces), so that a later build is judged by what it adds to them.
3. **Keep the unmodified originals** and the template's own guide in `manuscript/template-reference/`.
4. **Run `(cd manuscript && latexmk -C main.tex)`** before the first build on the new class: stale auxiliary files survive a switch and give misleading errors.
5. **Switch the preamble.** Fixes go in the preamble with a comment naming what each repairs, and the class is never edited. A bibliography style cannot be patched from the preamble: change the smallest thing, and keep the original beside it. A character an exported reference cannot render is a `\DeclareUnicodeCharacter` in the preamble, never an edit to `refs.bib` (core rule 2).
6. **Add the build's byproducts to `.gitignore`** and record the rules for tables, listings and citations that the class needs.
