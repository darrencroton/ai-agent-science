# A subject repository

For a paper that describes software or an instrument: the repository itself is the main source, and it keeps changing. Read it at the start of the paper, and again whenever a drafter's anchors disagree with the checkout. **Outside a paper**, give it the repository, a revision, the questions and where the report goes. What then applies is: read every file at the revision given, never from the working tree, and write nothing in the repository; treat forward plans, proposals and archives as not delivered; and read it whole, by question, across every branch, reporting file and place for each finding. The rest of this file, from linking into a workspace to the feature map against an outline, concerns a manuscript.

## Pin it and read at the pin

- Record the tag and commit the paper describes in the `sources` block (`<root>/  git:<rev>  cite`). Read every file at it with `git -C <root> show <rev>:<path>`, not from the working tree.
- Each section file opens with a comment naming the version its anchors were read at, and the command that re-reads a file at it. A checkout that has moved past the tag is re-read at the tag; `git diff --quiet <rev> HEAD -- <path>` says whether a file is as released.
- A re-measurement is a question for someone who may run the code (core rule 6).
- Link the repository into the workspace so that every anchor begins with its root, and write nothing in its files. The paper's own notes and figures live in the workspace.

## Cite only what was delivered

- Forward plans, design proposals and local archives are roots marked `never`. A plan is not a feature.

## Read it whole

- Use parallel readers by question (`skills/paper/start.md`, step 2, which also says how each note records its pin): capabilities, history, recorded runs and logs, tests (what the authors take correctness to mean), the development method, the products.
- Read the history across every branch, not only the main one. An unmerged branch can hold the one correctness comparison the paper needs, and the history answers questions the README cannot.
- **Build a feature map from the release history** in `paper/ingest/feature-map.md`: the changelog and tags read in order, one row per feature with the release that introduced it, where it lives and the outline section that covers it. A feature with no section is a question for the author.

## Follow the code where a guide disagrees

- Prose follows the code. The disagreement goes on one list for the subject's owner: the subject's own backlog only where the author has authorised writing to it (named in the workspace `AGENTS.md`), otherwise `paper/subject-notes.md`. Each entry gives the guide's words, the code's behaviour and both locations. So does a quirk that is neither a disagreement nor a hole in the draft, such as a configuration key nothing reads.
- It does not go in the paper's open questions, which would bury the author's decisions under the owner's chores. It becomes a `\gap{q}` in the manuscript only when it changes what a sentence says.
- A disagreement between the code and the **author's** notes is different: it is always a `\gap{q}` (`skills/paper/draft.md`).

## When the subject moves under a draft

While the subject is still changing (investigations running, a release coming), keep `paper/ingest/subject-delta.md`: one line per change to the subject that touches drafted text, giving what changed, the drafted passages it touches (section file and subsection) and whether it is released. Add a line when a change becomes known, and when a passage is drafted that a known change touches. At a re-pin, check the list against the traces that `tools/traces.py moved --from <old> --to <new> <root>` reports as anchored in files the re-pin changed; the revision that follows works from it, and a line leaves once its passages are rewritten. It is an index, never a source.

## Leaving detail to the subject's documentation

A paper may leave detail to the subject's own guides and cite them at the pin. Before a cut does so:

- Check that the guide holds each fact at the pin. A fact it lacks stays in the paper; it may also go on the owner's list (*Follow the code where a guide disagrees*).
- Check that the release is citable as a stable, archived version with a persistent identifier (e.g. a DOI minted by a release-archiving service). A git tag or repository URL alone is not.

Until both hold, the detail stays in the paper (core rule 7).
