# Backlog

Small, real items that are not being done now and must not be forgotten. The toolkit grows only where using it shows a genuine gap or friction, so each entry says what, where, why it waits, and what would show it is needed. An entry leaves when its work lands or when the owner decides it is not wanted; what is deliberately left out is under *Decided against*, below.

## Waiting for friction

**A literature route beyond ADS.** Deferred on purpose (*Decided against*, the row *Tools for fields beyond astronomy*). ADS holds arXiv and much beyond astronomy, and the skill's arXiv and DOI export fallbacks serve other fields (`skills/literature/SKILL.md`, *BibTeX and fetching*). The trigger is a paper whose literature neither ADS nor the web reaches; the smallest form is a paragraph in the skill on searching another index, not a second tool. The AI-writing paper (2026-11-25), outside astronomy, exported its references from ADS (27) and by DOI (3) and read the rest on the web, with no `\gap{cite}` left, so the trigger has not fired.

**Installing for a second user.** Skills are linked into a harness by a catalogue script that lives outside this repository; the README says only that "a catalogue script may do the linking". The test, when someone else installs it, is that they get from the README to a started paper without help; what they trip on decides the fix.

## Shown by use

Gaps that use has already shown; they wait only for the next round of toolkit changes, for the owner's review.

None is open at present.

## Decided against

These were considered and left out, each for the reason given, so that they are not proposed again.

| Left out | Why |
|---|---|
| A default for every author question | Built for a caller that has never existed; core rule 5 replaces it |
| Finding the workspace from somewhere else | The session works in the workspace; a project that wants a pointer writes one line |
| A procedure each for framing, style and venue | Framing is drafting with a different role and two rules; a style sheet is built once per paper; choosing a journal is a literature-shaped question asked once, and the durable part is the paper's own `venue.md` |
| Venue files in the toolkit | A journal's facts drift between papers; each paper fetches them once into its own `paper/venue.md`, current for it |
| A separate brief written for each drafter | With sources and conventions in `AGENTS.md`, intent and budgets in the outline and style in the style sheet, a drafter is told which section to write and what is particular to it |
| A register of promises between sections | A `\gap{todo}` under the heading it binds is visible in every build and blocks submission |
| A claims database, an approval registry or a state validator | `claims.md` is a table that no tool validates or depends on; the check stamp is one comment line that git can contradict |
| Capturing every word the author says | Conversation is summarised into confirmed records at key points, because verbatim fragments left beside the current direction go stale and bias later work; git is the history |
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
| A fixture paper in the toolkit, for testing the procedures and briefs | The toolkit names no subject, and a fixture goes stale as the design moves and cannot exercise `start`; the procedures and briefs are tested on a live paper, the checker's and challenger's briefs also by the seeded recipe in `skills/paper/review.md` (*Testing a reader brief*), and only the tools have unit tests |
