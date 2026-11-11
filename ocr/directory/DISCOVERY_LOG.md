# Discovery log

How the directory was searched, between 2026-11-10 and 2026-11-11. Raw results are saved in `evidence/`.

## 1. Starting point

The audit began from the existing repo: `MASTER_CATALOGUE.csv` (16 `TEL-OCR` records plus manuscript, library,
periodical and text-corpus records) and the earlier acquisition work in `ocr/acquisition/`. Those records were
re-checked first (see [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md)) and then used as seeds.

## 2. Query variants

`scripts/discover.py` ran the same list of about 34 query variants on every searchable platform, including:
Telugu OCR; Telugu handwritten; Telugu handwriting recognition; Telugu character recognition; Telugu printed text;
Telugu scene text; Telugu word images; Telugu document images; Telugu manuscripts / palm leaf; Telugu text recognition;
Indic OCR; Indian language OCR; Indic handwritten; Indic scene text; multilingual OCR Indian; Dravidian OCR;
తెలుగు (Telugu script); IndicSTR; IIIT-HW; ILOCR; Mozhi; Synthetic-IndicSTR and others. Hugging Face also got
tag-based listing (`language:te`, image tasks) and model searches (to find the datasets models were trained on).

## 3. Platforms searched by API

| Platform (API) | Queries run | Unique hits | Date |
|---|---|---|---|
| archive | 9 | 745 | 2026-11-11 |
| arxiv | 12 | 147 | 2026-11-11 |
| datacite | 34 | 542 | 2026-11-11 |
| dataverse | 34 | 1,803 | 2026-11-11 |
| figshare | 34 | 326 | 2026-11-11 |
| github | 34 | 610 | 2026-11-11 |
| hf | 106 | 1,517 | 2026-11-11 |
| kaggle | 30 | 172 | 2026-11-11 |
| openalex | 34 | 3,237 | 2026-11-11 |
| zenodo | 35 | 1,737 | 2026-11-11 |

How the hits were screened:
- **Hugging Face:** 795 datasets and 765 models were screened by tags, README text and file names (`screen_hf.py`); 118 candidates had both images and Telugu evidence and were read one by one. Model cards gave 117 more dataset leads.
- **Zenodo, Figshare, DataCite, Dataverse, Internet Archive:** titles and descriptions filtered for Telugu + OCR/handwriting/document terms, then read.
- **DataCite** also covered IEEE DataPort (DOI prefix 10.21227), Mendeley Data (10.17632) and Kaggle DOIs, because IEEE pages block scripts.
- **OpenAlex + arXiv:** 686 OpenAlex works and 147 arXiv papers mentioned Telugu with an OCR-related term. Their titles and abstracts were screened; papers that describe a dataset were followed to find the data.
- **GitHub:** repositories and their file trees checked for actual data (many have code only).
- **Kaggle:** search, metadata and file-list APIs (no login, nothing downloaded).
- **Semantic Scholar:** the run hit the API rate limit and crashed partway. No results were saved, so this channel counts as **not completed**.

## 4. Sites and platforms investigated directly

| Platform / site | What was done |
|---|---|
| ILOCR dataset catalogue (ilocr.iiit.ac.in/dataset/1-200) | Every ID probed; Telugu pages read in full |
| ILOCR API catalogue (/api_list/) | 1,456 entries parsed; Telugu rows extracted |
| ILOCR competition sites (IHTR 2022/2023, ICDAR 2024 HWD, ICDAR 2025 IHDR, ICPR 2024 WIRIndic) | Dataset pages and download links checked |
| CVIT project pages + USODI portal (cvit.iiit.ac.in) | Project list scanned for Telugu; USODI detection/recognition lists read |
| IEEE DataPort | Pages block scripts (403); metadata taken via DataCite DOIs |
| Mendeley Data | Public API used for dataset metadata |
| Kaggle | Public search + metadata + file-list APIs (no login, nothing downloaded) |
| Roboflow Universe | Pages block scripts (403); search-engine snippets only |
| TDIL-DC (tdil-dc.in) | Certificate expired; not bypassed |
| Bhashini ULCA / AIKosh | Portals are web apps; listings checked where reachable |
| University of Hyderabad DSpace + SCIS pages | DSpace HTTP 503; old pages 404 |
| HP Labs / LipiTk site | Dataset page and licence read |
| CMATERdb (Jadavpur) | Telugu numeral subset confirmed |
| IHDIA (ihdia.iiit.ac.in) | Indiscapes project pages |
| BhashaSutra / Sarvam / Krutrim / Cognitive Lab / AI4Bharat | HF orgs and project pages |
| Commercial vendors: FutureBeeAI, GTS.ai, Shaip, Defined.ai | Product listings checked for Telugu OCR |
| Telugu digital collections: Internet Archive, DLI, Chandamama, AP Press Academy, GOML palm-leaf, perspectivia.net | Collection pages / search APIs |
| SSRN, ACM DL, Springer, arXiv HTML | Paper pages for dataset links (SSRN/ACM block scripts) |

In total, **28** platforms and sites were investigated (10 by API sweep, 18 directly).

## 5. ILOCR in depth

- **Dataset catalogue:** every page from `/dataset/1/` to `/dataset/200/` was requested. 62 pages are live (all at ID 69 or below), 135 return 404, and 3 return HTTP 500 (IDs 13, 14, 59; ID 14 is Mozhi-Telugu, whose zip files still download).
  Telugu pages: 23 (IIIT-INDIC-HW-WORDS-Telugu), 36 (IndicSTR12-Telugu), 40 (IIIT-Synthetic-M-Telugu), 55 (IIIT-Synthetic-R-Telugu), 68 (IIIT-Synthetic-IndicSTR-Telugu), plus 14 (Mozhi-Telugu, page broken).
- **API catalogue (`/api_list/`):** a table of 1,456 OCR **models/APIs**, not datasets. 132 rows mention Telugu: layout detection, word recognition, page pipelines and script detection from IIIT Hyderabad, IIT Bombay, IIT Delhi, IIT Jodhpur and C-DAC, plus entries for Google OCR, Tesseract, EasyOCR and Surya. The `api_detail` pages return server errors. Recorded as one related resource (TOCR-144).
- **Competition sites:** IHTR 2022 and 2023 (TOCR-004/005), ICDAR 2024 handwriting (IHWWR TOCR-007, PLHWTR TOCR-008), ICDAR 2025 IHDR (TOCR-009; Telugu zips 404), ICPR 2024 WIRIndic (TOCR-080).

## 6. Papers

- 833 paper records were screened by title and abstract (686 OpenAlex + 147 arXiv).
- 36 papers are linked from directory rows; each was opened to find the dataset link, size, licence and Telugu share.
- Citations were followed from the main hubs (IIIT-HW-Telugu, IndicSTR12, IIIT-ILST, Mozhi, IndicDLP, BSTD, Nayana, PHDIndic_11) to related releases. This turned up HW-UC, roadside IndicSTR-Word, MIST and TEXTRON.

## 7. Rejected candidates

These looked relevant but are not Telugu OCR resources. They are kept in the CSV so nobody spends time on them again.

| ID | Candidate | Reason |
|---|---|---|
| TOCR-154 | [3D Telugu Character Recognition (IEEE DataPort yz7d-cz45)](https://ieee-dataport.org/documents/3d-telugu-character-recognition) | Accelerometer x/y/z sensor CSVs for in-air writing of 5 characters - no images. |
| TOCR-155 | [HSC-IndicDB (Mendeley dkmxgd8n79)](https://data.mendeley.com/datasets/dkmxgd8n79/1) | Description names Bengali, Devanagari, Kannada, Malayalam; Telugu not mentioned. |
| TOCR-156 | [Learn Telugu letters Alphabets with Audio (Mendeley 98rd3nx2n4)](https://data.mendeley.com/datasets/98rd3nx2n4/1) | Audio pronunciation learning resource, not OCR data. |
| TOCR-157 | [AI-powered multilingual OCR system for historical documents (Zenodo 2...](https://doi.org/10.5281/zenodo.20604818) | Typed as dataset but is a technical specification report; no data. |
| TOCR-158 | [nvidia/OCR-Synthetic-Multilingual-v1 (and Kaggle 24K starter subset)](https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1) | Languages en, ja, ko, ru, zh only - no Telugu. |
| TOCR-159 | [ICDAR RRC MLT-2017 / MLT-2019](https://rrc.cvc.uab.es/?ch=15) | Indian scripts are Bangla and Devanagari only - no Telugu. |
| TOCR-160 | [MITDI - Mixed-lingual Indic Texts in Digital Images (MTAP 2022)](https://doi.org/10.1007/s11042-022-12596-7) | English, Bangla, Hindi only. |
| TOCR-161 | [Transfer Learning for STR in Indian Languages - released real data (G...](https://cvit.iiit.ac.in/research/projects/cvit-projects/transfer-learning-for-scene-text-recognition-in-indian-languages) | Released real data is Gujarati and Tamil only; Telugu results use IIIT-ILST. |
| TOCR-162 | [interfaze-ai/ocr-mlt-50m](https://huggingface.co/datasets/interfaze-ai/ocr-mlt-50m) | 60 rows across 50 languages; no meaningful Telugu content. |
| TOCR-163 | [AbhishekBhandari/Indic-post-ocr-correction](https://huggingface.co/datasets/AbhishekBhandari/Indic-post-ocr-correction) | Gujarati, Hindi, Marathi only. |
| TOCR-164 | [Aus-23/indic-synthetic-scene-text-1000](https://huggingface.co/datasets/Aus-23/indic-synthetic-scene-text-1000) | Marathi, Hindi, Gujarati, Bengali only. |
| TOCR-165 | [Crossmodal-3600 caption sets (floschne/xm3600, xm3600_1k, dinhanhx/cr...](https://huggingface.co/datasets/floschne/xm3600) | Telugu image captions, not text in images. |
| TOCR-166 | [WIT (wikimedia/wit_base, VedaLabs/wit_base)](https://huggingface.co/datasets/wikimedia/wit_base) | Image-caption pairs; no Telugu found in sample; not OCR. |
| TOCR-167 | [CC3M-35L / COCO-35L (ai-enthusiasm-community)](https://huggingface.co/datasets/ai-enthusiasm-community/CC3M-35L) | Translated captions, not OCR. |
| TOCR-168 | [visheratin/laion-coco-nllb](https://huggingface.co/datasets/visheratin/laion-coco-nllb) | Translated captions, not OCR. |
| TOCR-169 | [ARTPARK-IISc Vaani (and benchmarks)](https://huggingface.co/datasets/ARTPARK-IISc/Vaani) | Speech dataset with prompt images; not OCR. |
| TOCR-170 | [DRISHTIKON (13ari / Vipashyana)](https://huggingface.co/datasets/13ari/DRISHTIKON) | Cultural VQA; no Telugu text found in sample; not OCR. |
| TOCR-171 | [neulab/CulturalGround and other cultural VQA sets (symile-m3, global-...](https://huggingface.co/datasets/neulab/CulturalGround) | General VQA/QA with Telugu questions; images are not text-centric. |
| TOCR-172 | [krutrim-ai-labs/ocr_rotation_bench](https://huggingface.co/datasets/krutrim-ai-labs/ocr_rotation_bench) | Page-rotation classification; no Telugu in sampled rows. |
| TOCR-173 | [Shaip OCR training data](https://www.shaip.com/solutions/optical-character-recognition-ocr-machine-learning/) | Custom-collection vendor page; no Telugu OCR product listed. |
| TOCR-174 | [GitHub UthejKaramalapudi/Handwritten_Charcater_Classificaition_For_Te...](https://github.com/UthejKaramalapudi/Handwritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images) | Code only; no images in repository. |
| TOCR-175 | [GitHub Harathi123/Telugu-Character-Recognition-using-CNN](https://github.com/Harathi123/Telugu-Character-Recognition-using-CNN) | Reuses HP Labs data (TOCR-021); no new data. |
| TOCR-176 | [GitHub alfahimmohammad/Telugu-Handwritten-Text-Recognition](https://github.com/alfahimmohammad/Telugu-Handwritten-Text-Recognition) | Reuses CVIT IIIT-HW-Telugu (TOCR-001); no new data. |
| TOCR-177 | [GitHub jaganmohanreddy2106/Telugu-Handwritten-Digit-Recognition](https://github.com/jaganmohanreddy2106/Telugu-Handwritten-Digit-Recognition) | 10 example digit images only; no dataset. |
| TOCR-178 | [Telugu Alphabets 52-letter chart (Zenodo 20079705)](https://doi.org/10.5281/zenodo.20079705) | Single educational chart image; record now HTTP 410 (removed). |
| TOCR-179 | [Telugu NLP / news / lyrics Kaggle sets (text-only, non-OCR)](https://www.kaggle.com/datasets/sudalairajkumar/telugu-nlp) | Text classification/NLP corpora surfaced by Kaggle search; not OCR and not needed as OCR LM sources. |

Beyond these 26 rows, several hundred search hits were discarded during screening without a row, for example
Telugu text-only NLP sets, speech sets, and Telugu-tagged HF sets with no images. The `hf_screen.json` and
`platform_candidates.txt` files in `evidence/discovery/` keep the screening decisions.

## 8. Channels not exhausted

- **Semantic Scholar** - run did not finish (rate limit). Re-run with an API key.
- **Google Scholar** - no API. Not searched systematically.
- **IEEE Xplore / Springer / Elsevier full text** - paywalled. Only abstracts and open versions were read, so dataset links inside paywalled papers may be missed.
- **Bhashini ULCA and AIKosh full listings** - JavaScript web apps. Only reachable listings were checked.
- **TDIL-DC** - certificate expired, not bypassed. The Telugu image corpus there is unconfirmed.
- **Roboflow Universe** - blocks scripts. Two Telugu projects are known only from search snippets.
- **Indian university repositories (Shodhganga theses, institutional DSpace)** - not searched systematically. Theses often describe private datasets.
- **Telugu-language web (Telugu-script search queries on general search engines)** - only lightly covered.
- **Direct contact with authors** - not done. Many unverified or inaccessible sets could probably be obtained by email.
