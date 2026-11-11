# Unavailable and gated datasets

Datasets that cannot simply be downloaded. Checked on 2026-11-11. No access control was bypassed: no TLS
verification was disabled, no logins were made, and no request forms were submitted.

## Gated (login, form or approval needed) - 11

These exist and can usually be obtained. The "How to get it" column gives the procedure.

| ID | Dataset | Category | Telugu size | How to get it | What we saw |
|---|---|---|---|---|---|
| TOCR-015 | [PHDIndic_11 - Telugu pages](https://ieee-dataport.org/open-access/phdindic11-page-level-handwritten-document-image-dataset-11-official-indic-scripts) | Script identification | 1,458 pages total; Telugu share NOT VERIFIED | Free IEEE DataPort account | Gated (login) |
| TOCR-022 | [Offline Handwritten Telugu Characters (Negi & M Rao, Univer...](https://ieee-dataport.org/documents/offline-handwritten-telugu-characters) | Character / glyph classification | 913 sheets x ~90 characters (~82,000 characters); 937 classes | Free IEEE DataPort account | Gated (login) |
| TOCR-024 | [Telugu Handwritten Character Dataset (Velpuru et al.)](https://ieee-dataport.org/open-access/telugu-handwritten-character-dataset) | Character / glyph classification | UNKNOWN sample count (335.47 MB; up to 1,924 character classes descri... | IEEE DataPort subscription/login | Gated |
| TOCR-026 | [Telugu Handwritten Vowels (Muppalaneni et al.)](https://ieee-dataport.org/documents/telugu-handwritten-vowels) | Character / glyph classification | 1,116 (train 875 / test 241) | IEEE DataPort login | Gated |
| TOCR-028 | [AsTel - Offline Assamese and Telugu Handwritten Characters](https://ieee-dataport.org/documents/astel-offline-assamese-and-telugu-handwritten-characters) | Character / glyph classification | 625 Telugu classes (sample count NOT VERIFIED) | IEEE DataPort login | Gated (page HTTP 403 to scripts) |
| TOCR-062 | [OCR-Bench1000-Telugu](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Telugu) | OCR image-text: printed | 1K-10K (HF size category) | HF login + manual approval | Gated (manual) |
| TOCR-083 | [HF gated copy: Bhashini-IITJ/Bharat-Scene-Text-Dataset](https://huggingface.co/datasets/Bhashini-IITJ/Bharat-Scene-Text-Dataset) | OCR image-text: scene text | See TOCR-082 | HF login + accept terms | Gated (auto) |
| TOCR-098 | [Nayana gated OCR/VQA family (Telugu configs)](https://huggingface.co/Nayana-cognitivelab) | OCR image-text: synthetic | UNKNOWN per repo (HF size categories 1K-1M) | HF login + manual approval | Gated (manual) |
| TOCR-108 | ["OCR Telugu Image Dataset" (IEEE DataPort a1kv-rj60)](https://ieee-dataport.org/documents/ocr-telugu-image-dataset) | Character / glyph classification | UNKNOWN (abstract cites 6,757,044 train / 972,309 val) | IEEE DataPort login | Gated |
| TOCR-109 | [IndicDLP - Telugu pages (document layout parsing)](https://cvit.iiit.ac.in/research/projects/cvit-projects/indicdlp) | Layout / detection (no transcription) | 119,806 total; Telugu 7.2% (~8,600 pages, computed from README share) | HF: login + accept terms; AIKosh download | Gated on HF; AIKosh/Zenodo routes |
| TOCR-138 | [CulturaX - Telugu](https://huggingface.co/datasets/uonlp/CulturaX) | Text-only corpus (OCR language modellin... | UNKNOWN (gated) | HF account + accept terms | Gated on HF (login + accept terms, automatic) |

## Inaccessible (broken links or never released) - 6

Links were tried on the check date. Contacting the authors is the only route for most of these.

| ID | Dataset | Category | Telugu size | How to get it | What we saw |
|---|---|---|---|---|---|
| TOCR-009 | [ICDAR 2025 IHDR Telugu (Indic Handwritten Document Recognit...](https://ilocr.iiit.ac.in/icdar_2025_Indic_HDR/dataset.html) | OCR image-text: handwritten | UNKNOWN (10,000 pages across 10 languages per site) | Contact organisers | Telugu zips HTTP 404 (checked 2026-11-10); charlist zip still downloads |
| TOCR-027 | [Handwritten Telugu Gunintam క (Ka)](https://doi.org/10.21227/phg6-m127) | Character / glyph classification | UNKNOWN | IEEE DataPort login | Both DOIs redirect (HTTP 302) to the IEEE landing page, which returns 404 (2026-11-11); m... |
| TOCR-039 | [GitHub srikarym/OCR_Telugu_code - final_dataset.hdf5 (Googl...](https://github.com/srikarym/OCR_Telugu_code) | Character / glyph classification | UNKNOWN | Google Drive link | Drive link returns HTTP 404 (2026-11-11) |
| TOCR-040 | [GitHub Mitradatta/Telugu-Character-Recognition - self-colle...](https://github.com/Mitradatta/Telugu-Character-Recognition) | Character / glyph classification | ~250 per character (claimed) | Not released | Data not public (repo has README only) |
| TOCR-046 | [Telugu Image Corpus - OCR (TDIL / C-DAC Noida OCR Consortiu...](https://tdil-dc.in/index.php?lang=en&option=com_download&task=showresourceDetails&toolid=264) | Image-only (transcription NOT VERIFIED) | 500 (search-snippet description) | TDIL registration (reported) | Site TLS certificate expired (2026-11-11); page not readable |
| TOCR-047 | [UHTelPCC: Telugu Printed Character Dataset (University of H...](http://scis.uohyd.ac.in/~chakcs/UHTelPCC.html) | Character / glyph classification | UNKNOWN | Contact authors | Project page 404; repository 503 |

## Commercial (sold by vendors) - 4

Only samples or product pages are public. Licence and price are set per purchase.

| ID | Dataset | Category | Telugu size | How to get it | What we saw |
|---|---|---|---|---|---|
| TOCR-012 | [FutureBeeAI Telugu Handwritten Sticky Notes OCR Image Datas...](https://www.futurebeeai.com/dataset/ocr-dataset/telugu-sticky-notes-ocr-image-dataset) | Image-only (no transcription) | 2,000+ (vendor claim) | Purchase / sales contact | Paid |
| TOCR-013 | [FutureBeeAI Telugu Shopping List OCR Image Dataset](https://www.futurebeeai.com/dataset/ocr-dataset/telugu-shopping-list-ocr-image-dataset) | Image-only (no transcription) | 2,000+ (vendor claim) | Purchase | Paid |
| TOCR-065 | [FutureBeeAI Telugu Newspaper, Magazine and Books OCR Image ...](https://www.futurebeeai.com/dataset/ocr-dataset/telugu-newspaper-book-magazine-ocr-image-dataset) | Image-only (no transcription) | 5,000 (vendor claim) | Purchase | Paid |
| TOCR-066 | [FutureBeeAI Telugu Product Image OCR Dataset](https://www.futurebeeai.com/dataset/ocr-dataset/telugu-product-image-ocr-dataset) | Image-only (no transcription) | 2,000 (vendor claim) | Purchase | Paid |

## Unverified (mentioned in papers or READMEs, no public data confirmed) - 17

Leads worth chasing, but nothing confirms the data is available.

| ID | Dataset | Category | Telugu size | How to get it | What we saw |
|---|---|---|---|---|---|
| TOCR-018 | [GitHub JayanthKalluri/TeluguWordRecognizer - "handwritten_t...](https://github.com/JayanthKalluri/TeluguWordRecognizer) | Image-only (transcription NOT VERIFIED) | UNKNOWN | Google Drive link | Not checked (Drive folder) |
| TOCR-019 | [Roboflow Universe: teluguocr/telugu-handwritten-ocr](https://universe.roboflow.com/teluguocr/telugu-handwritten-ocr) | Layout / detection (no transcription) | UNKNOWN | Roboflow account | Page returns HTTP 403 to automated clients |
| TOCR-020 | [Roboflow Universe: centurion-university-n60kx/telugu-handwr...](https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten) | Layout / detection (no transcription) | UNKNOWN | Roboflow account | HTTP 403 to automated clients |
| TOCR-023 | [UHTelHwCC: Telugu off-line handwritten character dataset (U...](https://doi.org/10.1007/978-3-031-07005-1_22) | Character / glyph classification | UNKNOWN | Contact authors | No public download found |
| TOCR-037 | [Telugu letters dataset (645 classes; IJRES 2024)](https://zenodo.org/records/10530992) | Character / glyph classification | 645 classes; sample count UNKNOWN | Contact authors | Only the article is deposited (Zenodo); no data files |
| TOCR-043 | [Multilingual OCR for Indic Scripts - printed page corpus (M...](https://doi.org/10.1109/DAS.2016.68) | OCR image-text: printed | UNKNOWN | UNKNOWN | No public release found |
| TOCR-044 | IIIT Telugu book collection (Pramod Sankar, Jawahar, Manmat... | OCR image-text: printed | 33 books | UNKNOWN | No public release found |
| TOCR-045 | [Building Data Sets for Indian Language OCR Research (annota...](https://doi.org/10.1007/978-1-84800-330-9_1) | OCR image-text: printed | UNKNOWN | UNKNOWN | No public release found |
| TOCR-064 | [Telugu document image classification set (Ramu, 2025)](https://zenodo.org/records/16778120) | Image-only (no transcription) | 1,000 (per paper) | Contact author | Article only |
| TOCR-102 | [OCR Synthetic Benchmark Dataset for Indic Languages (EkStep...](https://arxiv.org/abs/2205.02543) | OCR image-text: synthetic | 90K total; Telugu share UNKNOWN | UNKNOWN | No download link found |
| TOCR-107 | [Telugu character database (Konkimalla et al., ICIP 2018)](https://arxiv.org/abs/1711.07245) | Character / glyph classification | 17,387 classes; 6,757,044 train + 972,309 val (+test) | UNKNOWN | Original data location not found |
| TOCR-120 | [Telugu palm-leaf 3D character dataset (2016 paper)](https://www.griet.ac.in/images/1-s2.0-S2215098616303627-main.pdf) | Character / glyph classification | UNKNOWN | Contact authors | No public release found |
| TOCR-121 | [Transcription of Benjamin Schultze's Telugu-English Convers...](https://perspectivia.net/receive/pnet_mods_00006709) | Text-only corpus (OCR language modellin... | UNKNOWN | None | Landing page served a bot check to scripts |
| TOCR-128 | [HW-MLVQA (handwritten multilingual document VQA)](https://arxiv.org/abs/2507.15655) | Text-in-image benchmark (VQA / document... | 1,600 pages total; Telugu UNKNOWN | UNKNOWN | No dataset link in paper HTML |
| TOCR-143 | [On-line Handwriting Recognition of Indian Scripts - The Fir...](https://dblp.org/rec/conf/icfhr/MondalBPDM10) | Character / glyph classification | UNKNOWN | UNKNOWN | No release found |
| TOCR-180 | [Kaggle: rs synth indic data (ocrteamriad)](https://www.kaggle.com/datasets/ocrteamriad/rs-synth-indic-data) | OCR image-text: synthetic | 23,294 MB of TFRecords | Kaggle account | Open listing |
| TOCR-181 | [Kaggle: OCR Stress Test v2 Multilingual Benchmark (harishk2...](https://www.kaggle.com/datasets/harishk2209/ocr-stress-test-v2) | OCR image-text: printed | 183.6 MB | Kaggle account | Open listing |

## Link check

Every URL in the CSV was requested once with a HEAD request (or, if that failed, a 1 KB ranged GET).
337 links (241 unique) were checked. 19 did not return 2xx/3xx.
HTTP 403 from IEEE DataPort, Roboflow, SSRN and ACM is bot-blocking: those pages open in a normal browser,
and their metadata was confirmed through DataCite or search instead. Full results: `evidence/link_check.csv`.

| ID | Field | URL | Result |
|---|---|---|---|
| TOCR-010 | Research paper URL | https://doi.org/10.1145/3774521.3774605 | 403 |
| TOCR-011 | Official webpage URL | https://ieee-dataport.org/documents/assamese-and-telugu-handwritten-text-dataset | 403 |
| TOCR-019 | Official webpage URL | https://universe.roboflow.com/teluguocr/telugu-handwritten-ocr | 403 |
| TOCR-020 | Official webpage URL | https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten | 403 |
| TOCR-022 | Zenodo / Figshare / archive URL | https://dspace.uohyd.ac.in/handle/1/8547 | 503 |
| TOCR-026 | Research paper URL | https://doi.org/10.3138/jmbs-27676-sujjuri | 403 |
| TOCR-027 | Official webpage URL | https://doi.org/10.21227/phg6-m127 | 404 |
| TOCR-028 | Official webpage URL | https://ieee-dataport.org/documents/astel-offline-assamese-and-telugu-handwritten-charact... | 403 |
| TOCR-039 | Direct download URL | https://drive.google.com/file/d/1ucYy_Emht9MRLjQPaUydSKZzN1ZQ77dd/view | 404 |
| TOCR-041 | Zenodo / Figshare / archive URL | https://ilocr.iiit.ac.in/dataset/14/ | 500 |
| TOCR-046 | Official webpage URL | https://tdil-dc.in/index.php?lang=en&option=com_download&task=showresourceDetails&toolid=... | ERR URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILE... |
| TOCR-047 | Official webpage URL | http://scis.uohyd.ac.in/~chakcs/UHTelPCC.html | 404 |
| TOCR-047 | Zenodo / Figshare / archive URL | https://dspace.uohyd.ac.in/handle/1/8703 | 503 |
| TOCR-109 | Direct download URL | https://aikosh.indiaai.gov.in/home/datasets/details/indicdlp.html | ERR TimeoutError: The read operation timed out |
| TOCR-118 | Research paper URL | https://doi.org/10.2139/ssrn.4903434 | 403 |
| TOCR-126 | Official webpage URL | https://pressacademyarchives.ap.nic.in/ | ERR URLError: <urlopen error [Errno -5] No address associat... |
| TOCR-146 | Official webpage URL | https://aikosh.indiaai.gov.in/home/datasets | ERR TimeoutError: The read operation timed out |
| TOCR-159 | Official webpage URL | https://rrc.cvc.uab.es/?ch=15 | ERR URLError: <urlopen error [Errno -2] Name or service not... |
| TOCR-178 | Official webpage URL | https://doi.org/10.5281/zenodo.20079705 | 410 |
