# Current-state audit

Before the directory was built, the OCR-related entries already in the repo were re-checked. Date: 2026-11-11.

## What was already there

- `MASTER_CATALOGUE.csv` (200 sources) had **16 `TEL-OCR` records**: 15 datasets and 1 tool (Tesseract). OCR-relevant material also sat in manuscript, digital-library, periodical and text-corpus records.
- `ocr/acquisition/` (earlier phases) had downloaded and cleaned 10 open sets into a unified corpus (~15 GB, kept off GitHub).

## Corrections to the existing catalogue

| Record | What the catalogue says | What we found | Directory row |
|---|---|---|---|
| TEL-OCR-002 | Partially Verified; ~126K images | Verified: 126,413 images, but only 118,516 have a label line; 7,897 train images have no label. CC BY 4.0 confirmed. The catalogue merges two releases: IIIT-HW-Telugu (2018) and HW-WORDS v0.5. | TOCR-001, TOCR-002 |
| TEL-OCR-003 | Licence unknown; ">1,000 real word images" | ILOCR page states CC BY 4.0 for annotations. Telugu has 1,183 word crops (933/117/133) + 298 scene images, re-cropped from IIIT-ILST. | TOCR-071, TOCR-070 |
| TEL-OCR-005 | 458,964 rows | 458,964 is the HF table's row count. The data is 23,537 page image-text pairs in 219 book folders (the README says ~25,565 / 221). It is a subset of Telugu Wikisource. | TOCR-050 |
| TEL-OCR-010 | Partially Verified, MIT | Gated (manual approval). Licence tag MIT not checkable without access. | TOCR-062 |
| TEL-OCR-011 | Inaccessible (DSpace) | DSpace still HTTP 503. The same authors published the data on IEEE DataPort (Negi & Rao; ~82K characters, 937 classes; login needed). Recorded as one gated dataset. | TOCR-022 |
| TEL-OCR-012 | Unverified; size unknown | The IEEE "Varnamala" listing is a single image of 52 characters. It is not a training dataset. | TOCR-029 |
| TEL-OCR-014 | 20,000 image-text pairs, CC BY 4.0 | The Zenodo deposit is a 419 KB brochure from GTS.ai. The data is the Kaggle amancapy upload, which says CC BY-NC 4.0, so the catalogue's licence is wrong. | TOCR-096, TOCR-095 |
| TEL-OCR-015 | IndicDLP, CC BY 4.0 | It is layout-only (no transcriptions). Telugu is ~7.2% (~8,600 pages). HF copy is gated. | TOCR-109 |
| TEL-OCR-013 | Indiscapes | Telugu share not confirmed. Layout-only. | TOCR-111 |

These corrections are recorded in the directory only. `MASTER_CATALOGUE.csv` was **not changed**, so the original
audit trail stays as it is. Applying them to the master catalogue is a separate step.

## Mapping

All 16 `TEL-OCR` records map to directory rows. **78** distinct datasets in the directory have no catalogue record.

| Catalogue record | Directory row | Name | Status now | Category |
|---|---|---|---|---|
| TEL-DIAL-004 | TOCR-148 | Telugu Unicode fonts (Noto, Pothana2000, Vemana, Google Fon... | VERIFIED | Related resource (not a dataset) |
| TEL-DLIB-001 | TOCR-122 | Internet Archive - Telugu-language items | VERIFIED | Scanned archive (image-only) |
| TEL-DLIB-002 | TOCR-123 | Digital Library of India (DLI) - Telugu books | VERIFIED | Scanned archive (image-only) |
| TEL-LIT-001 | TOCR-049 | Telugu Wikisource - proofread and validated page scans | VERIFIED | OCR image-text: printed |
| TEL-LIT-001 | TOCR-135 | Telugu Wikisource text dump (wikimedia/wikisource 20231101.... | VERIFIED | Text-only corpus (OCR language modellin... |
| TEL-MSS-001 | TOCR-117 | Telugu Palm Leaf Manuscripts (GOML Chennai scans on Interne... | VERIFIED | Scanned archive (image-only) |
| TEL-OCR-001 | TOCR-041 | Mozhi-Telugu (printed word images) | VERIFIED | OCR image-text: printed |
| TEL-OCR-002 | TOCR-002 | IIIT-INDIC-HW-WORDS-Telugu (ILOCR v0.5) | VERIFIED | OCR image-text: handwritten |
| TEL-OCR-002 (as part of) | TOCR-001 | IIIT-HW-Telugu | VERIFIED | OCR image-text: handwritten |
| TEL-OCR-003 | TOCR-071 | IndicSTR12 real (CVIT release, all 12 languages) | VERIFIED | OCR image-text: scene text |
| TEL-OCR-004 | TOCR-021 | HPL Isolated Handwritten Telugu Character Dataset (HP Labs ... | PARTIALLY VERIFIED | Character / glyph classification |
| TEL-OCR-005 | TOCR-050 | AlbertoChestnut/telugu-ocr | VERIFIED | OCR image-text: printed |
| TEL-OCR-006 | TOCR-092 | Chitralekha - synthetic Telugu word images | VERIFIED | OCR image-text: synthetic |
| TEL-OCR-007 | TOCR-051 | harsha-desaraju/telugu-wikisource-text-images | VERIFIED | OCR image-text: printed |
| TEL-OCR-007 | TOCR-052 | harsha-desaraju/telugu-line-ocr-bench | VERIFIED | OCR image-text: printed |
| TEL-OCR-007 | TOCR-054 | harsha-desaraju/Telugu-book-text-images | VERIFIED | Image-only (no transcription) |
| TEL-OCR-007 | TOCR-093 | harsha-desaraju/telugu-synthetic-line-images | VERIFIED | OCR image-text: synthetic |
| TEL-OCR-008 | TOCR-097 | NayanaOCR Corpus 2025 - Telugu | VERIFIED | OCR image-text: synthetic |
| TEL-OCR-009 | TOCR-147 | Tesseract Telugu models and langdata (tel.traineddata) | VERIFIED | Related resource (not a dataset) |
| TEL-OCR-010 | TOCR-062 | OCR-Bench1000-Telugu | GATED | OCR image-text: printed |
| TEL-OCR-011 | TOCR-022 | Offline Handwritten Telugu Characters (Negi & M Rao, Univer... | GATED | Character / glyph classification |
| TEL-OCR-012 | TOCR-029 | Handwritten Telugu Alphabet Dataset: Vowels and Consonants ... | VERIFIED | Character / glyph classification |
| TEL-OCR-013 | TOCR-111 | Indiscapes / Indiscapes2 (historical Indic manuscript layou... | PARTIALLY VERIFIED | Layout / detection (no transcription) |
| TEL-OCR-014 | TOCR-096 | GTS.ai "Telugu Document Image Dataset" (and Zenodo brochure... | VERIFIED | OCR image-text: synthetic |
| TEL-OCR-015 | TOCR-109 | IndicDLP - Telugu pages (document layout parsing) | GATED | Layout / detection (no transcription) |
| TEL-OCR-016 | TOCR-113 | MDIW-13 - Multi-lingual Document Image database for script ... | VERIFIED | Script identification |
| TEL-PERIOD-001 | TOCR-124 | Telugu newspapers e-paper archive (newspapers-telugu, archi... | VERIFIED | Scanned archive (image-only) |
| TEL-PERIOD-002 | TOCR-125 | Historic Telugu magazines on archive.org (Bharathi, Andhra ... | VERIFIED | Scanned archive (image-only) |
| TEL-PERIOD-003 | TOCR-129 | Chandamama (Telugu edition) 1947-2012 scans | VERIFIED | Scanned archive (image-only) |
| TEL-PERIOD-005 | TOCR-126 | AP Press Academy digitised old newspapers (pre-1977) | PARTIALLY VERIFIED | Scanned archive (image-only) |
| TEL-SPEECH-018 | TOCR-145 | Bhashini ULCA - dataset/model portal | PARTIALLY VERIFIED | Related resource (not a dataset) |
| TEL-SPEECH-019 | TOCR-146 | AIKosh (IndiaAI) dataset platform | PARTIALLY VERIFIED | Related resource (not a dataset) |
| TEL-TXT-001 | TOCR-139 | Telugu Wikipedia dumps (tewiki) | VERIFIED | Text-only corpus (OCR language modellin... |
| TEL-TXT-004 | TOCR-137 | IndicCorp v2 - Telugu | VERIFIED | Text-only corpus (OCR language modellin... |
| TEL-TXT-005 | TOCR-136 | Sangraha - Telugu | VERIFIED | Text-only corpus (OCR language modellin... |
| TEL-TXT-006 | TOCR-138 | CulturaX - Telugu | GATED | Text-only corpus (OCR language modellin... |
