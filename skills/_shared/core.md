# Core

The rules every session and every subagent works under, whatever the task. Read it whole at the start; it is short so that it can be. Paper-specific rules live in the workspace `AGENTS.md`, `paper/outline.md` and `paper/style.md`, and nothing here is overridden by them.

## The eight rules

1. **Trace or gap.** Every checkable statement carries a trace that names a primary source precisely enough to open in one step, or it is a `\gap{kind}{note}`. There is no third option. *Checkable* means a number, unit, date or count; a named method; a comparison; an absence ("no test covers..."); a quantifier ("every", "only", "first"); and anything said about what another paper says. It applies in the body, a caption, a table and a figure. Connective and qualitative prose carries nothing. Under this rule:
   - **Primary sources only.** Never the manuscript itself, a note an agent wrote, a brief, a survey or memory; a frozen brief is a source only for what it declares (a test, a threshold, a holdout), and a web source with no key is cited through its note, which is its pinned record (*Trace forms*). The author's recollection is a claim like any other; testimony the author has confirmed (*What the author says*) is theirs, whoever typed it, and a source where nothing else can be.
   - **Copy, do not convert.** A value is written with the unit and convention its source uses (units and h-scalings, IMF, cosmology, aperture). Typesetting a unit is notation, not conversion; changing its value, scaling or convention is conversion. A value read off a figure is an estimate and is labelled as one.
   - **Derive in the open.** A number the paper derives (a percentage, a ratio) carries its derivation: the arithmetic in the trace, or a recorded check (rule 6).
   - **Pin what moves.** A source that can change is read at a version the workspace records, and the trace is written from that version. A measurement made on an earlier version is quoted with that version.
2. **References are exported, never composed.** BibTeX comes from an authority, byte for byte (`tools/ads.py export`, or the arXiv or DOI export), never rekeyed and never hand-edited; a record that will not render is fixed in the preamble. With no export, the citation is a `\gap{cite}`. A paper is cited only for what the agent has opened and read there.
3. **The writer does not check itself.** Nothing is called checked until an independent reader has re-opened its traces. Independent means a fresh context that did not write the text (a subagent, a second session, or another harness) and, at a milestone, another model where one is available. The session that owns the paper confirms each finding at source before changing anything: a finding is a lead, not an instruction.
4. **A claim is worded no stronger than its test.** Correct traces under an overstated claim are the failure traces cannot catch. A threshold has a recorded reason; a title says no more than was tested. A rewrite never changes a claim's strength silently; where the source cannot settle a sentence, it becomes a gap, not a softer sentence.
5. **The author owns the argument and their prose.** Propose, do not apply. Edit in place; never regenerate text the author wrote without showing what would be replaced and being told to go ahead. Ask with a recommendation, so that one reply can settle many questions. Act on a recommendation without an answer only where the author has delegated that kind of decision, and mark the result provisional. "Look into" is not "do": restate what is authorised before a round of changes.
6. **Read, do not run, with one exception.** The agent never runs the author's notes and analysis or the code the paper is about, and modifies them only where the author has authorised a named change: a run would make a new result nobody has reviewed. A number that exists only as the output of such a run is a `\gap{number}` that names the command that would produce it. The exception is the agent's own small read-only script over files already pinned in the workspace (a count, a ratio, a recomputation of a reported verdict). It is kept under `paper/checks/<slug>/` with its script, command and output; it is checked independently like any other trace; and a trace may then point at it. A check derives from sources and never adds a fact they do not hold.
7. **Shorter, and never by silent omission.** Every section has a budget in `paper/outline.md`, and a report or a question is as long as its decision needs. What the outline says a section must carry is never dropped to meet a budget: where the two conflict, the conflict goes to the author before the prose is written. A cut keeps every traced fact or names it as dropped.
8. **Memory.** A session starts and ends as below; a reader reads only what its brief allows. The argument lives in `paper/outline.md` only. Nothing the author owns is moved to tidy the layout.

## Trace forms

A trace is a LaTeX comment `% src: ...` above or beside the sentence it supports. It must contain at least one anchor a tool can recognise (a path from a declared root, a commit `<root>@<hex>`, a `refs.bib` key, or the keyword `search`); anything else in it is free text. A qualifier may say which part of the sentence a trace supports, with the anchors after the colon: `% src (footnote): ...`. Write a line number by looking at the file, never from memory.

| Source | Form |
|---|---|
| Code or a file | path from a declared root, line and owning symbol: `code/src/core/halo.c:212 (process_halo)`; a range or glob is allowed |
| A prose document | the path and a heading or a quoted phrase, not a line number: `notes/why.md "why the work was done"` |
| A commit | `<root>@<hex>`, root without its slash: `code@a654c228 "fix flybys"` |
| A paper | its `refs.bib` key and the page, equation, table or figure: `2021MNRAS.506.4210I Table 1` |
| A web source with no key | its note in the literature notebook, `paper/lit/web-<slug>.md`, with a quoted phrase |
| An absence or a search | `search <command> (<date>, <version>) -> <result>` |
| A count | the file and how it was counted, with the items nameable: `code/run.cfg (grep -c '^model_' -> 64)` |
| A pinned copy | a path inside it: `campaign-findings/<id>/findings.md "claim C3"` |
| The author's testimony | `notes/<slug>.md` with a quoted phrase of the confirmed record |

## Gap kinds

`\gap{kind}{note}`, with LaTeX's special characters in the note escaped. A draft prints it loudly in the text and the margin; the `[final]` option on `scipaper` fails the build while one remains. `tools/traces.py list` collects them with the traces.

| Kind | For |
|---|---|
| `number` | a value with no source yet; the note names the command that would produce it |
| `cite` | a reference not yet found and exported |
| `q` | a question for the author; the note carries its `Q<n>` |
| `logic` | a step that does not yet follow |
| `todo` | work promised, including a promise to another section, placed under the heading it binds |

## The workspace

The workspace is its own git repository and the working directory of every session that writes the paper. Every workspace path is relative to it and none begins with `../`; each source is linked or copied inside it. Toolkit paths (`skills/...`, `tools/...`) are relative to the installation root, which the workspace `AGENTS.md` names. The workspace `AGENTS.md` carries one fenced `sources` block (root, pin, `cite` or `never`) that says what may be cited and at what version; `tools/traces.py lint` reads it.

| File under `paper/` | Holds |
|---|---|
| `STATE.md` | what is true today; rewritten, never appended; two pages at most; no history |
| `outline.md` | the intent, the narrative, the argument and the sections table; changed only on the author's decision |
| `claims.md` | one row per claim the argument depends on: the claim as the paper may word it, what it rests on and its verdict |
| `open-questions.md` | open questions only, each with a recommendation; a resolved one becomes a journal line |
| `journal.md` | append-only; one line per decision (the decision, why, by whom; the author's marked confirmed), pointing to the file or record that holds any detail, and one per routine check; no other account of work done, which git holds |

Also three reference files, each built once at first need by its technique in `skills/paper/techniques/`, kept current, and never a source: `style.md` (the paper's style sheet), `venue.md` (the journal: its policies, its class and its instructions to referees) and `field.md` (what papers of this kind contain and what the field accepts). And `lit/` (the literature notebook), `ingest/` (agent-written indexes: never a source), `checks/` (rule 6) and `reviews/` (one directory per milestone review).

## What the author says

Conversation is not kept; what settles is. When something settles (a decision taken, a direction refined to the point of action, a fact only the author knows, a lesson), and at the latest before the session closes, write it concisely and completely, in the author's own terms. Show beside it anything in the live record (`notes/`, the outline's *Intent*, `AGENTS.md`, claims, open questions) that it contradicts or refines, with a recommendation; the author resolves it. Repeat the exact text back. It is the author's only once they confirm it, and silence is not confirmation; until then it is a draft, held with its text in `paper/STATE.md`, that no trace may cite.

Record it by what will rest on it. **Testimony** (why the work was done; a fact only the author knows) goes to `notes/<slug>.md`: the question it answers, the confirmed text and the date. **Direction** (a decision about the paper) goes into the live file it changes, and a **standing instruction** (how the work is run) into `AGENTS.md`. Each gets one journal line. A subject has one current record: a superseded one is replaced, git keeps it, its journal line says what changed, and the traces resting on it are re-checked (`skills/paper/revise.md`, step 8). Documents from outside the conversation (a co-author's comments, a referee's report), and anything the author asks to keep word for word, are kept as received.

## Start and end of a session

For the session that writes the paper; a reader follows its brief. Start with a clean `git status` and the expected last commit; read `paper/STATE.md`. Uncommitted changes in `manuscript/` are the author's: report them, and do not write to those files until the author's changes are committed or the author says to go ahead in them. Before drafting a section or commissioning a drafter, read `skills/paper/draft.md`: the paragraph plan and the drafted section each go to the stylist, and the section then to the checker. End by recording what has settled (*What the author says*), rewriting `STATE.md` and appending to the journal, then commit under the `## Commit policy` in the workspace `AGENTS.md`; where none is stated, ask. A session that may not commit still records, and says what is uncommitted.
