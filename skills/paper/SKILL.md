---
name: paper
description: Write a journal paper from an author's notes, figures, tables and analysis code, or from a software repository, in a git-isolated workspace with durable memory. Modes - start (ingest the material, scaffold the workspace, propose the argument and the open questions), draft (write or rewrite a methods, results or discussion section, marking every hole), voice (distil the author's past papers or style notes into this paper's voice profile), venue (which journals take this paper, and what shape papers of this kind take), iterate (an independent check that every trace in a drafted section says what its source says). Use for starting, writing, structuring or continuing a paper, and for choosing a journal. Literature questions go to the literature skill.
---

# paper

One skill, several modes. Each mode's procedure is in `modes/<mode>.md` and is
read in full when the mode runs; this file only routes to it and holds what
every mode shares.

| Mode | Use when | File |
|---|---|---|
| `start` | beginning a paper, or pointed at a directory of research material with no manuscript yet: ingest it, scaffold the workspace, propose the argument and the open questions | `modes/start.md` |
| `draft <section>` | writing or rewriting one methods, results or discussion section from the notes, figures and code, marking every hole | `modes/draft.md` |
| `voice` | the author has put past papers or style notes in `paper-voice/` and wants them applied, or the profile refreshed | `modes/voice.md` |
| `venue` | choosing a journal, and finding what shape papers of this kind take | `modes/venue.md` |
| `iterate <section>` | a section has just been drafted, or its sources have moved: an independent check that every trace says what its source says | `modes/iterate.md` |

Not built yet: `frame` (Introduction, Conclusions, Abstract, Title), `finish`,
and `iterate`'s structural read of a draft. If asked for one, say so and do not
improvise it.

## Picking the mode

`/paper <mode> [args]`, or plain conversation. The commands are shortcuts, not
an interface: this is a settled design rule, and the workspace's own `CLAUDE.md`
points every session at `paper/STATE.md`, so a session that was never given a
command still starts in the right place. If the mode is unclear, ask (AQ16).

Literature questions — novelty, build-on, support/contradict, mine, provenance, filling a
`\gap{cite}`, exporting BibTeX — are the `literature` skill, not a mode here.

## Before every mode

1. Find the workspace root, per `_shared/house-rules.md` *The workspace root*.
   `start` is the exception: it may run before any workspace exists, and its
   own *Before anything* replaces steps 1 and 2.
2. Read `paper/STATE.md` in full.
3. Read `_shared/memory.md` and `_shared/house-rules.md` from the installation
   (`../_shared/` relative to this file; the installation root itself is
   resolved per house-rules *Locating the installation*).
4. Read `_shared/author-questions.md`: the modes cite its ids where they ask the
   author. Its defaults apply only when running unattended, with no author at
   the keyboard.
5. Read the mode file in full and follow it.

They are the authority and are not restated here.
