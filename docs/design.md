# Design

Why ai-agent-science is shaped as it is: the problem, what "verifiable" means, the principles, the shape, the boundary with the engine that runs campaigns, what is left out, how it is tested, and the decisions settled. It is a design, not a history; the earlier Plan is archived and git keeps it. Read it before changing the shape of the toolkit. The files themselves are the rules.

**In one paragraph.** A paper is verifiable when every checkable sentence carries, beside it, a pointer to the primary source it rests on or a visible marker that it rests on nothing yet, and when someone other than the writer has opened those pointers. Everything else serves that, or serves the author's attention. The toolkit is one page of rules that is always read; a one-page map; six short procedures; four reader briefs handed to a fresh context; a literature skill; and two small deterministic tools. All feedback on the paper, from the trace checker to a journal's referee, goes through one loop. The paper's own rules live in its workspace, in three files that every drafter reads.

## 1. The problem

### What a scientist does

Writing a paper is not a pipeline. A scientist starts early, often before the results are in, and circles: decides what the paper is for (one claim, one reader, one venue in mind, which changes as the work is understood and is the author's alone); positions it in the literature; assembles the evidence, including new analysis where a claim has nothing under it; writes sections, methods and results first, framing last; reads the whole and reshapes it, which is most of the work and never happens only once; has it attacked before a referee does; and finally formats, submits and answers the referee. The author knows the work best and the surrounding literature less well than they would like.

### Where an agent helps

The legwork. Reading a large body of material and returning an index into it. Literature search and the novelty check, which can change an experiment before it runs. Drafting dense methods prose directly from code with a pointer beside every sentence. Checking: in the first paper written with this toolkit, independent checkers found wrong statements, many overstatements and weak anchors in every section they read, and every finding was real. Bookkeeping: questions with recommendations, promises between sections, a journal's broken class file. Simulated criticism: a two-model panel caught failures that the trace check missed.

### Where an agent reliably fails

Each of these was seen in that first paper.

| Failure | What it looked like |
|---|---|
| It writes too much | Every drafter overran its target, one by a third, another by well over double |
| It drifts from the author's intent | Six readers and an independent model converged on one headline; the author wanted another, and only the author's own account of why the work was done showed it |
| It loses the big picture | Section-by-section drafting missed whole features that a release-by-release map found |
| It overstates | "Only", "every" and "three" where the source says less; claims worded beyond their evidence before a word was drafted |
| It cannot see its own errors | Every drafter ran its own read-back, and independent checkers still found the errors |
| It treats its own writing as a source | Survey reports and briefs carried errors into drafts; a trace cited the paper's own table |
| It invents when nothing stops it | Not seen, because the trace rule and the exported bibliography stop it; the author's own recollection, checked as a claim, came back narrower |
| It breaks things when it compresses | A length cut introduced errors that only a second round found |
| It acts when asked to look | "Investigate and report" was treated as "do" |
| Its process grows | Thousands of lines of skill text, a numbered list of author questions, long profiles and logs after one week |

The scarce resource is the author's attention. An agent produces text, checks and questions far faster than the author can read them. A toolkit that is honest about this optimises what the author must read in order to decide, and keeps it short.

### What verifiable has to mean

For the author to put their name on text they did not write, four things must hold.

1. **Local.** The support for a sentence is beside it, in the manuscript source, and is reached in one step: a file and line at a fixed version, a page of a paper, a table in a pinned copy. No register to look up, no session history to trust.
2. **Fail-closed.** What has no support is a visible marker in the built PDF, and a manuscript with one marker left cannot be built in final mode. Silence is never the fallback.
3. **Independently re-opened.** "Checked" means that someone other than the writer, in a fresh context, opened the pointer and compared it with the sentence, and the record says when and at which version of the text.
4. **Cheap to audit.** The author can read twenty sentences with their sources side by side in ten minutes, and can see which parts of the paper have changed since they were last checked.

The toolkit never certifies anything. It makes the author's verification cheap and the unverified visible.

## 2. Principles

1. **The manuscript carries its own evidence.** Every checkable statement has a trace or a gap beside it, in the `.tex`. This is the one mechanism everything rests on; hundreds of traces across a paper's sections were each re-openable. A separate register of facts would drift from the text; a comment beside the sentence moves, and is cut, with it.
2. **The writer never checks itself.** Independence is the unit of verification: draft, then a fresh context opens every trace, then the session that owns the paper confirms each finding at source before changing anything. It was the most valuable step in the loop, and a reader's finding is a lead and not an instruction.
3. **Only primary sources are sources.** Not the draft, not an agent's survey, not a brief, not memory. Agent-written notes are an index. The author's recollection is a claim like any other; testimony the author has confirmed is theirs, whoever typed it, and a source where nothing else can be.
4. **The author owns the argument and their prose; the agent owns the legwork.** The agent proposes, marks and asks, and every question carries a recommendation so that one reply settles many. It does not decide the framing, does not rewrite what the author wrote, and does not act when asked to look.
5. **One loop for every reader.** A trace checker, a stylist, a simulated referee, the author with a red pen, a co-author and the journal's referee all produce the same thing, comments on the paper, and one mechanism handles them: numbered points, a disposition for each, the changes, a re-check of what changed.
6. **Shorter is the default, and length is decided before the prose exists.** A section has a budget in the outline and its paragraph plan is agreed before it is written. Compression after the fact is where errors come in.
7. **One place for each truth, and current truth apart from history.** The argument is in one file; what is true today is in one short file that is rewritten; decisions are appended to one log. A second handoff file drifted within a day. Anything written twice will disagree.
8. **A map, not a process; a tool only where failure is silent.** A small core is always read; everything else is read when its case arises; what is particular to one paper lives in its workspace. Every stage has a file, written to the depth its first real use needs and refined from that use (decision 17). A convention is preferred to a procedure, and a procedure to code, except where a failure would be silent (a gap left in a submission, an anchor lost in a cut, a composed reference); there a deterministic tool is right. KISS and DRY, and ordinary technology: Markdown, LaTeX, git and the standard library.

## 3. The shape

### The core

`skills/_shared/core.md` is read whole by every session and every subagent. Each of its eight rules has a recorded failure behind it. Three are easy to omit and caught most of the real errors or prevented the worst risks: the independent check with confirmation at source, claim strength, and read-do-not-run.

### Six procedures

`start`, `evidence`, `draft`, `review`, `revise` and `finish`: one for each stage that has steps. The other stages are a brief or a technique (section 6): what differs between a checker, a stylist and a referee is the brief, not the procedure.

### Four reader briefs

Each is a self-contained brief handed to a fresh context; what it reads for is in the brief. The stylist carries the most depth because an agent's default prose fails there in ways it cannot feel as a reader (decision 17).

### The literature skill and the evidence procedure

The `literature` skill's five questions each prevent a failure an agent shows when left to itself (its table); `evidence.md` holds the seam to the campaign engine (section 5).

### The tools

- **The gap macro** (`scipaper.sty`): a gap prints loudly in a draft and fails the build in final mode.
- **`tools/ads.py`**: search, and BibTeX exported byte for byte from an authority.
- **`tools/traces.py`** (standard library only): `list`, `lost`, `lint`, `stale`, `moved`, `sample`. A lost trace is silent, and two rule-level failures in the first paper were mechanical enough to check by rule rather than by reading. Whether the source says what the sentence says remains the checker's reading. `stale` reads the check stamp, one comment line at the top of a section naming the date and the reader of its last independent check; under an ask-first commit policy a section reads "checked, not yet committed" until the author approves. `moved` joins the files that changed in a source root to the traces anchored in them, because a source that moves under a checked trace is silent and `stale` reads only the manuscript. `sample` draws an audit sheet for the author, with the traces drawn at random by the tool.

### The workspace contract

The workspace is its own git repository and the working directory of every session that writes the paper. Each source the paper draws on is linked or copied inside it, so every trace is a path relative to the workspace and means the same on every machine. Three files carry the contract, `AGENTS.md`, `paper/outline.md` and `paper/style.md`, and every drafter reads them.

- **`AGENTS.md`** names the installation, says "read `STATE.md`, then the core", and holds the `sources` block, the commit policy, the paper's conventions and how it is run. It is the only instruction file, and it begins at about sixty lines and grows only with what the paper itself teaches. The `sources` block is fenced, with one line per root giving its pin (`git:<rev>`, `fixed` or `-`) and whether it may be cited; a fenced block and not a table, because nothing reflows it, and in this file and not another, because the harness already puts it in front of every agent and a second file would be a second place for a pin.

The memory files, the reference files and the handoff between sessions are in core (*The workspace*, *Start and end of a session*); the toolkit assumes no commit policy, and the author sets it at `start`. A decision recorded only in the agent's unconfirmed paraphrase is the agent's, not the author's, which is why the journal marks the decisions the author confirmed.

## 4. Generic and particular

The test for any sentence is whether a paper on a different subject, by a different author, for a different journal would need it. The toolkit holds the rules, the trace forms, the procedures and briefs, the technique for a subject repository, the form findings arrive in, and the scaffold. A paper's workspace holds which paths are sources and which are forbidden, the pin and the command that reads at it, who drafts and who checks on which model, the journal's facts and the field's norms (each determined once per paper, so current for it), the style decisions, its feature map, and every local file. The toolkit names no subject and carries no unpublished paper. Nothing is copied into a workspace except the scaffold and the gap macro.

## 5. The boundary with ai-agent-coder

The engine that runs campaigns names no domain, this toolkit names no subject, and only a brief names all the parts. The meeting point is three kinds of plain file that cross the boundary, and nothing else.

| Crossing | Direction | Form | Owner of the form |
|---|---|---|---|
| A question with a declared test | paper to campaign | sections of the engine's brief | the engine owns the brief's format; `evidence.md` owns what a science brief puts in it |
| A findings report, its ledger and its manifest | campaign to paper | a document in the dossier that ends with a list of every file it cites | `evidence.md` |
| A reader brief: the challenger, the checker, the referee or the stylist | either | a file in `skills/paper/readers/`, loaded by a task node as a pinned input, with the binding supplying what a workspace would (`skills/paper/review.md`, *Outside a paper workspace*) | the paper skill, shared |

The conventions for scoping a claim and for reporting findings were written by hand into several campaign briefs and need one home, which is `evidence.md` and the shared challenger brief. What is generic to any investigation and already lives in the engine stays there.

A Campaign Manager in the author's seat needs one rule, not a table of defaults, and it is core rule 5: where a procedure says the author decides, an unattended caller takes the recorded recommendation if the brief's author policy delegates that kind of decision, marks the result provisional, and otherwise leaves a gap and a question. No paper has been written by a campaign; when one is, the brief's author policy lists what is reserved.

The ai-agent-coder engine carries the boundary in three generic sentences of its campaign mode (since its commit `401a9f6`): a task node's prompt may be a reader brief from a method toolkit the brief pins, filled as that toolkit's own rule for an outside commissioner says; the acceptance audit may ask for a read-only check of an input; and a findings report stays short, leaves listings in the receipts, and ends with a list of every file it cites.

## 6. What is deliberately left out

| Left out | Why |
|---|---|
| A default for every author question | Built for a caller that has never existed; rule 5 replaces it |
| Finding the workspace from somewhere else | The session works in the workspace; a project that wants a pointer writes one line |
| A procedure each for framing, style and venue | Framing is drafting with a different role and two rules; a style sheet is built once per paper; choosing a journal is a literature-shaped question asked once, and the durable part is the paper's own `venue.md` |
| Venue files in the toolkit | A journal's facts drift between papers; each paper fetches them once into its own `paper/venue.md`, current for it |
| A separate brief written for each drafter | With sources and conventions in `AGENTS.md`, intent and budgets in the outline and style in the style sheet, a drafter is told which section to write and what is particular to it |
| A register of promises between sections | A `\gap{todo}` under the heading it binds is visible in every build and blocks submission |
| A claims database, an approval registry or a state validator | `claims.md` is a table that nothing validates and nothing depends on; the check stamp is one comment line that git can contradict |
| Capturing every word the author says | Conversation is summarised into confirmed records at key points, because verbatim fragments left beside the current direction go stale and bias later work; git is the history (decision 21) |
| Running analysis or making data figures | The agent that writes the paper must not also manufacture its results; new results come from the author or from a campaign and arrive as findings |
| Submission, or anything else that leaves the machine | The author's act |
| Word, Overleaf, reference managers, formats other than LaTeX | One real need at a time; LaTeX and git are what the trace mechanism rests on |
| A reply-letter procedure | The loop's dispositions, rendered for the editor with a `latexdiff`, are the reply (owner, 2026-11-21) |
| A figures technique | A few sentences in `draft.md`; anything further is the paper's own practice, in its `AGENTS.md` |
| A co-authors technique | Not yet met; a co-author's comments are a reader's, through `revise` |
| Scoring, voting or debate between reviewers | Independent readers, a merge and the author's judgement did the job |
| Lists of banned words; detection of AI-written prose | The stylist judges against this paper's intent and this author's style, not a generic list |
| Tools for fields beyond astronomy | `ads.py` is astronomy's; the rule (export from an authority) is generic, and the DOI path serves other fields until someone needs more |
| Lint checks that each cited paper was read, or of gap kinds and question ids | Citing only what was read is the author's responsibility (owner, 2026-11-25); a gap prints in a draft and fails the final build whatever its kind, and question ids are the session's |
| A record of the method's measures, kept for a paper about it (findings by kind, seeded recall, the author's time) | No paper about the workflow makes measured claims; revisit if one is wanted (owner, 2026-11-25) |

## 7. How components are tested

Every component is tested on a live paper, because the toolkit names no subject and so cannot hold a real section, and because a synthetic fixture goes stale as the design moves and cannot exercise `start`, which needs real, unscaffolded input. Two kinds of test.

- **On a real paper**: does the component reproduce or improve what was done there by hand? The challenger is run on claims whose narrowing is already known; `lint` is run on a manuscript whose rule-level failures are already known; `lost` is run across a cut whose moves are already known; a second agent checks a set of literature notes against the papers; a fresh session finds its way from `AGENTS.md` and `STATE.md` alone; a drafter told only which section to write produces a compliant one from the three contract files.
- **Seeded**: the recipe in `skills/paper/review.md`, repeated whenever a brief or a model changes; a recipe, not a fixture. It measures recall on mechanical errors, which is what the checker and the challenger are for.

The stylist and the referee are judged against the author's own reading. The stylist is judged round by round, and its plan mode also by whether the first plans it reads improve before prose is written. The referee's brief is written from the author's own refereeing practice and is judged on its first runs against the author's reading. The second test of the split between generic and particular is a second paper on a different subject: one paper cannot show whether the split is right, and a sixty-line `AGENTS.md` meeting a new subject will.

## 8. Settled decisions

The first fourteen were accepted by the owner on 2026-11-19; later decisions carry their dates.

1. One loop: `review` with four reader briefs, and `revise`; no separate style, referee or respond procedures.
2. Eight core rules, not five.
3. Superseded by 21.
4. `claims.md` and `paper/reviews/` are core, as a table and a directory convention with nothing that validates them.
5. `traces.py` with `list`, `lost`, `lint` and `stale`, the small trace format and the check stamp are built now.
6. The workspace is the working directory, with sources linked into it.
7. The owning session approves a paragraph plan; the author does for the first section of each role and whenever what a section must carry does not fit its budget.
8. Superseded by 15.
9. Superseded by 17: `skills/paper/evidence.md` is written now.
10. The earlier Plan is archived.
11. Reader briefs are tested by the seeded recipe in a live workspace, with no fixture in the toolkit.
12. A second paper, on a different subject, is the test of generic against particular.
13. The commit policy is one section in the workspace `AGENTS.md`, as the author confirmed it; the toolkit assumes none.
14. Model policy is two sentences: the reader is never the writer's context, and at a milestone it is a different model where one is available; which model takes which seat is written in each paper's `AGENTS.md`.
15. The owner's later decision the same day: the referee brief is written now, from the author's own refereeing instructions and reports (their form only, no content). It judges a paper against its field's culture, accepted practice and tolerances, surveyed once per paper, and against the journal's referee guidelines, fetched once; both are kept in the workspace.
16. The owner's later decision the same day: no venue files in the toolkit. What a paper can determine once (its journal's facts and referee instructions, its field's norms, its style) is determined at first need and kept in its workspace as a reference file, current for that paper.
17. The owner's decision of 2026-11-21: the toolkit is finished now as a complete first version, every stage with a file written to the depth its first use needs, and refined from that use, rather than each component waiting for its second need. The reply letter is left out. The stylist gets the most depth and is "central to the process and all planning of text and writing of the text": it reads the outline, each paragraph plan and each drafted section, as well as the whole at milestones.
18. The owner's later decision of 2026-11-21: the readers are generalised so that an investigation can commission them under its brief (a Campaign Manager) or plan (a Project Manager), with light touches that leave their paper use unchanged: one rule for what the binding supplies, a source policy for the checker, an early read for the referee on pinned material, and a document mode for the stylist.
19. The owner's decision of 2026-11-24, from the review of a paper's first milestone read: the style sheet carries an example for every rule and runs to about 2,400 words, some four pages (the owner proposed three, then approved four once an example on every rule took about 2,340 words); a subject that moves under a draft has a delta list; and detail is left to a subject's documentation only where it holds the fact and the release is archived with a persistent identifier.
20. The owner's decision of 2026-11-26: `traces.py moved` is built now, in the backlog's smallest form (the files `git diff` names on a root, joined to the traces that anchor in them), without waiting for a re-pin to show a trace missed.
21. The owner's decision of 2026-11-26: what the author says is kept as confirmed records, not verbatim. At a key point (a decision taken, a direction refined to the point of action, a fact only the author knows, a lesson) and at the latest before the session closes, it is written concisely, checked against the live record for conflicts, and repeated back; it is the author's, and a source, only once the author confirms it. Testimony is one current record per subject in `notes/<slug>.md`, with git as the history; the journal states decisions and marks the author's as confirmed. Documents from outside the conversation, and anything the author asks to keep word for word, stay verbatim. Verbatim capture had piled up partial and superseded fragments that sat beside the current direction and biased later work. Supersedes 3.
