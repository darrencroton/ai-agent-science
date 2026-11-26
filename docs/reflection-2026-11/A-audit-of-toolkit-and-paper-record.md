# Appendix A: fresh-eyes audit of the toolkit against the paper's record (requested on Fable 5.2; ran on Opus 5.5)

_Returned whole by the subagent (read-only; read the whole toolkit and the paper workspace at commit dcc3f06). The session asked for Fable 5.2 twice; the harness ran the agent on Opus 5.5 both times. Saved as received, 2026-11-27. The session's check of its claims is in the main document, section 2._

---

# Audit of the ai-agent-science paper toolkit, using the framework paper as evidence

## Summary

The core idea holds up under real use, and the record shows it. Every checkable sentence carries a trace or a gap, an independent checker reopens the sources, each reader's finding is treated as a lead to confirm, and the author decides through questions that come with recommendations. The first full checks found 83 problems in agent prose and the final checks found 25 more. Every one was confirmed at the source before anything changed, and several reader errors were caught that way before they could become wrong fixes.

The weaknesses are in how the work is organised, not in the commitments:

- **Expensive line-by-line verification ran before the paper's structure was settled.** The structural verdict (scope for PASA, missing precursors, a worked example, length) arrived only at the milestone, after about 40 reader passes on the text.
- **The toolkit relies on git for its record, but the workspace made 3 commits in two days.** Several workarounds followed from that.
- **Author gates were designed per section.** The author delegated them after the first section.
- **The stylist's proposals were accepted about 98% of the time by the same session that commissioned them.**
- **Auxiliary text outgrew the paper several times over.**

Most fixes are reorganisation and wording, not new machinery.

---

## What works (keep)

**1. Trace or gap, checked by a reader that did not write the text.** This is the toolkit's value, and the evidence is strong. First full checks by section (journal lines 42, 64–68, 79):

| Section | Traces checked | Findings |
|---|---|---|
| §3 | 60 | 11 |
| §5 | 25 | 12 |
| §6 | 33 | 13 |
| §4 | 49 | 10 |
| §2 | 34 | 16 (14 on §2, 2 on §3) |
| Framing | 72 | 21 |

The findings were substantive, not cosmetic. They include "'largest study' false: confirmed at source" (journal:79), a wrong-page anchor (Spracklen p. 2 → p. 7, journal:71) and "Liu+23 used outside its scope" (journal:87). Without the checker these would have shipped in fluent prose. Rule 3 ("the writer does not check itself") earned its cost here.

**2. "A finding is a lead, confirmed at source."** It worked in both directions:
- The literature reader corrected the simulated referees' own descriptions of sources: "Denario is an assistant, not autonomous; GhostCite and CiteCheck check existence, not support" (journal:84).
- A checker finding was declined at source because "p. 16 in the PDF held, not p. 13" (journal:88).

This is the rule that keeps a confident wrong reader from becoming a wrong edit. Keep it exactly as it is.

**3. References only from an authority.** All 55 entries in refs.bib were exported (journal:84; own-record A12), with no composed reference. When the batch export failed it was visible (subject-notes 11). It did not fail silently.

**4. Literature that narrows claims.** The C1–C3 literature reports returned *if narrowed* for all three claims (journal:35; claims.md lines 9–11). For example, "cannot see its own errors" became "limited without external feedback". This is commitment 4 working before any prose existed.

**5. The author-facing surface is well designed.**
- STATE.md is 33 lines.
- open-questions.md carries Q ids with a recommendation on each.
- "Ask with a recommendation so one reply settles many" worked: one "Please proceed" settled Q17–Q19, Q22 and Q23 (journal:47).
- The milestone dispositions separate what the session applied (groups A–D) from what goes to the author (group E, nothing applied).

This is exactly the design that "the author's attention is the scarce resource" calls for.

**6. The author decided, and could overrule.**
- The author chose narrative N1 over the stylist's preferred N2 (journal:23).
- The author proposed the grouping of the commitments over the session's (journal:33).
- The author's paragraphs (§1 ¶1 and ¶6) are drafted as proposals inside a `\gap{q}`, so the final build fails until the author rewrites or confirms them (01_introduction.tex header). That is a clean mechanical guarantee of rule 5 and worth generalising.

**7. Testimony kept as received.** notes/intent.md kept the author's words, slips included, and confirmed them. It drove the framing (and the "no measured claims" rule, Q3) for the rest of the paper.

**8. Reference files.**
- field.md reshaped the outline to the genre's form: Box 1, a limits section, declarations in the back matter (journal:20).
- venue.md caught the scope risk on day one (journal:17).
- The style sheet's quotations were independently checked: 40 of 40 verbatim (journal:19).

**9. Subject notes as a feedback channel.** Seventeen concrete, located friction reports came out of one paper. Keep this as a standing practice for any software or instrument paper.

**10. The trace tool.** `lost`, `stale`, `moved` and `sample` are the right primitives, and `lint` let readers spend their effort on meaning. The problems with them were caused by the commit policy (below), not by their design.

---

## What does not work

### P1. Structure was verified last and checked first (general; root cause: design and ordering)

The structural problems surfaced at the milestone, after every section had been planned, read by the stylist twice, drafted, checked and rechecked. Group E of the dispositions holds 11 points the author must decide, several of which reshape the paper:

- add a section or table on astronomy-specific failures (E1);
- add a worked results example (E2);
- add "how to start" (E3) and "who it suits" (E4);
- add a comparison table (E8);
- the paper is 11 pages against PASA's typical 10 (Q36).

The general and specialist referees also found direct precursors that the build-on literature search had missed: data-to-paper, Sandve+13, Wilson+17, showyourwork, and the citation-verification tools (dispositions B).

None of this needed a drafted paper:
- venue.md had already flagged "scope risk" at start (journal:17).
- The editor's report says the enquiry should go out "before the draft is built around PASA's norms" (03-referee-editor.md).
- The referee brief already allows an early read of outline and claims excerpts (referee.md:14).
- start.md:30 offers an optional "blind framing read".

Neither the early referee read nor the blind framing read was done; the journal records neither. The tools existed but nothing scheduled them, and the optional step was skipped.

Consequence: whatever the author decides on Q24–Q37 will be applied to text that has already been through stylist reads and full checks, and the changed text must be checked again. This is the most expensive ordering error in the record, and it will recur in any paper whose journal fit or framing is uncertain.

### P2. The toolkit depends on git, but the workspace barely used it (general; root cause: design)

The workspace has **3 commits** across the whole draft. The commit policy, "ask once at the end of each session" (AGENTS.md:32), comes from the author's global rule and is reasonable for a code repository. Here it disabled the toolkit's own machinery:

- review.md:9 requires readers to read committed text. The workaround was git blob hashes and a manifest of hashes (subject-notes 9; milestone brief.md).
- Every check stamp in STATE.md reads "not yet committed". So `stale`, which the toolkit calls "a submission gate", could not be used during drafting.
- 36 appendix counts wait for a commit (STATE.md, *Next* 1).
- Commitment 8 ("the record shows who did what") rests on git, but three omnibus commits cannot show it (subject-notes 5).
- The journal drifted into a work log to fill the gap, against core.md:58 ("no other account of work done, which git holds"). Own-record A9 counts 31 decision lines out of 89; the rest are work narration.
- Bookkeeping by hand slipped: three exports were "recorded late… the session had omitted these lines" (journal:78).

Q21 (checkpoint commits) is still open. The workspace is its own isolated repository and nothing is pushed. Asking for approval on every commit buys almost no safety there, and it costs the record.

### P3. Author gates were designed per section and abandoned after the first one (general; root cause: design)

draft.md:15 has the author accept "the first section of each role" and every conflict over what a section must carry. After §3, the author delegated plan acceptance and point dispositions for every remaining section (journal:50; AGENTS.md:47). From then on the session marked decisions "provisional": 13 such journal lines.

Everything then batched up for the end. At the full draft the author faces **17 open questions** (Q4, Q20, Q21, Q24–Q37) plus 11 E points, several of them structural. The author behaved rationally. The toolkit did not anticipate it: it describes many small gates and no designed delegation. Batching questions at a few deliberate gates is the right model, so design for it.

### P4. Stylist reads were rubber-stamped under delegation (general; root cause: design of who disposes)

stylist.md:12–13 lets the session dispose of plan-mode and section-mode reads. Under delegation the acceptance counts were:

- **Plan reads:** 7 of 7, 5 of 6, 8 of 8, 7 of 7, 9 of 9, 5 of 6, and all 9 framing points (journal:31, 37, 45, 52–54, 73).
- **Section reads:** 10 of 10, 7 of 7, 8 of 8, 9 of 9, 12 of 12, 12 of 12 (journal:40, 59–62, 77).
- **Milestone stylist:** all accepted except one sentence.

That is roughly 120 proposals with about 3 declined. "Confirmed at source" means nothing for a style point. Commitment 5 says the voice is the author's, yet the voice of this paper is one model instance's proposals approved by another instance of the same model, and the author saw none of them.

Two further observations:
- Per-section reads cannot see across sections. The milestone stylist's most useful points were repeats between sections ("kernel in §2 only; Peiris in §1 only…", dispositions D2) and inconsistent terms (D12).
- That cross-section drift is partly caused by the parallel-drafter design, in which no single context holds the whole paper.

### P5. Auxiliary text outgrew the paper (general; root cause: wording, and no designated home)

**Paragraph plans.** draft.md:13 asks for "one line per paragraph". The plans in reviews/ ran to:

| Plan | Words |
|---|---|
| §2 | 4,409 |
| §3 | 3,137 |
| §4 | 3,303 |
| §5 | 2,658 |
| §6 | 3,853 |
| Framing | 8,232 |

That is about 25,600 words of plans for a paper of roughly 8–9k words. In effect each plan was a traced pre-draft in table form, so the sources were gathered and quoted twice.

**Section source.** In sections 1–7, comment characters total about 97k against about 55k of prose. 04_workflow.tex opens with about 55 lines of revision history listing every cut, its reason and which disposition caused it.

The root cause: rule 7 says "a cut names what it drops", but revise.md:7 keeps routine dispositions "in the session", and git held no history, so the drafters put the record in the .tex file. That breaks VISION principle 6 (one place for each truth; history in git). It also makes the file that the author "edits directly and constantly" (AGENTS.md:72) hard for a human to edit.

**Overall.** reviews/, lit/reports, ingest/, field.md, venue.md and style.md total about 93k words. venue.md alone is 7,281 words, most of it notes on fixing the class file.

### P6. "A map, not a pipeline" is only half true (general; root cause: framing and wording)

SKILL.md:24 and README:20 say the stages "are not in order and none is a gate". Inside a section, though, the sequence is mandatory: core.md:70 and draft.md:53 require plan → stylist plan read → draft → stylist section read → checker → re-check, before a section counts as drafted.

The session followed that sequence exactly, for every section. Even the §4 stylist pointed out the contradiction in the paper's own prose (stylist-plan-04/stylist.md point 1). The honest description is a fixed inner section loop inside a flexible outer map.

The stage list also mixes two kinds of thing:
- what a scientist does: orient, position, draft, finish, respond;
- who reads the text: verify, style and shape, referee.

A newcomer reading the nine-row table cannot tell which rows they enter and which are services that run around them.

### P7. Independence is weaker than the commitment implies (general; root cause: a missing default)

All the milestone readers ran on the same model ("no other model is available", milestone brief.md). The specialist referee's first major point was that a fresh context of the same model is a weak independent reader, because of self-preference and correlated failures. The paper now has to concede this in §6 (dispositions C1).

core.md:13 asks for another model only "at a milestone… where one is available", and that was not available here. The briefs also do not cover selective citation: a sentence faithful to a well-chosen source passes both the checker and the challenger (subject-notes 16).

### P8. Outline spine and claims table repeat each other (general but mild; root cause: design)

Outline spine step 1 and claim C1, step 4 and C4, and so on say nearly the same thing twice (outline.md:26–37; claims.md:9–20). That conflicts with principle 6. In this paper, claims C4–C10 were never independently checked ("Checked by" is empty), and the claims table did little work until the challenger read it at the milestone.

That part is specific to this paper: it is a methods paper with no results section. The duplication is general.

### P9. Tool-level faults (general; root cause: implementation)

All are low cost to fix:
- backticked text is read for anchors despite the docstring (subject-notes 15);
- verbatim LaTeX is collected as live traces and gaps (12);
- one bad bibcode fails a whole batch export (11);
- no single file can be declared `never` (1);
- `sample` can be re-drawn with any seed, so "chosen by the tool, not the agent" holds only if the author draws it (14);
- review.md:10 assumes readers can write files, which this harness refused (10).

### Specific to this paper (set aside)

- A subject repository that contains its own workspace (subject-notes 2).
- The commitments renumbered for reading order (8).
- The very high trace density on statements about the framework's own documents. Many opinion sentences carry traces to VISION, for example "In our view a reader from another provider… is a stronger one" (06_guarantees.tex, around line 70). Most papers will trace less densely.
- VISION wording drift (subject-notes 3–7, 17). This is real, but it is documentation hygiene, not workflow design.
- The PASA scope problem itself. The general lesson from it is P1.

---

## Cost and efficiency

My count of fresh contexts from the journal is about **55**, not counting drafters' revision rounds:

| Work | Contexts | Notes |
|---|---|---|
| Ingest | 3 | |
| Field | 1 | |
| Style-quote check | 1 | |
| Literature | about 7 | reports C1, C2, C3, L1, L2, build-on, milestone-sources |
| Stylist | 15 | 1 outline, 7 plan reads (§3 twice), 6 section reads, 1 milestone |
| Drafters | 6 | |
| Checker | 16 | 6 full, about 7 re-checks, 3 final |
| Referees and challenger | 5 | |

**Per section, §3 is typical.** It went through:
1. plan;
2. stylist plan read;
3. author's regrouping and revision 2;
4. stylist plan re-read;
5. draft;
6. stylist section read;
7. revision;
8. full check;
9. re-check;
10. knock-on edits from §2's reads, checked with §2;
11. milestone revision;
12. final check (stamp r3).

That is about ten reader passes on one section of about 1,300 words, before the author has read it.

**Bought assurance:**
- The first full checks: 83 findings, all confirmed and accepted.
- The final checks after the milestone revisions: 25 more (journal:86–88). These show that revision reintroduces errors, so a final check cannot be skipped.
- The milestone challenger: about 13 claim-strength corrections in title, abstract and framing (dispositions A). That is the highest yield per context in the record.
- The literature narrowings of C1–C3.
- The milestone referees' structural points. They bought real assurance, but too late to be cheap.

**Mostly ceremony:**
- **Re-check rounds.** About 7 rounds produced about 9 findings, mostly anchors and cosmetics. Examples: §3 re-check 12 of 12 passed (journal:43); §4 round 3 4 of 4 passed (journal:70). A diff-scoped re-check is worth doing once per revision cycle, not once per round.
- **The second plan read for §3** (journal:37).
- **Running both a plan read and a section read of the same section,** when the section-read points were mostly local trims and the plan-read points were already applied.
- **Session disposition of style points.** It accepted nearly everything, so it added a step without adding judgement.
- **Paragraph plans** at three times the paper's length.
- **Revision logs in .tex headers**, plus a journal written as a work log.

Both exist only because git was not recording.

**A rough split.** About a third of the reader effort (first full checks, the final checks, the milestone challenger and referees, the literature) produced almost all the substantive changes. The remaining two-thirds (repeated stylist reads, re-check rounds, plans) produced polish or nothing. Moving structural review earlier would also have spared the coming re-verification of the E-driven additions.

---

## Fit with scientists

**Where it matches how scientists work:**
- Framing is written last (sections.md:49).
- The section roles (methods: re-derive the numbers; results: say what is seen, quantify it, say where it stops being true; discussion: the alternative in its strongest form) read like a good supervisor's advice.
- The narrative with its hand-offs matches how scientists talk about "the story".
- The dispositions table is the referee-response letter scientists already write.
- The questions-with-recommendations interface matches how a PI wants to be asked.
- Simulated referee angles, especially editor and adopter, are a natural idea to any scientist.

**Where it clashes:**

**Vocabulary.** A first-time user meets a dense layer of coined terms before writing a sentence:
- trace, gap, pin, root, `fixed/cite/never`, stamp;
- session and owning session, brief, reader, challenger, stylist;
- disposition, milestone;
- testimony, direction, standing instruction;
- ingest, spine, hand-off.

Each is precise, but core.md is written so tightly that agents misapply it. The plans ignored "one line per paragraph", and the journal ignored "no account of work done". A scientist reading core.md will struggle more. "Testimony" reads as legal; "author's notes" or "author's record" is what a scientist would say. "Ingest" and "spine" are engineering or editorial words.

**The stage map.** A scientist's mental model is roughly: decide the story and the journal, write, get colleagues' comments, revise, submit, answer the referees. The toolkit's nine stages break "get comments" into three stages named after readers, while hiding the one fixed sequence (the section loop). Neither matches.

**The .tex files.** Scientists live in the .tex (or in Overleaf). A section file that opens with 55 lines of revision history, with comments at twice the volume of the prose, is not something an author will "edit directly and constantly". Traces must stay beside their sentences. The history must leave.

**Artefacts.** The paper/ directory holds:
- STATE, outline, claims, open-questions, journal;
- style, venue, field;
- subject-notes, presubmission-enquiry;
- lit/, ingest/, checks/, reviews/.

That is about fourteen kinds of artefact. A scientist needs to look at three: STATE, open-questions and the PDF. The toolkit already intends this, but it never tells the author that the rest is agent-facing. Say so plainly in the README and in AGENTS.md.

**What a first-time user will trip over:**
1. The commit question at start, and its consequences (P2).
2. Being asked many questions before seeing any prose. A scientist reacts better to a draft than to a specification.
3. The scope: LaTeX, git and a single author, with Overleaf, Word and co-authors out (BACKLOG *Decided against*). This scoping is reasonable, but it caps adoption and should be stated up front.
4. The absence of a figure-first entry point. Many astronomers plan a paper around its figures, but the outline's sections table has no column for figures or tables. They went into "Must carry" here.

**Where imitating human practice is an unnecessary constraint:**
- Humans plan in detail because drafting is expensive. For an agent, drafting is cheap and checking is expensive. A whole gapped draft is cheaper to produce and easier for a human to judge than 25k words of paragraph plans.
- Humans review a paper once or twice because reviewers are scarce. Agents can review constantly, but each review costs author attention whenever it is disposed of properly.
- So the efficient agent workflow is: draft broadly and cheaply, review structure early with the author and the simulated editor or referee, then verify once, thoroughly, when the content is stable.

---

## Structural alternatives I would consider

**A. Two loops with explicit gates.** Replace the nine-row map with five phases a scientist recognises. Name the readers as services each phase calls.

1. **Frame:** intent, journal, field, style, literature, outline and claims. Ends at **Gate 1**: the author approves the story and the journal after an early panel (editor and generalist referee on excerpts, a blind framing read, build-on literature).
2. **Write:** the inner section loop, the only fixed sequence. **Gate 2** is a calibration gate on the first section only: the author reads it and its stylist dispositions, which sets the delegation for the rest.
3. **Review:** the whole-paper milestone panel. **Gate 3**: the author reads the PDF and decides the structural points.
4. **Submit:** freeze the content, run the full check, the author draws the audit sample, the final build. **Gate 4**: submission.
5. **Respond.**

Between gates the session decides provisionally by default, and the toolkit says so.

**B. A cheap whole draft before polishing section by section.** After Gate 1's story is approved, one context writes a gapped zero draft of the whole paper, traced where it is easy and gapped everywhere else. It is the object Gate 1's panel or Gate 2 reacts to, and it is marked as never the author's prose. This fixes cross-section repetition, lets the referees see the real paper early, and replaces most paragraph planning. Parallel drafters then revise sections of a coherent whole rather than write isolated ones.

**C. Verification at content freeze, not at every round.** `lint` and `lost` run continuously; they are mechanical and cheap. The checker does a full check once a section's content is stable, normally after Gate 3, plus one diff-scoped re-check per revision cycle. The challenger reads the claims table before drafting and the framing (title, abstract, introduction, conclusions) at review, where it earned most here. If the author wants an early warning, a single early check on the densest section is enough.

**D. A different relation to git.**
- The agent commits freely in the workspace: checkpoints before every reader commission, never pushing.
- Author approval moves to annotated tags at the gates.
- Commit trailers record who did what (for example a decided-by line for the author's decisions versus the agent's, and the reader that checked).
- Cut lists and routine dispositions go in commit messages.
- The journal shrinks back to decisions only.
- `stale` and `lost` then work as designed, and commitment 8 gains mechanical support.

**E. Fewer, merged artefacts.**
- Merge the outline's *Argument* spine into claims.md as an ordered table with the verdict beside each claim. The outline keeps intent, narrative and sections.
- Fold the *Open* section of STATE into open-questions.md, or the reverse.
- Move venue.md's class-fix notes beside the manuscript, under template-reference/.
- Cap paragraph plans; each line has its point and its anchors, with no quotations.

**F. Readers re-cut by when they pay off.**

| Reader | When |
|---|---|
| Checker | once per section at freeze, plus diff re-checks; another provider at the final check where one exists |
| Challenger | on the claims before drafting and on the framing at review; add a selective-citation attack ("was contrary work sought?") |
| Stylist | outline mode at Frame; one read per section; milestone mode for the whole; the author disposes of the first section's points |
| Referee | editor and generalist on excerpts at Gate 1; the full panel at Gate 3 |

**G. Unit of work.** Keep the section as the unit of drafting and checking, and the sentence as the unit of tracing. Make the claim the unit of the argument (alternative E) and the paper the unit of structural review (alternative B). I would not move to paragraph-level units. The record shows paragraph plans to be the costliest artefact for their yield.

---

## Top 10 recommended changes, ranked

**1. Add a framing gate with an early panel before any section is drafted.** Run the editor and generalist referee angles on outline and claims excerpts, a blind framing read, and the build-on search, then the author approves the story and the journal. The step becomes required, not optional (start.md:30; referee.md:14).
- **Benefit:** catches scope, missing precursors and structural additions (all of E1–E8 here) before about 40 reader passes are spent; the largest saving in the record.
- **Confidence:** high. **Complexity:** low.

**2. Let the agent commit in the workspace; reserve the author's approval for tags at gates.** Recommend this at start in place of an open "how are commits made?". Add trailers that distinguish author decisions from agent work.
- **Benefit:** readers read committed text again (no blob-hash workaround); `stale` and `lost` work during drafting; the journal returns to decisions only; commitment 8 is supported mechanically.
- **Confidence:** high. **Complexity:** low to medium.

**3. Redefine the author's role as four named gates, with provisional delegation as the default between them** (alternative A). Replace draft.md:15's per-role plan acceptance with Gate 2, the first-section calibration.
- **Benefit:** matches what the author actually did; puts the author's attention where judgement matters; avoids 17-question backlogs.
- **Confidence:** high. **Complexity:** low (wording).

**4. Scale the section loop to where it paid off.** Make three changes:
- one stylist read per section, either the plan or the section, not both, with no plan re-reads;
- a full check at content freeze, plus one diff-scoped re-check per revision cycle;
- the challenger always on the framing parts and on claims before drafting.
- **Benefit:** removes about half the reader contexts (re-check rounds, double stylist reads) and keeps every high-yield read.
- **Confidence:** medium to high. **Complexity:** low.

**5. Cap auxiliary text and give the cut record a home.**
- Paragraph plans: at most about 1 line per paragraph with anchors, under a word cap.
- Section header comments: the pin, the stamp and the labels only.
- Named cuts: in dispositions or commit messages.
- venue.md: split from the class-fix notes.
- **Benefit:** a .tex file the author can edit; less context for every drafter and reader; restores principle 6.
- **Confidence:** high. **Complexity:** low.

**6. Have the author dispose of the first section's stylist points and the style-sheet test before delegating style.** About 98% acceptance by the session shows that session disposition of style adds no judgement.
- **Benefit:** the voice becomes demonstrably the author's (commitment 5), and the author's preferences feed into style.md early.
- **Confidence:** medium. **Complexity:** low.

**7. Try a gapped whole-paper zero draft by one context right after the framing gate** (alternative B), replacing most paragraph planning.
- **Benefit:** the author and referees react to the real paper early; fewer cross-section repeats and term drift; uses the agent's cheap drafting rather than imitating human planning.
- **Confidence:** medium (untested here; risks anchoring the author on agent prose, so mark it as never the author's). **Complexity:** medium.

**8. Make another provider the default for the final checker and the challenger where one is reachable.** Record the model on each report. Add a selective-citation attack to the challenger.
- **Benefit:** answers the specialist referee's main objection, which the paper now has to concede; strengthens rule 3 where it matters most.
- **Confidence:** medium. **Complexity:** medium (harness-dependent).

**9. Rewrite the stage map as phases, with readers as services and the section loop named as the only fixed sequence.** Merge the spine into the claims table. Add a figures column to the sections table. Add a one-page glossary that maps the toolkit's terms to a scientist's words, and tell the author which three files are theirs to read.
- **Benefit:** a first-time user can find their place; the "map, not pipeline" claim becomes accurate; one place for the argument.
- **Confidence:** medium. **Complexity:** medium (a documentation rewrite).

**10. Fix the known tool faults.**
- Skip verbatim environments.
- Make backtick parsing match the docstring.
- Fall back to one-at-a-time export and name the failing bibcode.
- Allow file-level `never` roots.
- Have the author draw the audit sample, or derive its seed from the frozen commit.
- In review.md:10, make "return the report whole, the session files it" the normal path.
- **Benefit:** removes six documented workarounds, and closes the audit-seed loophole that the paper had to disclose.
- **Confidence:** high. **Complexity:** low.

**Not recommended:** changing the eight commitments, the trace and gap form, export-only references, or the rule that a finding is a lead. The record supports all of them. The changes above are about when and how often the machinery runs, and where the human stands. They are not about what the machinery is.
