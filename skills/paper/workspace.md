# The paper workspace

What a paper adds to `skills/_shared/core.md`: the forms a trace and a gap take in a manuscript, the workspace's files, how what the author says is recorded, and how a session starts and ends. Every session and every drafter that works in a workspace reads it after the core. A reader reads what its brief names.

A session starts and ends as below. The argument lives in `paper/outline.md` only. Nothing the author owns is moved to tidy the layout.

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
| `STATE.md` | what is true today, including what the paper still needs and from whom; rewritten, never appended; two pages at most; no history |
| `outline.md` | the intent, the narrative, the argument and the sections table; changed only on the author's decision |
| `claims.md` | one row per claim the argument depends on: the claim as the paper may word it, what it rests on and its verdict |
| `open-questions.md` | open questions only, each with a recommendation; a resolved one becomes a journal line |
| `journal.md` | append-only; one line per decision (the decision, why, by whom; the author's marked confirmed), pointing to the file or record that holds any detail, and one per routine check; no other account of work done, which git holds |

Also three reference files, each built once at first need by its technique in `skills/paper/techniques/`, kept current, and never a source: `style.md` (the paper's style sheet), `venue.md` (the journal: its policies, its class and its instructions to referees) and `field.md` (what papers of this kind contain and what the field accepts). And `lit/` (the literature notebook), `ingest/` (agent-written indexes: never a source), `checks/` (core rule 6) and `reviews/` (one directory per milestone review).

## What the author says

Conversation is not kept; what settles is. When something settles (a decision taken, a direction refined to the point of action, a fact only the author knows, a lesson), and at the latest before the session closes, write it concisely and completely, in the author's own terms. Show beside it anything in the live record (`notes/`, the outline's *Intent*, `AGENTS.md`, claims, open questions) that it contradicts or refines, with a recommendation; the author resolves it. Repeat the exact text back. It is the author's only once they confirm it, and silence is not confirmation; until then it is a draft, held with its text in `paper/STATE.md`, that no trace may cite.

Record it by what will rest on it. **Testimony** (why the work was done; a fact only the author knows) goes to `notes/<slug>.md`: the question it answers, the confirmed text and the date. **Direction** (a decision about the paper) goes into the live file it changes, and a **standing instruction** (how the work is run) into `AGENTS.md`. Each gets one journal line. A subject has one current record: a superseded one is replaced, git keeps it, its journal line says what changed, and the traces resting on it are re-checked (`skills/paper/revise.md`, step 8). Documents from outside the conversation (a co-author's comments, a referee's report), and anything the author asks to keep word for word, are kept as received.

## Start and end of a session

For the session that writes the paper; a reader follows its brief. Start with a clean `git status` and the expected last commit; read `paper/STATE.md`. Uncommitted changes in `manuscript/` are the author's: report them, and do not write to those files until the author's changes are committed or the author says to go ahead in them. Before drafting a section or commissioning a drafter, read `skills/paper/draft.md`: it says how settled a piece of text is, and which reads are due before anything rests on it. End by recording what has settled (*What the author says*), rewriting `STATE.md` and appending to the journal, which marks each decision as the author's, confirmed, or the session's, provisional, so that the record shows who did what; then commit under the `## Commit policy` in the workspace `AGENTS.md`; where none is stated, ask. A session that may not commit still records, and says what is uncommitted.
