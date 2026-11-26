# Vision

This document records why this repository exists, who it serves, the commitments that define it, and the principles that govern its design. It is written to outlive implementation details: skill names, commands, file layouts, harnesses and models will all change, and none of them is load-bearing here. It governs how the toolkit is changed; how a session behaves is governed by `skills/_shared/core.md`. A change that conflicts with a principle here gives way, or this document is deliberately revised.

## Why This Toolkit Exists

The tradition is that scientists write their own papers. A language model may help to edit and improve the text, but the words are ours. Journal policies on AI use follow from that: the model is not an author, the human is accountable, and its use is declared.

The practice has already moved on. More researchers use AI to write more of their papers, some of them all of it, and much of the result is what is now called AI slop. Policies such as these say who is responsible and what to declare, not how a scientist earns the right to sign a paper that a model drafted.

There are two responses. The first is to fight: ban, detect, punish. That is a losing battle. The second is to treat it as an opportunity: AI-enabled writing is coming whatever we do, so we should shape how it is done, and set the rules ourselves.

This toolkit takes the second position. Its claim is that **a scientist can be fully responsible for a paper they did not type**, as an engineer is for code an agent wrote, provided every sentence stays answerable to its evidence and the decisions about the science, the argument and the voice stay with the scientist. The toolkit exists to make that practical.

## Why Agents Need a Toolkit

Agents have become good writers. They still miss the broader context, culture and norms of the field, and they are too verbose: they miss the nuance of what to leave out and what to keep in.

Each gap has a part of the toolkit that answers it. For context and norms, the author's intent, the field's and the journal's norms, the literature and the author's own style are written down for each paper and read by its drafters and readers as their tasks require, so that the agent does not fall back on a generic voice. For verbosity and what to omit, there is the commitment to be shorter without silent omission, and a style loop that reads the plan and the text as they are written.

## What This Toolkit Is

Instructions and briefs for an agent that writes a journal paper with a scientist, two small programs (one for the literature, one for the traces) and a LaTeX package for gaps, for use in any agent harness that reads skills.

It makes the scientist the orchestrator of the writing, as a software engineer manages a developer. The scientist decides; the agents do the legwork; independent readers check what the agents produced.

It works beside the science as the science develops. A paper is often written while the work is still moving: writing is one way the most interesting questions are found, and whole sections are abandoned or rewritten on the way. The toolkit meets the scientist where they are, with every result in hand or with few. A claim with nothing under it becomes a question for the scientist or for a separate investigation, and what comes back re-enters the paper with its record.

It finds what is missing. A gap in the literature, a claim with no test, a number that no output produces, a guide that disagrees with its code: each is handed to the scientist as something to act on. That list is an outcome of the toolkit, not a defect of the draft.

Its parts stand alone. Searching the literature, framing a question and each independent reader can be used outside a paper by anyone who needs one of them. It favours no kind of paper: what a particular paper needs beyond these parts, its agent supplies in its own workspace.

Eight commitments define it. The rules that carry them out are in `skills/_shared/core.md`, which every agent reads; the record a paper keeps is set out in `skills/paper/workspace.md`.

1. **Trace or gap.** Every checkable statement has its primary source beside it, or an open gap that stays visible until it is closed. There is no third option, and a gap fails the final build.

2. **References come from an authority.** Bibliographic records are exported verbatim from an authority (a literature database, arXiv or a DOI), never composed by a model, and a paper is cited only for what the agent opened and read in it.

3. **The writer does not check itself.** Nothing is called checked until an independent reader that did not write the text has re-opened its sources. What the reader finds is a lead, confirmed at the source before anything changes.

4. **A claim is no stronger than its test.** Correct citations under an overstated claim are an error that checking sources cannot catch, so claim strength is read for separately.

5. **The author decides.** The agent proposes, marks and asks. The argument, the framing, the choice of results and the voice are the scientist's.

6. **Writing does not produce results.** The agent that writes the paper does not run the analysis it reports. Results come from the scientist, or from a separate investigation whose findings arrive with their records. The agent's own small read-only checks of what is already pinned in the workspace (a count, a recomputation) are kept with their scripts and checked like any other trace.

7. **Shorter, and never by silent omission.** Length is budgeted before the prose exists. A cut keeps every sourced fact or names what it drops, and where what a section must carry will not fit, the author decides.

8. **The record shows who did what.** What the agent did and what the author decided are kept under version control, so that anyone with access can see both.

Four of them carry an engineering practice over to prose: the trace and its independent check (1 and 3), the owner who decides (5) and the history (8). The other four answer what prose needs and code does not: references and results that a model can invent (2 and 6), a claim that outruns its test (4), and a cut that drops a fact unseen (7).

## The Roles

**The scientist, the orchestrator.** Owns the intent, the argument, the framing and their own voice. Says why the work was done, answers the agents' questions, and audits the result by opening sources, not by proofreading. The toolkit never certifies anything in the scientist's place.

**The agents, the developers.** They draft one section at a time from sources they have opened, search the literature, and keep the records. They own no decision about the science, the framing or the voice.

**The independent readers, the reviewers.** They work from separate briefs, each a fresh context that did not write the text, and at a milestone another model reads where one is available. Each brief asks one of four questions: does each sentence say what its source says, does each claim follow from its test, does the paper read well in the author's voice, would a referee accept it.

## A Parallel with Code Written by AI

A programmer whose agent writes most of the code is still responsible for it, and the profession has the means to make that real.

| In code written with AI | In a paper written with AI |
|---|---|
| A test that fails when the code is wrong | A trace beside each claim, compared with its source by an independent reader; a visible gap where there is no trace |
| Review by someone who did not write the change | An independent reader that did not write the text |
| A specification agreed before the code | The outline and the claims agreed before each pass of drafting, and changed as the science changes |
| Version control: who changed what, and why | The record of sources, checks and decisions |
| Pinned dependencies and reproducible builds | Sources read at a recorded version |

The engineer is trusted because the code passes tests they understand, has been read by someone else, and has a history they can explain, not because they typed it. A scientist can earn the same trust for a paper.

The parallel is not exact. A test gives the same answer each time it is run. The trace is only the test's fixture: the run is a reader's comparison of the sentence with its source, and that is a judgement.

## Who It Serves

**The scientist who wants to write with agents and sign every sentence.** They get the agents' speed without handing over responsibility, and a way to show that they kept it.

**The scientist who writes by hand.** Nothing here asks them to change. It is a yardstick for the work of those who use agents.

**Editors and referees.** The record is the author's to show: the sources used, what the readers found, what the author decided, and a random sample of traces with their sources. Shown, it is evidence where a declaration is only a statement, and it needs no detector. Whether and how it is released is the author's choice at the end of a paper.

**Anyone who needs one part.** A scientist with an idea and no paper yet, or the manager of an investigation who wants a claim tested or a result refereed: each part takes its inputs from whoever commissions it and does not need a paper around it.

## Design Principles

1. **Empower the agent; do not over-prescribe.** We do not build a brittle system in which everything is controlled, or attempted to be. Every paper is different. The goal is to give the agent the workflow and tools to meet the author's intent; over-engineering is the death of many otherwise useful toolkits.

2. **Grow only where use shows a genuine gap or friction.** The toolkit is simple, transparent and connected, and adds a part only when real use shows that something is missing or in the way. What waits, and what was decided against, is recorded in `docs/BACKLOG.md`.

3. **Responsibility, not keystrokes.** What matters is whether the scientist can answer for every sentence, not who typed it.

4. **A map, not a pipeline.** A small core is always read; everything else is read when its case arises. What a use requires is fixed: a claim is independently checked before anything rests on it, and the whole paper before it is submitted. When and how much is read before then is the scientist's call.

5. **A tool only where failure is silent.** A convention is preferred to a procedure, and a procedure to code, except where a failure would otherwise go unseen (a gap left in a submission, a trace lost in a cut, a composed reference); there a deterministic tool is right. The technology is ordinary: Markdown, LaTeX, git and Python's standard library.

6. **One place for each truth.** Anything written twice will disagree. What is true today is kept apart from its history, which git holds.

7. **Generic toolkit, particular workspace.** A sentence belongs in the toolkit only if a paper on a different subject, by a different author, for a different journal would need it; what is particular to one paper lives in its workspace. The toolkit names no subject and holds no paper.

## What the Toolkit Guarantees, and What It Does Not Claim

**Guaranteed mechanically.** In final mode each gap the typesetter reads raises an error, which fails the build as the workspace runs it. The trace tool checks the structure of traces (anchors, pins, paths and citation keys), reports a quoted phrase it cannot find in the text its trace names, names each trace lost in a change or moved to another file, and flags sections changed since their check stamps. The literature tool writes a reference as the authority returned it; nothing later compares the bibliography with that export. The author can draw a random sample of traces to audit.

**Claimed as judgement, not mechanism.** Whether a checkable sentence was left with neither trace nor gap, whether a source says what the sentence says, whether a claim follows from its test, whether the paper reads well, and whether a referee would accept it. The readers' findings are leads, and the decisions are the author's.

**Not claimed at all.**

- The readers are only as good as the models behind them, and the author's own audit is the last check.
- It does not make the science right. A source beside a sentence gives somewhere to check; an independent reader checks that the source supports it; neither shows that the source is right or the result matters.
- It does not stop a determined fraud. It makes careless work visible, and does not defend against an author who fabricates a coherent record.
- It does not make writing free. It moves the cost from typing to checking and deciding.
- Confidentiality remains the author's judgement. Sources, drafts and reviews may pass through a model provider, and unpublished data and manuscripts under review are subject to the journal's rules.

## Non-Goals

- **Not an autonomous AI scientist.** It writes, and it shows what the writing finds missing. The science is done by the scientist or by a separate investigation, finished or still under way. The toolkit does not choose the questions or run the analyses.
- **Not a detector of AI text.** It makes the work answerable whoever wrote it.
- **Not a consensus guideline or a journal policy.** It is a proposal for how to work, offered for the community to adopt, test and improve.

## Stability Note

Skill names, command names, file layouts, supported harnesses and models are implementation vocabulary and may evolve. The eight commitments are the identity of this repository. Revise this document deliberately or not at all.
