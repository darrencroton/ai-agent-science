# Draft

How one section is written from sources, tracing as it goes and marking every hole. Read it when drafting, whether as a drafter commissioned by the session or as the session itself. A section that reads as finished when it is not is the failure this procedure exists to prevent.

## How settled the text is

Text is in one of three states, shown as its *Status* in `paper/STATE.md`. The state says how much has been spent on the text and what may rest on it.

- **Sketch.** Provisional on purpose: an outline in prose, a sequence of figures, a passage written to find the argument or to show what the paper still needs. Core rule 1 holds (an assertion carries a trace or a gap), and most of a sketch is gaps. It opens with `\gap{todo}{sketch: <what it is for>}` under its heading, so that every build shows its state and the final build refuses it. A sketch needs no plan and no reader, and nothing is built on it.
- **Draft.** Written by this procedure: every source opened, a trace or a gap beside each checkable sentence, the read-back done, the build clean. Nobody else has yet read whether each source says what its sentence says.
- **Checked.** An independent reader has re-opened its traces (`skills/readers/SKILL.md`), and the stamp says when. It is a draft again wherever its wording, its evidence or what it is taken to mean changes (`skills/paper/revise.md`, step 8).

A check is due before anything rests on the text: a decision of the author's, another claim, a framing section that repeats it, a reader from outside the session (a co-author, a journal's referee) and submission, which needs everything checked (`skills/paper/finish.md`). Until then the author chooses when. Criticism of a sketch or a draft (the stylist, the challenger on a claim, a referee on excerpts) needs no check first. While the paper's shape is still moving, a full check of a section buys little, because it is spent again when the section is cut or rewritten.

## Read first

`skills/_shared/core.md`; the workspace `AGENTS.md` (the `sources` block, the build command); `paper/outline.md` (the *Intent*, the *Narrative* and the section's own row); `paper/style.md` (the author's voice) and, once a journal is chosen, `paper/venue.md` (its rules for tables, listings, characters and citations); the section's rows of `paper/claims.md`; and the section's role in `skills/paper/sections.md`. A section with a results role is preceded by the inventory in `skills/paper/evidence.md`. A framing section (conclusions, introduction, abstract, title) is drafted last: see its role there.

Then read the sections already drafted, for the notation and terms the paper already uses and for what it has already said, never as a source (core rule 1). Search them for `\gap{todo}` promises made to this section and keep them. If the section file exists, read it first, with its traces and gaps: filling gaps is edited in place; rewriting author prose is shown to the author and told to go ahead (core rule 5).

## 1. The paragraph plan, before any prose

One line per paragraph: its point, why it follows the one before, and its sources. Keep it to a line each: a plan that quotes its sources or runs to paragraphs is the section written twice. Every item the outline row says the section must carry appears in it, and the plan as a whole delivers the section's hand-off. Sum the lines to an estimate against the budget, and name the lines that may shrink if the section runs long. The plan is written to a file the session names (in `.scratch/` until accepted); the session, not the drafter, sends it to the stylist's plan mode (`skills/readers/stylist.md`) before any prose. A sketch has no plan.

**Coverage beats budget, and the conflict is settled before the prose exists.** If the estimate is over budget the drafter does not choose what to drop (core rule 7). It returns the plan with the overrun and the options: raise the budget; move named items to another section or an appendix; state an item more briefly. The owning session accepts the plan; the author does, for the first section of each role and whenever what the section must carry does not fit its budget. The outline is changed to match. A budget for a section of an unfamiliar kind is a guess, and the plan is where it is corrected cheaply. While the argument is still moving every budget is provisional: report the overrun, and leave the cut until the author has settled the shape, when it is made once (`skills/paper/revise.md`).

## 2. Gather and write

Open every source in this session; write nothing from memory of having read it. Science comes only from the sources the `sources` block allows: the author's notes, figures, tables, code, the subject at its pin, pinned copies and the literature notebook, each cited as core's trace forms say.

- **Notes:** follow the author's stated understanding; what the notes do not settle is a gap. **Tables:** a row is a better source than a value read off a plot.
- **Code:** write what it does, not what it is named or what a note says it does. A line anchor names the symbol that owns the line; a constant belongs to the line that defines it. Where code and the author's notes describe the method differently, give both traces, mark `\gap{q}` and choose neither.
- **Figures:** describe what is plotted, then check it against the caption, the notes and the code that made it. A mismatch is a `\gap{q}`, never a silent choice. A data figure comes from the author or an investigation, with the code that made it, never from the writing agent; a schematic is drafted first for accuracy, every label traced, then restyled without touching its facts. PDF, PNG and JPG are included as they are; a figure that exists only as EPS is converted into `manuscript/figures/` (never into the author's directory), after checking that a sibling file is not a different plot.
- **Trace as you write** (core rule 1): the `% src:` line goes immediately above the sentence; captions and tables carry claims too. A value with no source yet is `\gap{number}{<the command that would produce it>}`. A hole is marked as it is met, with a note saying what would fill it.
- Match the manuscript's own conventions (figure macro, citation commands, label names, section file `manuscript/sections/NN_slug.tex`). Every float has a `\label` and is referred to where it is discussed. Placeholders for figures are a `\gap{todo}` naming what the figure must show.
- A citation is a key that exists in `refs.bib`, or a `\gap{cite}`. The drafter never edits `refs.bib` (core rule 2); it lists each key it used with its identifier.

## 3. Read back, once

The drafter reads its own traces back against the open sources, and only for what a fresh reader would find hardest to see: **the direction of every comparison** (above or below, steeper or shallower), **quantities written as words** ("four", "twice", "half", "an order of magnitude"), and **a figure and the code said to have made it** (the legend, the number of curves, the guide lines and the tick range as well as the label; where they disagree, trace displayed values to the figure and raise a `\gap{q}`). Anything that does not survive becomes a gap, not a softer sentence (core rule 4). Then it reads the prose once against `paper/style.md` (what to avoid, and the exemplar for each kind of paragraph) and against the outline's narrative and the section's hand-off. The rest of the check is not the drafter's: the writer does not check itself (core rule 3).

## 4. Build and report

The build:

- Build with the command in `AGENTS.md`, in a fresh scratch copy of `manuscript/` made outside the workspace, with the section's `\input` added to the copy's `main.tex` (the scaffold's `\input` lines are commented out and `main.tex` is the session's, so the real build may omit the section).
- The session wires the real `main.tex`.
- A draft that compiles with gaps is the target.
- Judge the build by what it adds to `paper/venue.md`'s baseline warnings and run its greps, once a journal is chosen.
- Look at the rendered pages too, since a class can drop a character it cannot print without an error.
- Fix only what this edit broke.
- Where a fix would mean changing author prose, choosing between two versions of a figure or deciding something scientific, stop and report it.

Report in under 400 words:

1. The file written and the PDF's path.
2. Every gap, by kind, with what would fill it. This is the main output.
3. Questions for the author, each with a recommendation and no id: the session assigns ids and writes `paper/open-questions.md`.
4. Keys to export, each with its identifier (bibcode, arXiv id or DOI).
5. Words against the budget, counted with the one counter the workspace `AGENTS.md` names (counters differ by a tenth or more). A section that is running more than about a fifth over its plan's estimate is reported with what the drafter would cut, not cut silently and not padded.
6. Anything the sources disagreed about, anything unreadable, any statement the session made that proved wrong, and any row of the outline the section now contradicts.

A drafter writes its one section file and nothing else. The session writes everything shared: `main.tex`, `refs.bib`, `paper/open-questions.md`, `paper/STATE.md` and the journal. The section is then a draft. Before anything rests on it (*How settled the text is*), it goes to the stylist's section mode, once its shape is settled, and then, with the changes the session accepts, to an independent check (`skills/readers/SKILL.md`).
