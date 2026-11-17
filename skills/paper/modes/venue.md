# paper — mode: venue

## Before anything

The router's *Before every mode* comes first (`SKILL.md`). This mode searches
with the literature skill's tool and query craft, so read
`skills/literature/SKILL.md` — *The tool* and *Query craft*, and *Mode: mine*'s
fetch ladder — before searching.

*"Where does this go, and what shape should it be?"*

The one mode not about claims. Run it early — the structural half changes the
outline, and an outline is cheap to change before anything is drafted.

Output is **two sections of `paper/outline.md`** — venue, and structure — plus
ordinary rows in `paper/lit/index.md` for the analogues. Not a `<bibcode>.md`.

**Part A — the venues.** Find the journals whose stated scope covers the
paper, and **quote the scope rather than characterising it**, with the URL and
the date fetched; policy pages drift continuously, exactly as journal class
files do. Per venue also record: length norms; code and data availability
requirements; **review model including anonymity** — a double-anonymous
journal can be a hard blocker for a software paper whose package is named in
the abstract; cost; **AI-use policy**, which is now a standard axis and for a
paper where a model is part of the method outranks scope and prestige; and
turnaround if findable. Then name the venues ruled out and why, **including
any that have been archived or closed** — a journal that published an obvious
precedent may no longer accept submissions, and its back catalogue does not
say so.

**Part B — the structure.** Read four to six of the closest analogues —
closest in *kind*, not subject — and report each one's **actual section
headings in order**, length, figure and table counts, and what the figures do.
Then name the invariant template and where the variants diverge: a method
paper, an infrastructure paper, a data-release paper and a comparison project
are four different shapes, and picking the wrong one is a structural problem
no prose fixes. Say explicitly if the paper contains something the template
has **no slot for**, and propose where it goes with the precedent for it —
that is usually the finding that earns the mode its keep.

**Two fetching hazards specific to publisher sites**, on top of the fetch
discipline in the literature skill's *Mode: mine*. Publisher domains are heavily bot-walled: expect
`403`, and where text can only be recovered through a search index rather than
the page, **mark it lower-confidence and say which** — a venue decision can
turn on the difference. And treat a redirect off the publisher's own domain as
a failed fetch; policy URLs have been seen issuing off-domain `302`s.

## Close the session

The analogues get rows in `paper/lit/index.md` (format in `_shared/notebook.md`).
Two things for the close: an analogue's *why* says what it is an analogue **of** (length template, structural
precedent, must-differentiate competitor), and a venue decision carries **its
reason** into `STATE.md` — the reason is what a later session needs when a
referee or co-author reopens it.

Then update `paper/STATE.md` and append the `paper/journal.md` entry, per
`_shared/memory.md`.

## Switching the manuscript to a venue

Once the author has chosen, the manuscript moves from the scaffold's `article` class to the journal's own. Where `_shared/venues/<venue>.md` exists, read it first: it holds the fixes and baselines below, found once, so that they are not found again. `_shared/venues/` belongs to the installation, which is changed only through its development clone (house rules *Locating the installation*), so never edit the installed copy: facts found during a switch are recorded in the paper's journal and then added to the venue file in the development clone.

1. **Fetch the journal's official template bundle** (class, `.bst`, style files) and record the URL and the date fetched, in the preamble comment and in the journal. Templates are revised, and a journal's class files drift exactly as its policy pages do.
2. **Build the template's own sample first**, in a scratch directory, before any manuscript text goes near it. A journal's class can fail on a current TeX, and the failure then looks like the author's error. Record every fix, and the class's **baseline warnings** (the set the sample itself produces), in the journal, so that a later build is judged by what it adds to them. Test the `.bst` the same way, with a citation: a broken style shows only when the first reference goes in.
3. **Keep the unmodified originals** beside the manuscript, in `manuscript/template-reference/`, with the template's own guide.
4. **`(cd manuscript && latexmk -C main.tex)` before the first build on the new class.** Stale `.aux` files survive a class switch and give misleading errors.
5. **Then switch the preamble.** Fixes go in the preamble, with a comment saying what each repairs, and never in the class file. A fix to the `.bst` is the one exception, because a `.bst` cannot be patched from the preamble: change the smallest thing, and keep the original beside it.

Record the switch in `STATE.md` and the journal as for any other close.
