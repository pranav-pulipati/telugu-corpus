# Coverage report

What the directory covers, what is missing, and how sure we are that nothing big was missed. Checked on 2026-11-11.

## How complete is it?

We **cannot claim** this list includes every Telugu OCR dataset that exists. What we can say:

- Every major open dataset platform with a search API was swept with the same ~34 query variants (Section 3 of the discovery log), and swept again in round 2 with broader queries.
- ILOCR, the main Indian OCR consortium, was checked exhaustively (every dataset ID, the full API list, every competition site).
- Hits from the API sweeps that matched both Telugu and OCR terms were reviewed. Later query variants mostly brought back datasets we already had, which suggests the open platforms are close to fully covered.
- Round 2 (citations, theses, Roboflow, AIKosh, ULCA, Wayback, broader platform queries) added 10 distinct datasets. Most of them are unreleased, gated or very new (2025-26), not overlooked open releases. That is further evidence the open channels are close to saturated, but not proof.
- Gaps are most likely in: datasets described only in paywalled papers or theses, private university collections, Roboflow projects, government portals that need a browser, and commercial vendors.

## Distinct datasets by category

| Category | Distinct | of which VERIFIED | of which open licence |
|---|---|---|---|
| OCR image-text: printed | 11 | 6 | 7 |
| OCR image-text: handwritten | 4 | 2 | 0 |
| OCR image-text: scene text | 5 | 4 | 1 |
| OCR image-text: synthetic | 16 | 9 | 5 |
| Machine-labelled OCR (not human ground truth) | 3 | 1 | 1 |
| Character / glyph classification | 20 | 5 | 10 |
| Layout / detection (no transcription) | 4 | 2 | 2 |
| Script identification | 6 | 3 | 4 |
| Text-in-image benchmark (VQA / document understanding) | 7 | 1 | 3 |
| Image-only (no transcription) | 7 | 2 | 2 |
| Image-only (transcription NOT VERIFIED) | 6 | 0 | 2 |
| Scanned archive (image-only) | 6 | 4 | 1 |
| Text-only corpus (OCR language modelling) | 9 | 6 | 5 |

Telugu image-text OCR datasets by granularity (distinct): Word 12, Page 11, Other 8, Line 5.

## Well covered

- **Handwritten words:** IIIT-HW-Telugu / HW-WORDS (~126K words) and the competition sets built on it, plus HW-UC and IHWWR.
- **Synthetic printed and scene text:** millions of rendered words and lines (IIIT-Synthetic-M/R/IndicSTR, Chitralekha, harsha-desaraju sets).
- **Printed pages:** Telugu Wikisource (~127K proofread pages on free scans) and sets derived from it. Also Mozhi word/line images and the NayanaOCR page corpus.
- **Characters:** many small handwritten character sets (HP Labs, Negi & Rao, IEEE and Kaggle uploads).

## Gaps (little or no data found)

- **Real scene text is small.** Labelled Telugu photo crops number in the low thousands (IndicSTR12 ~1.2K, BSTD ~2.8K, roadside IndicSTR-Word, MIST).
- **Handwritten lines and pages with full transcriptions** are rare and mostly locked in competitions (IHDR 2025 links are dead) or gated.
- **Historical documents:** thousands of palm-leaf manuscripts and old newspapers are scanned, but almost none have ground-truth transcriptions.
- **Forms, receipts, tables with cell text, and printed newspaper ground truth:** only commercial samples or layout-only sets (MUSTARD has structure but no cell text; IndicDLP has layout but no text).
- **Licence clarity:** many community uploads have no licence; several re-uploads conflict with the original.
- **Telugu shares of multilingual sets:** now counted for PHDIndic_11 (85 pages), IndicVisionBench (89 OCR pages), ORB-Indic (89), MInfoVisQA (384), PMGSY boards (1,020), adaption doc-QA (135 pages), BhartiOCR (500,000). Still unknown for MDIW-13, Indiscapes, IndicDLP (only the ~7.2% share), Kaggle Indian Scripts and GlotOCR.
- **Announced but unreleased:** CHIPS (2,874 Telugu handwritten pages), UniLipi Telugu-script manuscripts, the JASTT 33,496-character corpus and the ICON 2023 scene-text set all exist only in papers so far.

## Search channels exhausted vs remaining

| Channel | State |
|---|---|
| Hugging Face (datasets + models + language tag listing) | Exhausted for the query list |
| Kaggle (public API) | Exhausted for the query list |
| GitHub (search + repo trees) | Exhausted for the query list |
| Zenodo, Figshare, DataCite (incl. IEEE DataPort, Mendeley), Harvard Dataverse, Internet Archive | Exhausted for the query list |
| OpenAlex, arXiv | Exhausted for the query list; abstracts only |
| ILOCR (datasets, APIs, competitions) and CVIT/USODI | Exhausted |
| Mendeley Data (search API), DataCite (all Telugu records) | Exhausted (round 2) |
| Shodhganga theses | Exhausted for 24 queries (round 2) |
| OpenAlex citation following (14 hub papers) | Exhausted (round 2) |
| Bhashini ULCA (public metrics) | Exhausted for listing; downloads need login |
| Semantic Scholar | **Partly done**: 4 of 36 planned queries attempted, 1 answered; stopped after repeated HTTP 429 |
| Google Scholar | **Indirect only** (blocks scripts; ~25 general web searches instead) |
| AIKosh | **Partly searched** (portal timing out; web-search enumeration only) |
| Roboflow Universe | **Partly searched** (search snippets only; pages block scripts) |
| TDIL-DC | **Blocked** (expired certificate; not bypassed) |
| Paywalled full text, other university repositories | **Not searched** |
| Author contact for unreleased data | **Not done** |
