# Licensing status

Checked on 2026-11-10. A licence counts as **stated** only if it is written on the dataset's own page, card or repository. A group-wide policy or a guess does not count.

## Correction to earlier reports

The phase-1 files (NEW_OCR_DATASETS.csv, VERIFIED_DOWNLOADS.csv, NEXT_DATA_COLLECTION_PLAN.md) said "CC BY 4.0 (ILOCR policy)" for these sets:
- WIRIndic
- IHWWR-1.0
- PLHWTR-1.0
- IIIT-Synthetic-M, -R and -IndicSTR

**That was too strong.** I re-read every dataset page and found:
- The IIIT-Synthetic pages have **no licence section**. I checked the Telugu, Malayalam and Urdu pages of all three families.
- The ICDAR 2024 HWD page (IHWWR/PLHWTR) and the ICPR 2024 WIRIndic page state **no licence** either. The "freely available for academic and research purposes" line on the WIRIndic page refers to the MLT dataset, not WIRIndic.
- The ILOCR "License" document is a policy text: "Bhashini *plans* to use the CC BY 4.0 license for its datasets". It is not a licence grant for a specific dataset.

So "verified CC BY 4.0" is **not** correct for the 3.6 million synthetic images. Their licence is not stated.

## Status of every source in the unified corpus

| Source | Pairs kept | Licence | Where it is stated | Commercial use | Can we redistribute? |
|---|---:|---|---|---|---|
| IIIT-INDIC-HW-WORDS-Telugu | 118,498 | CC BY 4.0 | Dataset page: "This dataset is under the license CC BY 4.0" | Allowed with attribution | Yes |
| Mozhi-Telugu (printed words) | 99,081 | CC BY 4.0 | Same sentence on every other-language Mozhi page (Assamese, Gujarati, Urdu…). The Telugu page crashes, so this is inferred from the identical template. | Allowed with attribution | Yes (attribution) |
| BSTD Telugu crops | 2,755 | Apache-2.0 | GitHub repository licence. No separate data licence. | Likely allowed. Confirm the data terms with IIT Jodhpur. | Yes (repo licence) |
| Sarvam Indic OCR Bench (Telugu) | 300 | Apache-2.0 | Hugging Face licence tag. Source pages carry publisher watermarks. | Tag allows it | Yes. Use for evaluation only. |
| IndicDLP eval sample (Telugu) | 10 | CC BY 4.0 | Hugging Face licence tag | Allowed | Yes |
| IndicSTR12-Telugu | 1,200 | CC BY 4.0 for the **annotations** | Dataset page. The images were crawled from Google Images, so the pictures belong to third parties. | Risky (image rights) | No (we don't share the images) |
| IIIT-Indic-HW-UC Telugu | 280,226 | **Not stated** | Project page has download links but no licence | Unknown | No |
| IHWWR-1.0 Telugu | 27,448 | **Not stated** | Competition page | Unknown | No |
| WIRIndic-Telugu | 20,000 | **Not stated** | Competition page | Unknown | No |
| IIIT-Synthetic-M-Telugu | 138,553 | **Not stated** | The page says "can be used only for pre-training purposes" | Unknown | No |
| IIIT-Synthetic-R-Telugu | 612,500 | **Not stated** | — | Unknown | No |
| IIIT-Synthetic-IndicSTR-Telugu | 2,999,658 | **Not stated** | — | Unknown | No |
| Telugu Wikisource pages | 0 pairs (text only) | Text CC BY-SA 4.0. Scans checked per file: 1,146 of 1,231 free (954 public domain, 172 CC BY-SA, 18 CC0, 1 CC BY 4.0, 1 CC BY-SA 3.0 de). | Commons/Wikisource file pages, via the API | Allowed (share-alike) for free scans | Yes, for free scans |

## Totals by licence status (real data only, after cleaning)

| Status | Pairs | Sources |
|---|---:|---|
| Open licence stated (CC BY / Apache), redistributable | **220,644** | HW-WORDS, Mozhi, BSTD, Sarvam, IndicDLP sample |
| Annotations open, images third-party | 1,200 | IndicSTR12 |
| No licence stated: research use only until confirmed | **327,674** | HW-UC, IHWWR, WIRIndic |
| **All real** | **549,518** | |

Synthetic: 3,750,711 pairs, all with no licence stated.

## What was not done, on purpose

- **Nothing restricted was downloaded.** All sources above were offered as open downloads with no login.
- **Excluded for licence reasons:**
  - Chandamama crops (Divs0910): no licence; the magazine is copyrighted
  - harsha-desaraju book/news sets: their labels are machine OCR, and their source books are modern
  - IIITS-THDB and Mendeley Telugu fractions: non-commercial only
  - IIIT-ILST: no redistribution allowed
  - Wikisource scans with no licence on their file page (85 files, 6,689 pages)
- **Wikimedia identification:** Wikimedia's robot policy blocked our page-image requests, because the policy asks automated clients to give contact details. I did **not** put your email or GitHub identity into requests without your OK.

## Who to ask

| Licence question | Contact | Pairs it would unlock |
|---|---|---:|
| IIIT-Indic-HW-UC, IHWWR/PLHWTR, WIRIndic | CVIT / ILOCR, IIIT Hyderabad (Prof. C V Jawahar, Dr Ajoy Mondal) | 327,674 real |
| IIIT-Synthetic-M/-R/-IndicSTR | Same group | 3,750,711 synthetic |
| BSTD data terms | Bhashini-IITJ (IIT Jodhpur) | 2,755 (already Apache via repo) |

A single email to CVIT asking them to confirm CC BY 4.0 for these sets (as on their HW-WORDS and Mozhi pages) would settle 4,078,385 of the 4,300,229 pairs (95%).
