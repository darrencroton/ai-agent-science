# paper — mode: iterate

`/paper iterate <section>` — an independent check that every trace in a drafted section says what its source says.

## Before anything

The router's *Before every mode* comes first (`SKILL.md`).

**Why it exists.** A drafter's own read-back (`draft` §5) misses what a fresh checker finds: the drafter cannot see overstatement in its own prose.

## 1. Choose what to check

A section just drafted, or a section whose sources have moved (a new subject version, an edited note). Check one section per checker.

## 2. Brief the checker

A fresh agent (a subagent, or a separate session where the harness has none) that did not draft the section, on a different model where one is available. **Read only, and it never runs code.** Fill in the template and send it:

```text
You are an independent trace checker for one section of a journal manuscript. You did not write it. Find every place where the prose, a table cell, an equation or a citation says something its cited source does not support. Be sceptical: a trace that looks right but points at the wrong thing is the failure you exist to catch.

Workspace root: <path>. The section: <file>. The subject: <repository and the version the anchors are pinned to>.
First read <root>/skills/_shared/house-rules.md: the integrity rules and Source comments.
READ ONLY. Edit no file. Run no code or tests (reading, grep, read-only git are fine).

For EVERY `% src:` comment, open the cited file at the cited place and check:
- Line anchors: the line exists and the named symbol owns it. Off by more than about 3 lines, or the wrong symbol, is a finding.
- Heading and quote anchors: the heading exists and the phrase appears verbatim.
- Substance. Reversed directions or comparisons. "always / never / only / every / any" stronger than the source. Counts and lists: recount, and check lists for completeness. A claim from one context (one driver, one format, one mode) generalised. Citations: is the cited paper the one for this point? Every symbol and sign of every equation. Verbatim listings: diff against the file.
- Absence claims ("nothing in X does Y"): re-run the search yourself and say whether it holds.
Then sweep for untraced quantities, including quantities in words ("two", "once", "half"), and for load-bearing claims with no trace.
Specific checks: <what the main session wants looked at, e.g. each \gap{q}: is it justified?>

Report (under <n> words): a table of findings with line, sentence, anchor, what is wrong, severity (wrong / overstated / weak anchor / cosmetic), and the fix you recommend. Then the number of anchors checked and the number that passed cleanly, the results of the specific checks, and what you could not check or passed with doubt.
```

## 3. Confirm every finding at source

The main session opens the source for each finding. **A finding is never applied on the checker's word**; the author is the verifier and the checker is a lead.

## 4. Fix

A fix that changes a claim's strength is made only to match its source, and it is listed in the report: **never silent**, as `_shared/house-rules.md` forbids. Where the source cannot settle it, the sentence becomes a `\gap`, not a softer one.

## 5. Two greps worth having

These are recipes, not tools.

**Promises.** List the forward references to sections not yet drafted, with what each promises, so that each is checked when that section is drafted (`draft` §3): `grep -n '\\ref{sec:' manuscript/sections/*.tex`, then keep the labels of undrafted sections.

**A move.** When text moves between files, list the `% src:` anchors and the `\gap` markers before and after, so "nothing lost" is checkable: `mkdir -p .scratch`, then `grep -h '% src:\|\\gap{' <files> | sort > .scratch/before.txt`, the same after into `.scratch/after.txt`, then `comm -3 .scratch/before.txt .scratch/after.txt`.

## 6. Close the session

Per `_shared/memory.md`: `STATE.md`, and a journal entry that carries the findings summary (counts by severity, what changed meaning, what was left open).
