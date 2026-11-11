# Adversarial completeness audit

**Question:** if an independent reviewer searches for Telugu OCR datasets, will everything they find already be in
[`telugu_ocr_final.csv`](../../telugu_ocr_final.csv)? Round 3 (2026-11-11) tried to answer that by attacking the catalogue from four
independent directions and by simulating the reviewer's own searches.

**Bottom line:** distinct datasets went from 92 (round 1) to 104 (round 2) to **115** now, in **239** rows.
Round 3 added 30 rows (12 new distinct datasets, the rest copies, unconfirmed leads or rejections)
and corrected 11 earlier rows.
Of the 34 dataset-type results returned by 14 simulated reviewer searches, **34** map to a row in the CSV.

## 1. Discovery channels investigated

| Pass | What was searched | Outcome |
|---|---|---|
| A. Institutions | IIIT-H/CVIT + ILOCR re-probe, UoH, IIT Bombay, IIT Madras, IISc MILE, C-DAC, NLTM/Bhashini, TDIL, AIKosh, Amrita, NITK, Telugu-state universities | ICDAR 2025 MLT-RSTR (TOCR-213), Amrita palm-leaf DB (212), Rasagna thesis sets (216), NITK memes (214); AIKosh/TDIL still unreachable |
| B. Papers | Crossref (20 queries, 2,516 records), OpenAlex citations (round 2), DataCite IEEE prefix sweep, arXiv/ACL pages, ICDAR/ICFHR competition reports | CVSI-2015 (210), meme datasets (215, 217, 218), handwritten script-ID sets (219, 220); UHTelPCC size; TOCR-108 conflict recorded |
| C. Platforms | HF full paginated listing (14 listings, 70,298 datasets), GitHub all-pages search (27 queries, 1,470 repos, 476 file trees), PwC archive, OpenDataLab, B2FIND, Roboflow, Kaggle (round 2) | rendered_wikipedia_te (221), NayanaIR-MonoBench-te (222), tiny CAPTCHA (223), 7 GitHub data repos (224-230); 4 GitHub repos rejected |
| D. Legacy / obscure | Wayback Machine, archived author pages, older competitions (CVSI 2015), British Library EAP, TDIL references in READMEs, palm-leaf and inscription searches | EAP038 Telugu books/periodicals (211); TDIL toolid 1892 lead; Tamil palm-leaf sets rejected |
| Reviewer simulation | 14 likely reviewer searches; every dataset-like result mapped to a row | 34/34 dataset results already/now in the CSV |

Earlier rounds (see [DISCOVERY_LOG.md](DISCOVERY_LOG.md)) covered Hugging Face, Kaggle, GitHub, Zenodo, Figshare, DataCite, Dataverse,
Internet Archive, OpenAlex, arXiv, Semantic Scholar (partial), Mendeley, Shodhganga, OpenAlex citations, ILOCR, CVIT, ULCA, AIKosh (via search),
Roboflow (via search) and the Wayback Machine. In total **50** platforms and sites have been investigated.

## 2. Search queries and sources used in round 3

- **Simulated reviewer searches (14):** Telugu OCR dataset; Telugu handwritten dataset download; Telugu text recognition dataset github; Telugu OCR dataset huggingface; Telugu character recognition dataset; Telugu scene text recognition dataset; Telugu palm leaf manuscript dataset; video script identification dataset CVSI 2015 Telugu; Telugu online handwriting dataset; Telugu newspaper digitization archive; ICDAR competition Indic scene text Telugu; Telugu handwritten documents pages transcription; Telugu OCR benchmark VLM; Telugu memes dataset.
- **Hugging Face full listing:** search=telugu (533); search=Telugu (533); search=tel_ (3,164); search=-te- (60,000); search=_te_ (60,000); search=indic (3,852); search=ocr (2,376); search=handwrit (284); search=scene-text (12); search=scene_text (12); search=text-recognition (38); search=document (1,319); filter=language:te (1,148); filter=language:tel (204). Every page was followed up to 60 pages per listing (only the noisy -te-/_te_ substring listings reached that cap); 70,298 datasets screened by tags and names.
- **GitHub (all result pages, up to the 1,000-result API cap):** telugu; telugu ocr; telugu handwritten; telugu handwriting; telugu character recognition; telugu dataset; telugu-ocr in:name; telugu text recognition; telugu scene text; telugu palm leaf; telugu manuscript; telugu digits; telugu letters; telugu alphabet; telugu word recognition; telugu printed; telugu script; indic ocr dataset; indic handwritten dataset; indian language ocr dataset; telugu inscription; telugu newspaper ocr; telugu synthetic; tesseract telugu; telugu crnn; telugu trocr; telugu htr. 1,470 repositories; file trees of 476 OCR-related repos checked for images, labels and archives.
- **Crossref:** telugu dataset handwritten; telugu character recognition dataset; telugu ocr dataset; telugu printed character dataset; telugu handwritten database; telugu word images dataset; telugu scene text dataset; telugu palm leaf dataset; telugu manuscript dataset; telugu document images; indic handwritten dataset; indic scene text dataset; indic ocr benchmark; indian scripts handwritten database; multi-script document database indian; telugu numerals dataset; telugu online handwriting; telugu text recognition; telugu script identification; telugu inscription recognition (2,516 records).
- **Other web searches:** institution names (IIT Bombay/AIKosh, C-DAC, IISc MILE, IIT Madras, Andhra/JNTU/IIIT Sri City/NIT Warangal), legacy terms (CVSI 2015, video script identification, online handwriting, palm leaf, inscriptions, newspapers digitisation, TDIL), meme datasets, handwritten documents/answer sheets, VLM OCR benchmarks.
- **Archives:** Papers with Code archive (15,008 dataset records), OpenDataLab, B2FIND, Wayback Machine (IIIT, UoH, TDIL, EAP pages).

## 3. Reviewer cross-check

Each result URL returned by the simulated reviewer searches, and where it sits in the CSV. "-" means the URL itself is not a row
(papers, models, demos and screened-out non-Telugu sets); the note says why.

| Reviewer query | Result URL | Kind | In CSV as | Note |
|---|---|---|---|---|
| Telugu OCR dataset | https://arxiv.org/pdf/1711.07245 | paper | - | Paper of TOCR-107 (Konkimalla et al. database) |
| Telugu OCR dataset | https://dspace.uohyd.ac.in/handle/1/8703 | dataset | TOCR-047 |  |
| Telugu OCR dataset | https://ieee-dataport.org/documents/ocr-telugu-image-dataset | dataset | TOCR-108 |  |
| Telugu OCR dataset | https://universe.roboflow.com/iitbresearchwork/telugu-ocr | dataset | TOCR-191 |  |
| Telugu OCR dataset | https://tickets-felicity.iiit.ac.in/images/Thesis/MS/Venkat_Rasagna_2013/Rasagn... | paper | - | Thesis test sets recorded as TOCR-216 |
| Telugu OCR dataset | https://ilocr.iiit.ac.in/dataset/40/ | dataset | TOCR-086 |  |
| Telugu OCR dataset | https://huggingface.co/harsha-desaraju/telugu-ocr-model | model | - | Model trained on TOCR-051/093; pipeline listed as TOCR-153 |
| Telugu OCR dataset | https://universe.roboflow.com/teluguocr/telugu-handwritten-ocr | dataset | TOCR-019 |  |
| Telugu OCR dataset | https://gts.ai/dataset-download/telugu-document-image-dataset/ | dataset | TOCR-096 |  |
| Telugu OCR dataset | https://huggingface.co/CharanS247/got-ocr2-telugu-handwritten | model | - | LoRA adapter trained on IIIT-HW-Telugu (TOCR-001/002); a model, not data |
| Telugu OCR dataset | https://www.github.com/ChillarAnand/likitham | dataset | TOCR-069 |  |
| Telugu OCR dataset | https://www.alphaxiv.org/abs/2104.04437 | paper | - | Paper of IIIT-ILST (TOCR-070) |
| Telugu handwritten dataset download | https://lipitk.sourceforge.net/datasets/teluguchardata.htm | dataset | TOCR-021 |  |
| Telugu handwritten dataset download | https://ieee-dataport.org/open-access/telugu-handwritten-character-dataset | dataset | TOCR-024 |  |
| Telugu handwritten dataset download | https://dspace.uohyd.ac.in/handle/1/8547 | dataset | TOCR-022 |  |
| Telugu handwritten dataset download | https://data.mendeley.com/datasets/mpjbr7nfv9 | dataset | TOCR-031 |  |
| Telugu handwritten dataset download | https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-indic-hw-words | dataset | TOCR-003 |  |
| Telugu handwritten dataset download | https://cvit.iiit.ac.in/research/projects/cvit-projects/indic-hw-data | dataset | TOCR-001 |  |
| Telugu handwritten dataset download | https://ieee-dataport.org/documents/telugu-handwritten-vowels | dataset | TOCR-026 |  |
| Telugu handwritten dataset download | https://ilocr.iiit.ac.in/icdar_2025_Indic_HDR/dataset.html | dataset | TOCR-009 |  |
| Telugu handwritten dataset download | https://ilocr.iiit.ac.in/dataset/23 | dataset | TOCR-002 |  |
| Telugu handwritten dataset download | https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten-pro... | dataset | TOCR-194 |  |
| Telugu handwritten dataset download | https://www.tensorflow.org/datasets/catalog/cmaterdb | dataset | TOCR-032 | TFDS copy of CMATERdb (TOCR-032) |
| Telugu text recognition dataset github | https://arxiv.org/pdf/2205.06740 | paper | - | Paper of Mozhi (TOCR-041) |
| Telugu text recognition dataset github | https://researchweb.iiit.ac.in/~pramod_sankar/CandD.html | dataset | TOCR-044, TOCR-186 | Archived copy linked from TOCR-044 and TOCR-186 |
| Telugu OCR dataset huggingface | https://huggingface.co/collections/gksriharsha/textline-ocr-data-662db1de52e194... | page | - | Collection containing only gksriharsha/chitralekha (TOCR-092) |
| Telugu OCR dataset huggingface | https://huggingface.co/spaces/Vipplav/telugu_ocr_test | tool | - | Demo Space, not data |
| Telugu character recognition dataset | https://ieee-dataport.org/documents/3d-telugu-character-recognition | dataset | TOCR-154 |  |
| Telugu character recognition dataset | https://link.springer.com/chapter/10.1007/978-981-13-9187-3_3 | paper | - | Paper of UHTelPCC (TOCR-047) |
| Telugu scene text recognition dataset | https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-ilst | dataset | TOCR-070 |  |
| Telugu scene text recognition dataset | https://ilocr.iiit.ac.in/dataset/68/ | dataset | TOCR-088 |  |
| Telugu scene text recognition dataset | https://cvit.iiit.ac.in/research/projects/cvit-projects/indicstr | dataset | TOCR-071, TOCR-089 | Project page of IndicSTR12 (TOCR-071) |
| Telugu palm leaf manuscript dataset | https://www.amrita.edu/publication/a-data-acquisition-and-analysis-system-for-p... | paper | TOCR-212 | Recorded as TOCR-212 |
| Telugu palm leaf manuscript dataset | https://www.griet.ac.in/images/1-s2.0-S2215098616303627-main.pdf | paper | TOCR-120 | Paper of TOCR-120 |
| Telugu palm leaf manuscript dataset | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10864864/ | dataset | TOCR-237 | Tamil palm-leaf set (THPLMD); no Telugu - screened out |
| Telugu palm leaf manuscript dataset | https://b2find.eudat.eu/dataset/f0497ec0-a60f-5710-96b4-2bf9adef6f56 | dataset | TOCR-238 | Hamburg palm-leaf word sets (Tamil manuscripts); no Telugu - screened out |
| video script identification dataset CVS... | https://www.ict.griffith.edu.au/cvsi2015/Dataset.php | dataset | TOCR-210 |  |
| Telugu online handwriting dataset | https://lipitk.sourceforge.net/hpl-datasets.htm | dataset | TOCR-021 |  |
| Telugu online handwriting dataset | https://biotech.iitm.ac.in/faculty_website/CNS_LAB/OHwCR.html | page | - | IIT Madras online Telugu HWR project page; no dataset released - screened out |
| Telugu newspaper digitization archive | https://eap.bl.uk/project/EAP038 | dataset | TOCR-211 |  |
| ICDAR competition Indic scene text Telu... | https://ilocr.iiit.ac.in/icpr_2024_wirindic/dataset.html | dataset | TOCR-080 |  |
| ICDAR competition Indic scene text Telu... | https://ilocr.iiit.ac.in/icdar_2025_MLT-RSTR/ | dataset | TOCR-213 |  |
| Telugu handwritten documents pages tran... | https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html | dataset | TOCR-007, TOCR-008 |  |
| Telugu OCR benchmark VLM | https://huggingface.co/datasets/krutrim-ai-labs/IndicVisionBench | dataset | TOCR-130 |  |
| Telugu OCR benchmark VLM | https://www.sarvam.ai/blogs/Sarvam-vision | page | - | Blog for Sarvam Indic OCR Bench (TOCR-059) |
| Telugu memes dataset | https://doi.org/10.1007/978-3-031-58495-4_2 | dataset | TOCR-214 |  |
| Telugu memes dataset | https://doi.org/10.1109/isacc65211.2025.10969246 | dataset | TOCR-217 |  |

## 4. Newly discovered datasets (round 3)

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

## 5. Why these were missed before

- **API caps:** round-1 Hugging Face searches stopped at 200 results per query and GitHub searches at the first page; the full listings in round 3 found the rendered Wikipedia, NayanaIR-MonoBench-te and tiny-CAPTCHA sets and seven small GitHub data repos.
- **Query scope:** meme datasets and video-frame script identification (CVSI 2015) do not use the words "OCR" or "handwritten", so earlier query lists did not reach them.
- **No Crossref pass before round 3:** Crossref surfaced the Springer/IEEE meme dataset papers.
- **Legacy material:** the British Library EAP038 Telugu print archive and the Amrita palm-leaf database are only described on institutional pages.

## 6. Existing catalogue errors corrected

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

Earlier corrections (rounds 1-2) are listed in [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md) and in the `Round 2 change` column.

## 7. Unresolved leads

[MISSING_DATASET_CANDIDATES.csv](MISSING_DATASET_CANDIDATES.csv) lists **49** candidates: 37 are already rows in the master
CSV but unconfirmed (status UNVERIFIED, an unreleased announcement, or unknown distinctness), and 12 are leads that are not rows
because nothing confirms they are Telugu image data. It is a supporting file; the master remains `telugu_ocr_final.csv`.

## 8. Inaccessible, gated and commercial sources

| ID | Dataset | Status | Reason |
|---|---|---|---|
| TOCR-009 | ICDAR 2025 IHDR Telugu (Indic Handwritten Document Recognit... | INACCESSIBLE | Telugu zips redirect to cdn.iiit.ac.in and return HTTP 404 (re-checked 2026-11-11); charlist zip still downlo... |
| TOCR-012 | FutureBeeAI Telugu Handwritten Sticky Notes OCR Image Datas... | COMMERCIAL | Paid |
| TOCR-013 | FutureBeeAI Telugu Shopping List OCR Image Dataset | COMMERCIAL | Paid |
| TOCR-015 | PHDIndic_11 - Telugu pages | GATED | Gated (login) |
| TOCR-022 | Offline Handwritten Telugu Characters (Negi & M Rao, Univer... | GATED | Gated (login) |
| TOCR-024 | Telugu Handwritten Character Dataset (Velpuru et al.) | GATED | Gated |
| TOCR-026 | Telugu Handwritten Vowels (Muppalaneni et al.) | GATED | Gated |
| TOCR-027 | Handwritten Telugu Gunintam క (Ka) | GATED | DOI target 404s but ieee-dataport.org/node/1880 resolves (301) to the listing; login needed for files |
| TOCR-028 | AsTel - Offline Assamese and Telugu Handwritten Characters | GATED | Gated (page HTTP 403 to scripts) |
| TOCR-039 | GitHub srikarym/OCR_Telugu_code - final_dataset.hdf5 (Googl... | INACCESSIBLE | Drive link returns HTTP 404 (2026-11-11) |
| TOCR-040 | GitHub Mitradatta/Telugu-Character-Recognition - self-colle... | INACCESSIBLE | Data not public (repo has README only) |
| TOCR-044 | IIIT-H Word Recognition Dataset (Telugu) | INACCESSIBLE | Download 404; page only on the Wayback Machine |
| TOCR-046 | Telugu Image Corpus - OCR (TDIL / C-DAC Noida OCR Consortiu... | INACCESSIBLE | Site TLS certificate expired (2026-11-11); page not readable |
| TOCR-047 | UHTelPCC: Telugu Printed Character Dataset (University of H... | INACCESSIBLE | Project page 404; repository 503 |
| TOCR-062 | OCR-Bench1000-Telugu | GATED | Gated (manual) |
| TOCR-065 | FutureBeeAI Telugu Newspaper, Magazine and Books OCR Image ... | COMMERCIAL | Paid |
| TOCR-066 | FutureBeeAI Telugu Product Image OCR Dataset | COMMERCIAL | Paid |
| TOCR-083 | HF gated copy: Bhashini-IITJ/Bharat-Scene-Text-Dataset | GATED | Gated (auto) |
| TOCR-098 | Nayana gated OCR/VQA family (Telugu configs) | GATED | Gated (manual) |
| TOCR-108 | "OCR Telugu Image Dataset" (IEEE DataPort a1kv-rj60) | GATED | Gated |
| TOCR-109 | IndicDLP - Telugu pages (document layout parsing) | GATED | Gated on HF; AIKosh/Zenodo routes |
| TOCR-138 | CulturaX - Telugu | GATED | Gated on HF (login + accept terms, automatic) |
| TOCR-182 | CHIPS - Corpus of Handwritten Indic Scripts (Telugu pages) | INACCESSIBLE | No dataset link on arXiv, GitHub or HF (checked 2026-11-11) |
| TOCR-184 | GlotOCR Bench - Telugu (Telu) | GATED | Gated (automatic) |
| TOCR-185 | BhartiOCR - Telugu | GATED | Gated (manual) |
| TOCR-186 | IIIT-H Word Recognition Synthetic Dataset (Telugu) | INACCESSIBLE | Download 404; page only on the Wayback Machine (researchweb.iiit.ac.in no longer resolves) |
| TOCR-188 | Handwritten Telugu character corpus (JASTT 2025, unreleased) | INACCESSIBLE | Announced for later release |
| TOCR-189 | UniLipi historical manuscript data - Telugu script | INACCESSIBLE | Project page dataset link is a "coming soon" placeholder (2026-11-11) |
| TOCR-213 | ICDAR 2025 Competition on Multi-lingual Roadside Scene Text... | INACCESSIBLE | All validation/test zips HTTP 404 (2026-11-11); Telugu charlist downloads |

Channels that blocked or failed: AIKosh (HTTP 504 / no response, rounds 2-3), TDIL-DC (expired TLS certificate, not bypassed), Roboflow
and IEEE DataPort pages (HTTP 403 to scripts; metadata via search and DataCite), Semantic Scholar (HTTP 429), Google Scholar (bot check).

## 9. Duplicate and derivative relationships

82 relationship pairs are recorded (details in [DUPLICATE_AND_MIRROR_REPORT.md](DUPLICATE_AND_MIRROR_REPORT.md)); 42 dataset rows
are mirrors, copies, subsets or compilations and are excluded from the distinct count.

## 10. Remaining discovery gaps

- AIKosh's full catalogue (including IIT Bombay's script datasets) could not be listed.
- TDIL-DC resources (Telugu image corpus TOCR-046, toolid 1892) remain unreachable without bypassing TLS.
- Roboflow project sizes/classes are known only from search snippets.
- Paywalled full texts (IEEE Xplore, Springer, Elsevier) were read only as abstracts.
- Semantic Scholar was only partly searched; Google Scholar only indirectly.
- Small student archives on GitHub (RAR/ZIP/CSV) were not opened.
- No authors were contacted; announced datasets (CHIPS, UniLipi, JASTT corpus, meme sets, UHTelPCC/UHTelHwCC) stay unconfirmed.

## 11. Readiness for independent cross-verification

- **Well defended:** anything findable through Hugging Face, Kaggle, GitHub, Zenodo, Figshare, DataCite/IEEE DataPort, Mendeley, ILOCR/CVIT,
  arXiv/OpenAlex/Crossref or a general web search for Telugu OCR/handwriting/scene-text/character datasets. All 34 dataset results of the
  simulated reviewer searches resolve to rows.
- **Partly defended:** portal-only sources (AIKosh, TDIL, Roboflow), paper-only datasets that were never released, and theses.
- **Honest limit:** the catalogue cannot prove that no dataset exists elsewhere. A reviewer who finds a dataset in the gaps above should
  add it via `scripts/entries_e.py` and re-run `build_directory.py`, `make_docs.py` and `validate_directory.py`.
