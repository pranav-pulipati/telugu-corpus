# Acquisition blockers

What stopped data from being acquired, as of 2026-11-10, and what would unblock it.

**Nothing restricted or copyrighted was downloaded into the project.**
- IIIT-ILST Telugu forbids redistributing its images. It was read once into a temporary folder for the duplicate check and is not kept here.
- `ocr/acquisition/data/` is git-ignored, so none of the bulk data gets committed.

## 1. Access blocked (login, gating or broken links)

| Source | Blocker | To unblock |
|---|---|---|
| ICDAR 2025 IHDR – Telugu (Task A/B, val/test) | Every Telugu zip returns HTTP 404 | Email the ILOCR / ICDAR 2025 IHDR organisers (contact page on the competition site) |
| IndicDLP (`ai4bharat/indicdlp`, HF) | Gated: needs an HF login plus accepting terms. This machine has no HF login. | The user logs in and accepts terms, or downloads from AIKosh. It is layout-only, so low priority for OCR. |
| NayanaOCRBench_Synthetic, 1DuBu1/NayanaOCR, ranjanhr1/nayanabench-rendered, octopus-ocr-indic-synth | Gated (manual or auto) | Request access. Most are derivatives of Nayana. |
| Bharat Scene Text (HF copy) | Gated | Not needed: the Google Drive copy is open and was used |
| PHDIndic_11, IEEE DataPort Telugu handwritten characters (2 sets) | Free IEEE account login required | The user creates an IEEE DataPort account. The data is CC BY 4.0. |
| UHTelPCC (Univ. of Hyderabad) | Project page returns 404 | Email Prof. Chakravarthy Bhagvati (SCIS, UoH) |
| onath IndicDLP block-OCR eval set (582 Telugu blocks) | Private on HF; only 10 rows public | Ask the author (Oikantik Nath, IIT Madras) |
| ILOCR dataset page for Mozhi-Telugu (`/dataset/14/`) | Page crashes (Django error) | Not needed: the files download from `/public/printed/phase-0/v0.5/telugu/akshara/` |

## 2. Licence unclear or restrictive (deliberately not downloaded)

| Source | Issue |
|---|---|
| IIIT-Indic-HW-UC Telugu (4.8 GB) | No licence on the project page. The same group's ILOCR policy is CC BY 4.0, but this isn't stated for this set. **Get written confirmation before using it.** Technically it downloads fine. |
| Divs0910/telugu-ocr-dataset (120,321 Chandamama crops) | No licence, no dataset card. Chandamama is a copyrighted magazine. |
| harsha-desaraju consensus-labelling / pdf-line / line-text / Telugu-text-image | The labels are machine OCR. The source books appear to be recent copyrighted titles, and the "news" set renders Andhra Jyothy articles. The uploader's MIT tag cannot license those texts. |
| IndicSTR12 / IIIT-ILST real images | Crawled from Google Images, so the images belong to third parties. ILST forbids redistribution. Annotations are CC BY 4.0 (ILOCR). Fine for research; risky for commercial models. |
| IIITS-THDB | Non-commercial research use only |
| NayanaOCRBench_Natural Telugu (461 pages) | CC BY-NC 4.0, so evaluation/research only |
| MIST | Research use; commercial use needs the authors' permission |
| Telugu Wikisource scans hosted locally (not on Commons), e.g. `గబ్బిలము` by Jashuva | Check the licence on each file page before using the image. The text is CC BY-SA. |
| WIRIndic / IHWWR / Synthetic sets | ILOCR's licence document is a policy text ("Bhashini plans to use CC BY 4.0"), not a per-dataset licence file. Treat as CC BY 4.0 with attribution and keep the policy URL on record. |

## 3. Technical or format blockers

| Source | Issue | Workaround |
|---|---|---|
| UHIndicPCwS (572 MB `.pkl`) | A Python pickle can run code when loaded, and its Telugu share is unknown | Don't load it with `pickle`. Inspect it with `pickletools` in a sandbox, or ask the authors for image files. |
| Synthdog-Multilingual-100 Telugu | The 10,000 Telugu images sit inside one 11.3 GB tar.gz with all non-Latin scripts. They can't be extracted without streaming the whole archive. | Stream-extract, keeping only the `te` paths |
| Large open zips (HW-UC 4.8 GB, Synthetic-IndicSTR 6.3 GB, Synthetic-R 2.05 GB, PLHWTR 3.0 GB, HW-WORDS 3.8 GB) | Not blocked: left out only for time and disk (~330 KB/s to 1.5 MB/s observed) | Run the downloads listed in NEXT_DATA_COLLECTION_PLAN.md |
| Network | One DNS failure during BSTD | `scripts/remotezip_fetch.py` skips files it already has; the rerun completed |

## 4. Sources that turned out to have no usable data

- **Zenodo 14965382** ("20,000 image-text pairs", catalogue TEL-OCR-014): the only file is a vendor brochure PDF.
- **IIIT-INDIC-HW-WILD, IIITS-THDB, PHDIndic_11, TEXTRON, MUSTARD, MIST, IndicDLP, miracl-vision:** these have images but no Telugu text transcriptions. They are not OCR-ready.
- **Palm-leaf manuscripts:** no public Telugu palm-leaf dataset with transcriptions was found. Published Telugu palm-leaf work (2012, 2016) did not release data. The GOML scans (TEL-MSS-001) are images only.
