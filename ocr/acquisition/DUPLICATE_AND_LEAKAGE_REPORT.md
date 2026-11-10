# Duplicate and leakage report: unified corpus

Checked on 2026-11-10. This complements the phase-1 `DUPLICATE_AND_OVERLAP_REPORT.md`, which covered source-level duplicates.

## Rule

Splits are made by **original document unit**, never by individual crop. A unit is a handwritten page, a book, a scene photo or a road video. Every crop from one unit goes into the same split.

This is enforced twice:
- `build_corpus.py assign` refuses to write if any `(source, group)` falls in two splits;
- `validate_unified.py` re-checks the exported shards.

**Result: 0 groups in more than one split**, across all 4,300,229 pairs.

## The official splits leaked, so most were replaced

| Source | Official split problem (measured) | What we did | Items that changed split |
|---|---|---|---:|
| IIIT-Indic-HW-UC | Split by individual word: **all 4,597 identifiable pages** have words in more than one of train/val/test | Re-split by page (or by ID block where pages are unknown). ICDAR 2024 test pages forced into test. | 68,923 |
| Mozhi | All **28 of 28 books** and 1,362 of 1,387 test pages also occur in train | Re-split by **book**: train 23, val 3, test 2 | 27,985 |
| IndicSTR12 | **154** scene photos have crops in both train and test | Re-split by scene: 229 / 37 / 32 | 434 |
| WIRIndic | Train and val share **42** road-video sequences; official test has no labels | Re-split labelled data by video sequence: 77 / 13 / 10 | 6,514 |
| IHWWR-1.0 | Only a training set has labels | Split by page: 1,115 / 151 / 144 pages | 5,499 |
| BSTD | **None**: official train/test share 0 of 647 scenes | Kept official test; val = held-out train scenes | 237 (train → val) |
| HW-WORDS | **None**: writer folders (6/2/3) and forms are disjoint | Kept official split | 0 |
| Synthetic-M/-R/-IndicSTR | No source documents | Kept official split | 0 |
| Sarvam, IndicDLP sample | Evaluation sets | Test only | 0 |

## Protecting an external benchmark (ICDAR 2024 handwriting)

- The ICDAR 2024 HWD Telugu test set covers 700 page IDs: 693 from the IHWWR word test zip and 700 from the PLHWTR page test zip. The IDs were taken from the zip listings and saved in `corpus_work/benchmark_test_pages.json`.
- All 700 of these pages are inside IIIT-Indic-HW-UC, with labels.
- **All 19,436 HW-UC words on those pages are in our test split; 0 are in train or val.** So a model trained on our train split can still be scored fairly on ICDAR 2024 Telugu.
- IHWWR words on pages that HW-UC also holds (35,809) were removed, so the same handwriting never appears twice.

## Duplicate checks on the final corpus

| Check | Scope | Result |
|---|---|---|
| Identical pixels, same collection | All 4,385,420 inputs | 217 dropped (185 real, 32 synthetic). 0 groups had conflicting labels. |
| Identical pixels across splits | Final corpus | **0** |
| Same image fingerprint and same label across sources (e.g. IndicSTR12 vs WIRIndic vs BSTD, Sarvam vs Mozhi) | Real collections | **0** |
| Same image fingerprint and same label across splits within a source | Final corpus | Synthetic-R **1,270**, Mozhi 8 (one-letter words like `ఆ`), HW-UC 1, all others 0 |
| Same handwritten page in two sources | IHWWR vs HW-UC | 35,809 IHWWR words removed |

## Known duplicates outside the corpus (deliberately not included)

| Not included | Because it duplicates |
|---|---|
| IHTR-2023 / IHTR-2022 Telugu | HW-WORDS (80,637 of 80,637 identical) |
| PLHWTR-1.0 page images | The same pages as IHWWR and HW-UC |
| IIIT-ILST Telugu | IndicSTR12 (1,151 of 1,200 re-crops); also no-redistribution |
| HF mirrors (darknight054, jai23023, ananya12k) | Official ILOCR/CVIT files (byte-identical) |
| MIST | Same road videos as WIRIndic; detection only |
| AlbertoChestnut, harsha-desaraju Wikisource sets | Telugu Wikisource (to be collected from source once) |

## Remaining risks (not fully solvable with the information released)

1. **Writers.** HW-UC and IHWWR give no writer IDs. One writer may have written several pages, so handwriting style can leak between splits even though pages don't. HW-WORDS is safe (writer folders are disjoint).
2. **HW-UC ID blocks.** 141,355 kept HW-UC crops (the numbered "manually annotated" folders) have no page ID. They are grouped in blocks of 10,000 or 50,000 consecutive IDs. By ID density, about 4–8% of their pages may straddle a block edge.
   - These crops are only in train (136,506) and val (4,849), never in test. So any straddle can only leak between train and val, never into test.
3. **Mozhi has only 28 books.** A 2-book test set is small and font-specific. Scores will vary a lot by which books are held out.
4. **Same shops on different videos.** WIRIndic videos from the same town can show the same signboards. Split by video removes repeated frames, not repeated shops.
5. **Synthetic test sets are weak.** 1,270 Synthetic-R test/train items look alike, and 99.8% of Synthetic-IndicSTR test words are in its train vocabulary. Use synthetic sets for pre-training only, never as an evaluation metric.
