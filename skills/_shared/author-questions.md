# Author questions

Every point where a skill asks the author is listed here once, with an id. **At the keyboard, ask** — the skill's own text governs, and nothing here changes it. **Unattended** — a caller with no author present, such as a Campaign Manager acting under a brief — take the recorded default, say in the report that it was taken, and record it in the journal (`paper/journal.md` in a paper). A brief's author policy may **reserve** any question marked reservable: a reserved question with no author present stops the work at that point and reports it. A default never decides something scientific: where none is safe, the default is to stop.

| Id | Where | The question | Unattended default | Reservable |
|---|---|---|---|---|
| AQ1 | `paper` start, *Before anything* | A workspace already exists: what should be re-ingested? | Nothing. Read `STATE.md`, report where the paper stands, and do only what the caller asked | no |
| AQ2 | `paper` start §1a | A second paper here: what suffix distinguishes its workspace? | The caller's short name for the paper; with none, stop (a default name could duplicate the first paper's) | no |
| AQ3 | `paper` start §5b | May the index block go into the project's agent-instruction file (and which one, where both are real files; and where it is a checked-in contract)? | No. The index entry goes in `<ws>/paper/CLAUDE-sci-paper.md`, and the report says it must be read by hand | yes |
| AQ4 | `paper` start §5d | The paper's short name and author list | Short name: the caller's, else the working directory's name. Authors: the caller's, else left as the visible placeholder and reported | yes |
| AQ5 | `paper` start §6 | Which journal? | Not decided: the plain `article` scaffold | yes |
| AQ6 | `paper` start §7 | Is the proposed argument right? | The outline is written as proposed and is not settled: `STATE.md` *Argument* says it is awaiting the author | yes |
| AQ7 | `paper` draft §1 | The section is not in the outline: may this row be added? | No. Draft nothing; report the proposed row | yes |
| AQ8 | `paper` draft §2; `house-rules.md` *Non-destructive editing* | May existing prose be restructured or rewritten? | No. Extend and fill gaps in place only; report the proposed rewrite | yes |
| AQ9 | `paper` draft §4 | Two versions of one figure: which is current? | Neither is chosen: a `\gap{q}` and an open question | no |
| AQ10 | `paper` voice §1 | May the agent choose the papers? | No: do not fetch; stop and report that `paper-voice/` is empty (a profile made with no author involved would bind every draft) | yes |
| AQ11 | `literature` novelty, step 1 | State the result as one testable sentence | The caller's claim as given; if it is not testable, that is the finding, reported | no |
| AQ12 | `literature` support/contradict | Which claim is this bound to? | Stop: no claim was named | no |
| AQ13 | `literature` *Before anything*, unbound | Where should the notes be written? | Nowhere: the answer is in the reply | no |
| AQ14 | `house-rules.md` Rule 2 | Which record should a BibTeX entry come from? | Rule 2's table order, and the report says which was used | no |
| AQ15 | `house-rules.md` *Locating the installation* | The installation root cannot be confirmed: where is it? | Stop and report; never guess a path | no |
| AQ16 | `paper` router, *Picking the mode* | The mode is unclear: which was meant? | Stop and report | no |
| AQ17 | `paper` voice §4 | The profile's disagreements: which way does each go? | Left in `voice.md`'s *Disagreements*, each with a recommendation; the profile is otherwise unchanged | no |
| AQ18 | `_shared/sections/results.md`, *Order results by the argument* | The outline's order and the figure numbering disagree: which governs? | A `\gap{q}` | no |
| AQ19 | `paper` start §1a (the case §1b describes) | Is the paper's subject the project itself? | Treat it as the subject: the reading that writes nothing into the project's tracked files | no |

A new point where a skill asks the author gets a row here in the same change.
