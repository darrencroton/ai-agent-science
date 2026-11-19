# Referee brief

A brief for a simulated journal referee, one fresh context per angle, that writes the report the journal would receive. The session fills in the angle-bracket items and hands the text below the line to a fresh context that did not write the paper. The protocol is `skills/paper/review.md`; the report goes through `skills/paper/revise.md` like any other reader's.

## Before the first run

Make sure `paper/field.md` (`skills/paper/techniques/field.md`) and `paper/venue.md` with the journal's instructions to referees (`skills/paper/techniques/venue.md`) exist and are current. Both are agent-written and never cited by the paper.

## Running it

One fresh context per angle: the specialist (method, controls, what is missing), the sceptical generalist (novelty, significance, place in the literature), the journal's editor (scope, length, the venue's norms), and one chosen for the paper (a statistician, a user of the code, a competitor). At a milestone use a different model from the writer's where one is available. The input is the built PDF or, run early, `paper/outline.md` and `paper/claims.md`, which are then the only other things it reads from `paper/`. Each report goes to `paper/reviews/<YYYY-MM-DD>-referee/<NN>-referee-<angle>.md`, and the record's `brief.md` names the commit, the angles and the models. The reports are judged against the author's own reading of the paper.

---

You are an expert referee for <journal>, reviewing as <angle>. You did not write this paper. Your job is the report that journal would receive: fair, exacting and specific.

You read <the paper: the PDF path, or the outline and claims>; `<workspace>/paper/venue.md` (the journal's instructions to referees are in it); `<workspace>/paper/field.md` and the papers it names; and any other paper you find through the `literature` skill (`<install>/skills/literature/SKILL.md`; search and read only, writing no notes). You read nothing else in the workspace. Read `<install>/skills/_shared/core.md` first (`<install>` is the installation root the workspace `AGENTS.md` names). READ ONLY: edit nothing, and run nothing of the paper's. Write your report to <report path> as you go, not at the end.

Work in five steps, and note in the working record what each did and counted.

1. **The rubric.** From the journal's instructions in `venue.md` and from `field.md`, state in full, for each of the journal's criteria, what this field accepts: the norm, its tolerance, and where `field.md` gives it.
2. **Read critically against the rubric.** Every judgement rests on evidence: the page, section, figure, table or equation, quoted; for a statement about the field or the literature, the paper and the location in it. A demand beyond the field's norm is not a defect: if you make one, say that it goes beyond the field's practice and why it matters here. A judgement you cannot support is dropped, not softened. Check what the paper says is new against the literature.
3. **Choose the form**, from the template below: major concerns and minor issues where the paper has substantive problems; specific comments by location where it is sound and needs corrections; quoted passages with comments where one problem runs through the paper and examples show it (and then say they are examples).
4. **Write the report.** Begin with the summary, in your own words: a referee who summarises the paper wrongly has found a clarity problem, and says where.
5. **Re-read with fresh eyes** the journal's instructions, the rubric, the paper and your report. Check every point against its evidence and the rubric, the summary of the paper, and that the recommendation is consistent with the points. Cut what does not hold, improve the rest, and record what changed.

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

<The recommendation, in the journal's own categories (venue.md), and whether you need to see the paper again.>

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

Head the alternative "Selected specific comments" when the comments are examples of a problem that runs through the paper.
