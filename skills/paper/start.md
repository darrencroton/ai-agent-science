# Start

How a new paper is oriented: the workspace made, the material read, the author asked why the work was done, and an argument proposed for the author to correct. Read it once, when there is no `paper/STATE.md` yet. A workspace that exists is resumed by reading its `paper/STATE.md`, not by starting again. A short outline and a long list of questions is a good outcome: the material is usually thin and untidy.

Read `skills/_shared/core.md` first.

## 1. Make the workspace

The session works in the workspace, which is its working directory. Ask the author which git repository, if any, will contain it, then which directory it is, offering a default: that repository's directory name with `-paper-workspace` appended or, with none, the paper's short name with `-paper-workspace` appended.

1. Copy the scaffold without overwriting anything: `cp -Rn <install>/skeleton/paper-workspace/. <directory>/` (`<install>` is the installation root), then `git init` there. Write the installation root into `AGENTS.md` where the scaffold names it, and the paper's short name where the scaffold has placeholders. Create `manuscript/sections/` and `manuscript/figures/`, which git cannot ship empty. Say which files were already there and left alone.
2. If the workspace sits inside another repository, add it to that repository's `.git/info/exclude` (local, untracked), never to its tracked files, unless the author asks otherwise. Nothing the toolkit writes may reach another repository's history.
3. Ask once how commits are to be made here, and write the answer under `## Commit policy` in `AGENTS.md`, once the author has confirmed the text (core, *What the author says*). Say what the choice costs: a reader needs text that cannot change under it, so a policy with no commit before a read means reading from copies (`skills/readers/SKILL.md`, step 3), and a check stamp counts as uncommitted until its commit is made. Make the first commit only under that policy.
4. Link or copy each source inside the workspace, so that no path begins with `../`: a live repository is a symbolic link, a folder of notes or figures may be either. The author's own files are used where they are and never moved or tidied. Write the `sources` block of `AGENTS.md`: one line per source, in the form its *Sources* section gives. Keep the scaffold's lines for the workspace's own directories. Forward plans, archives and anything an agent wrote about the sources are `never`.
5. A paper whose subject is a repository also reads `skills/paper/techniques/subject-repository.md` now.

## 2. Read the material

Count before listing: a data directory may hold millions of files, so count it and read only what the author points at. Report what is there (notes, figures, code, tables) before reading it.

- **Notes and tables, in full.** Mark each claim that carries a number and where the number came from. A note that maps onto no result or figure is a question. For each table record the columns, their units and any scaling convention.
- **Every figure, by looking at it.** PDF and PNG are read directly; EPS and PostScript are converted into `.scratch/` first (`gs -dEPSCrop`, whose absence gives a mostly blank page). Record the axes with units, what each line and colour is, what it shows and where the trend stops, and whether the axis labels, the caption and the notes agree with what appears to be plotted. A mismatch is a question.
- **Code, read and never run** (core rule 6): what it computes, its constants and cuts, what each axis plots. A data binding that cannot be resolved is said to be unresolved.
- **Large material goes to parallel readers**, one question each (for a repository: capabilities, history, recorded evidence, development method, products). Each writes an index note into `paper/ingest/` as it goes, not at the end, cites file and place for everything it reports, and ends with what it did not read. The notes are indexes: no trace points at them (core rule 1). Each opens with the pin and date it was read at and the sections it serves. When the pin moves it says so and is kept only as a lead for sections not yet written; it is archived once every section it serves is checked, after its remaining leads are carried forward and every reference to it is updated.

## 3. Ask before proposing

Before any claim is proposed, ask the author in one message: why was this work done; what surprised you; what is settled and what is still open or under way; what you most want the writing to settle; who must be convinced; who are the authors. Record each answer once, where core says (*What the author says*): the reason for the work and what surprised the author as testimony in `notes/<slug>.md`, the reader to be convinced in the outline's *Intent*, the authors in `manuscript/main.tex`, where the scaffold has the placeholder; the introduction will rest on them. What is still open is normal and is recorded as it is: an *open* row in `paper/claims.md` and a question, never a guess (`skills/paper/evidence.md`). A framing built from the material alone has been wrong where the author's reason was different, however many readers agreed.

Optionally commission a **blind framing read**: a fresh context given the material and no framing, asked what paper it would write and what a referee would say. It costs little and shows whether the framing is in the material or in the session's head.

## 4. Propose

Write, as proposals for the author to correct:

- **`paper/outline.md`.**
  - *Intent* first, drawn from step 3's testimony and confirmed by the author before it stands (core, *What the author says*).
  - Then the spine: one line per step of the argument, each naming what it rests on; a step resting on nothing is the paper's real open question.
  - Then the sections table, as the outline's *Sections* header defines it.
  - Budgets are guesses that the first paragraph plan corrects (`skills/paper/draft.md`).
  - The *Narrative*, one paragraph telling the paper's story to the reader the intent names, and the hand-offs come from the stylist's outline mode (`skills/readers/stylist.md`), commissioned once the intent and spine exist and `paper/field.md` names its exemplars, before the first paragraph plan; until then they are left empty.
- **`paper/claims.md`**: first rows, most of them unverified, each with what it would rest on.
- **`paper/open-questions.md`**: everything that could not be worked out, each with a recommendation and a short `Q<n>` id: a number no figure or code produces, two notes that disagree, a figure nothing explains, an unstated convention, a cut with no reason, the paper's evident point with nothing behind it. **Never invent a result to fill a hole**: if the notes do not say what was found, the paper does not yet know.
- **A first journal entry** recording the decisions made so far.

Build the reference files (core, *The workspace*) as each is needed. Once the field and genre are clear, `skills/paper/techniques/field.md` writes `paper/field.md`; the form its papers take can change the outline, so it is worth running early. Ask once which journal; "not decided yet" is an answer; `skills/paper/techniques/venue.md` finds one and writes `paper/venue.md`. Ask once whether the paper should sound like the author's own work; if so, `skills/paper/techniques/style-sheet.md` builds `paper/style.md` before anything is drafted.

## 5. What the author sees

One page: the proposed intent and spine, the narratives the stylist proposed (once it has read), the framings considered and why the first was chosen, and the questions with recommendations, most blocking first. Then ask whether the framing feels right: it is the author's decision, and a wrong one found now costs a sentence.

Criticism is cheapest now, while the paper is a page. Where the journal's scope, the novelty or the strength of a claim is in doubt, offer it before anything is drafted: the blind framing read (step 3); the `literature` skill's novelty and build-on questions; the challenger on the claims as worded (`skills/readers/challenger.md`); a referee's angle on excerpts of the outline and the claims, the editor's for scope (`skills/readers/referee.md`). The author chooses which, if any. Say what to do next: where claims have nothing under them, `skills/paper/evidence.md`; otherwise usually the draft of the section with the most material (`skills/paper/draft.md`).

Close as core, *Start and end of a session*, says.
