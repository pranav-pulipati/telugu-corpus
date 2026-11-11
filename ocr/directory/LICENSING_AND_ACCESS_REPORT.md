# Licensing and access report

What each dataset's licence allows, based on what the source itself states. Checked on 2026-11-11.
This is not legal advice. When a licence is missing, it is recorded as unknown and the data should be treated as
"all rights reserved" until the owner says otherwise.

## Summary by licence group

Grouped automatically from the `Licence` column (dataset rows only; related resources and rejected rows excluded).

| Licence group | Dataset rows | Distinct datasets | Distinct image-text OCR datasets |
|---|---|---|---|
| Open (CC BY / CC0 / MIT / Apache / PD) | 54 | 37 | 11 |
| Open, share-alike (CC BY-SA) | 7 | 5 | 2 |
| No derivatives (CC BY-ND) | 1 | 1 | 0 |
| Non-commercial only (CC BY-NC family) | 8 | 6 | 4 |
| Copyleft software licence (GPL) | 3 | 2 | 1 |
| Research / academic use terms | 6 | 5 | 2 |
| Commercial / vendor | 4 | 4 | 0 |
| Copyrighted source material (no licence) | 5 | 4 | 2 |
| Unknown / not stated | 57 | 28 | 8 |

## Access requirements

| What you need | Dataset rows |
|---|---|
| None (open download) | 85 |
| Kaggle account | 18 |
| Login / accept terms (HF, IEEE) | 16 |
| Other / unknown | 16 |
| Contact authors / request | 7 |
| Purchase | 3 |

## Licence problems found

- **Conflicting licences on the same data.** GTS.ai's Zenodo record (TOCR-096) says CC BY 4.0, but the Kaggle original it re-lists (TOCR-095) says CC BY-NC 4.0. Follow the stricter original.
- **IndicSTR12 (TOCR-071).** The ILOCR page states CC BY 4.0 for the annotations. The paper is CC BY-NC-ND, and the photos are third-party images. The existing catalogue (TEL-OCR-003) still says the data licence is unknown.
- **ILOCR datasets.** The ILOCR pages for HW-WORDS (TOCR-002) and IndicSTR12 (TOCR-072) state CC BY 4.0. The three IIIT-Synthetic pages (TOCR-086/087/088) have **no licence section**, so their licence is unknown. The competition sites say only "freely available for academic and research purposes", which is narrower.
- **Mirrors often drop the licence.** Kaggle and HF re-uploads of IIIT data usually say "Unknown" or add their own licence. The original's licence still applies.
- **Machine-labelled sets.** Sets labelled by Gemini or other models (for example TOCR-063) may also fall under the model provider's terms.
- **Scanned archives.** Newspaper, magazine and Chandamama scans (TOCR-124, 127, 129) carry the publishers' copyright even though they are freely viewable. Internet Archive items vary item by item.
- **Wikisource-derived sets** (TOCR-049 to 057) inherit CC BY-SA from the text. Their page scans are usually public-domain books, but each file's own licence should be checked (the acquisition phase found 127,326 of 134,015 pages on free scans).
- **No licence at all.** Most GitHub and Kaggle personal uploads state no licence (57 dataset rows are in the unknown group).

## Detail by licence group

### Open (CC BY / CC0 / MIT / Apache / PD) (54)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-002 | [IIIT-INDIC-HW-WORDS-Telugu (ILOCR v0.5)](https://ilocr.iiit.ac.in/dataset/23/) | CC BY 4.0 (stated on dataset page) | Allowed with attribution | Allowed with attribution | None |
| TOCR-003 | [IIIT-INDIC-HW-WORDS (multi-script umbrella)](https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-indic-hw-words) | NOT STATED on CVIT page (ILOCR per-language pages: CC BY 4.0) | UNKNOWN | UNKNOWN | None |
| TOCR-010 | [IIIT-INDIC-HW-WILD Telugu (SemiHastakshar unlabelled c...](https://lalithaevani.github.io/SemiHastakshar-page/) | CC BY 4.0 for own images; source terms for rebuilt crops | Allowed for own images | Allowed for own images | None |
| TOCR-011 | [Assamese and Telugu Handwritten Text Dataset](https://ieee-dataport.org/documents/assamese-and-telugu-handwritten-text-dataset) | CC BY 4.0 (DataCite) | Allowed with attribution | Allowed with attribution | IEEE DataPort account (login to download) |
| TOCR-015 | [PHDIndic_11 - Telugu pages](https://ieee-dataport.org/open-access/phdindic11-page-level-handwritten-document-image-dataset-11-official-indic-scripts) | Creative Commons Attribution (IEEE page) | Allowed with attribution | Allowed with attribution | Free IEEE DataPort account |
| TOCR-022 | [Offline Handwritten Telugu Characters (Negi & M Rao, U...](https://ieee-dataport.org/documents/offline-handwritten-telugu-characters) | Creative Commons Attribution (IEEE page) | Allowed with attribution | Allowed with attribution | Free IEEE DataPort account |
| TOCR-024 | [Telugu Handwritten Character Dataset (Velpuru et al.)](https://ieee-dataport.org/open-access/telugu-handwritten-character-dataset) | CC BY 4.0 (DataCite) | Allowed with attribution | Allowed with attribution | IEEE DataPort subscription/login |
| TOCR-025 | [Kaggle: "Final Dataset of Telugu Handwritten Character...](https://www.kaggle.com/datasets/sarath02003/telugu-handwritten) | Unknown / Apache-2.0 (sarath02003) / Unknown - original licence not s... | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-026 | [Telugu Handwritten Vowels (Muppalaneni et al.)](https://ieee-dataport.org/documents/telugu-handwritten-vowels) | Creative Commons Attribution (DataCite) | Allowed with attribution | Allowed with attribution | IEEE DataPort login |
| TOCR-027 | [Handwritten Telugu Gunintam క (Ka)](https://doi.org/10.21227/phg6-m127) | Creative Commons Attribution (DataCite) | Allowed with attribution | Allowed with attribution | IEEE DataPort login |
| TOCR-028 | [AsTel - Offline Assamese and Telugu Handwritten Charac...](https://ieee-dataport.org/documents/astel-offline-assamese-and-telugu-handwritten-characters) | CC BY 4.0 (DataCite) | Allowed with attribution | Allowed with attribution | IEEE DataPort login |
| TOCR-029 | [Handwritten Telugu Alphabet Dataset: Vowels and Conson...](https://ieee-dataport.org/documents/handwritten-telugu-alphabet-dataset-vowels-and-consonants-varnamala-ocr-and-pattern) | CC BY 4.0 (DataCite) | Allowed with attribution | Allowed with attribution | IEEE DataPort login |
| TOCR-030 | [Sapta Lipi HCR: Handwritten Character Dataset for Seve...](https://data.mendeley.com/datasets/r5vjyykm3x/1) | CC BY 4.0 | Allowed with attribution | Allowed with attribution | None |
| TOCR-032 | [CMATERdb 3.4.1 - Handwritten Telugu Numerals](https://www.tensorflow.org/datasets/catalog/cmaterdb) | NOT STATED by original; GitHub mirror says Apache-2.0 | UNKNOWN | UNKNOWN | None |
| TOCR-037 | [Telugu letters dataset (645 classes; IJRES 2024)](https://zenodo.org/records/10530992) | Article CC BY 4.0; data licence UNKNOWN | UNKNOWN | UNKNOWN | Contact authors |
| TOCR-041 | [Mozhi-Telugu (printed word images)](https://cvit.iiit.ac.in/usodi/tdocrmil.php) | CC BY 4.0 (stated on all other-language Mozhi pages; Telugu page brok... | Allowed with attribution (inferred) | Allowed with attribution (inferred) | None |
| TOCR-053 | [harsha-desaraju/telugu-line-text-image](https://huggingface.co/datasets/harsha-desaraju/telugu-line-text-image) | MIT tag (source books not licensed by uploader) | UNKNOWN | UNKNOWN | None |
| TOCR-054 | [harsha-desaraju/Telugu-book-text-images](https://huggingface.co/datasets/harsha-desaraju/Telugu-book-text-images) | MIT tag (source books modern; rights unclear) | UNKNOWN | UNKNOWN | None |
| TOCR-055 | [harsha-desaraju/telugu-book-line-images (+ -sample)](https://huggingface.co/datasets/harsha-desaraju/telugu-book-line-images) | MIT tag (rights of books unclear) | UNKNOWN | UNKNOWN | None |
| TOCR-057 | [harsha-desaraju/telugu-pdf-line-image-text](https://huggingface.co/datasets/harsha-desaraju/telugu-pdf-line-image-text) | MIT tag | UNKNOWN | UNKNOWN | None |
| TOCR-059 | [Sarvam Indic OCR Bench - Telugu](https://huggingface.co/datasets/sarvamai/indic-ocr-bench) | Apache-2.0 (HF tag) | Allowed by tag (source documents h... | Allowed by tag | None |
| TOCR-060 | [IndicDLP block-level OCR eval set (Telugu)](https://huggingface.co/datasets/onath/indicdlp-eval-set-22-sample) | CC BY 4.0 (sample) | Allowed (sample) | Allowed (sample) | Full set private; sample open |
| TOCR-062 | [OCR-Bench1000-Telugu](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Telugu) | MIT (HF tag) | Allowed by tag | Allowed by tag | HF login + manual approval |
| TOCR-064 | [Telugu document image classification set (Ramu, 2025)](https://zenodo.org/records/16778120) | Article CC BY 4.0; data UNKNOWN | UNKNOWN | UNKNOWN | Contact author |
| TOCR-068 | [GitHub Pumapumapumas/ml-class-project - scanned Telugu...](https://github.com/Pumapumapumas/ml-class-project) | MIT (repo) | Allowed by repo licence (page righ... | UNKNOWN | None |
| TOCR-072 | [IndicSTR12-Telugu (ILOCR v0.5)](https://ilocr.iiit.ac.in/dataset/36/) | CC BY 4.0 (stated on page) | Annotations allowed; image rights ... | Annotations allowed | None |
| TOCR-073 | [HF mirror/derivative: darknight054/indicstr12-crops](https://huggingface.co/datasets/darknight054/indicstr12-crops) | As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply | UNKNOWN | UNKNOWN | None |
| TOCR-074 | [HF mirror/derivative: darknight054/indicstr12-full](https://huggingface.co/datasets/darknight054/indicstr12-full) | As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply | UNKNOWN | UNKNOWN | None |
| TOCR-075 | [HF mirror/derivative: ananya12k/INDICSTR12_REAL_IMAGES](https://huggingface.co/datasets/ananya12k/INDICSTR12_REAL_IMAGES) | As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply | UNKNOWN | UNKNOWN | None |
| TOCR-076 | [HF mirror/derivative: jai23023/indicstr12-signboards (...](https://huggingface.co/datasets/jai23023/indicstr12-signboards) | As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply | UNKNOWN | UNKNOWN | None |
| TOCR-077 | [Kaggle mirror: IndicSTR12 Indic Scene Text Recognition...](https://www.kaggle.com/datasets/prathmeshzade/indicstr12-indic-scene-text-recognition) | MIT (Kaggle tag; upstream terms apply) | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-082 | [Bharat Scene Text Dataset (BSTD)](https://github.com/Bhashini-IITJ/BharatSceneTextDataset) | Apache-2.0 (repository; no separate data licence) | Likely allowed | Likely allowed | None (Google Drive) |
| TOCR-084 | [Indic-CIB: Indic Citizen Information Board dataset](https://huggingface.co/datasets/Litap007/indic-citizen-information-board) | Apache-2.0 | Allowed by tag | Allowed by tag | None |
| TOCR-090 | [Kaggle mirror: telugu scene text iiit (+ -val) (gottum...](https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-scene-text-iiit) | Apache-2.0 tag (not the uploader's to grant) | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-091 | [Kaggle mirror (mislabelled): "telugu handwritten datas...](https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-handwritten-dataset) | Apache-2.0 tag (not the uploader's to grant) | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-092 | [Chitralekha - synthetic Telugu word images](https://huggingface.co/datasets/gksriharsha/chitralekha) | MIT | Allowed | Allowed | None |
| TOCR-093 | [harsha-desaraju/telugu-synthetic-line-images](https://huggingface.co/datasets/harsha-desaraju/telugu-synthetic-line-images) | MIT | Allowed | Allowed | None |
| TOCR-100 | [Synthdog-Multilingual-100 - Telugu](https://huggingface.co/datasets/WueNLP/Synthdog-Multilingual-100) | Apache-2.0 | Allowed | Allowed | None |
| TOCR-101 | [Synthetic captchas library - Telugu 4-character](https://huggingface.co/datasets/remiai3/synthetic-captchas-library) | CC BY 4.0 | Allowed | Allowed | None |
| TOCR-102 | [OCR Synthetic Benchmark Dataset for Indic Languages (E...](https://arxiv.org/abs/2205.02543) | Paper CC BY 4.0; data UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| TOCR-103 | [Kaggle: Final_Telugu_Manuscript_Data (yvenkatasriramre...](https://www.kaggle.com/datasets/yvenkatasriramreddy/final-telugu-manuscript-data) | CC0-1.0 | Allowed | Allowed | Kaggle account |
| TOCR-104 | [banti_training (Telugu OCR glyph training data)](https://github.com/rakeshvar/banti_training) | None stated (code repos Apache-2.0) | UNKNOWN | UNKNOWN | None |
| TOCR-108 | ["OCR Telugu Image Dataset" (IEEE DataPort a1kv-rj60)](https://ieee-dataport.org/documents/ocr-telugu-image-dataset) | CC BY 4.0 (DataCite) | As stated | As stated | IEEE DataPort login |
| TOCR-109 | [IndicDLP - Telugu pages (document layout parsing)](https://cvit.iiit.ac.in/research/projects/cvit-projects/indicdlp) | MIT (repo) / CC BY 4.0 (Zenodo) | Allowed | Allowed | HF: login + accept terms; AIKosh download |
| TOCR-110 | [onath/dlp-sample (IndicDLP sample, telugu config)](https://huggingface.co/datasets/onath/dlp-sample) | CC BY 4.0 | Allowed | Allowed | None |
| TOCR-112 | [MUSTARD - Telugu tables (table structure recognition)](https://huggingface.co/datasets/badrivishalk/MUSTARD) | MIT | Allowed | Allowed | None |
| TOCR-113 | [MDIW-13 - Multi-lingual Document Image database for sc...](https://doi.org/10.5281/zenodo.6376096) | CC BY 4.0 | Allowed | Allowed | None |
| TOCR-114 | [Kaggle: Indian Scripts (12-script image classification)](https://www.kaggle.com/datasets/abhisheksubhashswami/indian-scripts) | CC0-1.0 | Allowed | Allowed | Kaggle account |
| TOCR-116 | [lipika-eval (font/script identification images)](https://huggingface.co/datasets/loopdesk-ai/lipika-eval) | Apache-2.0 | Allowed | Allowed | None |
| TOCR-117 | [Telugu Palm Leaf Manuscripts (GOML Chennai scans on In...](https://archive.org/details/telugu-palm-leaf) | Public Domain Mark 1.0 | Allowed | Allowed | None |
| TOCR-132 | [adaption-multilingual-doc-qa (magazines VQA remaster)](https://huggingface.co/datasets/Reubencf/adaption-multilingual-doc-qa) | CC BY 4.0 | Allowed | Allowed | None |
| TOCR-134 | [indic-citizen-information-board-pmgsy](https://huggingface.co/datasets/Litap007/indic-citizen-information-board-pmgsy) | CC BY 4.0 | Allowed | Allowed | None |
| TOCR-136 | [Sangraha - Telugu](https://huggingface.co/datasets/ai4bharat/sangraha) | CC BY 4.0 | See licence | See licence | None (CulturaX gated) |
| TOCR-137 | [IndicCorp v2 - Telugu](https://huggingface.co/datasets/ai4bharat/IndicCorpV2) | CC0 1.0 (per README) | See licence | See licence | None (CulturaX gated) |

### Open, share-alike (CC BY-SA) (7)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-049 | [Telugu Wikisource - proofread and validated page scans](https://te.wikisource.org/) | Text CC BY-SA 4.0; scans per file (1,146 of 1,231 free) | Allowed (share-alike) for free sca... | Allowed (share-alike) | None (API/dumps; bulk image fetch needs a po... |
| TOCR-050 | [AlbertoChestnut/telugu-ocr](https://huggingface.co/datasets/AlbertoChestnut/telugu-ocr) | CC BY-SA 4.0 | Allowed (share-alike) | Allowed (share-alike) | None |
| TOCR-051 | [harsha-desaraju/telugu-wikisource-text-images](https://huggingface.co/datasets/harsha-desaraju/telugu-wikisource-text-images) | CC BY-SA 4.0 | Allowed (share-alike) | Allowed (share-alike) | None |
| TOCR-052 | [harsha-desaraju/telugu-line-ocr-bench](https://huggingface.co/datasets/harsha-desaraju/telugu-line-ocr-bench) | CC BY-SA 4.0 | Allowed (share-alike) | Allowed (share-alike) | None |
| TOCR-133 | [nvidia/miracl-vision - Telugu](https://huggingface.co/datasets/nvidia/miracl-vision) | CC BY-SA 4.0 | Allowed (share-alike) | Allowed (share-alike) | None |
| TOCR-135 | [Telugu Wikisource text dump (wikimedia/wikisource 2023...](https://huggingface.co/datasets/wikimedia/wikisource) | CC BY-SA 3.0 / GFDL (HF tag); live Wikisource text is CC BY-SA 4.0 | See licence | See licence | None (CulturaX gated) |
| TOCR-139 | [Telugu Wikipedia dumps (tewiki)](https://dumps.wikimedia.org/tewiki/latest/) | CC BY-SA 4.0 | See licence | See licence | None (CulturaX gated) |

### No derivatives (CC BY-ND) (1)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-121 | [Transcription of Benjamin Schultze's Telugu-English Co...](https://perspectivia.net/receive/pnet_mods_00006709) | CC BY-ND 4.0 (DataCite) | Allowed (no derivatives) | Allowed (no derivatives) | None |

### Non-commercial only (CC BY-NC family) (8)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-014 | [IIITS-THDB (IIIT Sri City Telugu Handwriting Database)](https://chrizandr.github.io/IIITS-THDB/) | Non-commercial research and education only (project page) | Not allowed | NOT ALLOWED | None stated |
| TOCR-031 | [Handwritten Notations of Digits and Fractions in Telug...](https://data.mendeley.com/datasets/mpjbr7nfv9/1) | CC BY-NC-SA 4.0 | Not allowed | Allowed (non-commercial, share-ali... | None |
| TOCR-061 | [NayanaOCRBench Natural - Telugu](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Natural) | CC BY-NC 4.0 | Not allowed | Allowed (non-commercial) | None |
| TOCR-071 | [IndicSTR12 real (CVIT release, all 12 languages)](https://cvit.iiit.ac.in/research/projects/cvit-projects/indicstr) | CC BY 4.0 on annotations (ILOCR page); paper CC BY-NC-ND; images thir... | Risky (image rights) | Annotations yes; images unclear | None |
| TOCR-095 | [Telugu Document Image-Text Pairs (amancapy/telugu-scan...](https://www.kaggle.com/datasets/amancapy/telugu-scans) | CC BY-NC 4.0 (Kaggle) | Not allowed | Allowed (non-commercial) | Kaggle account |
| TOCR-096 | [GTS.ai "Telugu Document Image Dataset" (and Zenodo bro...](https://gts.ai/dataset-download/telugu-document-image-dataset/) | CC BY 4.0 claimed on Zenodo - conflicts with original CC BY-NC 4.0 | Treat as non-commercial (original ... | See original | Links to Kaggle |
| TOCR-097 | [NayanaOCR Corpus 2025 - Telugu](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025) | CC BY-NC 4.0 | Not allowed | Allowed (non-commercial) | None |
| TOCR-098 | [Nayana gated OCR/VQA family (Telugu configs)](https://huggingface.co/Nayana-cognitivelab) | Mostly none declared / CC BY-NC (OCRBench) | UNKNOWN | UNKNOWN | HF login + manual approval |

### Copyleft software licence (GPL) (3)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-016 | [TEXTRON INDIC datasets - Telugu handwritten pages](https://huggingface.co/datasets/badrivishalk/TEXTRON_INDIC_DATASETS) | GPL-3.0 (HF tag) | Allowed under GPL | Allowed under GPL | None |
| TOCR-035 | [Kaggle: Telugu Vowel Dataset (6 vowels)](https://www.kaggle.com/datasets/syamkakarla/telugu-6-vowel-dataset) | GPL-2.0 (Kaggle) | Allowed under GPL | Allowed under GPL | Kaggle account |
| TOCR-105 | [Telugu_OCR_Tesseract_Training (font box/tif training f...](https://github.com/saikrishnawanted/Telugu_OCR_Tesseract_Training) | GPL-3.0 | Allowed under GPL | Allowed under GPL | None |

### Research / academic use terms (6)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-009 | [ICDAR 2025 IHDR Telugu (Indic Handwritten Document Rec...](https://ilocr.iiit.ac.in/icdar_2025_Indic_HDR/dataset.html) | Site: "freely available for academic and research purposes" | UNKNOWN | UNKNOWN | Contact organisers |
| TOCR-021 | [HPL Isolated Handwritten Telugu Character Dataset (HP ...](https://lipitk.sourceforge.net/datasets/teluguchardata.htm) | HP Labs dataset licence (LipiTk site) | NOT VERIFIED | NOT VERIFIED | None |
| TOCR-046 | [Telugu Image Corpus - OCR (TDIL / C-DAC Noida OCR Cons...](https://tdil-dc.in/index.php?lang=en&option=com_download&task=showresourceDetails&toolid=264) | Research only (search snippet) | Not allowed (reported) | UNKNOWN | TDIL registration (reported) |
| TOCR-070 | [IIIT-ILST - Telugu (scene text)](https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-ilst) | Research only; images may not be redistributed | Not allowed | NOT ALLOWED | None (agree to terms) |
| TOCR-080 | [WIRIndic Telugu (ICPR 2024 Word Image Recognition in I...](https://ilocr.iiit.ac.in/icpr_2024_wirindic/dataset.html) | NOT STATED (page research line refers to MLT) | UNKNOWN | UNKNOWN | None |
| TOCR-081 | [MIST - Multilingual Incidental Scene Text (Telugu fram...](https://huggingface.co/datasets/Saumya-Mundra/MIST-Dataset) | Research use; ask authors for commercial | Not without permission | Raw imagery: ask authors | None |

### Commercial / vendor (4)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-012 | [FutureBeeAI Telugu Handwritten Sticky Notes OCR Image ...](https://www.futurebeeai.com/dataset/ocr-dataset/telugu-sticky-notes-ocr-image-dataset) | Commercial licence (vendor: "available for commercial use") | Allowed under purchase | NOT ALLOWED (commercial) | Purchase / sales contact |
| TOCR-013 | [FutureBeeAI Telugu Shopping List OCR Image Dataset](https://www.futurebeeai.com/dataset/ocr-dataset/telugu-shopping-list-ocr-image-dataset) | Commercial licence | Allowed under purchase | NOT ALLOWED | Purchase |
| TOCR-065 | [FutureBeeAI Telugu Newspaper, Magazine and Books OCR I...](https://www.futurebeeai.com/dataset/ocr-dataset/telugu-newspaper-book-magazine-ocr-image-dataset) | Commercial licence | Allowed under purchase | NOT ALLOWED | Purchase |
| TOCR-066 | [FutureBeeAI Telugu Product Image OCR Dataset](https://www.futurebeeai.com/dataset/ocr-dataset/telugu-product-image-ocr-dataset) | Commercial licence | Allowed under purchase | NOT ALLOWED | Purchase |

### Copyrighted source material (no licence) (5)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-058 | [Divs0910/telugu-ocr-dataset (Chandamama paragraph crop...](https://huggingface.co/datasets/Divs0910/telugu-ocr-dataset) | None declared; Chandamama is copyrighted | Not established | Not established | None |
| TOCR-094 | [harsha-desaraju/Telugu-text-image (rendered news chunk...](https://huggingface.co/datasets/harsha-desaraju/Telugu-text-image) | None declared; news text is publisher copyright | Not established | Not established | None |
| TOCR-124 | [Telugu newspapers e-paper archive (newspapers-telugu, ...](https://archive.org/details/newspapers-telugu) | Newspaper copyright (no licence field) | Not allowed | NOT ALLOWED | None |
| TOCR-127 | [Kaggle: Telugu Chandamama Books (harishml)](https://www.kaggle.com/datasets/harishml/telugu-chandamama-books) | Unknown; magazine copyright | Not established | Not established | Kaggle account |
| TOCR-129 | [Chandamama (Telugu edition) 1947-2012 scans](https://archive.org/search?query=collection%3Achandamama-magazine) | No licence field; magazine copyright | Not established | Not established | None |

### Unknown / not stated (57)

| ID | Dataset | Licence as stated | Commercial use | Redistribution | Access |
|---|---|---|---|---|---|
| TOCR-001 | [IIIT-HW-Telugu](https://cvit.iiit.ac.in/research/projects/cvit-projects/indic-hw-data) | NOT STATED on the CVIT page | UNKNOWN | UNKNOWN | None (direct download) |
| TOCR-004 | [IHTR 2022 Telugu track (ICFHR 2022 competition)](https://cvit.iiit.ac.in/ihtr2022/dataset.html) | NOT STATED | UNKNOWN | UNKNOWN | None |
| TOCR-005 | [IHTR 2023 Telugu track (ICDAR 2023 competition)](https://ilocr.iiit.ac.in/ihtr/dataset.html) | NOT STATED | UNKNOWN | UNKNOWN | None |
| TOCR-006 | [IIIT-Indic-HW-UC Telugu (Unconstrained Camera-captured...](https://cvit.iiit.ac.in/usodi/ucciohd.php) | NOT STATED on project page | UNKNOWN | UNKNOWN | None (direct download) |
| TOCR-007 | [IHWWR-1.0 Telugu (ICDAR 2024 HWD Task A)](https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html) | NOT STATED on competition page | UNKNOWN | UNKNOWN | None |
| TOCR-008 | [PLHWTR-1.0 Telugu (ICDAR 2024 HWD Task B)](https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html) | NOT STATED | UNKNOWN | UNKNOWN | None |
| TOCR-017 | [Kaggle mirror: IIT-INDIC-HW-WORDS Dataset (himanshukum...](https://www.kaggle.com/datasets/himanshukumarrajak/indic-data) | Unknown (Kaggle) | UNKNOWN | UNKNOWN (upstream terms apply) | Kaggle account to download |
| TOCR-018 | [GitHub JayanthKalluri/TeluguWordRecognizer - "handwrit...](https://github.com/JayanthKalluri/TeluguWordRecognizer) | None stated | UNKNOWN | UNKNOWN | Google Drive link |
| TOCR-019 | [Roboflow Universe: teluguocr/telugu-handwritten-ocr](https://universe.roboflow.com/teluguocr/telugu-handwritten-ocr) | UNKNOWN | UNKNOWN | UNKNOWN | Roboflow account |
| TOCR-020 | [Roboflow Universe: centurion-university-n60kx/telugu-h...](https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten) | UNKNOWN | UNKNOWN | UNKNOWN | Roboflow account |
| TOCR-023 | [UHTelHwCC: Telugu off-line handwritten character datas...](https://doi.org/10.1007/978-3-031-07005-1_22) | UNKNOWN | UNKNOWN | UNKNOWN | Contact authors |
| TOCR-033 | [MNIST-MIX (Telugu digits subset)](https://arxiv.org/abs/2004.03848) | NOT VERIFIED | UNKNOWN | UNKNOWN | See paper |
| TOCR-034 | [Kaggle: Multilingual Handwritten Digits Datasets (Telu...](https://www.kaggle.com/datasets/ayu8sh/hdr-datasets) | Unknown (Kaggle) | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-036 | [Kaggle: Handwritten Telugu Characters (bhaveshkarapu)](https://www.kaggle.com/datasets/bhaveshkarapu/handwritten-telugu-characters) | Unknown (Kaggle) | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-038 | [GitHub axlevisu/CNN-Telugu-OCR data folder](https://github.com/axlevisu/CNN-Telugu-OCR) | None stated | UNKNOWN | UNKNOWN | None |
| TOCR-039 | [GitHub srikarym/OCR_Telugu_code - final_dataset.hdf5 (...](https://github.com/srikarym/OCR_Telugu_code) | None stated | UNKNOWN | UNKNOWN | Google Drive link |
| TOCR-040 | [GitHub Mitradatta/Telugu-Character-Recognition - self-...](https://github.com/Mitradatta/Telugu-Character-Recognition) | None stated | UNKNOWN | UNKNOWN | Not released |
| TOCR-042 | [HF mirror: darknight054/indic-mozhi-ocr (telugu config)](https://huggingface.co/datasets/darknight054/indic-mozhi-ocr) | None declared (refers to source) | UNKNOWN | UNKNOWN | None |
| TOCR-043 | [Multilingual OCR for Indic Scripts - printed page corp...](https://doi.org/10.1109/DAS.2016.68) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| TOCR-044 | IIIT Telugu book collection (Pramod Sankar, Jawahar, M... | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| TOCR-045 | [Building Data Sets for Indian Language OCR Research (a...](https://doi.org/10.1007/978-1-84800-330-9_1) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| TOCR-047 | [UHTelPCC: Telugu Printed Character Dataset (University...](http://scis.uohyd.ac.in/~chakcs/UHTelPCC.html) | UNKNOWN | UNKNOWN | UNKNOWN | Contact authors |
| TOCR-048 | [UHIndicPCwS: University of Hyderabad Indic Printed Cha...](https://scis.uohyd.ac.in/~chakcs/datasets/UHIndicPCwS.html) | NOT STATED | UNKNOWN | UNKNOWN | None |
| TOCR-056 | [harsha-desaraju/consensus-labelling](https://huggingface.co/datasets/harsha-desaraju/consensus-labelling) | other | UNKNOWN | UNKNOWN | None |
| TOCR-063 | [kailasa-ngpt/gemini-3.7-flash-ocr (Telugu pages)](https://huggingface.co/datasets/kailasa-ngpt/gemini-3.7-flash-ocr-26-aug-2026) | other | UNKNOWN | UNKNOWN | None |
| TOCR-067 | [GitHub diuguide/telugu-ocr - page images with ground-t...](https://github.com/diuguide/telugu-ocr) | None stated | UNKNOWN | UNKNOWN | None |
| TOCR-069 | [GitHub ChillarAnand/likitham - ocropy Telugu line samp...](https://github.com/ChillarAnand/likitham) | No licence file | UNKNOWN | UNKNOWN | None |
| TOCR-078 | [Kaggle mirror: telugu scene text (srivarshachivukula5)](https://www.kaggle.com/datasets/srivarshachivukula5/telugu-scene-text) | Unknown | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-079 | [IIIT-IndicSTR-Word - Telugu (Indic Scene Text on the R...](https://cvit.iiit.ac.in/usodi/istr.php) | NOT STATED on page | UNKNOWN | UNKNOWN | None |
| TOCR-083 | [HF gated copy: Bhashini-IITJ/Bharat-Scene-Text-Dataset](https://huggingface.co/datasets/Bhashini-IITJ/Bharat-Scene-Text-Dataset) | other (HF) | UNKNOWN | UNKNOWN | HF login + accept terms |
| TOCR-085 | [Kaggle: Kannada-Centric Multilingual Meme Dataset (sur...](https://www.kaggle.com/datasets/surajx7x/new-dataset) | Unknown (Kaggle) | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-086 | [IIIT-Synthetic-M-Telugu](https://ilocr.iiit.ac.in/dataset/40/) | NOT STATED (no licence section on any IIIT-Synthetic page) | UNKNOWN | UNKNOWN | None |
| TOCR-087 | [IIIT-Synthetic-R-Telugu](https://ilocr.iiit.ac.in/dataset/55/) | NOT STATED | UNKNOWN | UNKNOWN | None |
| TOCR-088 | [IIIT-Synthetic-IndicSTR-Telugu](https://ilocr.iiit.ac.in/dataset/68/) | NOT STATED | UNKNOWN | UNKNOWN | None |
| TOCR-089 | [IndicSTR12 synthetic (CVIT synthetic.tar.gz, 13 langua...](https://cvit.iiit.ac.in/research/projects/cvit-projects/indicstr) | NOT STATED | UNKNOWN | UNKNOWN | None |
| TOCR-099 | [NayanaBench (Telugu)](https://huggingface.co/datasets/Nayana-cognitivelab/NayanaBench) | None declared | UNKNOWN | UNKNOWN | None |
| TOCR-106 | [chaitusvk/telugu_ocr_multi_line - generated line images](https://github.com/chaitusvk/telugu_ocr_multi_line) | None stated | UNKNOWN | UNKNOWN | None |
| TOCR-107 | [Telugu character database (Konkimalla et al., ICIP 201...](https://arxiv.org/abs/1711.07245) | UNKNOWN (paper promises code release) | UNKNOWN | UNKNOWN | UNKNOWN |
| TOCR-111 | [Indiscapes / Indiscapes2 (historical Indic manuscript ...](https://ihdia.iiit.ac.in/) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| TOCR-115 | [Kaggle: english hindi telugu text images (akash034)](https://www.kaggle.com/datasets/akash034/english-hindi-telugu-text-images) | Unknown | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-118 | [Telugu palm-leaf binarisation dataset ("Preserving Tel...](https://github.com/Bhavani-Pisini/Image-Binarization-Project) | None stated | UNKNOWN | UNKNOWN | Images not in repo; link NOT VERIFIED |
| TOCR-119 | [Telugu palm-leaf character crops (Sriram1908/TeluguMan...](https://github.com/Sriram1908/TeluguManuscriptOCRandTextReconstruction) | None stated | UNKNOWN | UNKNOWN | None |
| TOCR-120 | [Telugu palm-leaf 3D character dataset (2016 paper)](https://www.griet.ac.in/images/1-s2.0-S2215098616303627-main.pdf) | UNKNOWN | UNKNOWN | UNKNOWN | Contact authors |
| TOCR-122 | [Internet Archive - Telugu-language items](https://archive.org/search?query=language%3A%28Telugu+OR+tel%29) | Varies per item | Varies | Varies | None |
| TOCR-123 | [Digital Library of India (DLI) - Telugu books](https://archive.org/search?query=collection%3Adigitallibraryindia) | Mostly no licence stated | UNKNOWN | UNKNOWN | None |
| TOCR-125 | [Historic Telugu magazines on archive.org (Bharathi, An...](https://archive.org/search?query=title%3A%28%22andhra+patrika%22%29) | Varies | Varies | Varies | None |
| TOCR-126 | [AP Press Academy digitised old newspapers (pre-1977)](https://pressacademyarchives.ap.nic.in/) | UNKNOWN (Government of AP) | UNKNOWN | UNKNOWN | Web viewer |
| TOCR-128 | [HW-MLVQA (handwritten multilingual document VQA)](https://arxiv.org/abs/2507.15655) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| TOCR-130 | [IndicVisionBench (OCR task)](https://huggingface.co/datasets/krutrim-ai-labs/IndicVisionBench) | None declared on HF | UNKNOWN | UNKNOWN | None |
| TOCR-131 | [MInfoVisQA (multilingual infographic VQA)](https://huggingface.co/datasets/arnodjiang/MInfoVisQA) | other | UNKNOWN | UNKNOWN | None |
| TOCR-138 | [CulturaX - Telugu](https://huggingface.co/datasets/uonlp/CulturaX) | mC4/OSCAR terms | See licence | See licence | HF account + accept terms |
| TOCR-140 | [harsha-desaraju/telugu-ocr-text (+ -uncombined) - sour...](https://huggingface.co/datasets/harsha-desaraju/telugu-ocr-text) | None declared | UNKNOWN | UNKNOWN | None |
| TOCR-141 | [eswardivi/indiccorp_telugu_line](https://huggingface.co/datasets/eswardivi/indiccorp_telugu_line) | None declared (IndicCorp terms) | UNKNOWN | UNKNOWN | None |
| TOCR-142 | [TeluguOCR/corpora - Telugu Internet Unicode corpora](https://github.com/TeluguOCR/corpora) | None stated | UNKNOWN | UNKNOWN | None |
| TOCR-143 | [On-line Handwriting Recognition of Indian Scripts - Th...](https://dblp.org/rec/conf/icfhr/MondalBPDM10) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| TOCR-180 | [Kaggle: rs synth indic data (ocrteamriad)](https://www.kaggle.com/datasets/ocrteamriad/rs-synth-indic-data) | Unknown / other | UNKNOWN | UNKNOWN | Kaggle account |
| TOCR-181 | [Kaggle: OCR Stress Test v2 Multilingual Benchmark (har...](https://www.kaggle.com/datasets/harishk2209/ocr-stress-test-v2) | Unknown / other | UNKNOWN | UNKNOWN | Kaggle account |
