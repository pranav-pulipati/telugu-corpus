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
| openalex citations (round 2) | 14 | 79 | 2026-11-11 |
| crossref (round 3) | 20 | 2,516 | 2026-11-11 |
| datacite | 34 | 542 | 2026-11-11 |
| dataverse | 34 | 1,803 | 2026-11-11 |
| figshare | 34 | 326 | 2026-11-11 |
| github | 34 | 610 | 2026-11-11 |
| github deep, all pages + file trees (round 3) | 27 | 1,470 | 2026-11-11 |
| hf | 106 | 1,517 | 2026-11-11 |
| hf full paginated listing (round 3) | 14 | 70,298 | 2026-11-11 |
| kaggle | 30 | 172 | 2026-11-11 |
| mendeley (round 2) | 11 | 1,231 | 2026-11-11 |
| openalex | 34 | 3,237 | 2026-11-11 |
| kaggle (round 2, broader queries) | 20 | 458 | 2026-11-11 |
| hf (round 2, broader queries) | 37 | 776 | 2026-11-11 |
| datacite (round 2, broader queries) | 1 | 1,560 | 2026-11-11 |
| s2 (Semantic Scholar, partial) | 4 | 100 | 2026-11-11 |
| shodhganga (round 2) | 24 | 72 | 2026-11-11 |
| zenodo | 35 | 1,737 | 2026-11-11 |

How the hits were screened:
- **Hugging Face:** 795 datasets and 765 models were screened by tags, README text and file names (`screen_hf.py`); 118 candidates had both images and Telugu evidence and were read one by one. Model cards gave 117 more dataset leads.
- **Zenodo, Figshare, DataCite, Dataverse, Internet Archive:** titles and descriptions filtered for Telugu + OCR/handwriting/document terms, then read.
- **DataCite** also covered IEEE DataPort (DOI prefix 10.21227), Mendeley Data (10.17632) and Kaggle DOIs, because IEEE pages block scripts.
- **OpenAlex + arXiv:** 686 OpenAlex works and 147 arXiv papers mentioned Telugu with an OCR-related term. Their titles and abstracts were screened; papers that describe a dataset were followed to find the data.
- **GitHub:** repositories and their file trees checked for actual data (many have code only).
- **Kaggle:** search, metadata and file-list APIs (no login, nothing downloaded).
- **Semantic Scholar:** round 1 crashed on the rate limit. Round 2 re-ran it with slow pacing and long back-off for about 45 minutes: 4 of 36 planned queries were attempted, 1 returned results (100 papers) and the others got HTTP 429 even after retries, so the run was stopped. Returned papers were screened the same way as OpenAlex.

## 4. Sites and platforms investigated directly

| Platform / site | What was done |
|---|---|
| ILOCR dataset catalogue (ilocr.iiit.ac.in/dataset/1-200) | Every ID probed; Telugu pages read in full |
| ILOCR API catalogue (/api_list/) | 1,456 entries parsed; Telugu rows extracted |
| ILOCR competition sites (IHTR 2022/2023, ICDAR 2024 HWD, ICDAR 2025 IHDR, ICPR 2024 WIRIndic) | Dataset pages and download links checked |
| CVIT project pages + USODI portal (cvit.iiit.ac.in) | Project list scanned for Telugu; USODI detection/recognition lists read |
| IEEE DataPort | Pages block scripts (403); metadata taken via DataCite DOIs |
| Mendeley Data | Round 1: dataset metadata API; round 2: public search API (11 queries) |
| Kaggle | Public search + metadata + file-list APIs (no login, nothing downloaded) |
| Roboflow Universe | Pages block scripts (403); round 2: 4 site-restricted web searches found 8 Telugu projects |
| TDIL-DC (tdil-dc.in) | Certificate expired (Nov 2026); not bypassed; no Wayback copy of the resource page |
| Bhashini ULCA | Round 2: public data-metric endpoint (found in the open-source ULCA frontend) lists all 28 OCR corpora; 2 are Telugu |
| AIKosh (IndiaAI) | Round 2: portal returned 504/timeouts; dataset pages enumerated with site-restricted web searches |
| University of Hyderabad DSpace + SCIS pages | DSpace HTTP 503; old pages 404; round 2: Wayback copy of faculty page (no dataset links) |
| Shodhganga (INFLIBNET theses) | Round 2: DSpace 7 search API, 24 queries, 72 theses, 43 mention Telugu |
| Wayback Machine | Round 2: recovered the IIIT-H Word Recognition dataset pages (researchweb.iiit.ac.in no longer resolves) |
| Google Scholar | Round 2: redirects scripts to a bot check; covered indirectly by ~25 general web searches |
| HF datasets-server API | Round 2: Telugu row counts for 7 multilingual sets without downloading |
| ACL Anthology, JASTT, IOSR and other journal sites | Round 2: papers found through citations/search read for dataset links |
| Papers with Code archive (pwc-archive/datasets, 15,008 dataset records) | Round 3: full index filtered for Telugu and Indic OCR; nothing new |
| OpenDataLab / OpenXLab | Round 3: search API and web search; no Telugu datasets |
| B2FIND (EUDAT metadata aggregator) | Round 3: exact-phrase search; 44 hits, none OCR |
| IEEE DataPort (DataCite prefix 10.21227 + "telugu") | Round 3: all 48 records listed; every Telugu image dataset already in the CSV |
| ILOCR dataset catalogue re-probe (IDs 60-130) and competition sites | Round 3: no new Telugu pages; ICDAR 2025 MLT-RSTR found; IHDR/MLT-RSTR zips still 404 |
| Griffith CVSI-2015 site, British Library EAP, Amrita, NITK repositories | Round 3: legacy competition/archive pages and paper-only datasets |
| HP Labs / LipiTk site | Dataset page and licence read |
| CMATERdb (Jadavpur) | Telugu numeral subset confirmed |
| IHDIA (ihdia.iiit.ac.in) | Indiscapes project pages |
| BhashaSutra / Sarvam / Krutrim / Cognitive Lab / AI4Bharat | HF orgs and project pages |
| Commercial vendors: FutureBeeAI, GTS.ai, Shaip, Defined.ai | Product listings checked for Telugu OCR |
| Telugu digital collections: Internet Archive, DLI, Chandamama, AP Press Academy, GOML palm-leaf, perspectivia.net | Collection pages / search APIs |
| SSRN, ACM DL, Springer, arXiv HTML | Paper pages for dataset links (SSRN/ACM block scripts) |

In total, **50** platforms and sites were investigated (20 by API sweep, 30 directly).

## 5. ILOCR in depth

- **Dataset catalogue:** every page from `/dataset/1/` to `/dataset/200/` was requested. 62 pages are live (all at ID 69 or below), 135 return 404, and 3 return HTTP 500 (IDs 13, 14, 59; ID 14 is Mozhi-Telugu, whose zip files still download).
  Telugu pages: 23 (IIIT-INDIC-HW-WORDS-Telugu), 36 (IndicSTR12-Telugu), 40 (IIIT-Synthetic-M-Telugu), 55 (IIIT-Synthetic-R-Telugu), 68 (IIIT-Synthetic-IndicSTR-Telugu), plus 14 (Mozhi-Telugu, page broken).
- **API catalogue (`/api_list/`):** a table of 1,456 OCR **models/APIs**, not datasets. 132 rows mention Telugu: layout detection, word recognition, page pipelines and script detection from IIIT Hyderabad, IIT Bombay, IIT Delhi, IIT Jodhpur and C-DAC, plus entries for Google OCR, Tesseract, EasyOCR and Surya. The `api_detail` pages return server errors. Recorded as one related resource (TOCR-144).
- **Competition sites:** IHTR 2022 and 2023 (TOCR-004/005), ICDAR 2024 handwriting (IHWWR TOCR-007, PLHWTR TOCR-008), ICDAR 2025 IHDR (TOCR-009; Telugu zips 404), ICPR 2024 WIRIndic (TOCR-080).

## 6. Papers

- 833 paper records were screened by title and abstract (686 OpenAlex + 147 arXiv).
- 48 papers are linked from directory rows; each was opened to find the dataset link, size, licence and Telugu share.
- Citations were followed from the main hubs (IIIT-HW-Telugu, IndicSTR12, IIIT-ILST, Mozhi, IndicDLP, BSTD, Nayana, PHDIndic_11) to related releases. This turned up HW-UC, roadside IndicSTR-Word, MIST and TEXTRON.
- Round 2 added a systematic OpenAlex citation sweep (Section 7), 100 Semantic Scholar records and 72 Shodhganga theses.

## 7. Round 2 (second pass, 2026-11-11)

Round 2 went back to every channel left open after round 1 and re-checked all unconfirmed rows.

| Channel | What was run | Outcome |
|---|---|---|
| Semantic Scholar | slow re-run, 8 s pacing, back-off up to 150 s | 4/36 queries attempted, 1 answered (100 papers); Telugu dataset papers among them were already known from OpenAlex; the rest are NLP/speech |
| OpenAlex citations | 14 seed dataset papers, all citing works | Method papers only; confirmed the UHTelHwCC paper (TOCR-023) and that Indic-HW-Wild = TOCR-010; no new datasets |
| Shodhganga | 24 queries (Telugu OCR, handwriting, palm leaf, inscriptions, Indic script) | Private thesis data only; no rows |
| Web search (Google Scholar substitute) | ~25 queries on new 2025-26 datasets, digits, forms, newspapers, inscriptions, Vedic/Sanskrit, video text | CHIPS + ScrabbleGAN pages (TOCR-182/183) and PHDIndic_11 Telugu share via the PLATTER paper; GlotOCR (TOCR-184); ICON 2023 set (TOCR-187); JASTT corpus (TOCR-188); UniLipi (TOCR-189); ORB-Indic Telugu (TOCR-172 un-rejected); IIIT-H word sets (TOCR-044, 186) |
| Roboflow Universe | 4 site-restricted searches | 4 new project rows (TOCR-191..194) + TOCR-019 size |
| AIKosh | portal + JS bundle inspection (504/timeouts), 3 site-restricted searches | CATALIST rejected (no Telugu); TEXTRON mirror noted; Sanskrit post-OCR rejected |
| Bhashini ULCA | public data-metric endpoint | Telugu OCR corpora from Project Anuvaad (TOCR-208) |
| TDIL-DC | TLS retried (no bypass) + Wayback lookup | Still inaccessible |
| Kaggle | 20 broad queries x 10 pages + metadata/file lists | Palm-leaf binarisation pairs (TOCR-195), IITJ crops (TOCR-196); others had no Telugu evidence |
| Hugging Face | language:te + image/document modality listing, language:tel, 33 new search terms, datasets-server counts | BhartiOCR (TOCR-185), NayanaIR-CrossBench (TOCR-190), finepdfs (TOCR-197); Telugu counts for 7 multilingual sets |
| DataCite | every record mentioning Telugu (1,560, all types) | British Library Telugu card catalogues (TOCR-209) |
| Mendeley Data | public search API, 11 queries | No new Telugu OCR data |
| Wayback Machine | dead IIIT/UoH/TDIL pages | IIIT-H Word Recognition dataset + synthetic set recovered (downloads now 404) |
| 18 unconfirmed rows | each re-checked | TOCR-044 resolved; TOCR-098 Telugu repos listed; TOCR-102, 180, 181, 128 re-checked (still unconfirmed) |
| Multilingual sets | datasets-server statistics/filter, papers | Telugu counts for IndicVisionBench, MInfoVisQA, PMGSY boards, adaption doc-QA, ORB-Indic, PHDIndic_11; MDIW-13, Indiscapes, Kaggle Indian Scripts, IndicDLP still unknown |

### Theses on Shodhganga

21 Telugu OCR-related theses were found. Each built its own private data; none links to a public dataset, so none became a row.
Several say outright that no public Telugu dataset existed when they started.

| Year | Thesis | University / department | Handle |
|---|---|---|---|
| 2020 | Online Handwritten Character and Word Recognition in Indic scripts | Computer Science and Engineering | [10603/424094](https://shodhganga.inflibnet.ac.in/handle/10603/424094) |
| 11/11/2011 | RECOGNITION OF IMAGES AND PRINTED TELUGU CHARACTERS | Department of Physics and Computer Science | [10603/202072](https://shodhganga.inflibnet.ac.in/handle/10603/202072) |
| 2022 | A Novel Approach in Recognition of Handwritten Dravidian Characters for Secure Transmissi... | Faculty of Computer Science and Engineering | [10603/614597](https://shodhganga.inflibnet.ac.in/handle/10603/614597) |
| 2022 | A Novel Approach in Recognition of Handwrittten Dravidian Characters for Secure Transmiss... | Faculty of Computer Science and Engineering | [10603/522584](https://shodhganga.inflibnet.ac.in/handle/10603/522584) |
| n.d. | Extraction and recognition of middle zone components of telugu script using language model | Department of Electronics and Communication ... | [10603/192104](https://shodhganga.inflibnet.ac.in/handle/10603/192104) |
| 2020 | A frame work for handwritten character recognition for telugu script | Department of Computer Science and Engineeri... | [10603/331653](https://shodhganga.inflibnet.ac.in/handle/10603/331653) |
| 2018 | Pattern model for recognition of subset of Telugu characters on palm leaf scribings | Department of Electronics and Communication ... | [10603/316048](https://shodhganga.inflibnet.ac.in/handle/10603/316048) |
| n.d. | Some studies on recognition of handwritten Telugu characters | Department of Computer Science and Engineeri... | [10603/10438](https://shodhganga.inflibnet.ac.in/handle/10603/10438) |
| 29-10-2016 | Optical character recognition for telugu | Department of Electronics and Communication | [10603/129195](https://shodhganga.inflibnet.ac.in/handle/10603/129195) |
| 2018 | Pattern model for recognition of subset of Telugu characters on palm leaf scribings | Department of Electronics and Communication ... | [10603/333227](https://shodhganga.inflibnet.ac.in/handle/10603/333227) |
| 2023 | Department of computer science and engineering some adaptive approaches for handwritten c... | Department of Computer Science and Engineeri... | [10603/528873](https://shodhganga.inflibnet.ac.in/handle/10603/528873) |
| 2023 | image based telugu handwritten and printed character recognition using deep learning appr... | Department of Computer Science and  Engineer... | [10603/540129](https://shodhganga.inflibnet.ac.in/handle/10603/540129) |
| 27/11/2003 | DEVELOPMENT OF AN OPTICAL RECOGNITION SYSTEM FOR PRINTED TELUGU TEXT | Department of Physics and Computer Science | [10603/202149](https://shodhganga.inflibnet.ac.in/handle/10603/202149) |
| 2024 | recognition of telugu hand written text using deep convolutional neural networks | Department of Computer Science | [10603/694694](https://shodhganga.inflibnet.ac.in/handle/10603/694694) |
| 2009 | An investigation into Telugu font and character recognition | Department of Computer and Information Scien... | [10603/4166](https://shodhganga.inflibnet.ac.in/handle/10603/4166) |
|  | Segmentation of Telugu Text using Fringe Maps | Department of Computer and Information Scien... | [10603/312697](https://shodhganga.inflibnet.ac.in/handle/10603/312697) |
|  | An enhanced frame work for pre processing and character recognition systems suitable for ... | Department of Computer Science | [10603/203940](https://shodhganga.inflibnet.ac.in/handle/10603/203940) |
| n.d. | Some studies on recognition of handwritten Telugu Characters | Department of Computer Science and Engineeri... | [10603/124098](https://shodhganga.inflibnet.ac.in/handle/10603/124098) |
| 2023 | Printed Telugu Character Recognition System Using Augmented Convolutional Neural Network ... | Faculty of Computer Science and Engineering | [10603/614555](https://shodhganga.inflibnet.ac.in/handle/10603/614555) |
| 2025 | Investigation of Dictionary Learning Algorithms for Telugu Handwritten Character Recognit... | SCHOOL OF COMPUTER and INFORMATION SCIENCES | [10603/697931](https://shodhganga.inflibnet.ac.in/handle/10603/697931) |
| 2023 | Printed Telugu Character Recognition System using Augmented Convolutional Neural Network ... | Faculty of Computer Science and Engineering | [10603/618931](https://shodhganga.inflibnet.ac.in/handle/10603/618931) |

### Citation following (OpenAlex)

Every work citing the hub dataset papers was listed and screened (361 citing works, 79 kept for reading).
Nearly all are method papers that train on existing data or on private data they did not release; no new public dataset came from this channel.

| Seed paper | Citing works | Kept for reading |
|---|---|---|
| IIIT-INDIC-HW-WORDS (ICDAR 2021) | 42 | 12 |
| IIIT-HW-Telugu (ICFHR 2018) | 36 | 12 |
| Mozhi / Towards Deployable OCR | 11 | 3 |
| IIIT-ILST benchmark | 59 | 20 |
| IndicSTR12 | 12 | 5 |
| Konkimalla Telugu OCR database | 26 | 16 |
| UHTelPCC | 10 | 5 |
| PHDIndic_11 | 95 | 16 |
| Bharat Scene Text (BSTD) | 1 | 0 |
| PLATTER / CHIPS | 7 | 2 |
| IndicDLP | 4 | 0 |
| Indiscapes | 36 | 2 |
| HP Labs / Lipi Toolkit Telugu | - | - |
| Synthetic data for Indic STR (Synthetic-IndicSTR) | 22 | 9 |

### New rows added in round 2

| ID | Name | Category | Status | Distinct? |
|---|---|---|---|---|
| TOCR-182 | [CHIPS - Corpus of Handwritten Indic Scripts (Telugu pages)](https://arxiv.org/abs/2502.06172) | OCR image-text: handwritten | INACCESSIBLE | UNKNOWN (may be a re-composition of TOC... |
| TOCR-183 | [PLATTER ScrabbleGAN synthetic Telugu handwritten pages](https://arxiv.org/abs/2502.06172) | OCR image-text: synthetic | UNVERIFIED | UNKNOWN |
| TOCR-184 | [GlotOCR Bench - Telugu (Telu)](https://huggingface.co/datasets/cis-lmu/GlotOCR-bench) | OCR image-text: synthetic | GATED | Y |
| TOCR-185 | [BhartiOCR - Telugu](https://huggingface.co/datasets/Faizaniqbal/BhartiOCR) | OCR image-text: synthetic | GATED | Y |
| TOCR-186 | [IIIT-H Word Recognition Synthetic Dataset (Telugu)](https://web.archive.org/web/20221127093102/https://researchweb.iiit.ac.in/~pramod_sankar/CandD.html) | OCR image-text: synthetic | INACCESSIBLE | Y |
| TOCR-187 | [Multilingual multimodal scene-text dataset (NIT Silchar, IC...](https://aclanthology.org/2023.icon-1.16.pdf) | Script identification | UNVERIFIED | Y |
| TOCR-188 | [Handwritten Telugu character corpus (JASTT 2025, unreleased)](https://jastt.org/index.php/jasttpath/article/view/267) | Character / glyph classification | INACCESSIBLE | Y |
| TOCR-189 | [UniLipi historical manuscript data - Telugu script](https://ihdia.iiit.ac.in/unilipi/) | OCR image-text: handwritten | INACCESSIBLE | Y |
| TOCR-190 | [NayanaIR-CrossBench (multilingual visual document retrieval)](https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-CrossBench) | Text-in-image benchmark (VQA / document... | PARTIALLY VERIFIED | Y |
| TOCR-191 | [Roboflow Universe: iitbresearchwork/telugu-ocr](https://universe.roboflow.com/iitbresearchwork/telugu-ocr) | Layout / detection (no transcription) | UNVERIFIED | UNKNOWN |
| TOCR-192 | [Roboflow Universe: vihaveai/telugu-info-detector](https://universe.roboflow.com/vihaveai/telugu-info-detector) | Layout / detection (no transcription) | UNVERIFIED | UNKNOWN |
| TOCR-193 | [Roboflow Universe: fives-data-tpoav/telugu](https://universe.roboflow.com/fives-data-tpoav/telugu) | Script identification | UNVERIFIED | UNKNOWN |
| TOCR-194 | [Roboflow Universe: centurion-university-n60kx/telugu-handwr...](https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten-project) | Layout / detection (no transcription) | UNVERIFIED | UNKNOWN |
| TOCR-195 | [Kaggle: telugu_palm_leafs (chintuimmandi) - palm-leaf binar...](https://www.kaggle.com/datasets/chintuimmandi/telugu-palm-leafs) | Image-only (no transcription) | PARTIALLY VERIFIED | N (suspected copy of TOCR-118 data) |
| TOCR-196 | [Kaggle: IITJ Multilingual OCR Dataset (mayank7239)](https://www.kaggle.com/datasets/mayank7239/iitj-multilingual-ocr-dataset) | Image-only (transcription NOT VERIFIED) | PARTIALLY VERIFIED | N (suspected copy of TOCR-082) |
| TOCR-197 | [HuggingFaceFW/finepdfs - Telugu (tel_Telu)](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) | Text-only corpus (OCR language modellin... | PARTIALLY VERIFIED | Y |
| TOCR-198 | [SignboardText (IEEE DataPort 10.21227/5k09-4k21)](https://ieee-dataport.org/documents/signboardtext-0) | Rejected | REJECTED | N |
| TOCR-199 | [CATALIST / CATALISTd video scene text (IIT Bombay, on AIKos...](https://catalist-2021.github.io) | Rejected | REJECTED | N |
| TOCR-200 | [DohaScript handwritten Hindi (arXiv 2602.18089)](https://arxiv.org/abs/2602.18089) | Rejected | REJECTED | N |
| TOCR-201 | [IIEST-Indic-HW writer identification dataset](https://doi.org/10.1145/3774521.3774586) | Rejected | REJECTED | N |
| TOCR-202 | [EpiSAM / Shilalekhya stone-inscription datasets (IHDIA)](https://ihdia.iiit.ac.in/episam/) | Rejected | REJECTED | N |
| TOCR-203 | [arikatokachi/indic-synthetic-documents (+v2)](https://huggingface.co/datasets/arikatokachi/indic-synthetic-documents) | Rejected | REJECTED | N |
| TOCR-204 | [Nexdata 500,000 Images Multilingual OCR Dataset in 21 Langu...](https://huggingface.co/datasets/Nexdata-kr/500000-Images-Multilingual-OCR-Dataset-in-21-Languages) | Rejected | REJECTED | N |
| TOCR-205 | [DataCluster Labs Multilingual OCR Annotation Dataset (Kaggl...](https://huggingface.co/datasets/Dataclusterlabspvtltd/Multilingual_OCR_Annotation_Dataset) | Rejected | REJECTED | N |
| TOCR-206 | [A Benchmark and Dataset for Post-OCR Text Correction in San...](https://aikosh.indiaai.gov.in/home/datasets/details/a_benchmark_and_dataset_for_post_ocr_text_correction_in_sanskrit.html) | Rejected | REJECTED | N |
| TOCR-207 | [Indic-VizVQA-v2 (Kaggle armaansingh2340)](https://www.kaggle.com/datasets/armaansingh2340/indic-vizvqa-v2) | Rejected | REJECTED | N |
| TOCR-208 | [ULCA (Bhashini) OCR corpus - Telugu (Project Anuvaad)](https://bhashini.gov.in/ulca/datasets) | Machine-labelled OCR (not human ground ... | PARTIALLY VERIFIED | Y |
| TOCR-209 | [British Library AAS card catalogues: Telugu (digitised micr...](https://bl.iro.bl.uk/work/0249413b-6469-4c28-bb03-c4b3f9dd7403) | Scanned archive (image-only) | PARTIALLY VERIFIED | Y |

### Round-1 rows changed in round 2

| ID | Name | Change |
|---|---|---|
| TOCR-015 | PHDIndic_11 - Telugu pages | Telugu share found in PLATTER paper |
| TOCR-016 | TEXTRON INDIC datasets - Telugu handwritten pages | AIKosh mirror noted |
| TOCR-019 | Roboflow Universe: teluguocr/telugu-handwritten-ocr | Size from search snippet |
| TOCR-044 | IIIT-H Word Recognition Dataset (Telugu) | Resolved via archived IIIT page |
| TOCR-084 | Indic-CIB: Indic Citizen Information Board dataset | Telugu check |
| TOCR-098 | Nayana gated OCR/VQA family (Telugu configs) | Telugu repos listed from HF API |
| TOCR-102 | OCR Synthetic Benchmark Dataset for Indic Languages (EkStep... | Paper details added |
| TOCR-107 | Telugu character database (Konkimalla et al., ICIP 2018) | Size confirmed from arXiv 1711.07245 |
| TOCR-114 | Kaggle: Indian Scripts (12-script image classification) | File listing checked |
| TOCR-118 | Telugu palm-leaf binarisation dataset ("Preserving Telugu M... | Possible data release found |
| TOCR-128 | HW-MLVQA (handwritten multilingual document VQA) | Release re-checked |
| TOCR-130 | IndicVisionBench (OCR task) | Telugu share counted via HF API |
| TOCR-131 | MInfoVisQA (multilingual infographic VQA) | Telugu share counted via HF API |
| TOCR-132 | adaption-multilingual-doc-qa (magazines VQA remaster) | Telugu share counted via HF API |
| TOCR-134 | indic-citizen-information-board-pmgsy | Telugu rows found (earlier note was wrong) |
| TOCR-148 | Telugu Unicode fonts (Noto, Pothana2000, Vemana, Google Fon... | Kaggle font upload noted |
| TOCR-172 | ORB-Indic (krutrim-ai-labs/ocr_rotation_bench) - Telugu pag... | Un-rejected: Telugu confirmed in paper |
| TOCR-180 | Kaggle: rs synth indic data (ocrteamriad) | Files checked |
| TOCR-181 | Kaggle: OCR Stress Test v2 Multilingual Benchmark (harishk2... | Files checked |

## 8. Rejected candidates

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
| TOCR-173 | [Shaip OCR training data](https://www.shaip.com/solutions/optical-character-recognition-ocr-machine-learning/) | Custom-collection vendor page; no Telugu OCR product listed. |
| TOCR-174 | [GitHub UthejKaramalapudi/Handwritten_Charcater_Classificaition_For_Te...](https://github.com/UthejKaramalapudi/Handwritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images) | Code only; no images in repository. |
| TOCR-175 | [GitHub Harathi123/Telugu-Character-Recognition-using-CNN](https://github.com/Harathi123/Telugu-Character-Recognition-using-CNN) | Reuses HP Labs data (TOCR-021); no new data. |
| TOCR-176 | [GitHub alfahimmohammad/Telugu-Handwritten-Text-Recognition](https://github.com/alfahimmohammad/Telugu-Handwritten-Text-Recognition) | Reuses CVIT IIIT-HW-Telugu (TOCR-001); no new data. |
| TOCR-177 | [GitHub jaganmohanreddy2106/Telugu-Handwritten-Digit-Recognition](https://github.com/jaganmohanreddy2106/Telugu-Handwritten-Digit-Recognition) | 10 example digit images only; no dataset. |
| TOCR-178 | [Telugu Alphabets 52-letter chart (Zenodo 20079705)](https://doi.org/10.5281/zenodo.20079705) | Single educational chart image; record now HTTP 410 (removed). |
| TOCR-179 | [Telugu NLP / news / lyrics Kaggle sets (text-only, non-OCR)](https://www.kaggle.com/datasets/sudalairajkumar/telugu-nlp) | Text classification/NLP corpora surfaced by Kaggle search; not OCR and not needed as OCR LM sources. |
| TOCR-198 | [SignboardText (IEEE DataPort 10.21227/5k09-4k21)](https://ieee-dataport.org/documents/signboardtext-0) | Vietnamese/English signboards (UIT, VNU-HCM); surfaced in Telugu scene-text searches but has no Telugu. |
| TOCR-199 | [CATALIST / CATALISTd video scene text (IIT Bombay, on AIKosh)](https://catalist-2021.github.io) | English, Hindi and Marathi only. |
| TOCR-200 | [DohaScript handwritten Hindi (arXiv 2602.18089)](https://arxiv.org/abs/2602.18089) | Hindi only. |
| TOCR-201 | [IIEST-Indic-HW writer identification dataset](https://doi.org/10.1145/3774521.3774586) | Bengali and Hindi only. |
| TOCR-202 | [EpiSAM / Shilalekhya stone-inscription datasets (IHDIA)](https://ihdia.iiit.ac.in/episam/) | Single Indic script not named; no Telugu evidence on project pages or HF card. |
| TOCR-203 | [arikatokachi/indic-synthetic-documents (+v2)](https://huggingface.co/datasets/arikatokachi/indic-synthetic-documents) | Languages en, bn, hi, ta only (folders and tags). |
| TOCR-204 | [Nexdata 500,000 Images Multilingual OCR Dataset in 21 Languages](https://huggingface.co/datasets/Nexdata-kr/500000-Images-Multilingual-OCR-Dataset-in-21-Languages) | Commercial sample; listed languages do not include Telugu. |
| TOCR-205 | [DataCluster Labs Multilingual OCR Annotation Dataset (Kaggle + HF)](https://huggingface.co/datasets/Dataclusterlabspvtltd/Multilingual_OCR_Annotation_Dataset) | Vendor sample with he/th/ja/ar; no Telugu files. |
| TOCR-206 | [A Benchmark and Dataset for Post-OCR Text Correction in Sanskrit (AIK...](https://aikosh.indiaai.gov.in/home/datasets/details/a_benchmark_and_dataset_for_post_ocr_text_correction_in_sanskrit.html) | Sanskrit text only (Devanagari); no Telugu. |
| TOCR-207 | [Indic-VizVQA-v2 (Kaggle armaansingh2340)](https://www.kaggle.com/datasets/armaansingh2340/indic-vizvqa-v2) | Translated VizWiz/VQAv2 questions; images are not text-centric. |
| TOCR-231 | [HKS-NVC: Handwritten Kadamba Script numerals, vowels, consonants (IEE...](https://doi.org/10.21227/nhvr-w717) | Kadamba script (ancestor of Kannada-Telugu), not Telugu. |
| TOCR-232 | [GitHub NamineniBrahmani/multilingual-ocr](https://github.com/NamineniBrahmani/multilingual-ocr) | Six scripts (Nandinagari, Malayalam, Kannada, Devanagari, Sarada, Bengali); no Telugu folder. |
| TOCR-233 | [GitHub bitreaper42/DC_Indic scene-text evaluation set](https://github.com/bitreaper42/DC_Indic) | ground_truth.json has only English and Hindi regions. |
| TOCR-234 | [GitHub darshanrao/Ancient-Hand-Writtten-Recognition-Under-Data-Defici...](https://github.com/darshanrao/Ancient-Hand-Writtten-Recognition-Under-Data-Deficiency) | Tamil and Sanskrit data only. |
| TOCR-235 | [HASOC 2025 multimodal meme task (FIRE 2025)](https://ceur-ws.org/Vol-4173/) | Hindi, Gujarati, Bangla and Bodo memes; no Telugu. |
| TOCR-236 | [Synbols synthetic glyph datasets (ServiceNow)](https://github.com/ServiceNow/synbols) | No Telugu alphabet in the generator (code search 2026-11-11). |
| TOCR-237 | [Tamil handwritten palm-leaf manuscript dataset (THPLMD)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10864864/) | Tamil only; surfaces in Telugu palm-leaf searches. |
| TOCR-238 | [Hamburg palm-leaf manuscript word datasets (fdr.uni-hamburg.de)](https://b2find.eudat.eu/dataset/f0497ec0-a60f-5710-96b4-2bf9adef6f56) | Tamil manuscripts; no Telugu. |
| TOCR-239 | [IIST BCI Telugu datasets (EEG; IEEE DataPort)](https://doi.org/10.21227/32qq-c421) | Brain-signal recordings of Telugu speech/commands, not images. |

Beyond these 44 rows, several hundred search hits were discarded during screening without a row, for example
Telugu text-only NLP sets, speech sets, and Telugu-tagged HF sets with no images. The `hf_screen.json` and
`platform_candidates.txt` files in `evidence/discovery/` keep the screening decisions.

## 9. Round 3 (adversarial completeness pass, 2026-11-11)

Round 3 assumed an independent reviewer would search for Telugu OCR data and tried to find anything they could find that the CSV lacked.
Full details, including a reviewer cross-check table, are in [ADVERSARIAL_COMPLETENESS_AUDIT.md](ADVERSARIAL_COMPLETENESS_AUDIT.md).

| Pass | What was searched | Outcome |
|---|---|---|
| A. Institutions | IIIT-H/CVIT + ILOCR re-probe, UoH, IIT Bombay, IIT Madras, IISc MILE, C-DAC, NLTM/Bhashini, TDIL, AIKosh, Amrita, NITK, Telugu-state universities | ICDAR 2025 MLT-RSTR (TOCR-213), Amrita palm-leaf DB (212), Rasagna thesis sets (216), NITK memes (214); AIKosh/TDIL still unreachable |
| B. Papers | Crossref (20 queries, 2,516 records), OpenAlex citations (round 2), DataCite IEEE prefix sweep, arXiv/ACL pages, ICDAR/ICFHR competition reports | CVSI-2015 (210), meme datasets (215, 217, 218), handwritten script-ID sets (219, 220); UHTelPCC size; TOCR-108 conflict recorded |
| C. Platforms | HF full paginated listing (14 listings, 70,298 datasets), GitHub all-pages search (27 queries, 1,470 repos, 476 file trees), PwC archive, OpenDataLab, B2FIND, Roboflow, Kaggle (round 2) | rendered_wikipedia_te (221), NayanaIR-MonoBench-te (222), tiny CAPTCHA (223), 7 GitHub data repos (224-230); 4 GitHub repos rejected |
| D. Legacy / obscure | Wayback Machine, archived author pages, older competitions (CVSI 2015), British Library EAP, TDIL references in READMEs, palm-leaf and inscription searches | EAP038 Telugu books/periodicals (211); TDIL toolid 1892 lead; Tamil palm-leaf sets rejected |
| Reviewer simulation | 14 likely reviewer searches; every dataset-like result mapped to a row | 34/34 dataset results already/now in the CSV |

### New rows added in round 3

| ID | Name | Category | Status | Distinct? |
|---|---|---|---|---|
| TOCR-210 | [CVSI-2015 - ICDAR 2015 Competition on Video Script Identifi...](https://www.ict.griffith.edu.au/cvsi2015/Dataset.php) | Script identification | PARTIALLY VERIFIED | Y |
| TOCR-211 | [British Library Endangered Archives EAP038 - pre-1947 Telug...](https://eap.bl.uk/project/EAP038) | Scanned archive (image-only) | PARTIALLY VERIFIED | Y |
| TOCR-212 | [Telugu palm-leaf character database (Amrita, 2012)](https://www.amrita.edu/publication/a-data-acquisition-and-analysis-system-for-palm-leaf-documents-in-telugu/) | Character / glyph classification | UNVERIFIED | UNKNOWN |
| TOCR-213 | [ICDAR 2025 Competition on Multi-lingual Roadside Scene Text...](https://ilocr.iiit.ac.in/icdar_2025_MLT-RSTR/dataset.html) | OCR image-text: scene text | INACCESSIBLE | UNKNOWN (suspected same collection as T... |
| TOCR-214 | [Telugu Meme Dataset (domain and troll identification, NITK)](https://doi.org/10.1007/978-3-031-58495-4_2) | Image-only (transcription NOT VERIFIED) | UNVERIFIED | Y |
| TOCR-215 | [LT-EDI 2024 shared task: troll meme classification - Telugu](https://aclanthology.org/2024.ltedi-1.13.pdf) | Image-only (transcription NOT VERIFIED) | UNVERIFIED | N (suspected same data as TOCR-214) |
| TOCR-216 | [IIIT Telugu document test sets (Rasagna 2013 MS thesis)](https://cvit.iiit.ac.in/research/thesis/thesis-students/studies-in-recognition-of-telugu-document-images) | OCR image-text: printed | UNVERIFIED | UNKNOWN |
| TOCR-217 | [TelMeMood - multimodal Telugu meme sentiment dataset](https://doi.org/10.1109/isacc65211.2025.10969246) | Image-only (transcription NOT VERIFIED) | UNVERIFIED | Y |
| TOCR-218 | [Benchmark dataset for hateful memes detection in Telugu](https://doi.org/10.1007/978-3-032-13803-3_27) | Image-only (transcription NOT VERIFIED) | UNVERIFIED | Y |
| TOCR-219 | [Handwritten Indic script identification data (offline + onl...](https://arxiv.org/abs/1802.08568) | Script identification | UNVERIFIED | UNKNOWN |
| TOCR-220 | [Handwritten script identification text lines (Singh et al.,...](https://arxiv.org/abs/2009.07433) | Script identification | UNVERIFIED | UNKNOWN |
| TOCR-221 | [stefania-radu/rendered_wikipedia_te (rendered Telugu Wikipe...](https://huggingface.co/datasets/stefania-radu/rendered_wikipedia_te) | Image-only (no transcription) | VERIFIED | Y |
| TOCR-222 | [NayanaIR-MonoBench-te (Telugu visual document retrieval)](https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-MonoBench-te) | Text-in-image benchmark (VQA / document... | VERIFIED | Y |
| TOCR-223 | [Tiny Multilingual CAPTCHA Library - Telugu (remiai3/tiny-ca...](https://huggingface.co/datasets/remiai3/tiny-captcha-library) | OCR image-text: synthetic | VERIFIED | N (smaller release of TOCR-101 generato... |
| TOCR-224 | [GitHub medini-r/teluguChar (copy of HP Labs offline Telugu ...](https://github.com/medini-r/teluguChar) | Character / glyph classification | VERIFIED | N (mirror of TOCR-021) |
| TOCR-225 | [GitHub madhav007VDEV/telugu-ocr-realtime - character image ...](https://github.com/madhav007VDEV/telugu-ocr-realtime) | Character / glyph classification | PARTIALLY VERIFIED | Y |
| TOCR-226 | [GitHub ntbnaren7/telugu-fra-synthesizer - synthetic Telugu ...](https://github.com/ntbnaren7/telugu-fra-synthesizer) | Image-only (transcription NOT VERIFIED) | PARTIALLY VERIFIED | Y |
| TOCR-227 | [GitHub pavankarthik1/Telugu-Hand-Written-character-recognit...](https://github.com/pavankarthik1/Telugu-Hand-Written-character-recognition) | Image-only (transcription NOT VERIFIED) | PARTIALLY VERIFIED | Y |
| TOCR-228 | [GitHub keerthan-381 - Telugu palm-leaf handwritten characte...](https://github.com/keerthan-381/HandWritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images) | Character / glyph classification | PARTIALLY VERIFIED | Y |
| TOCR-229 | [GitHub aceveggie/TeluguTFRecords - Telugu character data in...](https://github.com/aceveggie/TeluguTFRecords) | Character / glyph classification | PARTIALLY VERIFIED | UNKNOWN |
| TOCR-230 | [GitHub Saisugandhasri - binarised Telugu character images (...](https://github.com/Saisugandhasri/A-novel-unsupervised-contrastive-learning-framework-for-Telugu-script-character-dataset-construction) | Image-only (no transcription) | PARTIALLY VERIFIED | Y |
| TOCR-231 | [HKS-NVC: Handwritten Kadamba Script numerals, vowels, conso...](https://doi.org/10.21227/nhvr-w717) | Rejected | REJECTED | N |
| TOCR-232 | [GitHub NamineniBrahmani/multilingual-ocr](https://github.com/NamineniBrahmani/multilingual-ocr) | Rejected | REJECTED | N |
| TOCR-233 | [GitHub bitreaper42/DC_Indic scene-text evaluation set](https://github.com/bitreaper42/DC_Indic) | Rejected | REJECTED | N |
| TOCR-234 | [GitHub darshanrao/Ancient-Hand-Writtten-Recognition-Under-D...](https://github.com/darshanrao/Ancient-Hand-Writtten-Recognition-Under-Data-Deficiency) | Rejected | REJECTED | N |
| TOCR-235 | [HASOC 2025 multimodal meme task (FIRE 2025)](https://ceur-ws.org/Vol-4173/) | Rejected | REJECTED | N |
| TOCR-236 | [Synbols synthetic glyph datasets (ServiceNow)](https://github.com/ServiceNow/synbols) | Rejected | REJECTED | N |
| TOCR-237 | [Tamil handwritten palm-leaf manuscript dataset (THPLMD)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10864864/) | Rejected | REJECTED | N |
| TOCR-238 | [Hamburg palm-leaf manuscript word datasets (fdr.uni-hamburg...](https://b2find.eudat.eu/dataset/f0497ec0-a60f-5710-96b4-2bf9adef6f56) | Rejected | REJECTED | N |
| TOCR-239 | [IIST BCI Telugu datasets (EEG; IEEE DataPort)](https://doi.org/10.21227/32qq-c421) | Rejected | REJECTED | N |

### Earlier rows changed in round 3

| ID | Name | Change |
|---|---|---|
| TOCR-009 | ICDAR 2025 IHDR Telugu (Indic Handwritten Document Recognit... | Links re-checked |
| TOCR-018 | GitHub JayanthKalluri/TeluguWordRecognizer - "handwritten_t... | Related repo found |
| TOCR-021 | HPL Isolated Handwritten Telugu Character Dataset (HP Labs ... | LipiTk index page added |
| TOCR-027 | Handwritten Telugu Gunintam క (Ka) | Working landing page and size found |
| TOCR-038 | GitHub axlevisu/CNN-Telugu-OCR data folder | Identified as compilation |
| TOCR-041 | Mozhi-Telugu (printed word images) | Internal page set noted |
| TOCR-047 | UHTelPCC: Telugu Printed Character Dataset (University of H... | Size from paper abstract |
| TOCR-106 | chaitusvk/telugu_ocr_multi_line - generated line images | Related repo found |
| TOCR-108 | "OCR Telugu Image Dataset" (IEEE DataPort a1kv-rj60) | Conflicting descriptions recorded |
| TOCR-113 | MDIW-13 - Multi-lingual Document Image database for script ... | IEEE DataPort copies noted |
| TOCR-174 | GitHub UthejKaramalapudi/Handwritten_Charcater_Classificait... | Related repo found |

## 10. Channels still open

- **Semantic Scholar** - partly done: 4 of 36 planned queries attempted and 1 answered before the run was stopped (repeated HTTP 429). Re-run with an API key.
- **Google Scholar** - blocks scripts; covered only through general web searches.
- **IEEE Xplore / Springer / Elsevier full text** - paywalled. Only abstracts and open versions were read, so dataset links inside paywalled papers may be missed.
- **AIKosh full listing** - the portal timed out (HTTP 504 / no response) in rounds 2 and 3; pages were found through web search only.
- **TDIL-DC** - certificate expired, not bypassed. The Telugu image corpus there is unconfirmed.
- **Roboflow Universe** - blocks scripts; 8 Telugu projects are known from search snippets only (sizes and classes unconfirmed).
- **Small GitHub archives** - a few student repos hold RAR/ZIP/CSV character data whose contents were not inspected (see MISSING_DATASET_CANDIDATES.csv).
- **ULCA downloads** - the two Telugu OCR corpora are listed, but downloading needs a login and a search request.
- **Institutional repositories beyond Shodhganga** (university DSpace sites) - only UoH was checked.
- **Direct contact with authors** - not done. CHIPS, UniLipi, the JASTT corpus, UHTelPCC/UHTelHwCC, the Telugu meme datasets and other unreleased sets could probably be requested by email.
