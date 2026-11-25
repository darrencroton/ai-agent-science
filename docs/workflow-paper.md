# A workflow for writing science with AI agents: the idea for a paper

*The paper has begun (2026-11-25), in a shorter form than this document proposes, in its own workspace, which holds its intent and decisions. This document is kept as a lead and is no longer maintained.*

The idea for a paper that offers the research community a method: how to write a scientific paper with AI agents so that it meets professional and ethical standards, faster than by hand and without adding to the flood of unverifiable text. ai-agent-science is the method's demonstration, not its subject. This document holds the argument, the context, the prior work found so far, the evidence the paper would need and the decisions still open, so that the paper can be started when the first paper written with the toolkit is mature. It is a record of an idea, not a draft; nothing here is a source.

The owner's intent, in their words (2026-11-21): "I don't want this to be about the repo itself, but the workflow as the community desparatly needs guidance on how to work in this new world and i'd like this paper to offer what i believe is an effective alternative. ai-agent-science can be the demonstration of this workflow, but it shouldn't be a paper just about it."

_Written 2026-11-21, at toolkit v6.1. Prior work was searched on that date, and every arXiv identifier below was checked against its arXiv title; entries marked "abstract" were read at abstract or README level only and must be read in full before the paper cites them._

## 1. The problem

Language models now write a growing share of the scientific literature. That is a gain where it speeds the work and sharpens its focus, and a harm where it produces text nobody can check. Signs of the harm, as found on the date above:

- An analysis of 950,965 papers estimates that LLM-modified text reaches up to 17.5% of computer-science abstracts and up to 6.3% in mathematics and the Nature portfolio (Liang et al. 2024, arXiv:2404.01268; abstract).
- Fabricated references reach accepted papers: one audit found 100 fabricated citations in 53 accepted NeurIPS 2025 papers (Ansari 2026, arXiv:2602.05930; abstract), and another estimates on the order of 10^5 hallucinated citations across 2025 preprints (Zhao et al. 2026, arXiv:2605.07723; seen only as quoted in another project's README, to be read).
- arXiv's computer-science section has required, since 31 October 2025, that review and position papers be peer reviewed first, because language models make them "relatively easy to churn out" (arXiv blog, 2025; read).
- Venues now experiment with AI as author and reviewer (Agents4Science 2025, arXiv:2511.15534; abstract), and reviews themselves are increasingly machine-written (a claim of about a fifth of one conference's reviews, unverified).

The community's guidance so far is mostly policy (to verify across publishers before the paper: one journal's author instructions, read for the first live paper, say that an AI cannot be an author, that its use must be declared, and that the human is accountable). Policy says what must be true and not how to make it true. What is missing is a method: a way of working in which a scientist uses an agent's speed and is still able to put their name to every sentence.

## 2. The argument

**The claim of the paper, as a hypothesis to test** (section 4 names the comparison): a paper written with an agent can be held to a stronger standard of verification than a comparable paper written by hand, at a cost the author can afford, if the work is organised around a small number of rules that separate the roles of author, writer, checker and investigator, and if the text carries its own evidence.

The paper argues for the workflow, not for a tool. Its parts, each stated so that a reader could adopt it with any agent or none:

1. **What "verifiable" must mean.** Four properties, each testable. *Local*: the support for a sentence sits beside it in the manuscript source and is reached in one step (a line of code at a fixed version, a page of a paper, a table in a pinned data file). *Fail-closed*: an unsupported statement is a visible marker that stops the final build, never silence. *Independently re-opened*: someone other than the writer has opened every pointer, and the record says when and against which version of the text. *Cheap to audit*: the author can draw a random sample of sentences with their sources and check them in minutes.
2. **Trace or gap.** Every checkable statement (a number, a named method, a comparison, a quantifier, an absence, anything said about another paper) carries a pointer to a primary source or an explicit gap. There is no third option, and the agent's own notes, summaries and memory are never sources. A gap is honest; a plausible sentence without support is the failure.
3. **The writer does not check itself.** A writer, human or model, cannot see its own errors. Checking is done by fresh readers that did not write the text, each with one question: does each sentence say what its source says; does each claim, as worded, follow from its test; does the paper communicate (its story, the flow of its ideas, its voice); would a referee in this field accept it. Their findings are leads, confirmed at the source before anything changes, and every reader's comments, the author's own included, go through one loop of numbered points and recorded dispositions.
4. **A claim no stronger than its test.** Correct citations under an overstated claim are the error that citation checks cannot catch. Claims are worded against their evidence before prose is written, and a rewrite never strengthens one silently.
5. **Separate writing from producing results.** The agent that writes the paper does not run the analysis it reports. Results come from the author or from a separate, audited investigation whose findings arrive as a pinned record with its receipts. This is the strongest guard against fabricated results, and it keeps the slop problem from becoming a fraud problem.
6. **The author owns the argument and the prose.** The agent proposes; the author decides. Its proposals arrive as questions with recommendations, so that the scarce resource, the author's attention, is spent on decisions and not on reading. The author's voice is learnt from their own papers and kept.
7. **References come from an authority.** Bibliographic records are exported, never composed: a reference the agent typed is a reference that may not exist.
8. **The record is the disclosure.** A git history of decisions, checks and dispositions shows exactly what the agent did and what the author decided, which is what such policies ask authors to declare.

**A worked example, for the paper** (illustrative, not from any real paper). A draft says "the code reproduces the reference results to better than 1 per cent in every configuration", with a trace to a test log. The checker opens the log: it covers three of five configurations, and the largest difference is 1.4 per cent in one. The finding goes to the author with the source quoted and a recommendation; the author narrows the sentence to the three configurations and the measured bound, and asks for the other two to be measured, which becomes a gap naming the command. The checker re-reads only the changed sentence; the record keeps the finding, the decision and the re-check. Nothing in the loop needed the author to read the log, only to decide.

**What the demonstration shows.** ai-agent-science implements the workflow as plain instructions any agent harness can read, a LaTeX macro that makes a gap fail the final build, and two small tools (trace inventory and lint; literature search and verbatim export). It is used to write a real paper, a platform paper in astronomy by a sole author, whose workspace records every check, finding and disposition. The paper would describe the toolkit only as far as needed to show the workflow is practical.

## 3. Prior work

The field is crowded and moving fast. No single idea above is new in isolation; the combination, and the choices listed under *What appears new*, appear to be.

| Work | Year | What it shares | What it lacks or does differently | Read |
|---|---|---|---|---|
| academic-research-skills (open Claude Code skill pack, github.com/Imbad0202/academic-research-skills) | 2025–26 | Almost the same shape: research, write, review, revise, finalise; stops for the author's confirmation at each stage; never runs experiments; a simulated reviewer panel; a traceability matrix for referee responses | Drafts the prose itself; its claim audit against sources is opt-in, and some checks are sampled or made by a model | README |
| data-to-paper (Ifargan et al., arXiv:2404.17605) | 2024 | "Human-verifiable" papers: results traced back to code and data | Autonomous: it runs the analysis and writes the paper; no positioning or referee response | abstract |
| Paper Pilot (Jha et al., arXiv:2608.28596) | 2026 | Human-in-the-loop, evidence-traceable manuscripts; owner gates; an audit log | Advisory model review only; a preliminary evaluation | title and abstract |
| The Agentic Scientist (Lange et al., arXiv:2610.18933) | 2026 | A claim-to-source map checked by a validator; an audit for overclaiming | Autonomous; machine learning only | secondary summary |
| Kosmos (Mitchener et al., arXiv:2511.02824) | 2025 | Every statement cited to code or literature; expert accuracy assessment | Autonomous; reports, not papers | abstract |
| The AI Scientist (Lu et al., arXiv:2408.06292; v2 arXiv:2504.08066) | 2024–25 | End to end, including an automated review | Autonomous; no per-claim provenance | abstract |
| Denario / CMBAgent (astronomy; 2025arXiv251026887V) | 2025 | Most of the research lifecycle, from an astronomy group | Autonomous at the other pole; no per-claim provenance | abstract |
| Agent-Native Research Artifacts (Liu et al., arXiv:2604.24658) | 2026 | Each claim linked to raw output | Replaces the paper with an executable artefact | abstract |
| STORM, PaperQA2, OpenScholar | 2024–26 | Source-grounded synthesis | Literature only; no paper, no verification by a second reader | not read (search results only) |
| showyourwork! (Luger et al., 2021arXiv211006271L, the Doppler-imaging paper that introduced it) | 2021 | Figures linked to the exact code and data; the build as the paper's test | Pre-LLM; figures and data only | read |

**What appears new.** (a) Fail-closed, per-sentence traces in the manuscript source: every checkable sentence, not only numbers or citations, carries a pointer or a gap, and the final build refuses a gap. (b) One trace grammar across source kinds, including the author's dated testimony as a citable source class, for facts only the author knows. (c) The author writes and owns the prose; the agent never manufactures results. (d) Independent fresh-context readers with separate questions (accuracy, claim strength, narrative, referee), including a creative reader for how the paper communicates. (e) Deterministic tools for what fails silently: lint of traces, traces lost in an edit, sections changed since their last check, random audit samples, and verbatim export of references.

**Must engage most closely:** academic-research-skills (the same form, widely used, by its public repository's count: the paper must show concretely what fail-closed traces and independent readers add over opt-in, sampled audits); data-to-paper (the established "human-verifiable" precedent); Paper Pilot and the Agentic Scientist (claim maps and owner gates); and the autonomous systems as the other pole of the design space. Also to read before writing: journal and publisher AI policies (COPE, the major publishers, the target journal), literate programming and executable-paper work, and studies of AI-generated peer review.

## 4. The evidence a paper needs

The workflow covers every stage, but a methods paper's claim must itself be worded no stronger than its test. At the date above the evidence is one paper, unfinished. Needed:

1. **A finished paper written with it**, ideally refereed: its workspace is the case study.
2. **A second paper on a different subject**, the test of what in the method is general and what was particular to the first.
3. **Measures from the record, kept as the work goes:** findings per section by the checker, by kind (wrong, overstated, weak anchor) and how many survived confirmation at source; claims narrowed by the challenger and why; rounds to convergence of each review; gaps opened and closed; traces lost in edits and caught; the share of stylist proposals the author took and declined; the author's restyling of drafted text.
4. **Seeded tests**: errors of named kinds planted in a copy of a checked section, run across models and repeated, to measure the checker's recall and false alarms (two runs so far, each on a different section: three of five found, then five of five).
5. **A baseline**: the same section written by the same agent without the workflow, and by an autonomous system, checked by the same independent reader.
6. **Cost**: the author's time per section, and the compute.
7. **Other authors**: at least one researcher other than the toolkit's author using the method, since the claim is that the community can adopt it.

Of these, (3) and two runs of (4) exist as observations from the first use, and the readers' use under an investigation has been tried once each on hand-written briefs (not yet under a running campaign); the rest are proposed tests. The baseline in (5) includes a comparable paper written by hand and checked by the same independent reader, which the headline hypothesis needs. Success would be stated in advance: for example, the checker's recall and false-alarm rate on seeded errors, the residual error rate a fresh reader finds in a finished section, and the author's time per section against the baseline. Start collecting (3), (4) and (6) now, so that the data exist when the paper is written.

## 5. Beyond one author at a keyboard

The method is meant to work under an unattended agent as well. In the architecture the toolkit belongs to, a Campaign Manager running an investigation stands in the author's seat: where a procedure says the author decides, it takes the recorded recommendation only if the investigation's brief delegates that kind of decision, marks the result provisional, and otherwise leaves a gap and a question. The reader briefs are written to be loaded by an investigation as pinned inputs: the challenger tests a headline claim, the checker audits a findings report's citations, the referee asks whether a result would survive review before a paper is written, and the stylist makes a findings report or a brief readable for the person who must act on it. This is designed (toolkit v6.1 gives every reader brief a rule for being commissioned by an investigation) and not yet exercised under a campaign; no paper has yet been written by one. The paper can present it as the direction, worded as such.

## 6. Limits and ethical position

- **Volume.** Anything that makes writing faster also lowers the cost of producing papers. The workflow's answer is that its cost is in verification and the author's attention, not in generating text; the paper should say this plainly and not claim more.
- **What it does not guarantee.** Traces show that a sentence says what its source says; they cannot show that the source is right, that the science is important or that the framing is the best one. Those remain the author's and the referee's judgements.
- **Model and tool dependence.** The readers are as good as the models that run them; their recall must be measured, not assumed. The demonstration uses LaTeX, git and an astronomy literature service, with general fallbacks; other fields need their own literature tools.
- **One author's taste.** The style and narrative reader is calibrated to one author; its value for others is untested.
- **Accountability.** The author remains answerable for every sentence; the workflow makes that answerability practical, it does not transfer it.
- **Confidentiality.** Sources, drafts and reviews pass through a model provider; unpublished data, others' manuscripts under review and anything confidential need the author's judgement and the venue's rules (the referee instructions of one journal, read for the first live paper, forbid putting a manuscript under review into any AI tool).
- **Disclosure.** The method makes full disclosure easy, and the venue's own statement on AI use sets its form; the paper should model it, including how the paper itself was written.

## 7. Open decisions (the owner's)

- **Audience and venue**: an astronomy methods venue reaches the community the demonstration comes from; a broader meta-science or research-practice venue reaches the community the argument is for. Possibly both: a short general paper and a fuller methods paper.
- **Timing**: when the first paper is submitted or mature, and a second has started.
- **Authorship**: sole, or with collaborators who adopt the method (which also answers point 7 of section 4).
- **Title**: something that names the workflow and the standard, not the toolkit.
- **How it is written**: with the workflow itself, which is both the natural test and the best demonstration.
