# Appendix E: usability probe (Haiku 5.5)

_Returned whole by the subagent (read-only; asked to read eight toolkit files and plan "start a paper and draft the introduction" for a soil-moisture paper, then report confusions). Saved as received, 2026-11-27._

---

## Toolkit usability test: ai-agent-science (read-only)

I read the eight files in the order given. I made no edits, created no files and committed nothing. I also checked that the files they point to exist: evidence.md, sections.md, finish.md, readers/stylist.md, readers/challenger.md, readers/referee.md, techniques/style-sheet.md, field.md, venue.md, skeleton AGENTS.md and outline.md, tools/traces.py, tools/ads.py, docs/VISION.md and docs/BACKLOG.md all exist. I did not open the files beyond the eight, so where my plan depends on them I say so.

On absorption: I have no timer, so I measure by size. The eight files total about 8,800 words. core.md alone is about 1,900 and is meant to be read whole by every session. Following the chain (start, draft, review, revise, checker) pulls in about a dozen further files. Holding the eight rules, the trace forms, the gap kinds and the workspace file list at once is the heaviest part. Most of the difficulty was in cross-references, not in any single rule.

### 1. Step-by-step plan for "start a paper and draft the introduction" (soil moisture and crop yield)

1. **Check for a workspace.** There is no `paper/STATE.md`, so begin at start.md. Read core.md whole first (SKILL.md, "Before any work"; start.md, first paragraph).
2. **Make the workspace.** Ask which git repository will hold it and which directory, offering the default `<repo>-paper-workspace` or `<short-name>-paper-workspace` (start.md §1). Run `cp -Rn <install>/skeleton/paper-workspace/. <dir>/`, then `git init`. Write the installation root into AGENTS.md and create `manuscript/sections/` and `manuscript/figures/` (start.md §1.1). If the folder sits inside another repository, add it to that repository's `.git/info/exclude` (start.md §1.2).
3. **Commit policy.** Ask once how commits should be made and write the confirmed answer under `## Commit policy` in AGENTS.md (start.md §1.3; core, *What the author says*). Make no commit before that.
4. **Link the sources.** Symlink or copy the notes, figures and code inside the workspace. Write the `sources` block in AGENTS.md. Forward plans and archives are `never` (start.md §1.4; core, *The workspace*).
5. **Read the material.** Count first. Read notes and tables in full. View every figure. Read code without running it (start.md §2; core rule 6). Large material goes to parallel readers that write indexes to `paper/ingest/` (start.md §2).
6. **Ask before proposing.** Send one message asking why the work was done, what surprised the author, who must be convinced, and who the authors are (start.md §3). Record the answers as testimony in `notes/<slug>.md`, the reader in the outline's *Intent*, and the authors in `main.tex` (start.md §3; core, *What the author says*). Optionally run a blind framing read (start.md §3).
7. **Propose.** Write `paper/outline.md` (intent, spine, sections table, budgets), `paper/claims.md` (first rows), `paper/open-questions.md` (each with a `Q<n>` and a recommendation) and a first journal entry (start.md §4).
8. **Reference files.** Ask which journal (venue.md, "not decided yet" is allowed). Ask whether the paper should sound like the author's own work, and if so build `paper/style.md` (style-sheet.md). Build `paper/field.md` (field.md) (start.md §4).
9. **Present.** One page to the author: intent, spine, framings, questions. Ask whether the framing feels right (start.md §5).
10. **The introduction.** draft.md says: "A framing section (conclusions, introduction, abstract, title) is drafted last: see its role there" (role in sections.md, which I did not open). So I would tell the user this before drafting anything.
11. **Read before drafting.** Read the list in draft.md "Read first": core, AGENTS.md, the outline's Intent, Narrative and intro row, style.md, claims rows, and the role in sections.md.
12. **Paragraph plan.** Write one line per paragraph with point, flow and sources, to `.scratch/` (draft.md §1). Sum against budget. Send it to the stylist's plan mode before any prose (draft.md §1; stylist.md, which I did not open).
13. **Gather and write.** Open every source in this session (draft.md §2). Put a `% src:` line above each checkable sentence. Mark holes as `\gap{number}{command}` or `\gap{cite}`. Get citations from the `literature` skill (SKILL.md, Position stage) and never edit `refs.bib` (draft.md §2).
14. **Read back and build.** Read traces back once for comparison direction, number words and figure descriptions (draft.md §3). Build in a scratch copy with the AGENTS.md command (draft.md §4). Report in under 400 words (draft.md §4).
15. **Check and record.** Send the section to the stylist's section mode, then to an independent checker in a fresh context (draft.md end; review.md protocol; checker.md brief). Apply any accepted points through revise.md. Write the `% checked:` stamp and commit under the commit policy (revise.md step 8). Rewrite STATE.md, append to the journal, and commit (core, *Start and end of a session*).

### 2. Where I was unsure, or where the text conflicts

- **Intro is drafted last, against the request.** The user asks to "draft the introduction" and draft.md says "A framing section (conclusions, introduction, abstract, title) is drafted last". Neither file says what to do when the author asks for it now. I would have to guess whether to write a provisional version.
- **Narrative: proposed or left empty?** SKILL.md Orient says "an argument and a narrative are proposed for the author to correct". start.md §4 says "The Narrative ... until then they are left empty", because it waits for the stylist's outline mode, which needs `paper/field.md` first.
- **"Fresh context" is never made operational.** core rule 3 says "a fresh context that did not write the text (a subagent, a second session, or another harness)". review.md adds "A reader launched in another harness is confirmed running before the session moves on: a tool can fail at once and say nothing." Nothing says how to start one in the harness I am in. Every independence step depends on this.
- **"Key" is undefined.** core rule 1 says "a web source with no key is cited through its note". The trace-forms table says "A web source with no key | its note in the literature notebook". I could not tell whether "key" means a `refs.bib` key, a bibcode or a URL.
- **Which sentences need traces?** core rule 1 says "Connective and qualitative prose carries nothing", and lists "a named method; a comparison; ... anything said about what another paper says". An intro sentence like "soil moisture is a key control on yield" is qualitative, but it asserts what the field has shown. There are no examples. The result would be either a gap on every sentence or none.
- **`cp -Rn` in a non-interactive shell.** start.md §1.1 says `cp -Rn`. The user's global CLAUDE.md says `cp` is aliased to `-i` and "hangs non-interactive runs — use `\cp`". The toolkit does not mention this, so the first command could hang.
- **Build check needs a journal that may not exist.** draft.md §4 says "Judge the build by ... `paper/venue.md`'s baseline warnings ... once a journal is chosen." start.md lets the author say "not decided yet". With no journal, the build check has no baseline and the file does not say what to do instead.
- **STATE.md is read but never created.** SKILL.md and core say to read `paper/STATE.md` first. start.md says "Read it once, when there is no `paper/STATE.md` yet", but no step creates it. I did not check whether the scaffold ships one.
- **When may the agent run a script?** core rule 6 forbids running the author's code, with one exception: "The agent's own small read-only script over files already pinned". A soil-moisture slope read from a table could be a `\gap{number}` or a check under `paper/checks/`. No rule decides which.
- **Commit under a policy that may say "ask".** review.md step 3 says "commits the text the reader reads ... under the workspace's commit policy". core says "where none is stated, ask". The global rule says never to commit without approval. Each review round may therefore need a yes first.
- **`.scratch/` is used but never defined.** draft.md puts the plan in `.scratch/`, and review.md calls it gitignored. The eight files do not say where that ignore rule lives.
- **Load.** The "eight rules" each carry sub-bullets. Rule 8 says "A session starts and ends as below", and the "below" is itself a separate section. I had to keep at least six cross-file pointers in mind at once.

### 3. What I would most likely get wrong or skip

- **Drafting the intro first.** The request is concrete and the drafted-last rule sits in a different file, so I would be tempted to write it straight away.
- **Skipping the question before proposing.** start.md §3 is a mandatory question, but the framing from the material is easy to produce, and I might treat the blind framing read as an optional extra and skip it.
- **Writing numbers from memory of the notes.** The intro will want a headline figure ("soil moisture explains X% of yield variance"). I would likely write it from the notes' prose rather than the table row, and rule 1's derivation requirement is easy to forget.
- **Forgetting that background claims need citations.** I would likely either trace nothing, or put `\gap{cite}` on everything and not run the literature skill to fill them.
- **Skipping the stylist's plan mode.** It sits in a separate file I had not read, and without a fresh context I might think it can be done by myself.
- **Committing too early.** The first commit needs the commit policy, and the global rule says ask first. I would probably ask once and forget the answer across the rest of the session.
- **Lost trace lines.** When the intro is edited after a source moves, I would not run `traces.py lost` unless reminded.

### 4. Rules that matter most, and what felt like ceremony

Matter most: rule 1 (trace or gap, primary sources only), rule 3 (the writer does not check itself), rule 5 (the author owns the argument and the prose), rule 6 (never run the author's code), rule 7 (coverage beats budget), and the ask-before-proposing step in start.md §3. These are the rules that stop the failures the toolkit exists to prevent.

Felt like ceremony: the dispositions table for every point, the `paper/reviews/<date>-<slug>/` record, the five-plant test of a reader brief, the `latexdiff` reply to the journal, the round-numbered check stamp, the "two pages at most" limit on STATE.md, a journal line for each routine check, and the 400-word report limit. Each is useful at milestone scale, but for one intro section they add reading without changing what gets verified.

### 5. One page I would keep

**Paper workspace: working rules**

1. Read `paper/STATE.md` if it exists. If not, the paper is new: start.md.
2. Every checkable sentence has a `% src:` line directly above it pointing at a primary source you opened this session, or a `\gap{kind}{note}`. Checkable means a number, unit, date, count, named method, comparison, absence, quantifier, or any claim about what another paper says. Qualitative connective prose carries nothing.
3. Copy values with the source's units and conventions. Derive derived numbers in the trace. Never convert silently.
4. Do not run the author's code or analysis. A number that exists only from a run is `\gap{number}{command}`.
5. You never certify your own text. An independent reader in a fresh context re-opens the traces. You may do a read-back, but it is not a check.
6. The author owns the argument and the prose. Propose; do not apply. Ask with a recommendation. Never regenerate author-written text without showing what would be replaced.
7. Word a claim no stronger than its test. Where the source cannot settle a sentence, make it a gap.
8. Never invent a result to fill a hole. If the notes do not say what was found, the paper does not yet know.
9. Ask before proposing. In your first message, ask why the work was done, what surprised the author, who must be convinced and who the authors are. Record each answer as the author's testimony only once they confirm it.
10. The intro, abstract, conclusions and title are drafted last. Draft the body first, then the framing.
11. Coverage beats budget. If a section cannot carry what the outline says it must, stop and ask the author. Do not drop items silently.
12. Plan each section before writing prose: one line per paragraph, sent to the stylist's plan mode. Then gather sources, write with traces, read back once, build in a scratch copy.
13. Verify in a fresh context before calling a section drafted. Apply accepted points through revise, and re-check whatever changed.
14. Commit only under the `## Commit policy` in AGENTS.md. If none is stated, ask. Record decisions in STATE.md and the journal before the session ends.

(About 400 words.)

### 6. Five changes for a less capable model

1. **Add a task router at the top of SKILL.md.** Map common requests to their first file: "start a paper" to start.md, "draft a section" to draft.md, "draft the intro" to a short note that framing sections go last. Right now a model has to hold the stage table and the drafted-last rule in its head at once. Put the exception beside the table so it cannot be missed.
2. **Give each independence step a concrete procedure.** Say how to start a fresh context in the common harnesses: a subagent with a brief path, or a second session with a stated read-only scope. Define "key" by example. Without this, the central requirement of the toolkit (rule 3) can be silently skipped.
3. **Put the shell and file mechanics in one place.** Write `\cp -Rn` in start.md and say why. Say which files are created at each step (STATE.md, `.scratch/`, `.gitignore`, the empty outline). Say whether the scaffold ships STATE.md. A model that hits a hang or a missing file has no fallback in the toolkit.
4. **Add worked examples for the two judgement calls.** One example for whether a background sentence needs a trace or a `\gap{cite}`. One for when a derived value is `\gap{number}` and when it is a `paper/checks/` script. Rules stated only in the abstract are the ones a less capable model applies inconsistently.
5. **Give each stage a short checklist, and move the rest of core.md out of the always-read path.** core.md is about 1,900 words to be read whole every time. Keep the trace forms, gap kinds, rules 1, 3, 5 and 6, and the session start and end in a short core. Move the workspace file list and the "what the author says" mechanics to the stage that first needs them. Each stage file would then list its own steps and the one or two rules that matter there.

Files read: /Users/dcroton/Local/testing-grounds/ai-agent-science/README.md, skills/paper/SKILL.md, skills/_shared/core.md, skills/paper/start.md, skills/paper/draft.md, skills/paper/review.md, skills/paper/revise.md, skills/paper/readers/checker.md (all under the same root). Existence checks only: the other files listed in section 0 above.
