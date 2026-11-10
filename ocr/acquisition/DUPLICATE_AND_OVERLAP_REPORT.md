# Duplicate and overlap report

How each check was done:
- **Exact copies:** compared image bytes (MD5).
- **Re-crops of the same picture:** compared small image fingerprints (average-hash).
- **Same handwritten page:** compared page IDs, then compared the words on those pages.

Everything was checked on 2026-11-10 against the downloaded or range-read files.

## Rule used for counting

A source counts as new data only if its images are not already in another counted source. Copies, mirrors and re-crops are listed below and counted **once**.

## Duplicate groups

| Group | Members | Verdict | Evidence |
|---|---|---|---|
| **Handwritten page collection (ILOCR 2024)** | IIIT-Indic-HW-UC Telugu, IHWWR-1.0, PLHWTR-1.0 | One collection of camera-captured pages, published three times with different word cuts | All 3,476 IHWWR train pages match PLHWTR train pages, and all 693 IHWWR test pages match PLHWTR test pages. 2,062 IHWWR pages are in HW-UC, and the same sentences appear on them (e.g. page 16918). All 700 PLHWTR test pages are in HW-UC. Count IHWWR (77,625, acquired) plus HW-UC words on other pages (~134,562). |
| **IIIT-INDIC-HW-WORDS** | HW-WORDS (TEL-OCR-002), IHTR-2023 train, IHTR-2022 | Same data | 80,637 of 80,637 identical (path, label) pairs |
| **IndicSTR12-Telugu real** | ILOCR IndicSTR12 (TEL-OCR-003), CVIT `real.zip`, HF darknight054 crops/full, jai23023 verified-twice and signboards, ananya12k zip | Same ~1,200 words | Mirror = 1,183 byte-identical images. ananya12k zip is the same size as CVIT `real.zip` to the byte. jai23023 has 1,183 Telugu rows. |
| **IndicSTR12 vs IIIT-ILST** | IndicSTR12-Telugu, IIIT-ILST Telugu (2017) | Re-crops of the same scene words | 1,151 of 1,200 words have the same label and a near-identical image. The IndicSTR12 paper says its Telugu words came from ILST. |
| **WIRIndic vs MIST** | WIRIndic-Telugu, MIST | Same road video (GoPro) | 95 of 193 MIST Telugu test frames are WIRIndic source frames. MIST is detection-only, so no recognition labels are double counted. |
| **BSTD** | Recognition crops, detection set, HF copy (gated) | One dataset | Crops are cut from the detection scenes |
| **Mozhi-Telugu** | ILOCR `akshara/*.zip`, HF darknight054 mirror | Same data | 9,876 of 9,876 test images and labels identical |
| **Telugu Wikisource** | te.wikisource (TEL-LIT-001), AlbertoChestnut (TEL-OCR-005), harsha wikisource-text-images and line-ocr-bench (TEL-OCR-007), wikimedia/wikisource text dump | One source | The ceiling is 134,241 proofread or validated pages. AlbertoChestnut holds 23,537 of them; harsha's lines are cut from the same pages. Never add these together. |
| **harsha book-line pipeline** | book-line-images, consensus-labelling, telugu-pdf-line-image-text | Same crops | pdf-line keeps only rows with tier 1–4 agreement from the same OCR-consensus run |
| **IndicDLP** | IndicDLP pages (TEL-OCR-015), onath block-OCR eval set | Blocks cut from pages | The eval set is a different task (text), so it is kept separately |
| **Chandamama** | Chandamama archive (TEL-PERIOD-003), Divs0910 paragraph crops | Derived | Same magazine scans |
| **HW-WILD** | IIIT-INDIC-HW-WILD Telugu | Contains 43,194 crops from IIITS-THDB and PHDIndic_11 | Per its own metadata. It is unlabelled, so it isn't counted anyway. |

## Overlap between splits (test leakage)

| Dataset | Problem |
|---|---|
| IIIT-Indic-HW-UC | Splits are made at word level, so one page has words in train, val and test (e.g. page 187978). Writer and page style leak into test. Re-split by page before use. |
| HW-UC vs ICDAR 2024 | All 700 PLHWTR/IHWWR test pages are inside HW-UC. Do not report ICDAR 2024 test scores after training on HW-UC. |
| WIRIndic | No frame is shared, but 42 (train–val) and 48 (train–test) video sequences are shared. Nearby frames show the same signboards. |
| Mozhi | 0 train/test overlap; 2 images appear in both train and val. |

## Not new compared with the existing catalogue

- **Already catalogued, now downloaded:**
  - Mozhi (TEL-OCR-001): 100,024 pairs
  - IndicSTR12 (TEL-OCR-003): 1,200 pairs
- **Already catalogued, only sampled:**
  - HW-WORDS (TEL-OCR-002)
  - Wikisource (TEL-LIT-001)
  - AlbertoChestnut (TEL-OCR-005)

## Catalogue figures that look wrong

These are reported here, not changed in the catalogue:

| Record | Problem |
|---|---|
| TEL-OCR-005 | "458,964 rows" counts text lines. The real figure is 23,537 image–text page pairs. |
| TEL-OCR-002 | 88,534 train images, but only 80,637 have labels. |
| TEL-OCR-014 | The Zenodo record holds a vendor sales PDF, not data. |
