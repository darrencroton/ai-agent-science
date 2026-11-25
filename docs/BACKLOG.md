# Backlog

Small, real items that are not being done now and must not be forgotten. The toolkit grows only where using it shows a genuine gap or friction, so each entry says what, where, why it waits, and what would show it is needed. An entry leaves when its work lands or when the owner decides it is not wanted; what is deliberately left out is in [`design.md`](design.md) §6.

## Waiting for friction

**A literature route beyond ADS.** Deferred on purpose (`design.md` §6, *Tools for fields beyond astronomy*). ADS holds arXiv and much beyond astronomy, and the skill's arXiv and DOI export fallbacks serve other fields (`skills/literature/SKILL.md`, *BibTeX and fetching*). The trigger is a paper whose literature neither ADS nor the web reaches; the smallest form is a paragraph in the skill on searching another index, not a second tool.

**Sources that move under a draft.** `tools/traces.py stale` reports manuscript changes since a section's check, not changes to its sources: a `fixed` file edited in place, or a pin moved, is noticed only by the session (`skills/paper/revise.md` step 8; `skills/paper/techniques/subject-repository.md`, on moving a pin). This is the session's responsibility today. Add a tool only if a re-pin shows traces being missed in practice; the smallest form would join `git diff --name-only <old>..<new>` on a root to the traces that anchor in it.

**Tests for `tools/ads.py`.** Only `tools/traces.py` has tests. The ADS tool is small and used daily, and its failures are loud (exit codes 2 and 3). Write tests when it next changes: standard-library `unittest` against the loopback stub the tool already allows (`SCI_PAPER_ADS_BASE`), covering token redaction, the refusal of redirects, `resolve` normalisation and `export`'s exit 3.

**Installing for a second user.** Skills are linked into a harness by a catalogue script that lives outside this repository; the README says only that "a catalogue script may do the linking". The test, when someone else installs it, is that they get from the README to a started paper without help; what they trip on decides the fix.

## Shown by use

Gaps that use has already shown; they wait only for the next round of toolkit changes, under the owner's review procedure.

**The owning session skips the stylist.** On the AI-writing paper (2026-11-25), Section 2 was drafted without either of the stylist's reads that `skills/paper/draft.md` requires: plan mode on the paragraph plan before any prose (step 1), and section mode on the drafted section before the checker (after step 4). The session briefed the drafter to read `draft.md` and follow its plan step, but never read `draft.md` itself; it ran the round from `skills/_shared/core.md`, which names the checker (rule 3) and not the stylist, and from the author's working instruction ("have Fable do the writing and you proofread and iterate with it"), reading its own proofread as the stylist's job. It was found only when the author asked whether the stylist had been used (that workspace's `paper/journal.md`, the Lesson line of 2026-11-25). The fix: the core tells the owning session to read `skills/paper/draft.md` before it commissions a drafter, and names the stylist's section read beside the checker, so that a session holding only the core in mind still runs both. The smallest form is one sentence in core rule 3 or in *Start and end of a session*.

**The workspace's directory name.** `skills/paper/start.md` §1 asks the author which directory the workspace is, with no default, and both workspaces so far are called `sci-paper-workspace`, a name that does not say which science it serves. The author names the directory when a paper is initialised, and the default offered is the directory of the parent repository with `-workspace` appended: `mimic-workspace`, `ai-agent-science-workspace` (the owner, 2026-11-25). Change `start.md` §1, and anywhere the README or the skeleton names the directory.
