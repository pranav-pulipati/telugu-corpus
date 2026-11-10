# Dataset statistics: unified Telugu OCR corpus

These are exact counts after cleaning, as of 2026-11-10. The source data is `data/corpus_work/assign/*.parquet` and `scripts/_corpus_stats.json`.

Each pair is one image plus its verified text. Images without text are never counted.

## Totals

| Collection | Train | Val | Test | Total | On disk |
|---|---:|---:|---:|---:|---:|
| Handwritten (real) | 349,333 | 36,756 | 40,083 | **426,172** | 8.1 GB |
| Printed (real) | 87,368 | 6,471 | 5,552 | **99,391** | 0.4 GB |
| Scene text (real) | 17,490 | 3,013 | 3,452 | **23,955** | 0.17 GB |
| **Real, all** | **454,191** | **46,240** | **49,087** | **549,518** | 8.7 GB |
| Synthetic | 2,567,303 | 560,908 | 622,500 | **3,750,711** | 6.2 GB |
| **Everything** | 3,021,494 | 607,148 | 671,587 | **4,300,229** | 14.9 GB in 876 shards |

## How this compares with phase 1

| | Real pairs on disk | Synthetic pairs on disk |
|---|---:|---:|
| End of phase 1 (raw, before cleaning) | 201,919 | 138,585 |
| Now (cleaned and deduplicated) | **549,518** | **3,750,711** |

The real data grew mostly from:
- IIIT-Indic-HW-UC: +280,226 handwritten
- IIIT-INDIC-HW-WORDS: +118,498 handwritten

## Per source

| Source | Collection | Unit | Kept | Train / Val / Test | Groups (train/val/test) | Distinct labels | Median label length (chars) | Median image (w×h px) |
|---|---|---|---:|---|---|---:|---:|---|
| HW-UC Telugu | handwritten | word | 280,226 | 246,759 / 14,031 / 19,436 | 3,695 / 302 / 700 pages-or-blocks | 96,843 | 6 | 402×170 |
| HW-WORDS Telugu | handwritten | word | 118,498 | 80,625 / 19,978 / 17,895 | 3,763 / 847 / 758 forms | 12,944 | 9 | 1201×293 |
| IHWWR-1.0 Telugu | handwritten | word | 27,448 | 21,949 / 2,747 / 2,752 | 1,115 / 151 / 144 pages | 9,920 | 6 | 447×186 |
| Mozhi Telugu | printed | word | 99,081 | 87,368 / 6,471 / 5,242 | 23 / 3 / 2 books | 54,818 | 6 | 141×48 |
| Sarvam bench Telugu | printed | text block | 300 | – / – / 300 | eval only | 300 | 184 | 804×265 |
| IndicDLP eval sample | printed | text block | 10 | – / – / 10 | eval only (one magazine issue) | 10 | 27 | 551×74 |
| WIRIndic Telugu | scene text | word | 20,000 | 14,555 / 2,656 / 2,789 | 77 / 13 / 10 road videos | 4,580 | 6 | 57×34 |
| BSTD Telugu | scene text | word | 2,755 | 1,976 / 237 / 542 | 453 / 53 / 141 scenes | 1,932 | 7 | 122×54 |
| IndicSTR12 Telugu | scene text | word | 1,200 | 959 / 120 / 121 | 229 / 37 / 32 scenes | 830 | 6 | 120×54 |
| Synthetic-M | synthetic | word | 138,553 | 138,553 / – / – | – | 68,898 | 6 | 56×32 |
| Synthetic-R | synthetic | word (often 2 joined) | 612,500 | 428,750 / 61,250 / 122,500 | – | 492,840 | 10 | 97×32 |
| Synthetic-IndicSTR | synthetic | word | 2,999,658 | 2,000,000 / 499,658 / 500,000 | – | 499,891 | 9 | 86×32 |

## Vocabulary overlap between test and train

This is the share of distinct test labels that also appear in train. A high value means the test set mostly checks words the model has already seen. It is not image leakage.

| Source | Test words seen in train |
|---|---:|
| HW-WORDS | 88.3% (the collection forms reuse one word list) |
| WIRIndic | 67.3% |
| HW-UC | 57.6% |
| IHWWR | 51.6% |
| Mozhi | 41.3% |
| IndicSTR12 | 33.6% |
| BSTD | 27.5% |
| Synthetic-R | 27.3% |
| Synthetic-IndicSTR | 99.8% (its official test set is almost all train words) |

## Granularity

- **Word level:** 4,299,919 pairs (all sources except the two block sets).
- **Text block level:** 310 pairs (Sarvam + IndicDLP sample). Evaluation only.
- **Page level:** 0 pairs. The 127,326 human-proofread Telugu Wikisource pages on free-licence scans have their text and licence downloaded, but not their page images (see TRAINING_READINESS_REPORT.md).

## Label types

| Label type | Pairs | Sources |
|---|---:|---|
| Human transcription | 549,218 | HW-UC, HW-WORDS, IHWWR, Mozhi, WIRIndic, BSTD, IndicSTR12, IndicDLP sample |
| Human, double-reviewed | 300 | Sarvam bench |
| Rendered text (exact by construction) | 3,750,711 | Synthetic-M, -R, -IndicSTR |
| **Machine-generated / OCR-derived** | **0** | Deliberately excluded (see LICENSING_STATUS.md) |
