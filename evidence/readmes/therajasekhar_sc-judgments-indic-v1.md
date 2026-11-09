---
pretty_name: SCI Judgments Indic v1 (sample)
license: cc-by-4.0
language:
- en
- hi
- te
task_categories:
- translation
- summarization
- text-retrieval
tags:
- supreme-court-india
- legal
- hindi
- telugu
- parallel-corpus
multilinguality: multilingual
size_categories:
- 10K<n<100K
source_datasets: []
configs:
- config_name: en
  data_files: data/en/*.parquet
- config_name: te
  data_files: data/te/*.parquet
- config_name: hi
  data_files: data/hi/*.parquet
- config_name: parallel-en-te
  data_files: data/parallel-en-te/*.parquet
- config_name: parallel-en-hi
  data_files: data/parallel-en-hi/*.parquet
---

# SCI Judgments Indic v1 — Dataset Card

> Status: full-parse v2 live 2026-09-11 — deep-cleaned text + quality flags (`garbled, script_ratio, dropped_lines, body_start`).
> Counts: en 38,356 (0 garbled) · te 2,543 (1,584 garbled, old scans) · hi 17,583 (11,026 garbled, old scans) · parallel-en-te 2,491 · parallel-en-hi 17,434.
> Filter `garbled==False` for clean text. Scanned pre-1970 regional PDFs need OCR (flagged, kept for provenance).

## Dataset Description

Supreme Court of India judgments with official Indic translations for MT / legal-NLP:

- `en` — English authoritative text (PDF-extracted, `data/parquet/en/`)
- `parallel-en-te`, `parallel-en-hi` — EN↔Telugu / EN↔Hindi document-aligned pairs from official eSCR/SUVAS translations

## Sources

- AWS bulk (primary): https://registry.opendata.aws/indian-supreme-court-judgments (`s3://indian-supreme-court-judgments/`), CC-BY-4.0 packaging
- eSCR: https://judgments.ecourts.gov.in/pdfsearch/?p=pdf_search/index&escr_flag=Y (translations)
- 2023 coverage measured: total 856, TEL 318 (37.1%), HIN 796 (93.0%)

## License and Attribution

- Underlying judgments public-domain per Copyright Act Sec 52(1)(q)(iv).
- Packaging CC-BY-4.0. Attribution: SCI / eSCR / SUVAS + AWS dataset. Cite access date 2026-09-11.
- Translations carry eSCR disclaimer ("general information, no legal effect").

## Intended Uses / Out-of-Scope

- Intended: EN↔TE/HI legal MT, retrieval, summarization.
- Out-of-scope: legal advice; no PII guarantee — judgments contain real litigant names.

## Preprocessing

`fetch (S3, --limit/--year) → extract (pypdf + pdfplumber fallback, <500 chars -> failed.jsonl) → build → build-parallel (base-stem join, ratio 0.5-2.0) → push`. See `pipeline.py`, `SOURCES.md`, `data/splits.json`.
