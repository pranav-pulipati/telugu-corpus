# Duplicate and mirror report

Many Telugu OCR datasets are uploaded more than once (Kaggle, Hugging Face, Google Drive) or are cut from a larger
release. Counting them separately would inflate the numbers, so each copy points back to its source.

- **69** distinct relationships between rows (each pair counted once).
- **38** dataset rows are marked as not distinct (mirror, copy, subset, derivative, re-listing or umbrella).
- Only rows marked `Y` in `Counts as distinct dataset` are counted in the totals (104).

## How copies were detected

1. **Same files**: Kaggle file listings and Hugging Face file trees compared by file names, folder layout and byte sizes. Nothing was downloaded.
2. **Same description or abstract**: DataCite/IEEE/Zenodo abstracts compared word for word.
3. **Same labels**: for data downloaded in the earlier acquisition phase, image paths and labels were compared one by one.
4. **The uploader says so**: README or dataset card names the source.

## Important findings

- **Kaggle "telugu-handwritten-dataset" (gottumukkalamadhuri) is not handwriting.** Its files match IIIT-Synthetic-R (rendered printed text). Marked as a mirror of TOCR-087 (TOCR-091).
- **IHTR 2023 Telugu train = IIIT-INDIC-HW-WORDS-Telugu train.** All 80,637 path+label pairs are identical (TOCR-005 vs TOCR-002).
- **IIIT-INDIC-HW-WORDS (TOCR-002) is the newer release of IIIT-HW-Telugu (TOCR-001).** Counted once.
- **IndicSTR12 real Telugu images are re-crops of IIIT-ILST** (TOCR-071 from TOCR-070); ILOCR's copy (TOCR-072) has 86 labels that differ from the CVIT release.
- **Roadside IIIT-IndicSTR-Word (TOCR-079) and the ICPR 2024 WIRIndic competition data (TOCR-080)** are the same collection.
- **Three Kaggle character uploads of 353.7 MB are byte-identical** (one row, TOCR-025).
- **GTS.ai's "Telugu Document Image Dataset" (Zenodo, catalogue TEL-OCR-014) is a brochure re-listing Kaggle amancapy/telugu-scans** (TOCR-096 to TOCR-095). The two state different licences (see the licensing report).
- **IEEE DataPort a1kv-rj60 (TOCR-108) has the same abstract as Konkimalla et al. 2018 (TOCR-107).** Suspected re-upload.
- **IndicSTR12 synthetic.tar.gz (TOCR-089, 62.7 GB) is suspected to be the same data as IIIT-Synthetic-IndicSTR (TOCR-088).** Not confirmed byte for byte.
- **Divs0910 Chandamama OCR set (TOCR-058) is built from the Chandamama scans (TOCR-129)** using the DIVYANSH-TEJA-09 pipeline.
- **The UoH DSpace record (catalogue TEL-OCR-011) and the IEEE DataPort Negi & Rao set (TOCR-022)** have the same authors and description and are treated as one dataset.

Found in round 2:

- **ORB-Indic (TOCR-172) and the IndicVisionBench OCR track (TOCR-130)** both come from Krutrim, both use Telugu Wikisource pages (TOCR-049) and both have exactly 89 Telugu pages. They are treated as the same pages (not confirmed image by image).
- **Kaggle telugu_palm_leafs (TOCR-195)** has 36 image/ground-truth pairs, matching the 36-image binarisation set of the "Preserving Telugu Manuscripts" paper (TOCR-118). It is probably that dataset's release.
- **Kaggle IITJ Multilingual OCR Dataset (TOCR-196)** holds per-language word crops with quadrilateral coordinates. It is suspected to be a copy of the IIT Jodhpur Bharat Scene Text crops (TOCR-082).
- **The ScrabbleGAN pages (TOCR-183)** are generated from IIIT-INDIC-HW-WORDS (TOCR-002), and **CHIPS (TOCR-182)** draws on the same word images (how much of CHIPS is re-composed is not stated clearly in the paper).
- **Roboflow iitbresearchwork/telugu-ocr (TOCR-191)** is suspected to be word-box annotations of PHDIndic_11 Telugu pages (TOCR-015), because the same workspace hosts a "Malayalam PhDIndic11" project.
- **IIIT-H Word Recognition Synthetic (TOCR-186)** renders the same 1,000-word vocabulary as the real IIIT-H word set (TOCR-044).
- **ULCA Project Anuvaad Telugu OCR corpus (TOCR-208)** comes from the same EkStep/Tarento group as the synthetic benchmark (TOCR-102). Overlap is possible but not confirmed.

## All relationships

| Row | Name | Distinct? | Related rows | Note |
|---|---|---|---|---|
| TOCR-001 | IIIT-HW-Telugu | Y | TOCR-002 | Parent of TOCR-002 (ILOCR v0.5 re-release, same word list/writers) and of the IHTR 2022/2023 Telugu tracks. |
| TOCR-002 | IIIT-INDIC-HW-WORDS-Telugu (ILOCR v0.5) | N (newer release of TOCR-001; family counted... | TOCR-001, TOCR-005, TOCR-018 | Same content as IHTR-2023 Telugu train (80,637/80,637 identical path+label pairs, TOCR-005); derived from TOCR-001; Kaggle/HF mirrors exist (TOCR-018). |
| TOCR-003 | IIIT-INDIC-HW-WORDS (multi-script umbrella) | N (umbrella; Telugu = TOCR-001) | TOCR-001 | Telugu part is TOCR-001/002; not counted separately. |
| TOCR-004 | IHTR 2022 Telugu track (ICFHR 2022 competition) | N (derivative) | TOCR-001 | Benchmark repackaging of TOCR-001/002; not independent data. |
| TOCR-005 | IHTR 2023 Telugu track (ICDAR 2023 competition) | N (duplicate) | TOCR-002 | Train = TOCR-002 train exactly (80,637/80,637 identical path+label pairs, checked 2026-11-10). |
| TOCR-006 | IIIT-Indic-HW-UC Telugu (Unconstrained Camera-captured Indi... | Y | TOCR-007 | Superset of the ICDAR 2024 HWD page collection: contains all 700 PLHWTR/IHWWR test pages and 2,062 IHWWR train pages (TOCR-007/008). |
| TOCR-007 | IHWWR-1.0 Telugu (ICDAR 2024 HWD Task A) | N (subset/re-crop of TOCR-006/008 pages) | TOCR-006, TOCR-008 | Word crops of PLHWTR pages (TOCR-008); 2,062 of 3,476 pages also in HW-UC (TOCR-006) with different segmentation. |
| TOCR-008 | PLHWTR-1.0 Telugu (ICDAR 2024 HWD Task B) | N (same pages as TOCR-006) | TOCR-006, TOCR-007 | Same pages as IHWWR (TOCR-007); all 700 test pages inside HW-UC (TOCR-006). |
| TOCR-010 | IIIT-INDIC-HW-WILD Telugu (SemiHastakshar unlabelled corpus) | Y | TOCR-014, TOCR-015 | Contains crops from IIITS-THDB (TOCR-014) and PHDIndic_11 (TOCR-015). |
| TOCR-014 | IIITS-THDB (IIIT Sri City Telugu Handwriting Database) | Y | TOCR-010 | 37,787 word crops reused (unlabelled) in TOCR-010. |
| TOCR-015 | PHDIndic_11 - Telugu pages | Y | TOCR-010, TOCR-016 | Telugu pages reused in TEXTRON (TOCR-016) and HW-WILD (TOCR-010). |
| TOCR-016 | TEXTRON INDIC datasets - Telugu handwritten pages | N (annotation layer on TOCR-015) | TOCR-015 | Pages from PHDIndic_11. |
| TOCR-017 | Kaggle mirror: IIT-INDIC-HW-WORDS Dataset (himanshukumarraj... | N (mirror) | TOCR-001, TOCR-003 | Mirror of IIIT datasets (TOCR-001..003). |
| TOCR-023 | UHTelHwCC: Telugu off-line handwritten character dataset (U... | UNKNOWN | TOCR-022 | May extend TOCR-022 (same institution); not confirmed. |
| TOCR-024 | Telugu Handwritten Character Dataset (Velpuru et al.) | Y | TOCR-025 | Possibly the source of the three identical Kaggle uploads (TOCR-025) - NOT VERIFIED. |
| TOCR-025 | Kaggle: "Final Dataset of Telugu Handwritten Characters" (3... | Y (one dataset; uploads are mirrors) | TOCR-024 | Three uploads are the same files (identical paths & size); origin suspected IEEE TOCR-024 (not verified). |
| TOCR-032 | CMATERdb 3.4.1 - Handwritten Telugu Numerals | Y | TOCR-033, TOCR-034 | Source for Telugu digits in MNIST-MIX (TOCR-033) and Kaggle hdr-datasets (TOCR-034); axlevisu repo "numbers" (3,000) likely the same. |
| TOCR-033 | MNIST-MIX (Telugu digits subset) | N (derivative) | TOCR-032 | Derivative of TOCR-032. |
| TOCR-034 | Kaggle: Multilingual Handwritten Digits Datasets (Telugu-op... | N (derivative) | TOCR-032 | Augmented derivative of TOCR-032. |
| TOCR-038 | GitHub axlevisu/CNN-Telugu-OCR data folder | Y | TOCR-032 | Numerals likely CMATERdb Telugu (TOCR-032) - same count 3,000. |
| TOCR-042 | HF mirror: darknight054/indic-mozhi-ocr (telugu config) | N (mirror) | TOCR-041 | Test split byte-identical to official (9,876/9,876 images and labels). |
| TOCR-043 | Multilingual OCR for Indic Scripts - printed page corpus (M... | UNKNOWN | TOCR-041 | Possibly superseded by Mozhi (TOCR-041). |
| TOCR-045 | Building Data Sets for Indian Language OCR Research (annota... | UNKNOWN | TOCR-046 | Possibly related to the TDIL OCR image corpus (TOCR-046). |
| TOCR-049 | Telugu Wikisource - proofread and validated page scans | Y | TOCR-050 | Parent of TOCR-050, 051, 052 and harsha line sets; count pages once. |
| TOCR-050 | AlbertoChestnut/telugu-ocr | N (derivative of TOCR-049) | TOCR-049 | Subset of TOCR-049. |
| TOCR-051 | harsha-desaraju/telugu-wikisource-text-images | N (derivative of TOCR-049) | TOCR-049 | Derived from TOCR-049. |
| TOCR-052 | harsha-desaraju/telugu-line-ocr-bench | Y (new human verification) | TOCR-049 | Derived from TOCR-049. |
| TOCR-055 | harsha-desaraju/telugu-book-line-images (+ -sample) | N (derivative of TOCR-054) | TOCR-054, TOCR-056 | Same crops as TOCR-056/057. |
| TOCR-056 | harsha-desaraju/consensus-labelling | N (labels on TOCR-055) | TOCR-055 | None identified |
| TOCR-057 | harsha-desaraju/telugu-pdf-line-image-text | N (filter of TOCR-056) | TOCR-056 | None identified |
| TOCR-058 | Divs0910/telugu-ocr-dataset (Chandamama paragraph crops) | Y | TOCR-129 | Derived from Chandamama archive scans (TOCR-129). |
| TOCR-060 | IndicDLP block-level OCR eval set (Telugu) | Y | TOCR-109 | None identified |
| TOCR-070 | IIIT-ILST - Telugu (scene text) | Y | TOCR-071 | 1,151 of 1,200 IndicSTR12-Telugu words are re-crops of these (TOCR-071/072). |
| TOCR-071 | IndicSTR12 real (CVIT release, all 12 languages) | Y | TOCR-070, TOCR-072 | Re-crops of IIIT-ILST Telugu (TOCR-070); 86 labels corrected vs ILOCR v0.5 (TOCR-072). |
| TOCR-072 | IndicSTR12-Telugu (ILOCR v0.5) | N (release of TOCR-071) | TOCR-071 | Official train/test share 154 scenes (leak); same images as TOCR-071 (1,183 byte-identical). |
| TOCR-073 | HF mirror/derivative: darknight054/indicstr12-crops | N (mirror) | TOCR-071 | Mirror/derivative of TOCR-071 (byte-identical to CVIT real.zip crops). |
| TOCR-074 | HF mirror/derivative: darknight054/indicstr12-full | N (mirror) | TOCR-071 | Mirror/derivative of TOCR-071 (full scenes from real.zip). |
| TOCR-075 | HF mirror/derivative: ananya12k/INDICSTR12_REAL_IMAGES | N (mirror) | TOCR-071 | Mirror/derivative of TOCR-071 (mirror of CVIT real.zip). |
| TOCR-076 | HF mirror/derivative: jai23023/indicstr12-signboards (+ -pr... | N (mirror) | TOCR-071 | Mirror/derivative of TOCR-071 (derivatives reformatted for VLM tuning). |
| TOCR-077 | Kaggle mirror: IndicSTR12 Indic Scene Text Recognition (pra... | N (mirror) | TOCR-071 | Mirror of TOCR-071. |
| TOCR-078 | Kaggle mirror: telugu scene text (srivarshachivukula5) | N (mirror) | TOCR-072 | Mirror of TOCR-072 (identical file naming). |
| TOCR-079 | IIIT-IndicSTR-Word - Telugu (Indic Scene Text on the Roadsi... | Y | TOCR-080 | Same data as WIRIndic Telugu (TOCR-080): same 10 languages, 25K/language, GoPro roadside, archive size matches. |
| TOCR-080 | WIRIndic Telugu (ICPR 2024 Word Image Recognition in Indic ... | N (release of TOCR-079) | TOCR-079, TOCR-081 | Competition packaging of TOCR-079; 95 of 193 MIST Telugu test frames are WIRIndic source frames (TOCR-081). |
| TOCR-081 | MIST - Multilingual Incidental Scene Text (Telugu frames) | Y | TOCR-079 | Same road footage as TOCR-079/080. |
| TOCR-083 | HF gated copy: Bhashini-IITJ/Bharat-Scene-Text-Dataset | N (mirror) | TOCR-082 | Mirror of TOCR-082. |
| TOCR-088 | IIIT-Synthetic-IndicSTR-Telugu | Y | TOCR-089 | Likely the Telugu part of the IndicSTR12 synthetic release (TOCR-089: "3M per language"). |
| TOCR-089 | IndicSTR12 synthetic (CVIT synthetic.tar.gz, 13 languages) | N (suspected same as TOCR-088) | TOCR-088 | Suspected same Telugu data as TOCR-088 (3M Telugu images both) - NOT VERIFIED. |
| TOCR-090 | Kaggle mirror: telugu scene text iiit (+ -val) (gottumukkal... | N (mirror) | TOCR-088 | Mirror of TOCR-088. |
| TOCR-091 | Kaggle mirror (mislabelled): "telugu handwritten dataset" (... | N (mirror) | TOCR-087 | Mirror of TOCR-087, despite the "handwritten" title. |
| TOCR-095 | Telugu Document Image-Text Pairs (amancapy/telugu-scans) | Y | TOCR-096 | Re-listed by GTS.ai with a CC BY 4.0 claim (TOCR-096). |
| TOCR-096 | GTS.ai "Telugu Document Image Dataset" (and Zenodo brochure... | N (re-listing) | TOCR-095 | Re-listing of TOCR-095; not independent data. |
| TOCR-097 | NayanaOCR Corpus 2025 - Telugu | Y | TOCR-098 | Built from NayanaDocs-Indic-45k (gated, TOCR-098). |
| TOCR-098 | Nayana gated OCR/VQA family (Telugu configs) | Y (gated family, counted once) | TOCR-097, TOCR-099 | Parents/variants of TOCR-097 and TOCR-099. |
| TOCR-107 | Telugu character database (Konkimalla et al., ICIP 2018) | Y | TOCR-108 | Same abstract appears on IEEE DataPort a1kv-rj60 (TOCR-108) under a different author. |
| TOCR-108 | "OCR Telugu Image Dataset" (IEEE DataPort a1kv-rj60) | N (suspected re-upload) | TOCR-107 | Suspected re-upload of TOCR-107 (identical abstract, different author); one search engine described it as handwritten shopping lists - contents NOT VERIFIED. |
| TOCR-109 | IndicDLP - Telugu pages (document layout parsing) | Y | TOCR-060, TOCR-110 | Block OCR eval set (TOCR-060) and dlp-sample (TOCR-110) derived from it. |
| TOCR-110 | onath/dlp-sample (IndicDLP sample, telugu config) | N (sample) | TOCR-109 | Sample of TOCR-109. |
| TOCR-118 | Telugu palm-leaf binarisation dataset ("Preserving Telugu M... | Y | TOCR-195 | Kaggle telugu_palm_leafs (TOCR-195) has 36 image/ground-truth pairs and is suspected to be this dataset. |
| TOCR-123 | Digital Library of India (DLI) - Telugu books | N (part of TOCR-122) | TOCR-122 | None identified |
| TOCR-125 | Historic Telugu magazines on archive.org (Bharathi, Andhra ... | N (part of TOCR-122) | TOCR-122 | None identified |
| TOCR-127 | Kaggle: Telugu Chandamama Books (harishml) | N (copy) | TOCR-129 | Subset copy of Chandamama archive (TOCR-129). |
| TOCR-129 | Chandamama (Telugu edition) 1947-2012 scans | Y | TOCR-058, TOCR-127 | Source of TOCR-058 and TOCR-127. |
| TOCR-130 | IndicVisionBench (OCR task) | Y | TOCR-049, TOCR-172 | Copies: AtharvImmverse/IndicVisionBench; lalit-03/IndicVisionBench (gated). OCR track Telugu pages likely the same 89 Wikisource pages as ORB-Indic (TOCR-172);... |
| TOCR-134 | indic-citizen-information-board-pmgsy | Y | TOCR-084 | Sibling of TOCR-084. |
| TOCR-140 | harsha-desaraju/telugu-ocr-text (+ -uncombined) - source vs... | Y | TOCR-094 | Text side of TOCR-094. |
| TOCR-141 | eswardivi/indiccorp_telugu_line | N (derivative of TOCR-137) | TOCR-137 | None identified |
| TOCR-172 | ORB-Indic (krutrim-ai-labs/ocr_rotation_bench) - Telugu pag... | N (suspected same pages as TOCR-130; derived... | TOCR-049, TOCR-130 | Derived from Telugu Wikisource (TOCR-049); suspected same 89 Telugu pages as IndicVisionBench OCR (TOCR-130). |
| TOCR-182 | CHIPS - Corpus of Handwritten Indic Scripts (Telugu pages) | UNKNOWN (may be a re-composition of TOCR-002... | TOCR-002, TOCR-015 | Built from IIIT-INDIC-HW-WORDS word images (TOCR-002); PLATTER also uses PHDIndic_11 Telugu pages (TOCR-015). |
| TOCR-183 | PLATTER ScrabbleGAN synthetic Telugu handwritten pages | UNKNOWN | TOCR-002 | Generated from TOCR-002. |
| TOCR-186 | IIIT-H Word Recognition Synthetic Dataset (Telugu) | Y | TOCR-044 | Same 1,000-word vocabulary as TOCR-044. |
| TOCR-188 | Handwritten Telugu character corpus (JASTT 2025, unreleased) | Y | TOCR-035 | Experiments in the paper use Kaggle 6-vowel set (TOCR-035), not this corpus. |
| TOCR-190 | NayanaIR-CrossBench (multilingual visual document retrieval) | Y | TOCR-097 | Same group as Nayana sets (TOCR-097/098/099). |
| TOCR-191 | Roboflow Universe: iitbresearchwork/telugu-ocr | UNKNOWN | TOCR-015 | Suspected word-box annotation of PHDIndic_11 Telugu pages (TOCR-015): same workspace has "Malayalam PhDIndic11" and PLATTER used PHDIndic_11 Telugu word boxes;... |
| TOCR-194 | Roboflow Universe: centurion-university-n60kx/telugu-handwr... | UNKNOWN | TOCR-020 | Same workspace as TOCR-020; may share images. |
| TOCR-195 | Kaggle: telugu_palm_leafs (chintuimmandi) - palm-leaf binar... | N (suspected copy of TOCR-118 data) | TOCR-118 | Same size and task as the "Preserving Telugu Manuscripts" binarisation set (TOCR-118, 36 images); suspected to be its data release (NOT VERIFIED). |
| TOCR-196 | Kaggle: IITJ Multilingual OCR Dataset (mayank7239) | N (suspected copy of TOCR-082) | TOCR-082 | Suspected re-upload of Bharat Scene Text crops (TOCR-082, IIT Jodhpur). |
| TOCR-208 | ULCA (Bhashini) OCR corpus - Telugu (Project Anuvaad) | Y | TOCR-102 | Same group as the EkStep synthetic benchmark (TOCR-102); overlap NOT VERIFIED. |
