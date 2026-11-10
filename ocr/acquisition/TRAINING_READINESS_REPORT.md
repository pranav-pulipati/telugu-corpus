# Training readiness report

Status on 2026-11-10. This report says what can be trained on now, what needs a licence answer first, and what is only fit for testing. Each verdict is backed by checks on the actual data.

## Short answer

- **549,518 real Telugu image–text pairs** are cleaned, deduplicated and split by page, book, scene or video, with no leakage between splits.
- **220,644 of them carry a stated open licence** and can be used now:
  - HW-WORDS: 118,498
  - Mozhi: 99,081
  - BSTD: 2,755
  - test-only sets: 310
- **327,674 more** (HW-UC, IHWWR, WIRIndic) are ready technically but have no stated licence. Use them for research only until IIIT Hyderabad confirms the terms.
- **3,750,711 synthetic pairs** are suitable for pre-training only. Their licence is not stated either.
- **Machine-generated labels: none in the corpus.**

## Evidence 1: automatic checks on every sample

`validate_unified.py` re-read all 876 shards (4,300,229 rows):

| Check | Result |
|---|---|
| Checksum mismatches | 0 |
| Images that fail to decode or have an odd colour mode | 0 |
| Empty labels, non-NFC labels or labels with zero-width characters | 0 |
| Duplicate IDs | 0 |
| Source groups appearing in more than one split | 0 |

## Evidence 2: manual audit of label quality

I read 186 randomly chosen kept items against their images: 16 per source, 10 for the IndicDLP sample. They were drawn with a fixed seed. The item-by-item verdicts are in `qa/manual_audit.csv`.

These samples are small, so the 95% ranges are wide. They detect big problems; they can't prove a dataset is clean.

| Source | Checked | Correct | Wrong label | Other problem | Error rate (95% range) |
|---|---:|---:|---:|---|---|
| HW-UC | 16 | 14 | 1 (a letter missing) | 1 unclear | 6% (1–28%) |
| IHWWR | 16 | 16 | 0 | 2 leave out punctuation visible in the crop | 0% (0–19%) |
| HW-WORDS | 16 | 15 | 1 (scrambled encoding `కనే్నసి`) | – | 6% (1–28%) |
| Mozhi | 16 | 15 | 0 | 1 unclear; quote style differs | 0% (0–19%) |
| WIRIndic | 16 | 8 | 0 | **7 partial crops** (label = full word, crop shows part); 1 unreadable | label 0%, but **~44% partial crops** |
| BSTD | 16 | 13 | 2 (one is a different word) | 1 unclear | 12.5% (3.5–36%) |
| IndicSTR12 | 16 | 14 | 2 (misspellings) | – | 12.5% (3.5–36%) |
| Sarvam blocks | 16 | 16 | 0 | checked by content, not character by character | 0% (0–19%) |
| IndicDLP sample | 10 | 10 | 0 | all from one magazine issue | 0% (0–28%) |
| Synthetic-M | 16 | 16 | 0 | – | 0% |
| Synthetic-R | 16 | 16 | 0 | – | 0% |
| Synthetic-IndicSTR | 16 | 12 | 0 | **4 unreadable images** | labels exact, but ~25% unreadable |

**Known label-quality issues found with full counts**, all fixed or flagged:
- BSTD `౦`/`ం` mix-up: 457 labels fixed.
- IndicSTR12: 86 labels replaced with the corrected CVIT release.
- Old-encoding (`legacy_ra_order`) and invalid sign sequences: 5,686 flagged.

## Readiness by source

| Source | Pairs | Verdict | Use it for | Caveats |
|---|---:|---|---|---|
| **HW-WORDS** (handwritten) | 118,498 | **Ready, CC BY 4.0** | Train + official writer-disjoint test | Boxed forms are cleaner than real notes. 88% of test words also appear in train. |
| **Mozhi** (printed words) | 99,081 | **Ready, CC BY 4.0** | Train + book-held-out test | Only 28 books, so the test set (2 books) is small. Don't compare with official Mozhi scores (the official split leaks). |
| **BSTD** (scene words) | 2,755 | **Ready, Apache-2.0** | Train + test | About 1 in 8 labels may be wrong (audit). Small. |
| **HW-UC** (handwritten) | 280,226 | **Ready technically; licence pending** | Main handwriting training set; its test split = ICDAR 2024 test pages | No writer IDs. About 141K crops are grouped by ID blocks. |
| **IHWWR** (handwritten) | 27,448 | **Ready technically; licence pending** | Train | Only pages not already in HW-UC |
| **WIRIndic** (scene words) | 20,000 | **Ready technically; licence pending** | Train with care | Many crops cut off part of the word. Only 4,580 distinct words. |
| **IndicSTR12** (scene words) | 1,200 | **Hold** | Small eval at most | The pictures belong to third parties. About 12% of labels are wrong. |
| **Sarvam bench** | 300 | **Evaluation only** | Printed-block test | Never train on it |
| **IndicDLP sample** | 10 | **Not useful alone** | – | 10 blocks from one magazine |
| **Synthetic-M / -R / -IndicSTR** | 3,750,711 | **Pre-training only; licence not stated** | Warm-up before real data | IndicSTR: ~25% unreadable. Their own test splits are not meaningful (vocabulary overlap). |

## Recommended evaluation suite

These are the fixed test splits in `data/unified/*/test`. Never train on them.

| Test set | Pairs | What it measures |
|---|---:|---|
| HW-UC test (= ICDAR 2024 HWD Telugu test pages) | 19,436 | Real camera-captured handwriting; comparable with ICDAR 2024 |
| HW-WORDS official test (writer-disjoint) | 17,895 | Clean handwriting by unseen writers |
| Mozhi held-out books | 5,242 | Printed words from unseen books |
| Sarvam blocks | 300 | Printed text blocks (textbooks, dictionaries, newspapers), reviewed twice |
| WIRIndic held-out videos | 2,789 | Road-sign text |
| BSTD official test | 542 | Scene text from different photos |

## Not ready yet: Telugu Wikisource pages

- **Downloaded:** the official dump (2026-11-01, SHA-1 verified). It contains 134,015 human-proofread pages (54,483 validated, 79,532 proofread), and the scan licence of all 1,231 books.
- **Eligible:** 127,326 of those pages are on public-domain or CC scans.
- **Blocker:** Wikimedia refuses bulk page-image requests unless the client identifies itself with contact details (robot policy). I didn't add your email or GitHub identity without permission. **0 pairs from this source are counted.**
- **To resume:** run `WIKIMEDIA_CONTACT="<email or project URL you choose>" python -I ocr/acquisition/scripts/wikisource_collect.py images --width 1280 --workers 2`. Then re-run `build_corpus.py scan wikisource_te_pages`, then `assign all`, then `export wikisource_te_pages`.
- **Even then:** the labels are page-level and content-faithful, not layout-faithful (columns merged, page numbers dropped). They suit page-level or VLM-style OCR as they are. Line-level training needs a line-alignment step.

## Biggest gaps

1. **Licence confirmation from IIIT Hyderabad.** This one email decides 327,674 real and 3.75M synthetic pairs.
2. **Real printed text beyond 28 books.** Mozhi is the only large real printed set. Wikisource images (blocked above) would add about 127K pages from about 1,100 books.
3. **Historical and palm-leaf documents:** there is still no public Telugu set with transcriptions.
