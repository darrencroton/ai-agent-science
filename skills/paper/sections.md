# Sections

What each section role must do for its reader. Read the role of the section being drafted (`skills/paper/draft.md`); a section that carries two roles reads both and interleaves them deliberately. The roles are the words in the *Role* column of the sections table in `paper/outline.md`: `methods`, `results`, `discussion`, `framing`. Headings are whatever the paper uses; the outline gives them.

## Methods

*The reader can select the same sample and re-derive the same numbers.* Understanding the approach is not enough.

- **Order:** data, sample, measurement, model, what is held fixed. Each step is answerable without reading ahead.
- **Every cut carries a number and a reason** (resolution limit, completeness, a signal-to-noise floor, matching an earlier sample). If the sources give the threshold and not the reason, write the threshold and mark the reason `\gap{q}`: never invent a plausible justification.
- **State conventions once, explicitly, and never convert** (core rule 1, *Copy, do not convert*): cosmology, scaling conventions, units. Find where the source declares them (notes, code, a table caption), trace it, and state it here as well.
- **Name every piece of software with its version.** A version written down nowhere is `\gap{number}`. A citation for context the sources do not give (the paper that introduced a method or a dataset) is the paper's own choice, found and read through the `literature` skill.
- **The checklist depends on the kind of paper.** Simulation: box size, particle number and mass, softening, snapshots, cosmological parameters, finders and tree builders, physics switched on. Observation: survey and release, area, limits, completeness, redshift determination, selection function. Model: free parameters, what they were tuned against, what was held fixed ("tuned to X" is a load-bearing claim and needs a trace). Software or instrument: what it takes in, what it does, what it assumes, what it does not do, how it was tested. Where the paper is the method, this role carries the argument and there may be no results section.
- **Tense:** past for what was done, present for what the code or model does.
- **Not here:** results, motivation, comparison with other work. A paragraph that argues for something belongs in discussion.

## Results

*The reader can say what was measured and how strongly, without being told what it means.*

One result per paragraph, in this order:

1. **Point at the figure or table first**: `Figure~\ref{fig:x} shows...`. The reader is looking at it as they read.
2. **Say what is seen**, in the plainest words.
3. **Quantify it**: the number, range, slope or significance, with its trace or `\gap{number}`.
4. **Say where it stops being true**: the bin where the statistics run out, the resolution limit, the redshift beyond which the sample is incomplete. A result with no stated limit reads as an overclaim.

- **Never state what the figure does not show.** The common failure is a true sentence, supported by the notes, that the cited figure does not display. Cite what does show it, or drop the reference.
- **A comparison with earlier work is a fact here and an argument in discussion**: "steeper than the slope of `\citet{X}`" belongs here; why they differ does not.
- **Put the caveat in the paragraph with the number** (scatter, the count in the extreme bin, which error bars they are). A caveat collected at the end is skipped.
- **Order results by the argument**, as the outline sets it, not by the order the figures were made. If the figure numbering disagrees, say so and ask; never silently renumber.
- **Not here:** explanation, implications, the limits of the model as opposed to the limits of the measurement.

## Discussion

*The reader can say why the result matters and what would change their mind.*

- **Every point rests on a result the paper established**, not on general knowledge of the field. Rhetorically the sentence refers back to the result ("the rise seen in Figure 4"); scientifically each number or premise in it carries a trace to the original source, never to the results section (core rule 1). A point with no result behind it is `\gap{logic}{no result supports this: it needs <the figure>, or belongs in the introduction}`. This is the commonest fault and invisible from inside the draft, because the author knows the fact the paper never states.
- **The paragraph shape:** what was found, in a clause, by reference; what it means physically, as mechanism and not restatement; how it sits against earlier work, in both directions (a discussion citing only support is the one a referee takes apart); what would break it.
- **Take the alternative explanation in its strongest form**, then say why it is disfavoured; if it cannot be ruled out, say so and open a question.
- **Do not restate results.** A paragraph that is a number and a figure reference belongs in results.
- **Calibrate to the ladder** (core rule 4): is consistent with, suggests, indicates, shows, demonstrates, proves. Pick the rung the evidence reaches and no higher.
- **Weave limitations in beside the claim they limit**, unless the venue requires a separate section. "The model does not include this" is a limitation; "this does not happen" is a result.
- A priority claim ("first shown by") needs the actual first paper, found by the `literature` skill.
- **Not here:** new results, new methods, anything the reader has not been shown.

## Framing: conclusions, introduction, abstract, title

Drafted last and in that order, from `paper/outline.md`, the supportable rows of `paper/claims.md` and the literature reports, and after the body they summarise. They are written with `skills/paper/draft.md` like any section.

- **Every claim made here maps to a claim id and appears in the body with the same value.** The drafter lists each framing claim with its id and where the body states it, in its report. A number in the abstract that the body does not state is a gap. A framing sentence carries the trace the body's sentence has; it never traces to the body.
- **A claim is worded no stronger than the claims table's verdict allows** (core rule 4). A claim marked *unsupported* does not appear, and one marked *if narrowed* appears only in its narrowed wording.
- **Conclusions:** what the body showed and what it does not show. **Nothing appears in the conclusions for the first time**: a conclusion the body does not support is a `\gap{logic}`, not a new paragraph.
- **Introduction:** the field, in the literature's words with exported citations; the gap, claimed only as far as the `literature` skill's report supports it, with what was searched; what this paper does. Its motive is the author's own, from testimony (`notes/`), so much of it is proposed and marked for the author to rewrite: the first paragraph and the last are the author's. A **provisional introduction** may be drafted early, to help find the argument; it comes back heavily gapped and is not checked until the body is.
- **Abstract:** what was done, found and concluded, with only numbers the body states, and no citation the body does not make.
- **Not here:** anything the reader needs in order to follow the body but has not yet met; define it in the body.
