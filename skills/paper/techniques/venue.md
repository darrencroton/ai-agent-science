# A venue

Choosing a journal, and switching the manuscript to its class. Read it when the author has no journal yet (the structural half changes the outline, which is cheap to change before anything is drafted) and again when one is chosen.

## Choosing

Ask the `literature` skill where the closest papers (the build-on question) were published, then read each candidate journal's own pages. Policy pages drift as class files do, so every fact is recorded with its URL and the date fetched.

For each journal quote its scope rather than characterising it, and record what discriminates: length norms; code and data requirements; the review model, **including anonymity** (a double-anonymous journal can be impossible for a software paper that names its package); cost; the **policy on AI use**, which for a paper where a model is part of the method can outweigh scope and prestige; and turnaround if it can be found. Name the journals ruled out and why, including any archived or closed: a journal that published an obvious precedent may no longer take submissions.

Read four to six of the closest papers, closest in *kind* and not in subject, and report each one's actual headings in order, length, figure and table counts, and what the figures do. Name the template they share, where they diverge, and anything the paper has that the template has no slot for, with the precedent for where it goes: that finding is usually the one that matters.

Publisher sites refuse automated readers. Expect `403`; where text was recovered only through a search index, say so and mark it lower confidence; treat a redirect off the publisher's own domain as a failed fetch.

**Return** a short list, each journal with its norms and two or three exemplar papers of the same genre. The exemplars give the stylist and the referee their standard (`skills/paper/review.md`), so they get rows in `paper/lit/index.md` saying what each is an analogue of. **The author decides.** Record the decision and its reason in the journal (a later referee or co-author reopens it), and propose any structural change to `paper/outline.md` for the author.

## Switching to the journal's class

If `skills/paper/venues/<journal>.md` exists, read it first: it holds the fixes and baselines below, found once. Otherwise:

1. **Fetch the official bundle** (class, bibliography style, style files) and record the URL and date in the preamble comment and the journal.
2. **Build the bundle's own sample first**, in a scratch directory, before any manuscript text goes near it. A class can fail on a current TeX and the failure then looks like the author's error. Test the bibliography style with a citation: a broken one shows only when the first reference goes in. Record every fix and the class's **baseline warnings** (those the sample itself produces), so that a later build is judged by what it adds to them.
3. **Keep the unmodified originals** and the template's own guide in `manuscript/template-reference/`.
4. **Run `(cd manuscript && latexmk -C main.tex)`** before the first build on the new class: stale auxiliary files survive a switch and give misleading errors.
5. **Switch the preamble.** Fixes go in the preamble with a comment naming what each repairs, and the class is never edited. A bibliography style cannot be patched from the preamble: change the smallest thing, and keep the original beside it. A character an exported reference cannot render is a `\DeclareUnicodeCharacter` in the preamble, never an edit to `refs.bib` (core rule 2).
6. **Add the build's byproducts to `.gitignore`** and rules for tables, listings and citations that the class needs.

## Recording it

Write `skills/paper/venues/<journal>.md` in the toolkit's source repository, not the installed copy: the template and the date fetched, each preamble fix, the bibliography style's fix, characters, baseline warnings, rules for tables and listings, the citation style, greps that check conformance, and what the journal's referees are asked to judge. Until then, the facts are in the paper's journal. Record the switch in `paper/STATE.md` and the journal as for any decision.
