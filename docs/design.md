# Design

Why ai-agent-science is shaped as it is: the problem, what "verifiable" means, the principles, the shape, the boundary with the engine that runs campaigns, what is left out, how it is tested, and what is built when. It is a design, not a history; the earlier Plan is archived and git keeps it. Read it before changing the shape of the toolkit. The files themselves are the rules.

**In one paragraph.** A paper is verifiable when every checkable sentence carries, beside it, a pointer to the primary source it rests on or a visible marker that it rests on nothing yet, and when someone other than the writer has opened those pointers. Everything else serves that, or serves the author's attention. The toolkit is one page of rules that is always read; a one-page map; five short procedures; four reader briefs handed to a fresh context; a literature skill; a thin evidence skill that is the seam to the campaign engine; and two small deterministic tools. All feedback on the paper, from the trace checker to a journal's referee, goes through one loop. The paper's own rules live in its workspace, in three files that every agent reads.

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
3. **Only primary sources are sources.** Not the draft, not an agent's survey, not a brief, not memory. Agent-written notes are an index. The author's recollection is a claim like any other; the author's dated testimony is a source where nothing else can be.
4. **The author owns the argument and their prose; the agent owns the legwork.** The agent proposes, marks and asks, and every question carries a recommendation so that one reply settles many. It does not decide the framing, does not rewrite what the author wrote, and does not act when asked to look.
5. **One loop for every reader.** A trace checker, a stylist, a simulated referee, the author with a red pen, a co-author and the journal's referee all produce the same thing, comments on the paper, and one mechanism handles them: numbered points, a disposition for each, the changes, a re-check of what changed.
6. **Shorter is the default, and length is decided before the prose exists.** A section has a budget in the outline and its paragraph plan is agreed before it is written. Compression after the fact is where errors come in.
7. **One place for each truth, and current truth apart from history.** The argument is in one file; what is true today is in one short file that is rewritten; decisions are appended to one log. A second handoff file drifted within a day. Anything written twice will disagree.
8. **A map, not a process; a tool only where failure is silent.** A small core is always read; everything else is read when its case arises; what is particular to one paper lives in its workspace. A component is built at its second real need. A convention is preferred to a procedure, and a procedure to code, except where a failure would be silent (a gap left in a submission, an anchor lost in a cut, a composed reference); there a deterministic tool is right. KISS and DRY, and ordinary technology: Markdown, LaTeX, git and the standard library.

## 3. The shape

### The core

`skills/_shared/core.md` is read whole by every session and every subagent. It holds eight rules: trace or gap; references are exported, never composed; the writer does not check itself; a claim is worded no stronger than its test; the author owns the argument and their prose; read, do not run, with one exception; shorter, and never by silent omission; memory. Each rule has the evidence of a recorded failure behind it. Three are easy to omit and caught most of the real errors or prevented the worst risks: the independent check with confirmation at source, claim strength, and read-do-not-run. It also holds the trace forms, the gap kinds, how the author's words are sorted, and the start and end of a session.

Rule 6 states its exception: the agent never runs the author's analysis or the code the paper is about, since that would make a new result nobody has reviewed; but its own small read-only script over files already pinned in the workspace (a count, a ratio, a recomputation of a reported verdict) is a check, kept with its script, command and output, and checked like any other trace.

### The map

`skills/paper/SKILL.md` is one page listing the stages a scientist moves through (orient, position, evidence, draft, verify, style and shape, referee, finish, respond) and the file to read for each. The stages are not in order and none is a gate. The agent may leave the map; the core still holds.

### Five procedures

`start` (make the scaffold; ask the broad questions before proposing any claim: why was the work done, what surprised you, who must be convinced; propose the intent, the spine and the questions). `draft` (write a paragraph plan against the budget, then the section from sources opened in this session, tracing as it goes, marking every hole, with a short read-back, a build and a short report). `review` (how a fresh context is commissioned and what its report looks like). `revise` (the one loop). `finish` (submission; not yet written, section 8). Building a style sheet and choosing a venue are techniques, and framing is a role in `sections.md` with two extra rules; none is a procedure: what differs between a checker, a stylist and a referee is the brief, not the procedure.

### Four reader briefs

Each is a self-contained brief handed to a fresh context.

- **The checker** opens every trace, recounts every count, checks every equation, checks that each citation is the paper cited for that statement, re-runs each absence search, and sweeps for quantities with no trace. After any later change it reads only the changed sentences.
- **The challenger** takes a claim as worded and what it rests on and tries to show it does not follow: a threshold with no recorded reason, a margin that shrinks under refinement, the effective size of the design, a title that says more than its test, an effect every model shows alike, a holdout already seen, a number older than the version described.
- **The stylist** reads the built PDF as an editor would, against the outline's intent, the budgets and the style sheet. It begins with a reverse outline, one line per paragraph, so that the paper's shape can be read in two pages, and proposes cuts, merges and moves. It is advice to the author, not an instruction to the agent.
- **The referee** gets only the PDF, the venue file and a few papers of the same genre, and nothing from the workspace's memory. It runs once per angle (specialist, sceptical generalist, the journal's editor, and one chosen for the paper) and reports in the journal's form, beginning with what it takes the paper to claim.

### One loop

An independent reader's report, the author's own reading and a journal's referee are all split into numbered points. The session confirms each point at source, disposes of it in one table (accept, accept with a different change, decline with the reason, or leave to the author), brings the author every point that touches the argument, applies the accepted changes through the outline, the claims, the other sections and the promises between them, names every trace that disappeared, and sends everything changed since the section's last check back to the checker. A milestone leaves a review record; a routine check leaves one journal line. A cut keeps every traced fact or names it as dropped.

### The literature and evidence skills

The `literature` skill answers five questions, each a place where an agent left to itself fails in a known way: has this been done (softening a paper that scoops the result); what is closest and what did it leave open (inferring a gap the paper never stated); what supports or contradicts one claim (searching one direction only); what comparison values can be taken, with their conventions and locations; and where a dataset or tool came from (asserting it on a brief's word). It has a tool, a rule that a paper is cited only for what was opened and read, a notebook that records what was read so that nothing is chased twice, and three lines of query craft: snowball from a close paper before searching by keyword, a hit count is not relevance, and finding nothing is not novelty. A trace to literature leads with the paper and the location in it, never with the note, because an agent-written note is an index and not a source.

The `evidence` skill is thin. It states how a claim with nothing under it becomes a question with a declared test, the form findings come back in, and how a paper pins them and reads them into its claims (section 5).

### The tools

- **The gap macro** (`scipaper.sty`): a gap prints loudly in a draft and fails the build in final mode.
- **`tools/ads.py`**: search, and BibTeX exported byte for byte from an authority.
- **`tools/traces.py`** (standard library only): `list`, `lost`, `lint`, `stale`. A lost trace is silent, and two rule-level failures in the first paper were mechanical enough to check by rule rather than by reading. `lint` checks that each trace has an anchor it recognises, falls under no root marked `never`, exists at its pin, and that each citation key is in the bibliography; whether the source says what the sentence says remains the checker's reading. `stale` reads the check stamp, one comment line at the top of a section naming the date and the reader of its last independent check; the text as checked is the version in the commit that last changed that line, so under an ask-first commit policy a section reads "checked, not yet committed" until the author approves. `sample`, an audit sheet of traces drawn by the tool so that the agent cannot choose them, waits for submission.

### The workspace contract

The workspace is its own git repository and the working directory of every session that writes the paper. Each source the paper draws on is linked or copied inside it, so every trace is a path relative to the workspace and means the same on every machine. Three files carry the contract and are read by every agent.

- **`AGENTS.md`** names the installation, says "read `STATE.md`, then the core", and holds the `sources` block, the commit policy, the paper's conventions and how it is run. It is the only instruction file, and it begins at about sixty lines and grows only with what the paper itself teaches. The `sources` block is fenced, with one line per root giving its pin (`git:<rev>`, `fixed`, or none) and whether it may be cited; a fenced block and not a table, because nothing reflows it, and in this file and not another, because the harness already puts it in front of every agent and a second file would be a second place for a pin.
- **`paper/outline.md`** opens with the intent in the author's words, then the argument, then the sections with role, budget and what each must carry.
- **`paper/style.md`**: register, spelling, person and tense, notation, defined terms and a few exemplar paragraphs, in two pages at most.

Five memory files keep apart what is true today (`STATE.md`, rewritten, two pages), what the paper argues (`outline.md`), what each claim rests on (`claims.md`, a table), what the author must decide (`open-questions.md`, open ones only) and what was decided, by whom and why (`journal.md`, append-only, no account of work done because git holds it). That is the whole handoff: a session ends by rewriting `STATE.md`, appending to the journal, and committing under the policy in `AGENTS.md`. The toolkit assumes no commit policy; the author sets it at `start`. Changes found uncommitted in the manuscript at the start of a session are the author's and are reported, and the session does not write to those files until they are committed or the author says to go ahead.

The author's words are sorted by what will rest on them. Testimony (why the work was done; a fact only the author knows) is a primary source: verbatim, dated, in a new note, never edited. Direction goes into the live file it changes with one journal line quoting the words. A standing instruction goes into `AGENTS.md`. Conversation is not kept. In doubt, classify upward; the closing message lists what was recorded. A decision recorded only in the agent's paraphrase is the agent's, not the author's, which is why the journal quotes the author.

## 4. Generic and particular

The test for any sentence is whether a paper on a different subject, by a different author, for a different journal would need it. The toolkit holds the rules, the trace forms, the procedures and briefs, a journal's quirks, the technique for a subject repository, the form findings arrive in, and the scaffold. A paper's workspace holds which paths are sources and which are forbidden, the pin and the command that reads at it, who drafts and who checks on which model, the style decisions, its feature map, and every local file. The toolkit names no subject and carries no unpublished paper. Nothing is copied into a workspace except the scaffold and the gap macro.

## 5. The boundary with ai-agent-coder

The engine that runs campaigns names no domain, this toolkit names no subject, and only a brief names all the parts. The meeting point is three plain files that cross the boundary, and nothing else.

| Crossing | Direction | Form | Owner of the form |
|---|---|---|---|
| A question with a declared test | paper to campaign | sections of the engine's brief | the engine owns the brief's format; `evidence` owns what a science brief puts in it |
| A findings report, its ledger and its manifest | campaign to paper | a document in the dossier that ends with a list of every file it cites | `evidence` |
| A brief for an independent challenge | either | `skills/paper/readers/challenger.md`, loaded by a task node as a pinned input | the paper skill, shared |

The conventions for scoping a claim and for reporting findings were written by hand into several campaign briefs and need one home, which is the thin `evidence` skill and the shared challenger brief. Scoping states the claim as a question, names the headline, gives each threshold a reason, states the effective design, names the holdout before the first change, asks for the trend under refinement and not three passes, treats an effect all models share as a question about the input, and does the literature before the brief is frozen. Findings keep to a short report with the listings left in the receipts; the paper pins them by their manifest, checks each verdict against its receipts, and reads each claim into `claims.md` with two verdicts side by side, the campaign's and the paper's. What is generic to any investigation and already lives in the engine stays there.

A Campaign Manager in the author's seat needs one rule, not a table of defaults, and it is core rule 5: where a procedure says the author decides, an unattended caller takes the recorded recommendation if the brief's author policy delegates that kind of decision, marks the result provisional, and otherwise leaves a gap and a question. No paper has been written by a campaign; when one is, the brief's author policy lists what is reserved.

## 6. What is deliberately left out

| Left out | Why |
|---|---|
| A default for every author question | Built for a caller that has never existed; rule 5 replaces it |
| Finding the workspace from somewhere else | The session works in the workspace; a project that wants a pointer writes one line |
| A procedure each for framing, style and venue | Framing is drafting with a different role and two rules; a style sheet is built once per author; choosing a journal is a literature-shaped question asked once, and the durable part is the venue file |
| A separate brief written for each drafter | With sources and conventions in `AGENTS.md`, intent and budgets in the outline and style in the style sheet, a drafter is told which section to write and what is particular to it |
| A register of promises between sections | A `\gap{todo}` under the heading it binds is visible in every build and blocks submission |
| A claims database, an approval registry or a state validator | `claims.md` is a table that nothing validates and nothing depends on; the check stamp is one comment line that git can contradict |
| Capturing every word the author says | Only what will rest on the words is kept, and the rest goes stale |
| Running analysis or making data figures | The agent that writes the paper must not also manufacture its results; new results come from the author or from a campaign and arrive as findings |
| Submission, or anything else that leaves the machine | The author's act |
| Word, Overleaf, reference managers, formats other than LaTeX | One real need at a time; LaTeX and git are what the trace mechanism rests on |
| Scoring, voting or debate between reviewers | Independent readers, a merge and the author's judgement did the job |
| Lists of banned words; detection of AI-written prose | The stylist judges against this paper's intent and this author's style, not a generic list |
| Tools for fields beyond astronomy | `ads.py` is astronomy's; the rule (export from an authority) is generic, and the DOI path serves other fields until someone needs more |

## 7. How components are tested

Every component is tested on a live paper, because the toolkit names no subject and so cannot hold a real section, and because a synthetic fixture goes stale as the design moves and cannot exercise `start`, which needs real, unscaffolded input. Two kinds of test.

- **On a real paper**: does the component reproduce or improve what was done there by hand? The challenger is run on claims whose narrowing is already known; `lint` is run on a manuscript whose rule-level failures are already known; `lost` is run across a cut whose moves are already known; a second agent checks a set of literature notes against the papers; a fresh session finds its way from `AGENTS.md` and `STATE.md` alone; a drafter told only which section to write produces a compliant one from the three contract files.
- **Seeded**: copy a checked section to scratch, plant five errors of named kinds (a changed number, a strengthened quantifier, a trace moved to the wrong line, a converted unit, a swapped citation), run the reader and count. This measures recall on mechanical errors, which is what the checker and the challenger are for, and it is repeated whenever a brief or a model changes. It is a recipe in `skills/paper/review.md`, not a fixture. It says nothing about judgement.

The stylist and the referee are judged against the author's own reading. Each is briefed by hand first and its brief written from what produced substantive criticism, so that there is one referee and not two. The second test of the split between generic and particular is a second paper on a different subject: one paper cannot show whether the split is right, and a sixty-line `AGENTS.md` meeting a new subject will.

## 8. Build order, and what is not yet written

Written: the core, the map, the scaffold, `start`, `draft`, `review`, `revise`, the checker and challenger briefs, the section roles, the techniques, the PASA venue file, the literature skill, and the tools `ads.py` and `traces.py`.

| Not yet written | Triggered by |
|---|---|
| The stylist brief | A hand-run pass on a complete first draft, before the author's own read, with its reverse outline and two-page report, taken through `revise` with the author's reading; then the brief is written from what survived |
| The referee brief | A hand-run pass, with the instructions, angles and two good reports from the author's own referee project, first on the outline and claims, then on the whole paper; then the brief is written |
| The `evidence` skill | The first session that chooses a paper's science focus and uses campaign findings once; its form is fixed above and its text is written from what that session used |
| `finish`, the audit sheet and the letter | The first paper to reach submission: the final-mode build, a clean `lint` and `stale`, the framing check (every number in the abstract, introduction and conclusions appears in the body with the same value and a claim id behind it), the audit sheet, the submission bundle with comments stripped, the venue's checklist and its statement on AI use; and the reply to a real referee, a letter rendered from the dispositions and a `latexdiff` PDF |
| A figures technique; a co-authors technique | Their second need; one use so far stays in that paper's `AGENTS.md`, and co-authors have not yet been met |

The ai-agent-coder engine needs no change for this design. Three small generic sentences are worth adding there, at a time when no campaign depends on the engine's pinned version: a campaign's final report ends with a list of every file it cites and stays short with listings left in the receipts; an auditor may ask for a check of an input and is not limited to re-reading captures; and a brief may name a pinned input as the prompt for the independent challenge.

## 9. Settled decisions

All fourteen recommendations were accepted by the owner on 2026-11-19.

1. One loop: `review` with four reader briefs, and `revise`; no separate style, referee or respond procedures.
2. Eight core rules, not five.
3. The author's words are sorted into testimony, direction, standing instruction and conversation; only testimony makes a verbatim note.
4. `claims.md` and `paper/reviews/` are core, as a table and a directory convention with nothing that validates them.
5. `traces.py` with `list`, `lost`, `lint` and `stale`, the small trace format and the check stamp are built now; `sample` waits for submission.
6. The workspace is the working directory, with sources linked into it.
7. The owning session approves a paragraph plan; the author does for the first section of each role and whenever what a section must carry does not fit its budget.
8. The author supplies the referee project's instructions, angles and two good reports; the first hand prototype runs on the outline and claims before the science focus is chosen.
9. The `evidence` skill is written after the first focus session; the challenger brief is written now.
10. The earlier Plan is archived and this document replaces it.
11. Reader briefs are tested by the seeded recipe in a live workspace, with no fixture in the toolkit.
12. A second paper, on a different subject, is the test of generic against particular.
13. The commit policy is one section in the workspace `AGENTS.md`, in the author's words; the toolkit assumes none.
14. Model policy is two sentences: the reader is never the writer's context, and at a milestone it is a different model where one is available; which model takes which seat is written in each paper's `AGENTS.md`.
