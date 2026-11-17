# ai-agent-science

**Work in progress — stage 2a built; the rest is being built by writing a real paper.**

The science-method toolkit: a small set of [Claude Code](https://claude.com/claude-code) skills that hold how scientific work is done, apart from any subject it is done on. Today that is a `paper` skill with modes, which helps a working astronomer turn notes, figures, tables and analysis code (or a software repository) into a journal paper and keep working on it for as long as it takes, and a `literature` skill, which searches the astronomical literature and keeps a notebook of what it found. There is one stdlib script, for ADS access, and one LaTeX package, for gap markers.

It is built for the way papers actually get written: **starting before the picture is complete, and letting the writing shape the result.** The first draft is deliberately incomplete, with every hole marked rather than smoothed over. The astronomer is the verifier: the system never claims a number, method or citation is correct, it makes what it did visible and traceable so you can check it fast. Where a skill would ask the author a question, a recorded default lets a caller with no author present, such as a Campaign Manager running under a brief, use the skills too.

It was called sci-paper until 2026-11-17.

## Status

| | |
|---|---|
| Design | see [`docs/ai-agent-science - Plan.md`](docs/ai-agent-science%20-%20Plan.md), which is also the build record |
| Built (stage 2a, 2026-11-17) | the rename; one `paper` skill with modes `start`, `draft`, `voice`, `venue` and `iterate` (the trace check); `literature` unbound from the paper, with five modes and three bindings (in a paper, in a named notebook, unbound); a recorded default for every author question; the Mimic paper's lessons folded in, including the first venue file (PASA) |
| Stage 2b | the Mimic paper is the vehicle: `iterate`'s structural read, `frame` (Introduction, Conclusions, Abstract, Title) and `finish` are built by writing it |
| Stage 3 | `scope`, `findings` and `challenge`, and the catalogue of evidence clauses. Not built |

The architecture this belongs to, with stages 2a, 2b and 3 and the other repositories it works with, is `docs/dev/AGENTIC-SCIENCE-ARCHITECTURE.md` in the Mimic repository.

## What is here

```text
docs/ai-agent-science - Plan.md   # the design, the build record and the status. start here
tools/ads.py                      # the only script: ADS/SciX, stdlib only
skills/
├── _shared/                      # data the skills read, not skills
│   ├── memory.md                 # what to read first, what to write last, open questions
│   ├── house-rules.md            # integrity rules, gap markers, % src:, the workspace root
│   ├── notebook.md               # the literature notebook's format
│   ├── author-questions.md       # every point where a skill asks the author, with its unattended default
│   ├── sections/                 # rhetorical moves per section role
│   └── venues/                   # one file per venue: pasa.md
├── paper/
│   ├── SKILL.md                  # the router
│   ├── modes/                    # start, draft, voice, venue, iterate
│   └── templates/                # the drafting brief
└── literature/SKILL.md           # query craft and five modes
skeleton/
├── root/                         # appended into the working directory (an index only)
└── workspace/                    # copied to become sci-paper-workspace*/
    ├── CLAUDE.md
    ├── paper-voice/README.md
    ├── paper/                    # STATE, journal, outline, open questions, lit
    └── manuscript/               # main.tex + scipaper.sty
```

## The two skills

`/paper <mode>`:

- `start` — read the notes, look at the figures, propose an argument and a list of questions; for a software paper, read the repository and its release history too
- `draft <section>` — write a methods, results or discussion section from notes, code or figures, marking what it cannot answer; or several at once from a shared drafting brief
- `voice` — distil past papers or style notes into this paper's own voice profile
- `venue` — which journals take this paper, what shape papers of this kind take, and how to switch the manuscript to the one chosen
- `iterate <section>` — an independent check that every trace in a drafted section says what its source says

`/literature <mode>`:

- `novelty`, `build-on`, `support/contradict` and `mine` — has this been done, what is closest, what supports or contradicts this claim, and what values can I compare against
- `provenance` — who made this dataset or tool, and where is that written down

`frame` and `finish`, and `iterate`'s structural read, are the remaining modes, and are not built.

## Using it

Install once, globally: this repo is composed into a shared agent home (the `ai-agent-home` repo) as a manifest-managed clone, `repos/ai-agent-science`, which links `skills/paper` and `skills/literature` into the one catalogue each harness reads. The skills are then available from any working directory.

`/paper start` scaffolds a paper **workspace** — always `sci-paper-workspace/`, a fixed-name subdirectory of wherever you are, and always its own independent git repository. The workspace keeps its historical name, as do `scipaper.sty` and a few other names written into live workspaces; they belong to the workspace format, not to the toolkit. Nothing the toolkit creates or touches reaches the project's own git history: your working directory's agent-instruction file gets one small appended index block, and its `.gitignore` gets one appended line excluding the workspace entirely (a paper whose subject is the project itself touches neither). Everything the paper needs — its draft, its memory, its literature notes, an optional `paper-voice/` of past papers to write like — lives inside that one isolated directory, and your own `notes/`, `figures/` and `code/` stay exactly where your project already keeps them.

Between sessions the project remembers itself in `paper/` — a short living state file, an append-only journal, the argument spine, open questions each with a recommendation, and literature notes. A new conversation picks up where the last one stopped. `/literature` works inside a paper, in a notebook directory you name, or with no paper at all.

Needs an [ADS/SciX API token](https://ui.adsabs.harvard.edu/user/settings/token) and `latexmk`. No third-party Python packages, no node, no MCP client.

## Licence

MIT
