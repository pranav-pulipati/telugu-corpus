# Telugu Corpus — Source Catalogue

This is a checked list of **200 places on the internet where Telugu data is publicly available**: books, poems,
newspapers, magazines, palm-leaf manuscripts, dictionaries, government documents, speech recordings, scanned images
and labelled datasets.

The list was audited on 2026-11-09:
- 4 entries were rejected and moved to an archive.
- 53 entries were corrected.
- Every Hugging Face dataset was checked for real Telugu text, not just a "Telugu" tag.

The audit results are in the `audit/` folder; start with `audit/AUDIT_REPORT.md`.

**Telugu OCR datasets:** a separate, more detailed directory of every Telugu OCR dataset found (181 rows, 92 distinct
datasets) is in [`telugu_ocr_final.csv`](telugu_ocr_final.csv). How to read it, the counts and the reports are in
[`ocr/directory/README.md`](ocr/directory/README.md).

For each source, the list records:
- the link
- what is inside
- the file format
- the labels and annotations
- how much Telugu data there is
- how to download it
- whether it can be used commercially

## Which file to open

**`MASTER_CATALOGUE.xlsx`** has everything in one file. It has these tabs:

| Tab | What it has |
|---|---|
| Master Catalogue | All 200 active sources, one row each |
| Summary | Counts by category, status and quality |
| Taxonomy | The 16 categories |
| Field Dictionary | What each column means |
| Verification Log | The checks done for each fact, with links |
| HF Telugu Inventory | All 1,563 Hugging Face datasets tagged Telugu, with whether Telugu text was actually found |
| Rejected (archive) | The 4 rejected entries and why they were rejected |

The same data is also stored as CSV files:
- `MASTER_CATALOGUE.csv` — all active sources
- `catalogues/` — one file per category
- `VERIFICATION_LOG.csv` — the checks and evidence links

## Most useful columns

| Column | Meaning |
|---|---|
| collection_name, collection_url | Name of the source and its link |
| description | What is inside |
| primary_category | Type of data (literature, newspapers, manuscripts, speech, ...) |
| formats, modality | File types (PDF, text, images, audio) |
| annotations | Labels that come with the data |
| size_telugu | How much Telugu data there is |
| acquisition_method | How to download it |
| license, commercial_use | Whether you are allowed to use it |
| verification_status | How much we checked: Verified / Partially Verified / Unverified / Inaccessible |
| quality_rating | How trustworthy the entry is: High / Medium / Low |
| telugu_content_check | For Hugging Face datasets: whether real Telugu text was found in the data |
| count_in_totals | "No" means this source is a copy or part of another one, so don't count its data twice |

## Folders you don't need to open

- `audit/` — the audit report, change log, and lists of invalid, duplicate and licence-uncertain sources
- `data/` — the source files the spreadsheet is generated from (`data/rejected/` holds the rejected entries)
- `scripts/` — the programs that apply the audit, build the spreadsheet and run the checks
- `evidence/` — saved copies of what websites returned, kept as proof

To rebuild everything after a change, run these in order:
`scripts/apply_audit.py`, `scripts/build.py`, `scripts/validate.py`, `scripts/audit_outputs.py`.
