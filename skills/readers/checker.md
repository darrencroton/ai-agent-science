# Checker brief

A brief for one independent trace check of one section, or of another document whose statements cite their sources (a findings report, a ledger, a plan) commissioned as `skills/readers/SKILL.md`, *Outside a paper workspace*, says. For such a document the session names its pointer form and its source policy, which replaces the `sources` block: a declared test rests on the frozen brief, a recorded decision on the decision log, and a measured value on its receipt or output. The session fills in the angle-bracket items and hands the text below the line to a fresh context that did not write the section. The protocol is `skills/readers/SKILL.md`.

---

You are an independent trace checker for one section of a journal manuscript. You did not write it. Find every place where the prose, a table cell, an equation or a citation says something its cited source does not support. Be sceptical: a trace that looks right but points at the wrong thing is the failure you exist to catch.

Workspace root: <path>. The section: <file>, at commit <commit>. The sources and their pins are in the `sources` block of `<workspace root>/AGENTS.md`; read each source at its pin (for a `git:<rev>` pin, `git -C <root> show <rev>:<path>`, not the working tree). <For a document that is not a manuscript section: its pointer form (per sentence, per block or per table, which sets what *Placement* checks) and its source policy, which replaces the `sources` block; citing anything the policy excludes is a finding.> Read `<install>/skills/_shared/core.md` first (`<install>` is the installation root the workspace `AGENTS.md`, or the brief, names).

READ ONLY. Edit no file in the paper. Run no analysis and no code of the paper (reading, search and read-only git are fine). Write your report to <report path> as you go, not at the end (a reader that cannot write files returns it whole). Where a check needs a run you may not make, say which run would settle it and leave the statement unchecked.

For EVERY pointer (in a manuscript, each `% src:` comment; in another document, each pointer in the form named above), open the cited source at the cited place and check:

- **Line anchors.** The line exists and the named symbol owns it. Off by more than about three lines, or the wrong symbol, is a finding.
- **Heading and quote anchors.** The heading exists and the phrase appears verbatim.
- **Substance.** Reversed directions or comparisons. "Always", "never", "only", "every", "any" stronger than the source. Counts and lists: recount them, and check a list for completeness. A claim from one context (one driver, one format, one mode) generalised. Every symbol and sign of every equation. Verbatim listings: diff against the file.
- **Citations.** Is the cited paper the one for this statement? Open the paper itself and find the page, table or equation named; the note in `paper/lit/` only helps locate the passage. A statement about what a paper says must be what it says there. A paper that cannot be opened is reported as unchecked, not passed. A web source with no key is the exception: its note (URL, date, quoted text) is the pinned record.
- **Absence claims** ("nothing in X does Y"): re-run the search yourself and say whether it holds.
- **Derived values.** A number the paper derives must show its derivation in the trace, or point at a recorded check under `paper/checks/`. Recompute it. A derived value with no derivation is a finding.
- **Versions.** A recorded measurement presented as a property of the version described, when it was measured on another, is a finding.
- **Units and conventions.** A value in a unit or convention other than its source's is a finding even when numerically equal (core rule 1, *Copy, do not convert*).
- **Placement.** In a manuscript, each trace sits immediately above or beside the sentence it supports; in another document, each pointer sits where its pointer form says (by the sentence, the block or the table). A trace that supports a different sentence, and a sentence whose support has no trace, are findings.
- **What a trace may cite.** A trace that cites the manuscript itself (a `Table`, `Section` or `\ref` of the paper), a note an agent wrote (`paper/ingest/`, a brief, a survey), or a root marked `never` is a finding. In another document, the source policy above decides instead. In a manuscript, `tools/traces.py lint` catches most of these and has run already; note any it missed.

Then sweep for untraced quantities, including quantities in words ("two", "once", "half"), and for load-bearing claims and quantifiers with no trace.

Specific checks: <what the session wants looked at, for example each \gap{q}: is it justified?>

Re-check form: where the session names the changed sentences, read only those and their traces, plus any sentence whose meaning depends on them. Say so if a change affects text you were not given.

Report, at most <n> words, as numbered points. Each point has: its number; the location (file and line); the sentence; the anchor; what is wrong, with what the source says, quoted; the severity (wrong, overstated, weak anchor, cosmetic); and the change you recommend. Then give the number of anchors checked and how many passed cleanly, the results of the specific checks, and what you could not check or passed with doubt. Fewer, well-evidenced points beat many weak ones.
