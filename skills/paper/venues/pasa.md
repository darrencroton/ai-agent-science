# Venue: PASA (Publications of the Astronomical Society of Australia)

Facts true for any paper submitted to PASA, found by building the journal's own template on a current TeX. Paper-specific choices (spelling, macros) are not here. How to switch a manuscript to a journal's class is in `skills/paper/techniques/venue.md`.

## Template

Cambridge's "PAS LaTeX template 2022" (`pas.cls` v1.0, 2021/04/29, with `paslike.bst`), downloaded 2026-11-16 from the "Downloadable Zip File - PASA LaTeX template" link on PASA's "Preparing your materials" author-instructions page. Check the page for a newer one before relying on this. The class loads `natbib` with author-year citations.

## Preamble fixes

All tested on TeX Live 2022. None edits the class.

1. **The class replaces the kernel's `\document` with a copy from before 2020.** The copy skips the begin-document hooks that set up the colour stack and `hyperref`, so the template's own guide fails with "Extra \endgroup" and colour-stack errors. Keep the kernel's `\document` and re-add the class's one addition (opening its `.tab` file). `amsmath` goes first, before the class, because the class loads `cleveref`, which must come after it:

   ```latex
   \RequirePackage{amsmath}
   \let\KernelDocument\document
   \documentclass{pas}
   \makeatletter
   \let\document\KernelDocument
   \AtBeginDocument{\if@filesw\immediate\openout\@maintab\jobname.tab\fi\process@table}
   \makeatother
   ```

2. **The class's modified `tabular` mis-sets `p{}` columns**: rows overprint and reorder. Never use `p{}`. Use `l` columns and wrap long text in a macro, for example `\newcommand{\tcell}[2]{\parbox[t]{#1}{\raggedright #2}}` used as `\tcell{4cm}{...}`.

## The bibliography style

`paslike.bst` reports "can't pop an empty literal stack" for every `@article` while still writing a correct bibliography, which makes `latexmk` exit non-zero. The fault is a stray `output` after `format.vol.num.pages` in the `article` function (line 512 of the 2022 file); deleting that one token fixes it. Keep the unmodified file as `manuscript/template-reference/paslike-original.bst`.

## Characters

Core rule 2 applies (a record that will not render is fixed in the preamble, never in `refs.bib`): add a `\DeclareUnicodeCharacter` with a comment naming the record or the listing. Seen so far:

- `\DeclareUnicodeCharacter{2500}{--}`: ADS exported a record with U+2500 (box drawing) where the source has an en dash, which stops pdfLaTeX.
- `\DeclareUnicodeCharacter{2014}{---}`: an em dash in a verbatim listing printed as `|` under this class, with no error.

A manuscript may need others; add them here when found.

## Build output

`pas.cls` writes `main.tab` beside the build, so add `*.tab` to the workspace `.gitignore` when switching to PASA.

## Baseline warnings

`pas.cls` emits overfull `\vbox` warnings of 42 to 797 pt on every page, from its output routine. The template's own guide produces the same set. Judge a build by the warnings it adds to these, not by the log being clean. Errors, undefined references and undefined citations are never baseline.

## Tables and listings

- **Tables:** caption first, then `\toprule`, `\midrule` and `\botrule`; no vertical rules; the body wrapped as `{\tablefont\begin{tabular}{@{\extracolsep{\fill}}ll...}...\end{tabular}}`. A table wider than a column is `table*`. The class resets the table counter at `\appendix`.
- **Listings** (configuration or run-file excerpts): `verbatim` inside a `figure`, in `\footnotesize`; `figure*` if a line is wider than about 50 characters. **Inspect the rendered PDF**: the class drops characters it cannot print without an error (see *Characters*).

## Citations

`natbib`, author-year: `\citet{}` and `\citep{}`; `\bibliographystyle{paslike}`.

## Conformance checks

Only what the evidence above states as a PASA requirement, as greps over `manuscript/`:

```sh
grep -n 'begin{tabular}' main.tex sections/*.tex | sed 's/\\extracolsep{[^}]*}//g' | grep -E 'p\{|\|'   # a p{} column or a vertical rule (\extracolsep stripped first: it contains "p{")
grep -n 'begin{tabular}' main.tex sections/*.tex | grep -v tablefont   # a table body not wrapped in \tablefont
```

The full submission checklist belongs in `skills/paper/finish.md`, written when a paper reaches submission.
