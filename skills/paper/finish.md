# Finish

Making the paper ready for the author to submit. Read it when the author says the paper is ready, and again before a revision goes back. Each step points to where it is done; submission itself is the author's act.

1. **Every trace checked.** `tools/traces.py lint` reports nothing and `stale` reports every file checked since its last change. A source pinned `git:` or `fixed` that has moved since a stamp has its traces re-checked first (`skills/paper/revise.md`, step 8), since `stale` compares only the manuscript.
2. **The framing check** (`skills/paper/sections.md`, *Framing*) on the title, abstract, introduction and conclusions.
3. **The reads.** The stylist's milestone read and the author's full read are disposed of (`skills/paper/revise.md`).
4. **The author's audit.** `tools/traces.py sample 20`, read by the author beside the sources.
5. **The venue.** `paper/venue.md` checked for drift (`skills/paper/techniques/venue.md`); its checklist met (length, data availability, the statement on AI use, declarations); its conformance greps clean.
6. **The final build.** No `\gap` remains: set `[final]` on `scipaper` and build in a fresh scratch copy (`skills/paper/draft.md`, step 4). Then the bundle the journal receives: `latexpand --empty-comments main.tex` into a new, empty directory with the class and any file it loads (a journal logo, say), the bibliography style, `scipaper.sty`, the `.bbl` from a build of the source (keeping `main` as the name, so the two match), and the figures, built clean there and judged against the venue's baseline warnings. The traces stay in the workspace, not in the bundle.
7. **Record the submitted commit** (a tag, `submitted-<YYYY-MM-DD>`, and a journal line). A reply to the journal's referee is diffed against it.
