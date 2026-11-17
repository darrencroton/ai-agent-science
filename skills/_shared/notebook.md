# Literature notebook

The notebook is a directory — `paper/lit/` in a paper workspace, or whichever directory a caller names. Its format is the same in every binding, so a notebook can move between a paper and a campaign.

`index.md` is a flat roster — one row per paper that has entered play,
whether or not it has been read:

```markdown
| Bibcode | Handle | Why it is in play | Read |
|---|---|---|---|
| 2006MNRAS.365...11C | Croton+06 | the radio-mode model we compare against | yes |
| 2015MNRAS.451.2663H | Henriques+15 | later calibration of the same model | no |
```

**Where a work has no bibcode**, put its identifier in that column instead —
`arXiv:2305.16291`, or a bare DOI — and say so plainly rather than leaving the
cell empty. Rule 2's other two exporting paths exist precisely for these, and
a later session that sees a blank first column will go looking in ADS for
something ADS does not have.

**Where a roster was assembled without `ads.py`** — a web reconnaissance pass,
say — the bibcodes in it are reconstructed rather than read, and the table
carries one line at the top saying so. They are re-resolved at export time
regardless; the note is what stops them being trusted in the meantime.

The *Handle* is what the prose calls the paper. *Why it is in play* is one
clause, and it is the field that stops the same paper being chased twice in
three months' time.

`<bibcode>.md` exists **only for papers actually read in depth**. The
asymmetry is deliberate: a stub file per search hit would be hundreds of empty
files. The filename is the bibcode exactly as ADS writes it, `.md` appended —
`2013ARA&A..51..511K.md`. Bibcodes contain `&` and `.`, which are fine in a
filename but need quoting in a shell.

```markdown
# 2006MNRAS.365...11C — Croton+06

**Read:** 2026-08-21 · [ADS](https://ui.adsabs.harvard.edu/abs/2006MNRAS.365...11C)

## What it does
<two or three sentences: the sample or simulation, the method, the headline result>

## Why it matters here
<what this paper takes from it, or argues against — one paragraph>

## Extracted values
| Value | Where in the paper | Notes |
|---|---|---|
| $M_{\rm crit} = 10^{12.5}\,h^{-1}M_\odot$ | Table 2, row 3 | their $h=0.73$, Chabrier IMF |
| bright-end slope steepens above $L^*$ | Fig. 8 — **visual estimate** | not quoted as a measured value |

## Caveats
<sample limits, cosmology, IMF, mass definition, aperture, resolution — whatever
would make a comparison unfair. Each one names where in the paper it is stated,
the same as a value does: these live in a methods section nobody will find again
without the pointer, and they are what decides whether a comparison is fair at all.>
```

**Every extracted value names where in the paper it came from** — the table and
row, the equation number, the section. That location is what a `% src:` into
this file eventually points at. The visual-estimate rule in
`_shared/house-rules.md` applies to these notes too, and the label is written
here rather than left to be remembered, so that it travels with the number.

**A web source** — a data portal, a repository page, anything with no paper behind it — gets a note `web-<slug>.md` and an index row whose identifier column carries `web:<slug>`:

```markdown
# web:example-portal — Example data portal

**Fetched:** 2026-11-16 · <URL> · **Confidence:** read from the page itself

## What it says
<what the page states, quoted, each with where on the page: heading, table or line>
```

**Confidence** is one of *read from the page itself* or *recovered only through a search index* — say which, and say the second is lower: the page was not seen, and what a snippet shows may have moved since. Pages change, so the date is part of the record.
