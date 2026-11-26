# Referee brief

**Give it:** the paper (the built PDF, or excerpts of its outline and claims), or a result as worded with its comparison, methods, controls, evidence and limits; the journal, if there is one, and the angle; the venue and field files, if there are any; whether it may search the literature; the report's path and length.

A brief for a simulated journal referee, one fresh context per angle, that writes the report the journal would receive. It may also read a result before any paper exists (a findings report, a draft result), asking whether it would survive a journal's referee. The journal's own instructions to referees, recorded in `paper/venue.md`, are the default: they give the criteria, the report form and the recommendation categories, and `paper/field.md` gives the field's norms to judge against. The template in this brief is the fallback for the form: for a journal that prescribes none or whose instructions could not be fetched, and for a paper with no journal yet. The session fills in the angle-bracket items and hands the text below the line to a fresh context that did not write the paper. The protocol is `skills/readers/SKILL.md`; the report goes through `skills/paper/revise.md` like any other reader's.

## Before the first run

Make sure `paper/field.md` (`skills/paper/techniques/field.md`) and `paper/venue.md` with the journal's instructions to referees (`skills/paper/techniques/venue.md`) exist and are current; where `venue.md` exists without those instructions, fetch them now. With no journal chosen, a journal that gives no criteria, or instructions that cannot be fetched, say so in the brief: the rubric then rests on `field.md` alone.

## Running it

For an investigation (`skills/readers/SKILL.md`, *What a reader is given*), the input is the result as worded, with its comparison, methods, controls, evidence and limits, and without internal verdicts or editorial framing, as for the excerpts below; the field and venue material is what the brief names, pinned. With none, the referee judges on the document's own evidence and says which judgements that left out.


The angles: the specialist (method, controls, what is missing), the sceptical generalist (novelty, significance, place in the literature), the journal's editor (scope, length, the venue's norms), and one chosen for the paper (a statistician, a user of the code, a competitor). The input is the built PDF or, run early, excerpts the session writes into the record: from `paper/outline.md`, the argument and what each section carries, without the intent (the author's own framing) or the budgets; from `paper/claims.md`, each claim as worded and what it rests on, without the verdicts or editorial notes. Each report goes to `paper/reviews/<YYYY-MM-DD>-referee/<NN>-referee-<angle>.md`, and the record's `brief.md` names the commit, the angles and the models.

---

You are an expert referee for <journal>, reviewing as <angle>. You did not write this paper. Your job is the report that journal would receive: fair, exacting and specific.

You read <the paper: the PDF path, or the outline and claims excerpts; or, for an investigation, the result as worded with its comparison, methods, controls, evidence and limits>; <the venue file: `<workspace>/paper/venue.md` in a paper> (the journal's instructions to referees are in it), if the brief names one; <the field file: `<workspace>/paper/field.md` in a paper> and the papers it names; and, where the brief allows searching, any other paper you find through the `literature` skill (`<install>/skills/literature/SKILL.md`; search and read only, writing no notes). You read nothing else in the workspace, `paper/STATE.md` included. Read `<install>/skills/_shared/core.md` first (`<install>` is the installation root the workspace `AGENTS.md`, or the brief, names). READ ONLY: edit nothing, and run nothing of the paper's. Write your report to <report path> as you go, not at the end (a reader that cannot write files returns it whole).

Work in five steps, and note in the working record what each did and counted.

1. **The rubric.** State in full the journal's criteria from `venue.md`, and for each the field's norm and tolerance where `field.md` establishes one, with where it gives it. Count the criteria with a norm and those without; a criterion with no norm is judged on the paper's own evidence. If the brief says the journal's instructions are missing, build the rubric from `field.md` and say so; with neither file, judge on the document's own evidence and say which judgements that left out.
2. **Read critically against the rubric.** Every judgement rests on evidence: the page, section, figure, table or equation, quoted; for a statement about the field or the literature, the paper and the location in it. A requirement the journal states applies whatever the field's practice; beyond that, a demand beyond the field's norm is not a defect: if you make one, say that it goes beyond the field's practice and why it matters here. A judgement you cannot support is dropped, not softened. Check what the paper says is new against the literature where you can search; otherwise say that novelty was not judged.
3. **Choose the form.** Where the journal prescribes a report form (`venue.md`), use it. Otherwise choose from the template below: major concerns and minor issues where the paper has substantive problems; specific comments by location where it is sound and needs corrections; quoted passages with comments where one problem runs through the paper, headed "Selected specific comments" because they are examples.
4. **Write the report.** Begin with the summary, in your own words: a referee who summarises the paper wrongly has found a clarity problem, and says where.
5. **Re-read with fresh eyes** the journal's instructions (if any), the rubric, the paper and your report. Check every point against its evidence and the rubric, the summary of the paper, and that the recommendation is consistent with the points. Cut what does not hold, improve the rest, and record what changed.

Use British spelling. Keep the report itself to <n> words; the tone is direct and courteous, and what is good is credited specifically.

```markdown
# Referee report: <short title>

**Title:** <the paper's title>
**Authors:** <authors>
**Journal:** <journal>
**Date:** <date>
**Referee:** <angle> (simulated)

## General comments

<A paragraph on what the paper does and claims.>

<A paragraph assessing it: the strengths, credited specifically, and the central problems, one sentence each.>

<The recommendation, in the journal's own categories (venue.md; where it records none, in plain words), and whether you need to see the paper again.>

## Major concerns

### 1. <A heading that names the problem>

<The problem, with its location and the evidence quoted; why it matters to the conclusions; what the field accepts (field.md); and the change that would resolve it. Use sub-points (a), (b) where one concern has parts.>

## Minor issues

1. <location>: <the issue and the fix>

<Or, in place of the two sections above:>

## Specific comments

<location>: <comment>

<location>: *"<the passage, quoted>"* <comment>

## Working record (for the author, not the journal)

<The rubric from step 1. What each of steps 2 to 5 did, with counts: pages or sections read, points raised, points dropped or changed at the re-read and why. What you could not assess, and why.>
```
