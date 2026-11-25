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

Eight commitments define it. The rules that carry them out are in `skills/_shared/core.md`, which every session reads. The reasons and the decisions behind them are in `docs/design.md`.

1. **Trace or gap.** Every checkable statement has its primary source beside it, or an open gap that stays visible until it is closed. There is no third option, and a gap fails the final build.

2. **References come from an authority.** Bibliographic records are exported verbatim from an authority (a literature database, arXiv or a DOI), never composed by a model, and a paper is cited only for what the agent opened and read in it.

3. **The writer does not check itself.** Nothing is called checked until an independent reader that did not write the text has re-opened its sources. What the reader finds is a lead, confirmed at the source before anything changes.

4. **A claim is no stronger than its test.** Correct citations under an overstated claim are an error that checking sources cannot catch, so claim strength is read for separately.

5. **The author decides.** The agent proposes, marks and asks. The argument, the framing, the choice of results and the voice are the scientist's.

6. **Writing does not produce results.** The agent that writes the paper does not run the analysis it reports. Results come from the scientist, or from a separate investigation whose findings arrive with their records.

7. **Shorter, and never by silent omission.** Length is budgeted before the prose exists. A cut keeps every sourced fact or names what it drops, and where what a section must carry will not fit, the author decides.

8. **The record shows who did what.** What the agent did and what the author decided are kept under version control, so that anyone with access can see both.

## The Roles

**The scientist, the orchestrator.** Owns the intent, the argument, the framing and their own voice. Says why the work was done, answers the agents' questions, and audits the result by opening sources, not by proofreading. The toolkit never certifies anything in the scientist's place.

**The agents, the developers.** They draft one section at a time from sources they have opened, search the literature, and keep the records. They own no decision about the science, the framing or the voice.

**The independent readers, the reviewers.** They work from separate briefs, each a fresh context that did not write the text, and at a milestone another model reads where one is available. Each brief asks one of four questions: does each sentence say what its source says, does each claim follow from its test, does the paper read well in the author's voice, would a referee accept it.

## A Parallel with Code Written by AI

A programmer whose agent writes most of the code is still responsible for it, and the profession has the means to make that real.

| In code written with AI | In a paper written with AI |
|---|---|
| A test that fails when the code is wrong | A trace beside each claim, and a visible gap where there is none |
| Review by someone who did not write the change | An independent reader that did not write the text |
| A specification agreed before the code | The outline and the claims agreed before the prose |
| Version control: who changed what, and why | The record of sources, checks and decisions |
| Pinned dependencies and reproducible builds | Sources read at a recorded version |

The engineer is trusted because the code passes tests they understand, has been read by someone else, and has a history they can explain, not because they typed it. A scientist can earn the same trust for a paper.

## Who It Serves

**The scientist who wants to write with agents and sign every sentence.** They get the agents' speed without handing over responsibility, and a way to show that they kept it.

**The scientist who writes by hand.** Nothing here asks them to change. It is a yardstick for the work of those who use agents.

**Editors and referees.** The author can show them the record: the sources used, what the readers found, what the author decided, and a random sample of traces with their sources. That is evidence, not a bare declaration, and needs no detector.

## Design Principles

1. **Empower the agent; do not over-prescribe.** We do not build a brittle system in which everything is controlled, or attempted to be. Every paper is different. The goal is to give the agent the workflow and tools to meet the author's intent; over-engineering is the death of many otherwise useful toolkits.

2. **Grow only where use shows a genuine gap or friction.** The toolkit is simple, transparent and connected, and adds a part only when real use shows that something is missing or in the way.

3. **Responsibility, not keystrokes.** What matters is whether the scientist can answer for every sentence, not who typed it.

The principles of the toolkit's shape (a map, not a pipeline; a tool only where failure is silent; one place for each truth; ordinary technology) are in `docs/design.md` §2.

## What the Toolkit Guarantees, and What It Does Not Claim

**Guaranteed mechanically.** In final mode a gap left in the manuscript stops the build. The trace tool checks the structure of traces (anchors, pins, paths and citation keys), names each trace lost in a change or moved to another file, and flags sections changed since their check stamps. The literature tool exports a reference byte for byte. The author can draw a random sample of traces to audit.

**Claimed as judgement, not mechanism.** Whether a checkable sentence was left with neither trace nor gap, whether a source says what the sentence says, whether a claim follows from its test, whether the paper reads well, and whether a referee would accept it. The readers' findings are leads, and the decisions are the author's.

**Not claimed at all.**

- The readers are only as good as the models behind them, and the author's own audit is the last check.
- It does not make the science right. A source beside a sentence gives somewhere to check; an independent reader checks that the source supports it; neither shows that the source is right or the result matters.
- It does not stop a determined fraud. It makes careless work visible, and does not defend against an author who fabricates a coherent record.
- It does not make writing free. It moves the cost from typing to checking and deciding.
- Confidentiality remains the author's judgement. Sources, drafts and reviews may pass through a model provider, and unpublished data and manuscripts under review are subject to the journal's rules.

## Non-Goals

- **Not an autonomous AI scientist.** It writes up work that someone has done. It does not choose questions or run analyses.
- **Not a detector of AI text.** It makes the work answerable whoever wrote it.
- **Not a consensus guideline or a journal policy.** It is a proposal for how to work, offered for the community to adopt, test and improve.

## Stability Note

Skill names, command names, file layouts, supported harnesses and models are implementation vocabulary and may evolve. The eight commitments are the identity of this repository. Revise this document deliberately or not at all.
