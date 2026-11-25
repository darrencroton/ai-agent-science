# Backlog

Small, real items that are not being done now and must not be forgotten. The toolkit grows only where using it shows a genuine gap or friction, so each entry says what, where, why it waits, and what would show it is needed. An entry leaves when its work lands or when the owner decides it is not wanted; what is deliberately left out is in [`design.md`](design.md) §6.

## Waiting for friction

**A literature route beyond ADS.** Deferred on purpose (`design.md` §6, *Tools for fields beyond astronomy*). ADS holds arXiv and much beyond astronomy, and the skill's arXiv and DOI export fallbacks serve other fields (`skills/literature/SKILL.md`, *BibTeX and fetching*). The trigger is a paper whose literature neither ADS nor the web reaches; the smallest form is a paragraph in the skill on searching another index, not a second tool.

**Sources that move under a draft.** `tools/traces.py stale` reports manuscript changes since a section's check, not changes to its sources: a `fixed` file edited in place, or a pin moved, is noticed only by the session (`skills/paper/revise.md` step 8; `skills/paper/techniques/subject-repository.md`, on moving a pin). This is the session's responsibility today. Add a tool only if a re-pin shows traces being missed in practice; the smallest form would join `git diff --name-only <old>..<new>` on a root to the traces that anchor in it.

**Tests for `tools/ads.py`.** Only `tools/traces.py` has tests. The ADS tool is small and used daily, and its failures are loud (exit codes 2 and 3). Write tests when it next changes: standard-library `unittest` against the loopback stub the tool already allows (`SCI_PAPER_ADS_BASE`), covering token redaction, the refusal of redirects, `resolve` normalisation and `export`'s exit 3.

**Installing for a second user.** Skills are linked into a harness by a catalogue script that lives outside this repository; the README says only that "a catalogue script may do the linking". The test, when someone else installs it, is that they get from the README to a started paper without help; what they trip on decides the fix.
