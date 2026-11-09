# Telugu Corpus — Source Catalogue

This is a list of **204 places on the internet where Telugu data is publicly available**: books, poems, newspapers,
magazines, palm-leaf manuscripts, dictionaries, government documents, speech recordings, scanned images and labelled
datasets.

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
| Master Catalogue | All 204 sources, one row each |
| Summary | Counts by category and status |
| Taxonomy | The 16 categories |
| Field Dictionary | What each column means |
| Verification Log | The links we used to check each fact |
| HF Telugu Inventory | All 1,563 Telugu datasets found on Hugging Face |

The same data is also stored as CSV files:
- `MASTER_CATALOGUE.csv` — all sources
- `catalogues/` — one file per category: `literature_books.csv`, `newspapers_periodicals.csv`,
  `manuscripts_inscriptions.csv`, `speech.csv`, `ocr_handwriting.csv`, and so on
- `VERIFICATION_LOG.csv` — evidence links for each fact

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
| verification_status | Whether we confirmed the details ourselves (Verified / Partially Verified / Unverified / Inaccessible) |

## Folders you don't need to open

- `data/` — the source files the spreadsheet is generated from
- `scripts/` — the programs that build the spreadsheet and check the links
- `evidence/` — saved copies of what websites returned, kept as proof

To regenerate the spreadsheet after editing anything in `data/records/`, run `python scripts/build.py`.
