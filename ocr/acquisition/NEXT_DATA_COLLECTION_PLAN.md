# Telugu OCR data: what we have and what to collect next

> **Superseded (phase 2):** this was the plan at the end of phase 1. Current counts are in DATASET_STATISTICS.md, licence status in LICENSING_STATUS.md (some licences below were corrected), and next steps in TRAINING_READINESS_REPORT.md.

Status on 2026-11-10. "Pairs" means an image with its correct Telugu text. Images without text are not counted. Each underlying collection is counted once (see DUPLICATE_AND_OVERLAP_REPORT.md).

## 1. Newly acquired: on disk now, in `ocr/acquisition/data/`

**New sources (not in the existing catalogue):**

| Type | Dataset | Pairs | Licence |
|---|---|---:|---|
| Handwritten (real) | IHWWR-1.0 Telugu train | 77,625 (63,341 Telugu words) | Not stated (see LICENSING_STATUS.md) |
| Scene text (real) | WIRIndic-Telugu train+val | 20,000 | Not stated (see LICENSING_STATUS.md) |
| Scene text (real) | BSTD Telugu | 2,760 | Apache-2.0 |
| Printed blocks (real, eval) | Sarvam Indic OCR Bench Telugu | 300 | Apache-2.0 |
| Printed blocks (real, eval) | IndicDLP eval sample Telugu | 10 | CC BY 4.0 |
| **Real, new: total** | | **100,695** | |
| Synthetic printed words | IIIT-Synthetic-M-Telugu | 138,585 | Not stated (see LICENSING_STATUS.md) |

**Already catalogued, but downloaded for the first time:**

| Type | Dataset | Pairs |
|---|---|---:|
| Printed words (real) | Mozhi-Telugu (TEL-OCR-001), verified against the official release | 100,024 |
| Scene text (real) | IndicSTR12-Telugu (TEL-OCR-003) | 1,200 |

**Downloaded but not counted:**
- 5,000 unlabelled WIRIndic test images
- the Mozhi official test zip (verification copy)
- the IndicSTR12 mirrors
- 6 Wikisource probe pages

**In total:** 201,919 real labelled Telugu OCR pairs on disk (100,695 from new sources + 101,224 previously catalogued), plus 138,585 synthetic.

Before training:
- remove the 14,284 punctuation-only IHWWR labels;
- fix the BSTD `౦` → `ం` labels;
- keep Sarvam and IndicDLP as test sets only.

## 2. Identified and checked, not yet acquired

| Priority | Dataset | Type | Pairs available | Why not yet | Action |
|---|---|---|---:|---|---|
| 1 | IIIT-Indic-HW-UC Telugu | Handwritten, real | 200,000 (~134,562 beyond IHWWR) | Licence not stated; 4.8 GB | Email CVIT (Ajoy Mondal / C V Jawahar) to confirm CC BY 4.0. Then download, re-split by page, and drop ICDAR 2024 test pages. |
| 2 | Telugu Wikisource validated/proofread pages | Printed, real | 134,241 pages (page text) | Needs line alignment | Build our own page→line aligner (Mozhi or Tesseract line boxes + text alignment), starting with the 54,605 validated pages. Skip books whose scans are hosted locally under unclear licences. |
| 3 | IIIT-INDIC-HW-WORDS-Telugu (TEL-OCR-002) | Handwritten, real | 118,516 | Time (3.8 GB) | Download. Open, CC BY 4.0. |
| 4 | PLHWTR-1.0 Telugu train | Handwritten pages | 3,496 pages | Same handwriting as IHWWR | Download only if page/line-level HTR is needed |
| 5 | IIIT-Synthetic-R-Telugu | Synthetic | 612,500 | Time (2.05 GB) | Download; strip the leading space in labels |
| 6 | IIIT-Synthetic-IndicSTR-Telugu | Synthetic scene | 2,999,658 | 6.3 GB; many unreadable images | Download the val split first; filter by quality |
| 7 | IEEE DataPort Telugu handwritten characters (2 sets) | Character | ~82,000 characters (913 sheets) + unknown | IEEE login | Create a free account and download (CC BY 4.0) |
| 8 | Synthdog-Multilingual Telugu | Synthetic pages | 10,000 (per card) | Inside an 11.3 GB tar | Stream-extract the `te` files |
| 9 | NayanaOCRBench Natural Telugu | Printed pages, real | 461 | CC BY-NC | Use only as an extra evaluation set |
| 10 | IndicDLP Telugu (TEL-OCR-015) | Layout | ~8,600 pages, boxes only | Gated | Only if layout detection is in scope |

**Rough ceiling if items 1–3 and 5 are completed:** about 100,695 + 134,562 + 118,516 ≈ **354,000 new real labelled pairs**, plus Wikisource lines, plus ~750,000 synthetic. This is on top of the 101,224 already-catalogued pairs now on disk.

## 3. Requests to send

1. **CVIT / ILOCR** (IIIT Hyderabad):
   - written licence for IIIT-Indic-HW-UC;
   - the ICDAR 2025 IHDR Telugu files (links are 404);
   - whether IHWWR/WIRIndic test labels can be released.
2. **Oikantik Nath** (IIT Madras): the full 582-block Telugu IndicDLP OCR eval set.
3. **Prof. C. Bhagvati** (Univ. of Hyderabad): UHTelPCC images and licence (page is 404).
4. **Divs0910** (HF) and **harsha-desaraju** (HF): source and rights for the Chandamama crops and the book-line sets. Do not use these until the rights are clear.

## 4. Gaps that no open source fills

- **Real printed lines with human-checked text, outside Wikisource:** none found. Wikisource alignment (item 2) is the only large legal route.
- **Telugu palm-leaf or historical manuscripts with transcriptions:** none public.
  - Options: partner with GOML / Tamil Virtual Academy for transcriptions of TEL-MSS-001 scans, or run a small in-house transcription effort.
- **Newspaper and government printed pages with text:** none open.
  - Gazette and assembly PDFs that have a text layer could be rendered to page/text pairs. Check each department's licence first.

## 5. How to reproduce

```bash
# re-check everything on disk, rebuild VERIFIED_DOWNLOADS.csv and samples/
python -I ocr/acquisition/scripts/verify_downloads.py      # needs pillow + pyarrow

# list or sample a remote zip without downloading it
python -I ocr/acquisition/scripts/remotezip.py <zip-url> <out-dir> --n 10
# fetch only matching files from a remote zip
python -I ocr/acquisition/scripts/remotezip_fetch.py <zip-url> <out-dir> '<regex>'
```

The download URLs and SHA-256 checksums are in `VERIFIED_DOWNLOADS.csv`.
