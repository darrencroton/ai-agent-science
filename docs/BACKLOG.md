# Backlog

Small, real items that are not being done now and must not be forgotten. The toolkit grows only where using it shows a genuine gap or friction, so each entry says what, where, why it waits, and what would show it is needed. An entry leaves when its work lands or when the owner decides it is not wanted; what is deliberately left out is in [`design.md`](design.md) §6.

## Waiting for friction

**A literature route beyond ADS.** Deferred on purpose (`design.md` §6, *Tools for fields beyond astronomy*). ADS holds arXiv and much beyond astronomy, and the skill's arXiv and DOI export fallbacks serve other fields (`skills/literature/SKILL.md`, *BibTeX and fetching*). The trigger is a paper whose literature neither ADS nor the web reaches; the smallest form is a paragraph in the skill on searching another index, not a second tool. The AI-writing paper (2026-11-25), outside astronomy, exported its references from ADS (27) and by DOI (3) and read the rest on the web, with no `\gap{cite}` left, so the trigger has not fired.

**Sources that move under a draft.** `tools/traces.py stale` reports manuscript changes since a section's check, not changes to its sources: a `fixed` file edited in place, or a pin moved, is noticed only by the session (`skills/paper/revise.md` step 8; `skills/paper/techniques/subject-repository.md`, on moving a pin). This is the session's responsibility today. Add a tool only if a re-pin shows traces being missed in practice; the smallest form would join `git diff --name-only <old>..<new>` on a root to the traces that anchor in it.

**Tests for `tools/ads.py`.** The tests for token redaction and the refusal of redirects have landed in `tools/test_ads.py`, because those failures are silent: a leaked token raises no error. What waits for the next change to the tool is `resolve` normalisation and `export`'s exit 3.

**Installing for a second user.** Skills are linked into a harness by a catalogue script that lives outside this repository; the README says only that "a catalogue script may do the linking". The test, when someone else installs it, is that they get from the README to a started paper without help; what they trip on decides the fix.

## Shown by use

Gaps that use has already shown; they wait only for the next round of toolkit changes, under the owner's review procedure.

None is open at present.
