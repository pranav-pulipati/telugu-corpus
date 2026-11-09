---
language:
- te
license: cc-by-sa-4.0
task_categories:
- image-to-text
pretty_name: Telugu OCR Dataset
size_categories:
- 10K<n<100K
---

# Telugu OCR Dataset

A corpus of aligned scanned page images and human-transcribed Telugu text, sourced from [Telugu Wikisource](https://te.wikisource.org). Built for OCR model training and evaluation.

## Stats

| | |
|---|---|
| Total page pairs | ~25,565 |
| Books | 221 |
| Total size | ~11 GB |
| License | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |

## Dataset Structure

```
dataset/
  <book_title>/
    page_0001.jpg   ← scan image
    page_0001.txt   ← transcribed Telugu text (UTF-8)
    page_0004.jpg
    page_0004.txt
    ...
    meta.json       ← per-book metadata
corpus_profile.json ← index of all books with quality and curation details
curation_decisions.json ← approved/excluded status for every book in the manifest
```

Page numbers are not always consecutive — gaps indicate pages with no transcription available.

---

## corpus_profile.json

Top-level file. One JSON object per book covering every book in the original manifest (including excluded ones).

| Field | Type | Description |
|---|---|---|
| `index_title` | string | Wikisource index page title (unique identifier) |
| `filename` | string | Original PDF filename on Wikimedia Commons |
| `page_count` | int | Total scan pages in the source PDF |
| `mime_type` | string | MIME type of source file (usually `application/pdf`) |
| `size_mb` | float | Source file size in MB |
| `telugu_ratio` | float | Fraction of non-whitespace, non-digit characters in the Telugu Unicode block (ఀ–౿), sampled from 3 evenly-spaced pages |
| `telugu_pct` | float | `telugu_ratio` as a percentage |
| `no_transcriptions` | bool | `true` if no transcribed pages were found on Wikisource |
| `quality_samples` | int[] | ProofreadPage quality levels from sampled pages (see Quality Levels below) |
| `quality_avg` | float | Mean of `quality_samples` |
| `quality_label` | string | Human-readable label for `round(quality_avg)` |
| `decision` | string | `"approved"` or `"excluded"` |
| `exclusion_reason` | string | Why the book was excluded (empty if approved) |
| `decided_at` | string | ISO 8601 timestamp of the curation decision |
| `auto_decision` | bool | `true` if decided automatically by the pipeline |
| `profiled_at` | string | ISO 8601 timestamp of language profiling |

Approved books pass all three criteria: ≥ 80% Telugu script ratio, ≥ 50 scan pages, and at least one transcribed page.

---

## dataset/\<book\>/meta.json

One file per book directory. Describes what was actually downloaded.

| Field | Type | Description |
|---|---|---|
| `status` | string | `"done"` if completed successfully |
| `saved` | int | Number of page pairs (image + text) saved |
| `total_pages` | int | Total scan pages in the source PDF |
| `filename` | string | Original PDF filename |
| `pages` | object | Map of `"page_number" → { "quality": int }` for every downloaded page |

The `pages` object contains only pages that have both an image and a transcription. Pages missing from this map either had no transcription or failed to download.

---

## Quality Levels

From the Wikisource [ProofreadPage extension](https://www.mediawiki.org/wiki/Extension:ProofreadPage):

| Level | Label | Meaning |
|---|---|---|
| 0 | `no_text` | Blank or image-only page |
| 1 | `not_proofread` | Transcription exists but has not been reviewed |
| 2 | `problematic` | Flagged as having errors |
| 3 | `human_proofread` | Reviewed and corrected by a human editor |
| 4 | `validated` | Reviewed and validated by a second human editor |

Levels 3 and 4 are the most reliable ground truth for OCR evaluation.

---

## Source & License

All text transcriptions and original book scans are from [Telugu Wikisource](https://te.wikisource.org) and are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Attribution: Telugu Wikisource contributors.

---

## Author

**Alberto J. Chestnut**
Contact: [data@chest.nu](mailto:data@chest.nu)

---

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{chestnut2026telugu,
  author    = {Chestnut, Alberto J.},
  title     = {Telugu OCR Dataset},
  year      = {2026},
  publisher = {Hugging Face},
  note      = {Sourced from Telugu Wikisource (CC BY-SA 4.0)},
  url       = {https://huggingface.co/datasets/AlbertoChestnut/telugu-ocr},
  doi       = { 10.57967/hf/9079 }

}
```
