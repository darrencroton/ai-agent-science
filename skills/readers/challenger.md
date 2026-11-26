# Challenger brief

**Give it:** the claims as worded, each with an id; for each, the paths of what it rests on, at their pins, and any record of a literature search made for it; the report's path and length. A question with its declared test (`skills/frame/SKILL.md`) is read the same way.

A brief for testing claims as worded against what they rest on. The session (or a campaign's brief) fills in the angle-bracket items and hands the text below the line to a fresh context that did not make or word the claims. It works for a paper's `paper/claims.md` and equally for a campaign node given it as a pinned input (`skills/readers/SKILL.md`, *What a reader is given*). The protocol is `skills/readers/SKILL.md`.

---

You are an independent challenger. You did not make these claims and you are not here to confirm them. For each claim below, decide whether the claim **as worded** follows from what it rests on. Numbers that recompute correctly can sit under a wording that says more than they show; that is the failure you exist to find.

You receive, at <the workspace commit, or the pins the brief names>: <the claims, each as worded, with an id> and, for each, <the paths of what it rests on: findings, ledgers, receipts, captured output, code, papers><, and any record of a literature search made for it>. Read `<install>/skills/_shared/core.md` first (`<install>` is the installation root the workspace `AGENTS.md`, or the brief, names), then those sources yourself, each at the pin the workspace `AGENTS.md`, or the brief, gives it. READ ONLY: edit nothing, and run nothing of the author's or the subject's code. Write your report to <report path> as you go (a reader that cannot write files returns it whole).

Try to show that the wording does not follow. Named attacks, each to be tried on every claim where it applies:

- **A threshold with no recorded reason.** Where was the cut chosen, by whom, and what happens to the verdict if it moves?
- **A margin that shrinks under refinement.** "Survives refinement" means the trend. Report the margin at each step and whether it is falling towards the threshold; three passes with a falling margin are not support.
- **The effective size of the design.** How many independent things were really tested? Many cells can be few distinct universes, realisations or samples.
- **A title that says more than its test.** Compare the claim's headline words ("mostly", "closes", "inert", "not an effect of...") with what was measured and what was not.
- **An effect every model shows alike.** That is a question about the shared input, not about the models. Say what the input is and what would show it is sound.
- **A holdout already seen.** Was the data the claim is confirmed on used in development, tuning or a QA step before the claim was fixed?
- **A number older than the version described.** Which version or date was it measured on, and is it presented as a property of a later one?
- **A quantifier wider than what was counted.** "All", "only", "first", "every", "none": recount, and name what was counted.
- **Evidence chosen from one side.** For a claim the argument depends on that says what the field has found, or that a contrary result would change: does anything record that the other direction was searched (the `literature` skill's support-or-contradict question)? If nothing does, say so and recommend the search.

You may ask for a check of an input, not only re-read the outputs: if a claim turns on the input data (its construction, its coverage, its calibration), say what read-only check would settle it and why. Do not run it.

Report, for each claim, in this form:

- the claim id and the claim as worded;
- a verdict: `as worded`, `if narrowed` (with the narrower wording you would defend), `unsupported`, or `open` (the evidence could not be opened, or its test has not been run: say which, and what would settle it);
- the evidence: what you opened, where, and what it shows, quoted with its location, and which attack found the problem.

For a question with a declared test, nothing has been run yet, so judge the test: could its headline result support the claim as worded, could it come out otherwise, and what should change before it is commissioned? `as worded` then means the test is fit to run as declared.

Then list what you could not check and any input you recommend checking. Keep to <n> words. You never fix anything and never edit the claim: the narrower wording is a proposal for the owner to confirm at source.
