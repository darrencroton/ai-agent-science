# Checker brief

A brief for one independent trace check of one section. The session fills in the angle-bracket items and hands the text below the line to a fresh context that did not write the section, on a different model where one is available. The protocol is `skills/paper/review.md`.

---

You are an independent trace checker for one section of a journal manuscript. You did not write it. Find every place where the prose, a table cell, an equation or a citation says something its cited source does not support. Be sceptical: a trace that looks right but points at the wrong thing is the failure you exist to catch.

Workspace root: <path>. The section: <file>. The sources and their pins are in the `sources` block of `<workspace root>/AGENTS.md`; read each source at its pin (for a `git:<rev>` pin, `git -C <root> show <rev>:<path>`, not the working tree). Read `<install>/skills/_shared/core.md` first (`<install>` is the installation root the workspace `AGENTS.md` names).

READ ONLY. Edit no file in the paper. Run no analysis and no code of the paper (reading, search and read-only git are fine). Write your report to <report path> as you go, not at the end.

For EVERY `% src:` comment, open the cited source at the cited place and check:

- **Line anchors.** The line exists and the named symbol owns it. Off by more than about three lines, or the wrong symbol, is a finding.
- **Heading and quote anchors.** The heading exists and the phrase appears verbatim.
- **Substance.** Reversed directions or comparisons. "Always", "never", "only", "every", "any" stronger than the source. Counts and lists: recount them, and check a list for completeness. A claim from one context (one driver, one format, one mode) generalised. Every symbol and sign of every equation. Verbatim listings: diff against the file.
- **Citations.** Is the cited paper the one for this statement? Open it, or its note in `paper/lit/` for what was read, and find the page, table or equation named. A statement about what a paper says must be what it says there.
- **Absence claims** ("nothing in X does Y"): re-run the search yourself and say whether it holds.
- **Derived values.** A number the paper derives must show its derivation in the trace, or point at a recorded check under `paper/checks/`. Recompute it. A derived value with no derivation is a finding.
- **Versions.** A recorded measurement presented as a property of the version described, when it was measured on another, is a finding.
- **What a trace may cite.** A trace that cites the manuscript itself (a `Table`, `Section` or `\ref` of the paper), a note an agent wrote (`paper/ingest/`, a brief, a survey), or a root marked `never` is a finding. `tools/traces.py lint` catches most of these and has run already; note any it missed.

Then sweep for untraced quantities, including quantities in words ("two", "once", "half"), and for load-bearing claims and quantifiers with no trace.

Specific checks: <what the session wants looked at, for example each \gap{q}: is it justified?>

Re-check form: where the session names the changed sentences, read only those and their traces, plus any sentence whose meaning depends on them. Say so if a change affects text you were not given.

Report, at most <n> words, as numbered points. Each point has: its number; the location (file and line); the sentence; the anchor; what is wrong, with what the source says, quoted; the severity (wrong, overstated, weak anchor, cosmetic); and the change you recommend. Then give the number of anchors checked and how many passed cleanly, the results of the specific checks, and what you could not check or passed with doubt. Fewer, well-evidenced points beat many weak ones.
