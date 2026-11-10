# Cleaning report

Run on 2026-11-10 with `scripts/build_corpus.py` (stages `scan → assign → export`).

## Ground rules

- **Originals are never modified.** All downloads stay in `data/<dataset>/zips/` (or the original parquet files), with SHA-256 sums in `VERIFIED_DOWNLOADS.csv`.
- **Nothing is dropped silently.** Every input item has a row in `data/corpus_work/assign/<source>.parquet` with its `drop` reason (or its split, if kept).
- **Every label change is recorded.** Each kept sample in `data/unified/` stores `raw_text` (the original label), `text` (the cleaned label) and `text_changes` (which rules fired).

## What was checked

All 4,385,420 input items were checked: 634,677 real and 3,750,743 synthetic.

| Check | How | Result |
|---|---|---|
| Corrupt images | Full decode of every image with Pillow | **0 corrupt** in all 4,385,420 |
| Blank images | Pixel range < 16 or standard deviation < 3 (real word crops only) | 66 dropped (49 HW-UC, 17 HW-WORDS) |
| Empty labels | After cleaning | 0 |
| Placeholder labels | `NA`, `N/A`, `#`, `null` … | 33,306 dropped (all HW-UC, mostly blank crops) |
| Exact duplicates | Same decoded pixels in the same collection | 185 real + 32 synthetic dropped. No duplicate group had conflicting labels. |
| Near-duplicates across sources | Same 64-bit image hash and same label | 0 found |
| Image–text alignment | Manual audit of 186 random kept items (see TRAINING_READINESS_REPORT.md) | Problems found and measured, not fixed automatically |

## Rules that drop items

| Rule | Applies to | Why | Dropped |
|---|---|---|---:|
| `punctuation_only` | Real word-level sets | Visual check: crops of `.` `,` `?` include parts of neighbouring letters; useless for training | 13,094 (IHWWR 11,742 · Mozhi 940 · HW-UC 410 · BSTD 2) |
| `digits_only_unreliable` | IHWWR, HW-UC (camera pages) | Visual check of 10: ~4 did not match the label. They are copied sentence-ID numbers. | 2,699 (IHWWR 2,540 · HW-UC 159) |
| `placeholder_label` | All | Label is not a transcription | 33,306 |
| `blank_image` | Real word-level sets | Nothing visible to read | 66 |
| `exact_duplicate_image` | All | Keep the first copy only | 217 |
| `overlap_page_in_hw_uc` | IHWWR | Same handwritten page also appears in HW-UC (which has more words per page). Keep one copy of each page. | 35,809 |

**The 14,284 IHWWR "punctuation-only" samples:** that earlier figure counted every label with no Telugu letter. The exact breakdown:

| Group | Count | Action |
|---|---:|---|
| Punctuation only | 11,742 | Removed |
| Digits only | 2,540 | Removed, after the visual check above |
| Latin letters | 2 | Kept and flagged |
| **Total** | **14,284** | |

## Rules that change labels

Each rule runs on every source; the counts below are among kept items.

| Rule | What it does | Kept items changed |
|---|---|---|
| `digit_zero_to_anusvara` | Telugu digit zero `౦` (U+0C66) right after a Telugu letter or sign becomes anusvara `ం` (U+0C02). The two look identical, but the digit is wrong inside a word. | BSTD 457 (16.6%) · Synthetic-R 1,374 · Synthetic-IndicSTR 936 · HW-UC 11 |
| `zero_width_removed` | Removes ZWNJ, ZWJ, zero-width space, BOM and soft hyphen. They are invisible, so a model can't learn them from the image. | HW-UC 1,031 · Sarvam 10 · IndicSTR12 1 |
| `nfc` | Unicode NFC normalisation | Synthetic-R 4,270 · HW-UC 16 · Sarvam 1 |
| `whitespace` | Trim; collapse spaces (word sets); keep line breaks (block sets) | Synthetic-R 612,500 (every label had a leading space) · BSTD 142 · HW-UC 101 · Sarvam 7 · IndicDLP 4 · IndicSTR12 2 · Mozhi 1 |
| `literal_backslash_n` | Turns a literal `\n` in labels into a real line break | IndicDLP sample 4 |
| IndicSTR12 label correction | Uses the corrected label from CVIT's newer `real.zip` release when the image bytes are identical. A mirror label with quoting junk is not used. | 86 of 1,200 (e.g. `ప్రాధమిక → ప్రాథమిక`) |

**Rule removed after evidence.** A rule stripping quotation marks from word labels was tried and then **removed**. Mozhi and Synthetic-M images really contain the printed quotes, so stripping them would have created errors.

## Flagged, not changed

These items are kept, with their flags in the `text_flags` column, because an automatic fix could be wrong.

| Flag | Meaning | Kept items |
|---|---|---|
| `legacy_ra_order` | Old font-encoding order such as `స్ర్తీ` for `స్త్రీ` | 3,970 (mostly synthetic; HW-WORDS 89, Mozhi 88) |
| `invalid_sign_sequence` | Two vowel signs or a double virama in a row (e.g. HW-WORDS `కనే్నసి` for `కన్నేసి`) | 1,716 (Synthetic-IndicSTR 1,217 · Synthetic-R 286 · HW-UC 166 · HW-WORDS 35) |
| `latin` | Contains Latin letters | 274 real (110 of them in the Sarvam test blocks) + 181 synthetic |
| `digits_only` | Number-only labels in printed and scene sets (these are valid there) | Mozhi 1,275 · BSTD 1 · Synthetic-M 2,215 |

If you want a strict training set, drop items with `legacy_ra_order` or `invalid_sign_sequence`. That removes 0.13% of the data.

## Image standardisation

- **Containers:** all images go into Parquet shards with a fixed schema (`image`, `image_format`, `text`, `raw_text`, `collection`, `granularity`, `source`, `source_key`, `group_id`, `orig_split`, `label_type`, `licence`, `licence_status`, `redistributable`, `text_flags`, `text_changes`, `width`, `height`, `extra`).
- **Formats and modes:** every image was checked to be JPEG or PNG, in L or RGB colour mode, with no EXIF rotation. All 4,300,229 kept images already met this, so their bytes are stored unchanged (no lossy re-encoding). The code to convert anything else to PNG is in `standardise()`.
- **Labels:** stored as UTF-8 and NFC.

## Results

| Source | Input | Kept | Dropped |
|---|---:|---:|---:|
| HW-UC Telugu | 314,243 | 280,226 | 34,017 |
| HW-WORDS Telugu | 118,515 | 118,498 | 17 |
| IHWWR-1.0 Telugu | 77,625 | 27,448 | 50,177 |
| Mozhi Telugu | 100,024 | 99,081 | 943 |
| WIRIndic Telugu | 20,000 | 20,000 | 0 |
| BSTD Telugu | 2,760 | 2,755 | 5 |
| IndicSTR12 Telugu | 1,200 | 1,200 | 0 |
| Sarvam bench Telugu | 300 | 300 | 0 |
| IndicDLP eval sample | 10 | 10 | 0 |
| **Real total** | **634,677** | **549,518** | **85,159** |
| Synthetic-M | 138,585 | 138,553 | 32 |
| Synthetic-R | 612,500 | 612,500 | 0 |
| Synthetic-IndicSTR | 2,999,658 | 2,999,658 | 0 |
| **All** | **4,385,420** | **4,300,229** | **85,191** |

## How to reproduce

```bash
python -I ocr/acquisition/scripts/build_corpus.py scan all     # decode + normalise + QA facts
python -I ocr/acquisition/scripts/build_corpus.py assign all   # drop rules, dedup, leakage-safe splits
python -I ocr/acquisition/scripts/build_corpus.py export all   # unified shards
python -I ocr/acquisition/scripts/build_corpus.py checksums
python -I ocr/acquisition/scripts/validate_unified.py          # independent re-check
python -I ocr/acquisition/scripts/corpus_report.py             # statistics + DATASET_MANIFEST.csv
```

These need pillow and pyarrow.
