# Sample inspection report

Checked on 2026-11-10. Every dataset below was downloaded (fully or partly). Each one was checked in three ways:

1. **Counting.** Every label line was counted and matched to an image on disk (`scripts/verify_downloads.py`).
2. **Label checks.** Labels were checked for empty text, non-Telugu text, odd Unicode and duplicate images.
3. **Visual check.** 6–8 random image/label pairs were viewed by eye. (Phase 2: `samples/` now holds 8 cleaned pairs per source, only from sources with a stated open licence.)

"Labelled pairs" means an image together with its correct text. Images without text are never counted.

## Summary

| ID | Dataset | Type | Labelled pairs | Missing images | Empty labels | Visual check |
|---|---|---|---:|---:|---:|---|
| ACQ-01 | WIRIndic-Telugu | scene text, real | 20,000 | 0 | 0 | Labels correct. About half the crops cut off part of the word, but the label still gives the full word |
| ACQ-02 | IHWWR-1.0 Telugu train | handwritten, real | 77,625 | 0 | 0 | Labels correct. Full stops visible in the images are left out of the labels |
| ACQ-03 | BSTD Telugu crops | scene text, real | 2,760 | 0 | 0 | Labels correct. 16.6% use the wrong character (see below) |
| ACQ-04 | Sarvam Indic OCR Bench (Telugu) | printed blocks, real | 300 | 0 | 0 | Correct, including tables and mixed English |
| ACQ-05 | IndicDLP eval sample (Telugu) | printed blocks, real | 10 | 0 | 0 | Correct. Some labels contain a literal `\n` |
| ACQ-06 | IIIT-Synthetic-M-Telugu | synthetic words | 138,585 | 0 | 0 | Correct (rendered text) |
| ACQ-07 | Mozhi-Telugu (HF mirror) | printed words, real | 100,024 | 0 | 0 | Correct. Test split identical to the official release (ACQ-08) |
| ACQ-09/10/12 | IndicSTR12-Telugu + mirrors | scene text, real | 1,200 | 0 | 0 | Mostly correct. 87 labels fixed in the mirror |
| ACQ-11 | Telugu Wikisource, 6 validated pages | printed pages, real | 6 | 0 | 0 | Text matches the page, but not the layout |

## Findings per dataset

**WIRIndic-Telugu (ACQ-01)**
- The labels are 100% Telugu and correctly encoded.
- Only 4,580 different words appear across 20,000 images. Shop-sign words repeat a lot; for example, "సెంటర్" appears 441 times.
- The crops are small (median 58×34 pixels) and often blurred.
- No video frame appears in more than one split. However, 42–48 road-video sequences do, so the test score will look somewhat better than real-world performance.

**IHWWR-1.0 (ACQ-02)**
- 63,341 labels are Telugu words.
- 14,284 labels are punctuation or digits that were cropped as separate "words": 7,783 `.`, 2,443 `,`, plus `?`, `"`, `(` and others.
- The 175 duplicate images are all these punctuation crops.
- Remove punctuation-only items before training.

**BSTD (ACQ-03)**
- 457 of 2,760 labels use the Telugu digit zero `౦` (U+0C66) instead of the anusvara `ం` (U+0C02). Examples: `ప్రసాద౦`, `తెల౦గాణ`, `జ౦క్షన్`.
- The fix is mechanical: replace `౦` with `ం` when it follows a letter.
- The images are polygon-masked crops, with black outside the text area.

**Sarvam bench (ACQ-04)**
- These are long text blocks (median 184 characters).
- 110 of the blocks contain English, as expected for dictionary and textbook pages.
- Some source pages carry publisher watermarks ("KTBS"). The benchmark is Apache-2.0, but the source documents have their own copyright. Use it for testing only.

**Synthetic-M (ACQ-06)**
- The labels have 68,898 different words.
- There are 181 labels with Latin letters and 32 duplicate images. Both are harmless.

**Mozhi (ACQ-07)**
- The mirror's test split was compared with the official ILOCR test zip: all 9,876 images and labels are identical.
- There is no train/test overlap. Two images appear in both train and validation.

**IndicSTR12 (ACQ-09/10/12)**
- The HF mirror holds the same images and corrects 87 labels; for example, `ప్రాధమిక` becomes `ప్రాథమిక`.
- A few mirror labels have CSV quoting junk, such as `"తలంచు"""`.
- One official label was seen to be wrong: `రప్నోట్` where the sign reads `రఫ్‌నోట్`.

**Wikisource pages (ACQ-11)**
- The proofread text matches the scan word for word. However:
  - wiki markup is mixed in (`{{Center|…}}`, `<poem>`, `'''`);
  - page numbers are dropped;
  - two-column pages are merged into one text flow.
- So it can be used as page-level text only, until lines are aligned to the image.

## Sampled only (not fully downloaded)

These sets were read inside the remote zip files, using byte-range requests. The full label files were fetched, plus a few images from each.

| Dataset | What was checked | Result |
|---|---|---|
| IIIT-INDIC-HW-WORDS-Telugu (val/test/train) | All label files + 10 images per split | Labels correct. Train has 88,534 images but only 80,637 labels |
| IIIT-Indic-HW-UC Telugu | All split label files + 6 images | Camera photos of handwriting. 200,000 labels, only 477 of them punctuation. Some extra folders contain blank crops labelled `NA` |
| PLHWTR-1.0 Telugu | Listing + 8 pages with their text | Page text matches the handwriting. The writer's page number is not in the label |
| IIIT-Synthetic-R-Telugu | All label files + images | Correct. Labels start with a space, and some join two words |
| IIIT-Synthetic-IndicSTR-Telugu | val/test labels + images | Labels correct, but about 1 in 3 images is close to unreadable |
| IHTR-2023 Telugu | Label files | Train is an exact copy of HW-WORDS train |
| BSTD all-language zip | Annotation JSON | 2,215 + 545 Telugu words confirmed |
