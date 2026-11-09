---
license: cc0-1.0
language:
- en
- te
pretty_name: Telugu History, public-domain sources
size_categories:
- 100K<n<1M
task_categories:
- text-retrieval
- question-answering
tags:
- history
- india
- andhra-pradesh
- telangana
- telugu
- epigraphy
- ocr
- public-domain
configs:
- config_name: pages
  data_files: data/pages-*.parquet
  default: true
- config_name: passages
  data_files: data/passages-*.parquet
- config_name: sources
  data_files: data/sources.parquet
- config_name: embeddings
  data_files: data/embeddings-*.parquet
---

# Telugu History: public-domain sources

This dataset holds the text of **767 public-domain books, documents and magazine issues** on the history of the Telugu land, the region of unified Andhra Pradesh (Telangana, Coastal Andhra and Rayalaseema). There are **227,618 scanned pages** of text, split into **365,239 search passages** (about 94.5 million words). **27,652 passages are in Telugu script**, 8,001 in Devanagari and 9,109 mixed. Embeddings are included for every passage.

It is the public-domain part of the research library behind **[teluguhistory.org](https://teluguhistory.org)**, a free, bilingual (English and Telugu) history site where every sentence is footnoted to a book and page. Both are part of [Open Telugu](https://opentelugu.org).

## What is in it

| Config | One row per | Main fields |
|---|---|---|
| `pages` (default) | scanned page | `source_key`, `pdf_page` (1-based), `printed_page` (as printed on the page, when detected), `text`, `method` (`textlayer` = the scan's own text layer, `existing-ocr` / `ia-ocr-page` / `tesseract-eng` / `tesseract-tel` / `tesseract-tel+eng` / `tesseract-san` = OCR), `quality` (0–1, an automatic estimate), `script`, `scan_url` (the page on archive.org, where available) |
| `passages` | passage of about 200–350 words | `passage_id`, `source_key`, `pdf_page_first`, `pdf_page_last`, `words`, `script`, `text` |
| `sources` | source (**every** source in the library, about 5,600) | `title`, `author`, `year`, `language`, `licence`, `licence_class`, `licence_checked`, **`text_included`**, `archive_id`, `source_url`, `page_count` |
| `embeddings` | passage | `passage_id`, `embedding`: 1,024 float16 values from [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) (dense, normalised; each passage cut to the model's 512-token window) |

The sources are mostly:
- Madras and Hyderabad district manuals and gazetteers;
- the Imperial Gazetteers;
- *Epigraphia Indica*, *Indian Antiquary* and South Indian inscription volumes;
- archaeology reports;
- Mackenzie-era and colonial histories;
- older Telugu books, grammars and literary texts;
- issues of the Telugu monthly *Bharati* from 1924 to 1930.

The scans come mainly from the [Internet Archive](https://archive.org), including the Digital Library of India collection, and from Wikisource.

## What is not in it, and why

- **Cite-only works:** books still in copyright. The website summarises and cites them but never reproduces them. They appear in `sources` with `text_included = false`.
- **"Public domain in India" works:** Indian government publications of 1936–1965. They are public domain in India but may not be elsewhere, so they are left out of this US-hosted dataset.
- **Unchecked guesses:** sources tagged public domain only by an automatic guess, for example from a date in an inventory. They are left out until checked, and may be added in later versions.

A source's text is included only if it was **published before 1931**, or is an **Indian government work published before 1936**, **and** that status was checked.

## Licence

- **The underlying texts are in the public domain.**
- **This compilation** (selection, page and passage splits, metadata and embeddings) is released under **[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)**. You may use it for any purpose without asking.
- **A request, not a condition:** when you use a passage, **cite the original book and its page** (the `sources` and `scan_url` fields give them), and if useful, this dataset.

## Quality: please read

- **Machine-read text:** most text comes from OCR of old scans. Expect misread letters and numbers, broken words across lines, and running heads and page numbers mixed into the text. Telugu OCR is weaker (roughly one error per line). Check the page image (`scan_url`) before quoting or relying on a detail.
- **Page labels:** `printed_page` is detected automatically and can be missing or wrong. `pdf_page` (with `scan_url`) is exact.
- **Licence data:** the `sources` licence fields come from the project's catalogue; report any mistake you find.

## How it was made

1. The books were collected from open archives into a local library: about 5,500 distinct files, roughly 1.27 million pages, of which this dataset is the checked public-domain part.
2. The text was taken from each PDF's text layer when good, otherwise from existing OCR, or OCRed with Tesseract (English; Telugu alone for Telugu print, which reads better than Telugu + English; Sanskrit).
3. Pages were split into passages of about 200–350 words, and embedded with bge-m3 for meaning search.
4. teluguhistory.org uses the same corpus to check its own footnotes. Each cited sentence is matched against the passages of the cited book, to pinpoint the supporting text and catch wrong page numbers.

## Example

```python
from datasets import load_dataset
pages = load_dataset("opentelugu/telugu-history-public-domain", "pages", split="train")
sources = load_dataset("opentelugu/telugu-history-public-domain", "sources", split="train")
print(pages[0]["text"][:300], pages[0]["scan_url"])
```

## Versions

- **2026-10-18:** still 767 sources; 227,618 pages (was 220,699) and 365,239 passages (was 352,235). Newly read pages of books the website cites and of the Kakatiya collection's public-domain books; embeddings for every passage.
- **2026-10-17:** 767 sources (was 680). Added the *Bharati* issues of 1924–1930, more Telugu books (grammars, literary texts, yakshagana) and newly read pages of cited books. Removed two scans digitised by the Sundarayya Vignana Kendram (*Kridabhiramamu* and *Velugotivari Vamsavali*), whose digitiser asks for permission to reproduce. Embeddings now cover every passage.
- **2026-10-15:** first version, 680 sources.

## Contact

Corrections and questions are welcome: [opentelugu.org/contact](https://opentelugu.org/contact/).
