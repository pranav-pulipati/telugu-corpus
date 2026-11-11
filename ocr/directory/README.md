# Telugu OCR Dataset Directory

A checked list of every Telugu OCR dataset we could find: printed, handwritten, scene-text and synthetic
image-text data, plus related resources (character sets, layout sets, scanned archives, text corpora).
It tells you **what each dataset contains, whether it really has Telugu, whether it has transcriptions,
how to get it, and what the licence allows**.

This is a directory, not a download. No dataset was bulk-downloaded to build it.

**Last updated:** 2026-11-11

## The main file

**[`telugu_ocr_final.csv`](../../telugu_ocr_final.csv)** (repo root): one row per dataset, mirror, related resource or rejected
candidate, with the 36 requested columns plus three classification columns:

- **Resource category** - what kind of resource it is (see below). Filter on this first.
- **Counts as distinct dataset** - `Y` means it is its own dataset. `N (...)` means it is a mirror, copy, subset or derivative of another row (the row ID is named). `UNKNOWN` means we could not tell.
- **Existing catalogue record** - the matching `record_id` in the repo's `MASTER_CATALOGUE.csv`, if any.

Rows are numbered `TOCR-001` to `TOCR-181`. Unknown facts are written as `UNKNOWN` or `NOT VERIFIED`, never guessed.
`Direct download URL` is filled only where a real file link was seen. Where a login or form is needed, the official page is given instead.

Tip: to get usable OCR training data, filter `Resource category` starting with `OCR image-text`, `Counts as distinct dataset` = `Y`,
and `Verification status` = `VERIFIED`. That gives **21** datasets.

## Totals

| | Rows |
|---|---|
| All rows in the CSV | 181 |
| Dataset rows (excludes related resources and rejected) | 145 |
| **Distinct datasets** (`Counts as distinct dataset` = Y) | **92** |
| ...of which Telugu image-text OCR datasets (printed / handwritten / scene / synthetic) | 30 |
| Possible extra datasets, distinctness unknown (mostly unconfirmed leads) | 18 |
| Mirrors, copies, subsets and derivatives | 35 |
| Related resources (tools, models, fonts, portals; not datasets) | 10 |
| Rejected candidates | 26 |
| Duplicate / derivative relationships recorded | 55 |
| Rows matching a record in the existing catalogue | 36 |

## Categories

| Category | Rows | Distinct datasets | What it means |
|---|---|---|---|
| OCR image-text: printed | 17 | 10 | Images of printed/born-digital Telugu text with human-made or human-checked transcriptions. |
| OCR image-text: handwritten | 10 | 3 | Images of handwritten Telugu words/lines/pages with transcriptions. |
| OCR image-text: scene text | 14 | 5 | Photos of signs, boards and other real-world text (and born-digital images like memes) with transcriptions. |
| OCR image-text: synthetic | 19 | 12 | Computer-rendered Telugu text images; the label is the exact text that was rendered. |
| Machine-labelled OCR (not human ground truth) | 4 | 2 | Image-text pairs whose text came from an OCR engine or an AI model, not a person. Use with care. |
| Character / glyph classification | 28 | 19 | Single characters, vowel signs or digits sorted into classes. Good for character recognisers, not for word/line OCR. |
| Layout / detection (no transcription) | 8 | 4 | Boxes or regions (text blocks, tables, lines) without the text itself. Not OCR transcription data. |
| Script identification | 5 | 5 | Images labelled only with which script/language they contain. |
| Text-in-image benchmark (VQA / document understanding) | 7 | 6 | Question-answer or retrieval sets built on text-heavy images. Tests reading, but labels are not transcriptions. |
| Image-only (no transcription) | 9 | 7 | Telugu text images without any text labels. |
| Image-only (transcription NOT VERIFIED) | 7 | 6 | Images where labels may exist but could not be confirmed. |
| Scanned archive (image-only) | 8 | 5 | Large collections of scanned books, newspapers or manuscripts. Raw material only - no ground truth. |
| Text-only corpus (OCR language modelling) | 9 | 8 | Plain Telugu text with no images. Useful for OCR language models, spell-checking and rendering synthetic data - never image-text data. |
| Related resource (not a dataset) | 10 | 0 | Tools, models, fonts and portals that help build OCR data. Not counted as datasets. |
| Rejected | 26 | 0 | Candidates that turned out to have no Telugu, no images, or no data. Kept so nobody re-checks them. |

## Verification status

Counts are for dataset rows; "distinct" counts only rows marked `Y`.

| Status | Rows | Distinct | Meaning |
|---|---|---|---|
| VERIFIED | 74 | 45 | Landing page or files were opened on the check date and the key facts (Telugu content, labels, size, licence) were confirmed from the source itself. |
| PARTIALLY VERIFIED | 33 | 29 | The resource exists and some facts were confirmed, but at least one important fact (often the Telugu share, size or licence) could not be. |
| UNVERIFIED | 17 | 2 | Known only from a paper, a README or a third-party mention. Existence of public data not confirmed. |
| INACCESSIBLE | 6 | 4 | Was published but the link is now broken (404/500, expired certificate, dead host) or the data was never released. |
| GATED | 11 | 8 | Available only after login, a request form, accepting terms or approval. |
| COMMERCIAL | 4 | 4 | Sold by a vendor; only samples or brochures are public. |
| DISCONTINUED | 0 | 0 | Officially withdrawn by its owner. (No entry has this status.) |
| REJECTED | 26 | - | Checked and found not to be a Telugu OCR resource. |

## Other documents

| File | What it has |
|---|---|
| [DATASET_DETAILS.md](DATASET_DETAILS.md) | A short profile of every row, grouped by category |
| [DISCOVERY_LOG.md](DISCOVERY_LOG.md) | Where we searched, which queries, what came back, what was followed up |
| [DUPLICATE_AND_MIRROR_REPORT.md](DUPLICATE_AND_MIRROR_REPORT.md) | Which rows are copies, subsets or derivatives of others |
| [UNAVAILABLE_AND_GATED_DATASETS.md](UNAVAILABLE_AND_GATED_DATASETS.md) | Gated, broken, commercial and unconfirmed datasets, with how to get access |
| [LICENSING_AND_ACCESS_REPORT.md](LICENSING_AND_ACCESS_REPORT.md) | Licences grouped by what they allow, and licence conflicts found |
| [COVERAGE_REPORT.md](COVERAGE_REPORT.md) | What is well covered, what is missing, and which search channels are still open |
| [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md) | Audit of the OCR entries in the existing `MASTER_CATALOGUE.csv` |

## How it was built

- `scripts/entries_a.py`, `entries_b.py`, `entries_c.py` - the records, written by hand from the evidence.
- `scripts/build_directory.py` - checks IDs and cross-references, writes `telugu_ocr_final.csv` and `evidence/counts.json`.
- `scripts/make_docs.py` - writes these Markdown files from the CSV, so counts always match.
- `scripts/discover.py`, `screen_hf.py`, `fetch_pages.py` - the search sweeps; results in `evidence/discovery/` and `evidence/pages/`.
- `scripts/link_check.py` - checks every link (HEAD or 1 KB request); results in `evidence/link_check.csv`.
- `evidence/ilocr/` - the ILOCR dataset-page probe and the parsed API list.

To rebuild after editing a record:
`python3 ocr/directory/scripts/build_directory.py && python3 ocr/directory/scripts/make_docs.py`
