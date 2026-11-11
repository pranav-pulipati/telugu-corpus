# Dataset details

One short profile per row of `telugu_ocr_final.csv`, grouped by category. Checked on 2026-11-11.
Fields marked UNKNOWN or NOT VERIFIED could not be confirmed from the source.


## OCR image-text: printed (19)

_Images of printed/born-digital Telugu text with human-made or human-checked transcriptions._

### TOCR-041 - Mozhi-Telugu (printed word images)

Word crops from scanned printed Telugu books with human-verified transcriptions; official train/val/test.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed, scanned books); Printed word recognition; granularity Word; Real
- **Size:** 100,024 (80,337 / 9,811 / 9,876); 28 books (word images)
- **Labels:** Yes - Word transcription
- **Licence:** CC BY 4.0 (stated on all other-language Mozhi pages; Telugu page broken) (commercial: Allowed with attribution (inferred); redistribution: Allowed with attribution (inferred))
- **Access:** Open download (zips HTTP 200; dataset page HTTP 500); needs: None
- **Source:** CVIT, IIIT Hyderabad; Minesh Mathew, Ajoy Mondal, C. V. Jawahar
- **Link:** https://cvit.iiit.ac.in/usodi/tdocrmil.php
- **Paper:** https://arxiv.org/abs/2205.06740
- **Download:** https://ilocr.iiit.ac.in/public/printed/phase-0/v0.5/telugu/akshara/{train,val,test}.zip
- **Overlap:** Official splits leak: all 28 books and 1,362/1,387 test pages also in train (phase-2 check).
- **Quality:** Audit 15/16 correct; 940 punctuation-only crops.
- **Notes:** Mozhi crops come from ~1,000 internally scanned pages per language; the full pages were not released.
- **Existing catalogue:** TEL-OCR-001

### TOCR-042 - HF mirror: darknight054/indic-mozhi-ocr (telugu config)

Parquet re-upload of Mozhi with UUID ids (file names dropped).

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-041
- **Language / script:** Multilingual (13 languages; telugu config) / Telugu
- **Content:** Image (printed); Printed word recognition; granularity Word; Real
- **Size:** 100,024 Telugu rows (word images)
- **Labels:** Yes - Word transcription
- **Licence:** None declared (refers to source) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual uploader; darknight054
- **Link:** https://huggingface.co/datasets/darknight054/indic-mozhi-ocr
- **Overlap:** Test split byte-identical to official (9,876/9,876 images and labels).

### TOCR-043 - Multilingual OCR for Indic Scripts - printed page corpus (Mathew, Singh, Jawahar 2016)

IIIT printed-page corpus used for multilingual Indic OCR (12 Indian languages + English) in DAS 2016; precursor work to Mozhi.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Multilingual (12 Indian + English) / Telugu
- **Content:** Image (printed pages); Printed text recognition; script ID; granularity Word / line; Real
- **Size:** UNKNOWN (UNKNOWN)
- **Labels:** Yes (per paper) - NOT VERIFIED
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No public release found; needs: UNKNOWN
- **Source:** CVIT, IIIT Hyderabad; Minesh Mathew, Ajeet Kumar Singh, C. V. Jawahar
- **Link:** https://doi.org/10.1109/DAS.2016.68
- **Paper:** https://doi.org/10.1109/DAS.2016.68
- **Overlap:** Possibly superseded by Mozhi (TOCR-041).

### TOCR-044 - IIIT-H Word Recognition Dataset (Telugu)

Printed Telugu word images of 1,000 distinct words sampled from 33 Digital Library of India books; labels hand-corrected (>99% accurate).

- **Status:** INACCESSIBLE · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed words, TIF); Word recognition; granularity Word; Real
- **Size:** 32,773 word images (5-530 per word; 52 MB TIF) (word images)
- **Labels:** Yes - Word label (1,000 classes)
- **Licence:** None stated (cite DAS 2010) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Download 404; page only on the Wayback Machine; needs: None when live
- **Source:** CVIT, IIIT Hyderabad; UMass; K. Pramod Sankar, C. V. Jawahar, R. Manmatha
- **Link:** https://web.archive.org/web/20221127093102/https://researchweb.iiit.ac.in/~pramod_sankar/CandD.html
- **Paper:** NOT VERIFIED (DAS 2010; "Nearest neighbor based collection OCR")
- **Download:** http://cvit.iiit.ac.in/docsearch/thatz1000.tar (HTTP 404 on 2026-11-11)

### TOCR-045 - Building Data Sets for Indian Language OCR Research (annotated corpus, 2009)

Book chapter describing large annotated document-image corpora built for Indian-language OCR (consortium effort; Telugu among target languages).

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Multilingual (Indian languages) / Telugu
- **Content:** Image (printed); Printed OCR ground truth; granularity Page / word; Real
- **Size:** UNKNOWN (UNKNOWN)
- **Labels:** Yes (per chapter) - NOT VERIFIED
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No public release found; needs: UNKNOWN
- **Source:** IIIT Hyderabad and OCR consortium; C. V. Jawahar et al.
- **Link:** https://doi.org/10.1007/978-1-84800-330-9_1
- **Paper:** https://doi.org/10.1007/978-1-84800-330-9_1
- **Overlap:** Possibly related to the TDIL OCR image corpus (TOCR-046).

### TOCR-049 - Telugu Wikisource - proofread and validated page scans

Scanned book pages with human-proofread (level 3) or validated (level 4) Telugu transcriptions; the source of most open Telugu page/line OCR sets.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned printed books) + text; Page-level OCR ground truth; granularity Page; Real
- **Size:** 134,015 proofread/validated pages (79,532 L3 + 54,483 L4) in 2026-11-01 dump; 127,326 on free-licence scans (pages)
- **Labels:** Yes - Page transcription (wiki markup; layout not preserved)
- **Licence:** Text CC BY-SA 4.0; scans per file (1,146 of 1,231 free) (commercial: Allowed (share-alike) for free scans; redistribution: Allowed (share-alike))
- **Access:** Open; needs: None (API/dumps; bulk image fetch needs a policy-compliant User-Agent)
- **Source:** Wikimedia / Telugu Wikisource community; Volunteers
- **Link:** https://te.wikisource.org/
- **Download:** https://dumps.wikimedia.org/tewikisource/ (text + quality levels); page images via Commons file pages
- **Overlap:** Parent of TOCR-050, 051, 052 and harsha line sets; count pages once.
- **Quality:** Columns merged, page numbers dropped; needs line alignment for line OCR.
- **Existing catalogue:** TEL-LIT-001

### TOCR-050 - AlbertoChestnut/telugu-ocr

Wikisource page scans with page transcriptions organised by book.

- **Status:** VERIFIED · **Distinct:** N (derivative of TOCR-049) · **Parent:** TOCR-049
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned printed pages); Page OCR; granularity Page; Real
- **Size:** 23,537 page pairs in 219 book folders (README: ~25,565 / 221) (page image-text pairs)
- **Labels:** Yes - Page transcription
- **Licence:** CC BY-SA 4.0 (commercial: Allowed (share-alike); redistribution: Allowed (share-alike))
- **Access:** Open (HF); needs: None
- **Source:** Individual; AlbertoChestnut
- **Link:** https://huggingface.co/datasets/AlbertoChestnut/telugu-ocr
- **Overlap:** Subset of TOCR-049.
- **Quality:** Catalogue figure 458,964 counts text lines, not pairs.
- **Existing catalogue:** TEL-OCR-005

### TOCR-051 - harsha-desaraju/telugu-wikisource-text-images

Line crops cut from Wikisource proofread pages and aligned to the page text, with CER-based acceptance flags.

- **Status:** VERIFIED · **Distinct:** N (derivative of TOCR-049) · **Parent:** TOCR-049
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed lines); Line recognition; granularity Line; Real
- **Size:** 659,924 rows (accepted subset smaller; flag column) (line crops)
- **Labels:** Yes - Line text (automatic alignment; accepted/reject flags)
- **Licence:** CC BY-SA 4.0 (commercial: Allowed (share-alike); redistribution: Allowed (share-alike))
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/telugu-wikisource-text-images
- **Overlap:** Derived from TOCR-049.
- **Quality:** Labels from automatic alignment, not per-line human review.
- **Existing catalogue:** TEL-OCR-007

### TOCR-052 - harsha-desaraju/telugu-line-ocr-bench

1,044 Wikisource line crops with human-verified transcriptions for evaluation.

- **Status:** VERIFIED · **Distinct:** Y (new human verification) · **Parent:** TOCR-049
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed lines); Line recognition (benchmark); granularity Line; Real
- **Size:** 1,044 (line crops)
- **Labels:** Yes - Human-verified line text
- **Licence:** CC BY-SA 4.0 (commercial: Allowed (share-alike); redistribution: Allowed (share-alike))
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/telugu-line-ocr-bench
- **Overlap:** Derived from TOCR-049.
- **Existing catalogue:** TEL-OCR-007

### TOCR-053 - harsha-desaraju/telugu-line-text-image

Line images from Telugu PDFs with text (e.g. Panchatantram), file and page provenance.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed lines from PDFs); Line recognition; granularity Line; Real (PDF render or scan - NOT VERIFIED)
- **Size:** 101,046 (line crops)
- **Labels:** Yes - Line text (origin of text NOT VERIFIED)
- **Licence:** MIT tag (source books not licensed by uploader) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/telugu-line-text-image

### TOCR-058 - Divs0910/telugu-ocr-dataset (Chandamama paragraph crops)

Paragraph crops from scanned Chandamama magazines aligned automatically to text (match_score); built by a GitHub pipeline with ground-truth JSON per issue.

- **Status:** VERIFIED · **Distinct:** Y · **Parent:** TOCR-129
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned printed magazine); Paragraph recognition; granularity Paragraph; Real
- **Size:** 120,321 (pipeline README: ~70,000 paragraphs target) (paragraph crops)
- **Labels:** Yes (automatic alignment) - Paragraph text + match score (not human-verified)
- **Licence:** None declared; Chandamama is copyrighted (commercial: Not established; redistribution: Not established)
- **Access:** Open (HF, 10.7 GB); needs: None
- **Source:** Individual; Divyansh Teja (inferred from handles)
- **Link:** https://huggingface.co/datasets/Divs0910/telugu-ocr-dataset
- **Overlap:** Derived from Chandamama archive scans (TOCR-129).

### TOCR-059 - Sarvam Indic OCR Bench - Telugu

Text-block crops from real Telugu documents (19th c. to present) with ground truth reviewed twice by language experts.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (23 languages; Telugu rows identified) / Telugu
- **Content:** Image (printed blocks); Block-level OCR (evaluation); granularity Text block; Real
- **Size:** 300 Telugu test blocks (+51 in small_representative, a subset) (block crops)
- **Labels:** Yes - Block transcription, double-reviewed
- **Licence:** Apache-2.0 (HF tag) (commercial: Allowed by tag (source documents have own copyright); redistribution: Allowed by tag)
- **Access:** Open (HF); needs: None
- **Source:** Sarvam AI; Sarvam AI
- **Link:** https://huggingface.co/datasets/sarvamai/indic-ocr-bench
- **Quality:** Audit 16/16 (block level); some source pages carry publisher watermarks.

### TOCR-060 - IndicDLP block-level OCR eval set (Telugu)

Cropped text blocks from IndicDLP pages with transcriptions; 582 Telugu blocks in the private full set, 10 in the public sample.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y · **Parent:** TOCR-109
- **Language / script:** Multilingual (23 languages) / Telugu
- **Content:** Image (printed blocks); Block-level OCR (evaluation); granularity Text block; Real
- **Size:** 582 Telugu (private) / 10 Telugu (public sample, one magazine issue) (block crops)
- **Labels:** Yes - Block transcription
- **Licence:** CC BY 4.0 (sample) (commercial: Allowed (sample); redistribution: Allowed (sample))
- **Access:** Sample open; full set private; needs: Full set private; sample open
- **Source:** IIT Madras (author of IndicDLP); Oikantik Nath
- **Link:** https://huggingface.co/datasets/onath/indicdlp-eval-set-22-sample

### TOCR-061 - NayanaOCRBench Natural - Telugu

Real Telugu document pages (e.g. TTD Sapthagiri magazine) with OmniDocBench-style layout + markdown/HTML text.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (22 languages; te config) / Telugu
- **Content:** Image (real document pages); Page OCR + layout (evaluation); granularity Page; Real
- **Size:** 461 Telugu pages (page images)
- **Labels:** Yes - Layout boxes + markdown/HTML text
- **Licence:** CC BY-NC 4.0 (commercial: Not allowed; redistribution: Allowed (non-commercial))
- **Access:** Open (HF); needs: None
- **Source:** CognitiveLab; CognitiveLab (Nayana team)
- **Link:** https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Natural

### TOCR-062 - OCR-Bench1000-Telugu

Small Telugu OCR evaluation set (images + labels.txt + metadata.jsonl).

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image; OCR evaluation; granularity UNKNOWN; UNKNOWN
- **Size:** 1K-10K (HF size category) (images)
- **Labels:** Yes (labels.txt) - Text labels (NOT VERIFIED)
- **Licence:** MIT (HF tag) (commercial: Allowed by tag; redistribution: Allowed by tag)
- **Access:** Gated (manual); needs: HF login + manual approval
- **Source:** Individual; meharuhanzz
- **Link:** https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Telugu
- **Existing catalogue:** TEL-OCR-010

### TOCR-067 - GitHub diuguide/telugu-ocr - page images with ground-truth manifest

Course/research repo with 1,924 Telugu page images and a ground-truth manifest for selected pages.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned pages); Page OCR; granularity Page; Real (assumed)
- **Size:** 1,924 page images; GT for a selected subset (page images)
- **Labels:** Partial - Ground-truth manifest (format NOT VERIFIED)
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual / course project; diuguide
- **Link:** https://github.com/diuguide/telugu-ocr

### TOCR-172 - ORB-Indic (krutrim-ai-labs/ocr_rotation_bench) - Telugu pages

Rotation-robust OCR benchmark: Wikisource page images in 11 Indic languages with human-edited transcriptions, presented at 4 and 8 rotation classes.

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (suspected same pages as TOCR-130; derived from TOCR-049)
- **Language / script:** Multilingual (11 Indic; Telugu 89) / Telugu
- **Content:** Image (rotated printed pages); Orientation detection + OCR evaluation; granularity Page; Real pages (rotated)
- **Size:** 966 pages total; Telugu 89 (paper Table 1) (page images)
- **Labels:** Yes - Rotation label + page transcription (Wikisource pagetext)
- **Licence:** Krutrim Community License 1.0 (commercial: Per Krutrim licence (NOT VERIFIED); redistribution: Per Krutrim licence (NOT VERIFIED))
- **Access:** Open (HF; Indic files 226 MB + 509 MB); needs: None
- **Source:** Krutrim AI Labs; Suranjan Goswami, Abhinav Ravi, Raja Kolla, Ali Faraz, Shaharukh Khan, Akash, Chandra Khatri, Shubham Agarwal
- **Link:** https://huggingface.co/datasets/krutrim-ai-labs/ocr_rotation_bench
- **Paper:** https://arxiv.org/abs/2511.04161
- **Overlap:** Derived from Telugu Wikisource (TOCR-049); suspected same 89 Telugu pages as IndicVisionBench OCR (TOCR-130).
- **Notes:** Round 1 rejected this row after sampling English rows; the paper confirms Telugu.

### TOCR-181 - Kaggle: OCR Stress Test v2 Multilingual Benchmark (harishk2209)

Indic folders include gu, tamil ...; Telugu presence NOT VERIFIED (file list fetch failed).

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Multilingual (Telugu NOT VERIFIED) / Telugu
- **Content:** Image; OCR; granularity UNKNOWN; UNKNOWN
- **Size:** 183.6 MB (bytes)
- **Labels:** UNKNOWN - UNKNOWN
- **Licence:** Unknown / other (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; UNKNOWN
- **Link:** https://www.kaggle.com/datasets/harishk2209/ocr-stress-test-v2
- **Notes:** 144 images + ground_truth.csv; file names carry no language; Telugu presence still NOT VERIFIED.

### TOCR-216 - IIIT Telugu document test sets (Rasagna 2013 MS thesis)

Laser-print, good-real and challenging-real Telugu document image sets with ground truth, used to evaluate document-level Telugu OCR.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed pages); Printed Telugu OCR evaluation; granularity Page / word; Real + laser-printed
- **Size:** UNKNOWN (one set ~200 pages per search snippet) (pages)
- **Labels:** Yes (per thesis) - Text ground truth
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Internal; no release found; needs: Contact CVIT
- **Source:** CVIT, IIIT Hyderabad; Venkat Rasagna (supervised by C. V. Jawahar)
- **Link:** https://cvit.iiit.ac.in/research/thesis/thesis-students/studies-in-recognition-of-telugu-document-images
- **Paper:** Rasagna_Thesis2013.pdf on the IIIT thesis server (tickets-felicity.iiit.ac.in; TLS certificate invalid on 2026-11-11)
- **Overlap:** Likely drawn from the same DLI book pages as TOCR-044/045.


## OCR image-text: handwritten (12)

_Images of handwritten Telugu words/lines/pages with transcriptions._

### TOCR-001 - IIIT-HW-Telugu

Original CVIT release of offline handwritten Telugu word images with word transcriptions, written by multiple writers on boxed forms.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (offline handwriting, scanned forms); Handwritten word recognition; word spotting; granularity Word; Real
- **Size:** >120,000 (official page: "over 120K handwritten words") (word images)
- **Labels:** Yes - Word-level Unicode transcription
- **Licence:** NOT STATED on the CVIT page (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (page live 2026-11-11); needs: None (direct download)
- **Source:** CVIT, IIIT Hyderabad; Kartik Dutta, Praveen Krishnan, Minesh Mathew, C. V. Jawahar
- **Link:** https://cvit.iiit.ac.in/research/projects/cvit-projects/indic-hw-data
- **Paper:** https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2018/spotting-recognition-handwritten.pdf
- **Download:** https://cvit.iiit.ac.in/images/Projects/wordlevel-Indicscripts/IIIT-HW-Telugu.zip ; https://cvit.iiit.ac.in/images/Projects/wordlevel-Indicscripts/IIIT-HW-Telugu_v1.tar.gz
- **Overlap:** Parent of TOCR-002 (ILOCR v0.5 re-release, same word list/writers) and of the IHTR 2022/2023 Telugu tracks.
- **Quality:** See TOCR-002 for measured label quality of the re-release.
- **Existing catalogue:** TEL-OCR-002 (as part of)

### TOCR-002 - IIIT-INDIC-HW-WORDS-Telugu (ILOCR v0.5)

Handwritten Telugu word images from boxed forms, with official train/val/test splits, label files and training vocabulary.

- **Status:** VERIFIED · **Distinct:** N (newer release of TOCR-001; family counted once) · **Parent:** TOCR-001
- **Language / script:** Telugu / Telugu
- **Content:** Image (offline handwriting); Handwritten word recognition; granularity Word; Real
- **Size:** 126,413 images (88,534 / 19,980 / 17,899); 118,516 labelled (train gt has 80,637 lines) (word images)
- **Labels:** Yes - Word transcription (tab-separated gt.txt) + vocabulary
- **Licence:** CC BY 4.0 (stated on dataset page) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Open download (zips HTTP 200, 2026-11-10); needs: None
- **Source:** CVIT / NLTM OCR consortium, IIIT Hyderabad; Santhoshini Gongidi, C. V. Jawahar
- **Link:** https://ilocr.iiit.ac.in/dataset/23/
- **Paper:** https://doi.org/10.1007/978-3-030-86337-1_30
- **Download:** https://ilocr.iiit.ac.in/public/handwritten/phase-0/v0.5/telugu/IIIT-INDIC-HW-WORDS-Telugu/{train,val,test}.zip
- **Overlap:** Same content as IHTR-2023 Telugu train (80,637/80,637 identical path+label pairs, TOCR-005); derived from TOCR-001; Kaggle/HF mirrors exist (TOCR-018).
- **Quality:** Phase-2 audit: 15/16 labels correct; 35 labels have invalid sign order (legacy encoding, e.g. కనే్నసి); 17 blank crops; official splits writer-disjoint.
- **Notes:** Train zip holds 7,897 images with no label line.
- **Existing catalogue:** TEL-OCR-002

### TOCR-003 - IIIT-INDIC-HW-WORDS (multi-script umbrella)

Umbrella benchmark of handwritten word images in 10 Indic scripts; Telugu portion is the earlier IIIT-HW-Telugu release.

- **Status:** VERIFIED · **Distinct:** N (umbrella; Telugu = TOCR-001)
- **Language / script:** Multilingual (10 Indic scripts incl. Telugu) / Multiple incl. Telugu
- **Content:** Image (offline handwriting); Handwritten word recognition; granularity Word; Real
- **Size:** 872K new instances in 8 scripts + earlier Devanagari & Telugu sets; Telugu subset = TOCR-001/002 (word images)
- **Labels:** Yes - Word transcription
- **Licence:** NOT STATED on CVIT page (ILOCR per-language pages: CC BY 4.0) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (per-language zips on CVIT page; Telugu not re-hosted there); needs: None
- **Source:** CVIT, IIIT Hyderabad; Santhoshini Gongidi, C. V. Jawahar
- **Link:** https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-indic-hw-words
- **Paper:** https://doi.org/10.1007/978-3-030-86337-1_30
- **Overlap:** Telugu part is TOCR-001/002; not counted separately.
- **Quality:** See TOCR-002.

### TOCR-004 - IHTR 2022 Telugu track (ICFHR 2022 competition)

Competition packaging of IIIT-INDIC-HW Telugu words (train 80,637 / val 19,980 / test 18,898 per competition page).

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (derivative) · **Parent:** TOCR-001
- **Language / script:** Telugu / Telugu
- **Content:** Image (offline handwriting); Handwritten word recognition; granularity Word; Real
- **Size:** Train 80,637 / Val 19,980 / Test 18,898 (competition page table) (word images)
- **Labels:** Yes (train/val); test labels not released - Word transcription
- **Licence:** NOT STATED (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (HTTP 200, 2026-11-10); needs: None
- **Source:** CVIT, IIIT Hyderabad; Competition organisers (CVIT)
- **Link:** https://cvit.iiit.ac.in/ihtr2022/dataset.html
- **Download:** https://cvit.iiit.ac.in/ihtr2022/assets/dataset/{trainingset,validationset,testset}.zip (all-language zips, 27.8 / 4.8 / 10.9 GB)
- **Overlap:** Benchmark repackaging of TOCR-001/002; not independent data.

### TOCR-005 - IHTR 2023 Telugu track (ICDAR 2023 competition)

Competition packaging of IIIT-INDIC-HW Telugu: train 80,637, val 1,000, test 5,000 (test unlabelled).

- **Status:** VERIFIED · **Distinct:** N (duplicate) · **Parent:** TOCR-002
- **Language / script:** Telugu / Telugu
- **Content:** Image (offline handwriting); Handwritten word recognition; granularity Word; Real
- **Size:** Train 80,637 / Val 1,000 / Test 5,000 (word images)
- **Labels:** Yes (train/val); test unlabelled - Word transcription
- **Licence:** NOT STATED (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (HTTP 200, 2026-11-10); needs: None
- **Source:** CVIT / ILOCR, IIIT Hyderabad; Competition organisers
- **Link:** https://ilocr.iiit.ac.in/ihtr/dataset.html
- **Download:** https://ilocr.iiit.ac.in/ihtr/assets/dataset/trainingset/telugu.zip ; testset/Telugu.zip ; validationset.zip
- **Overlap:** Train = TOCR-002 train exactly (80,637/80,637 identical path+label pairs, checked 2026-11-10).

### TOCR-006 - IIIT-Indic-HW-UC Telugu (Unconstrained Camera-captured Indic Offline Handwriting)

Camera-captured handwritten Telugu pages segmented into word crops with transcriptions; official word-level splits plus extra manually annotated folders.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (camera-captured handwriting); Handwritten word recognition; granularity Word (page annotations behind it); Real
- **Size:** 314,243 labelled crops in zip; 200,000 in official splits (150K/20K/30K); 280,226 after cleaning (phase 2) (word images)
- **Labels:** Yes - Word transcription; 33,306 placeholder "NA" labels
- **Licence:** NOT STATED on project page (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (zip CRC-checked 2026-11-10); needs: None (direct download)
- **Source:** CVIT, IIIT Hyderabad; Ajoy Mondal, C. V. Jawahar
- **Link:** https://cvit.iiit.ac.in/usodi/ucciohd.php
- **Paper:** https://doi.org/10.1007/978-3-031-78495-8_21
- **Download:** https://cvit.iiit.ac.in/images/datasets/indic_handwritten/telugu.zip (4.82 GB)
- **Overlap:** Superset of the ICDAR 2024 HWD page collection: contains all 700 PLHWTR/IHWWR test pages and 2,062 IHWWR train pages (TOCR-007/008).
- **Quality:** Audit 14/16 correct; official splits leak (all 4,597 identifiable pages split across train/val/test).

### TOCR-007 - IHWWR-1.0 Telugu (ICDAR 2024 HWD Task A)

Word crops from camera-captured handwritten Telugu pages; labelled training set and unlabelled test set.

- **Status:** VERIFIED · **Distinct:** N (subset/re-crop of TOCR-006/008 pages) · **Parent:** TOCR-006
- **Language / script:** Telugu / Telugu
- **Content:** Image (camera-captured handwriting); Handwritten word recognition; granularity Word; Real
- **Size:** Train 77,625 (labelled; 63,341 Telugu words, 14,284 punctuation/digit crops) / Test 9,585 (unlabelled) (word images)
- **Labels:** Yes (train only) - Word transcription
- **Licence:** NOT STATED on competition page (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (HTTP 200); needs: None
- **Source:** CVIT / ILOCR, IIIT Hyderabad; Competition organisers (Ajoy Mondal et al.)
- **Link:** https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html
- **Paper:** https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2024/Competition_on_Recognition_and_VQA_on_Handwritten_Documents.pdf
- **Download:** https://ilocr.iiit.ac.in/icdar_2024_hwd/assets/dataset/IHWR-1.0/Training-Set/Word_Level_Telugu_Training_Set.zip ; .../Test-Set/Word_Level_Telugu_Test_Set.zip
- **Overlap:** Word crops of PLHWTR pages (TOCR-008); 2,062 of 3,476 pages also in HW-UC (TOCR-006) with different segmentation.
- **Quality:** Audit 16/16 correct after removing punctuation-only crops.

### TOCR-008 - PLHWTR-1.0 Telugu (ICDAR 2024 HWD Task B)

Page images of camera-captured Telugu handwriting with page-level text of the prompted sentences (train); test pages unlabelled.

- **Status:** VERIFIED · **Distinct:** N (same pages as TOCR-006) · **Parent:** TOCR-006
- **Language / script:** Telugu / Telugu
- **Content:** Image (camera-captured handwriting); Page-level handwritten text recognition; granularity Page; Real
- **Size:** Train 3,496 pages (text) / Test 700 pages (no labels) (page images)
- **Labels:** Yes (train) - Page text (no word boxes in released train zip)
- **Licence:** NOT STATED (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download; needs: None
- **Source:** CVIT / ILOCR, IIIT Hyderabad; Competition organisers
- **Link:** https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html
- **Download:** https://ilocr.iiit.ac.in/icdar_2024_hwd/assets/dataset/PLHWTR-1.0/Training-Set/Page_Level_Telugu_Training_Set.zip (3.0 GB) ; Test-Set (742 MB)
- **Overlap:** Same pages as IHWWR (TOCR-007); all 700 test pages inside HW-UC (TOCR-006).
- **Quality:** Writer page numbers not transcribed; some lines run off the photo.

### TOCR-009 - ICDAR 2025 IHDR Telugu (Indic Handwritten Document Recognition)

Telugu validation/test pages for word detection (Task A) and page recognition (Task B) in a 10-language competition.

- **Status:** INACCESSIBLE · **Distinct:** Y (distinct, currently inaccessible)
- **Language / script:** Telugu / Telugu
- **Content:** Image (camera-captured handwriting); Handwritten word detection; page recognition; granularity Page; Real
- **Size:** UNKNOWN (10,000 pages across 10 languages per site) (page images)
- **Labels:** Yes for validation (boxes / page text) per site - Word boxes; page transcription
- **Licence:** Site: "freely available for academic and research purposes" (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Telugu zips redirect to cdn.iiit.ac.in and return HTTP 404 (re-checked 2026-11-11); charlist zip still downloads; needs: Contact organisers
- **Source:** CVIT / ILOCR, IIIT Hyderabad; Competition organisers
- **Link:** https://ilocr.iiit.ac.in/icdar_2025_Indic_HDR/dataset.html
- **Download:** https://ilocr.iiit.ac.in/icdar_2025_Indic_HDR/assets/dataset/Task-{A,B}/{Validation,Test}/Telugu-*.zip (all return HTTP 404)
- **Overlap:** Site lists HW-UC, IHWWR, PLHWTR, IHTR as pre-training sets; likely same collection effort.

### TOCR-017 - Kaggle mirror: IIT-INDIC-HW-WORDS Dataset (himanshukumarrajak/indic-data)

38.6 GB Kaggle upload of IIIT handwritten word datasets (IIIT-HW-Dev and others, 9 scripts per description).

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-003
- **Language / script:** Multilingual / Telugu
- **Content:** Image (offline handwriting); Handwritten word recognition; granularity Word; Real
- **Size:** 38,572.8 MB total; Telugu share NOT VERIFIED (bytes)
- **Labels:** Yes - Word transcription
- **Licence:** Unknown (Kaggle) (commercial: UNKNOWN; redistribution: UNKNOWN (upstream terms apply))
- **Access:** Open listing (Kaggle API); needs: Kaggle account to download
- **Source:** Individual uploader; himanshukumarrajak
- **Link:** https://www.kaggle.com/datasets/himanshukumarrajak/indic-data
- **Overlap:** Mirror of IIIT datasets (TOCR-001..003).

### TOCR-182 - CHIPS - Corpus of Handwritten Indic Scripts (Telugu pages)

Page-level handwritten Indic OCR dataset labelled for word detection and recognition, released with the PLATTER page-level HTR system; 10 languages.

- **Status:** INACCESSIBLE · **Distinct:** UNKNOWN (may be a re-composition of TOCR-002 words)
- **Language / script:** Multilingual (10 Indic; Telugu rows in Table 4) / Telugu
- **Content:** Image (handwritten pages); Page-level handwritten text detection + recognition; granularity Page (word boxes); Pages built from real handwritten word images (IIIT-INDIC-HW-WORDS); page layout composition NOT VERIFIED
- **Size:** Telugu 1,951 train / 504 val / 419 test (2,874 pages); 25,290 pages all languages (page images)
- **Labels:** Yes (per paper) - Word boxes + word transcriptions
- **Licence:** UNKNOWN (paper says data/code released; no data licence found) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No dataset link on arXiv, GitHub or HF (checked 2026-11-11); needs: No public link found
- **Source:** IIT Bombay; Badri Vishal Kasuba, Dhruv Kudale, Venkatapathy Subramanian, Parag Chaudhuri, Ganesh Ramakrishnan
- **Link:** https://arxiv.org/abs/2502.06172
- **Paper:** https://arxiv.org/abs/2502.06172
- **Overlap:** Built from IIIT-INDIC-HW-WORDS word images (TOCR-002); PLATTER also uses PHDIndic_11 Telugu pages (TOCR-015).

### TOCR-189 - UniLipi historical manuscript data - Telugu script

Annotated palm-leaf/paper manuscript pages (50-600 pages per script) and ~2.5M synthetic lines per script for 13 Indic scripts incl. Telugu, for a unified multi-script manuscript OCR.

- **Status:** INACCESSIBLE · **Distinct:** Y
- **Language / script:** Sanskrit and other languages in Telugu script (13 scripts total) / Telugu
- **Content:** Image (historical manuscripts + synthetic lines); Historical manuscript line OCR; granularity Line; Real + synthetic
- **Size:** Telugu: UNKNOWN (50-600 real pages per script; ~2.5M synthetic lines per script) (pages / lines)
- **Labels:** Yes - Line transcription (unified WX romanisation)
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Project page dataset link is a "coming soon" placeholder (2026-11-11); needs: Not released
- **Source:** IHDIA / CVIT, IIIT Hyderabad; UniLipi authors (IIIT Hyderabad)
- **Link:** https://ihdia.iiit.ac.in/unilipi/
- **Paper:** https://arxiv.org/abs/2608.28195


## OCR image-text: scene text (15)

_Photos of signs, boards and other real-world text (and born-digital images like memes) with transcriptions._

### TOCR-070 - IIIT-ILST - Telugu (scene text)

About 1,000 real scene images per script (Devanagari, Telugu, Malayalam) with word boxes (XML) and cropped word images with transcriptions.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (3 scripts) / Telugu
- **Content:** Image (scene); Scene text detection + recognition; granularity Word (+scene boxes); Real
- **Size:** 1,211 Telugu cropped words (WordImagesList) (word crops)
- **Labels:** Yes - Word boxes (XML) + transcription
- **Licence:** Research only; images may not be redistributed (commercial: Not allowed; redistribution: NOT ALLOWED)
- **Access:** Open download; needs: None (agree to terms)
- **Source:** CVIT, IIIT Hyderabad; Minesh Mathew, Mohit Jain, C. V. Jawahar
- **Link:** https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-ilst
- **Paper:** https://arxiv.org/abs/2104.04437
- **Download:** https://cvit.iiit.ac.in/images/datasets/iiit-ilst/IIIT-ILST.zip (639 MB, 3 scripts)
- **Overlap:** 1,151 of 1,200 IndicSTR12-Telugu words are re-crops of these (TOCR-071/072).

### TOCR-071 - IndicSTR12 real (CVIT release, all 12 languages)

Real scene-text word crops and full scene images for 12 Indian languages crawled from Google Images; Telugu subset 1,183 crops + 298 scenes.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (12) / Telugu
- **Content:** Image (scene); Scene text recognition; detection; granularity Word (+scenes); Real
- **Size:** >27,000 word images total; Telugu 1,183 crops (933/117/133) + 298 scenes (word crops)
- **Labels:** Yes - Word transcription; boxes for full scenes
- **Licence:** CC BY 4.0 on annotations (ILOCR page); paper CC BY-NC-ND; images third-party web content (commercial: Risky (image rights); redistribution: Annotations yes; images unclear)
- **Access:** Open download; needs: None
- **Source:** CVIT, IIIT Hyderabad; Harsh Lunia, Ajoy Mondal, C. V. Jawahar
- **Link:** https://cvit.iiit.ac.in/research/projects/cvit-projects/indicstr
- **Paper:** https://arxiv.org/abs/2403.08007
- **Download:** https://cvit.iiit.ac.in/images/datasets/IndicSTR12/real.zip (1.38 GB)
- **Overlap:** Re-crops of IIIT-ILST Telugu (TOCR-070); 86 labels corrected vs ILOCR v0.5 (TOCR-072).
- **Quality:** Audit 14/16 correct (2 misspellings).
- **Existing catalogue:** TEL-OCR-003

### TOCR-072 - IndicSTR12-Telugu (ILOCR v0.5)

ILOCR packaging of the Telugu real IndicSTR12 crops with train/test split.

- **Status:** VERIFIED · **Distinct:** N (release of TOCR-071) · **Parent:** TOCR-071
- **Language / script:** Telugu / Telugu
- **Content:** Image (scene); Scene text recognition; granularity Word; Real
- **Size:** 1,200 (900 / 300); 660 unique train words (word crops)
- **Labels:** Yes - Word transcription
- **Licence:** CC BY 4.0 (stated on page) (commercial: Annotations allowed; image rights third-party; redistribution: Annotations allowed)
- **Access:** Open download; needs: None
- **Source:** ILOCR, IIIT Hyderabad; Harsh Lunia, Ajoy Mondal, C. V. Jawahar
- **Link:** https://ilocr.iiit.ac.in/dataset/36/
- **Download:** https://ilocr.iiit.ac.in/public/scenetext/phase-0/v0.5/telugu/IndicSTR12/{train,test}.zip (8.5 MB)
- **Overlap:** Official train/test share 154 scenes (leak); same images as TOCR-071 (1,183 byte-identical).

### TOCR-073 - HF mirror/derivative: darknight054/indicstr12-crops

Hugging Face re-upload of IndicSTR12 real data (byte-identical to CVIT real.zip crops).

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-071
- **Language / script:** Multilingual (Telugu subset) / Telugu
- **Content:** Image (scene); Scene text recognition; granularity Word; Real
- **Size:** 1,183 Telugu crops (images)
- **Labels:** Yes - Word transcription
- **Licence:** As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual uploader; darknight054
- **Link:** https://huggingface.co/datasets/darknight054/indicstr12-crops
- **Overlap:** Mirror/derivative of TOCR-071 (byte-identical to CVIT real.zip crops).

### TOCR-074 - HF mirror/derivative: darknight054/indicstr12-full

Hugging Face re-upload of IndicSTR12 real data (full scenes from real.zip).

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-071
- **Language / script:** Multilingual (Telugu subset) / Telugu
- **Content:** Image (scene); Scene text recognition; granularity Word; Real
- **Size:** 298 Telugu scenes with boxes (images)
- **Labels:** Yes - Word transcription
- **Licence:** As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual uploader; darknight054
- **Link:** https://huggingface.co/datasets/darknight054/indicstr12-full
- **Overlap:** Mirror/derivative of TOCR-071 (full scenes from real.zip).

### TOCR-075 - HF mirror/derivative: ananya12k/INDICSTR12_REAL_IMAGES

Hugging Face re-upload of IndicSTR12 real data (mirror of CVIT real.zip).

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-071
- **Language / script:** Multilingual (Telugu subset) / Telugu
- **Content:** Image (scene); Scene text recognition; granularity Word; Real
- **Size:** real.zip re-upload (1,382,967,649 bytes, identical size) (images)
- **Labels:** Yes - Word transcription
- **Licence:** As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual uploader; ananya12k
- **Link:** https://huggingface.co/datasets/ananya12k/INDICSTR12_REAL_IMAGES
- **Overlap:** Mirror/derivative of TOCR-071 (mirror of CVIT real.zip).

### TOCR-076 - HF mirror/derivative: jai23023/indicstr12-signboards (+ -preprocessed, -verified-twice)

Hugging Face re-upload of IndicSTR12 real data (derivatives reformatted for VLM tuning).

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-071
- **Language / script:** Multilingual (Telugu subset) / Telugu
- **Content:** Image (scene); Scene text recognition; granularity Word; Real
- **Size:** 298 Telugu signboards / 1,183 verified-twice crops (images)
- **Labels:** Yes - Word transcription
- **Licence:** As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual uploader; jai23023
- **Link:** https://huggingface.co/datasets/jai23023/indicstr12-signboards
- **Overlap:** Mirror/derivative of TOCR-071 (derivatives reformatted for VLM tuning).

### TOCR-077 - Kaggle mirror: IndicSTR12 Indic Scene Text Recognition (prathmeshzade)

Kaggle re-upload of IndicSTR12 real/verified_twice with annotations.csv.

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-071
- **Language / script:** Multilingual (12) / Telugu
- **Content:** Image (scene); Scene text recognition; granularity Word; Real
- **Size:** 1,373 MB (all 12 languages) (bytes)
- **Labels:** Yes - Word transcription
- **Licence:** MIT (Kaggle tag; upstream terms apply) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; Prathmesh Zade
- **Link:** https://www.kaggle.com/datasets/prathmeshzade/indicstr12-indic-scene-text-recognition
- **Overlap:** Mirror of TOCR-071.

### TOCR-078 - Kaggle mirror: telugu scene text (srivarshachivukula5)

Kaggle upload whose file names match the ILOCR IndicSTR12-Telugu crops.

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-072
- **Language / script:** Telugu / Telugu
- **Content:** Image (scene); Scene text recognition; granularity Word; Real
- **Size:** 8.6 MB (ILOCR set is 8.5 MB) (bytes)
- **Labels:** Yes (assumed, same files) - Word transcription
- **Licence:** Unknown (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; srivarshachivukula5
- **Link:** https://www.kaggle.com/datasets/srivarshachivukula5/telugu-scene-text
- **Overlap:** Mirror of TOCR-072 (identical file naming).

### TOCR-079 - IIIT-IndicSTR-Word - Telugu (Indic Scene Text on the Roadside)

Word crops extracted from GoPro roadside videos in 10 Indian languages; 25,000 words per language.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (10) / Telugu
- **Content:** Image (scene, video frames); Scene text recognition; granularity Word; Real
- **Size:** 250,000 total (10 languages); Telugu ~25,000 (word crops)
- **Labels:** Yes - Word transcription
- **Licence:** NOT STATED on page (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (HTTP 200); needs: None
- **Source:** CVIT, IIIT Hyderabad; Ajoy Mondal, Krishna Tulsyan, C. V. Jawahar
- **Link:** https://cvit.iiit.ac.in/usodi/istr.php
- **Download:** https://cvit.iiit.ac.in/images/datasets/indic_scene_text_roadside/telugu.tar.gz (167.8 MB)
- **Overlap:** Same data as WIRIndic Telugu (TOCR-080): same 10 languages, 25K/language, GoPro roadside, archive size matches.

### TOCR-080 - WIRIndic Telugu (ICPR 2024 Word Image Recognition in Indic scene text)

Competition release of the roadside Telugu word crops: train 17,500 / val 2,500 labelled, test 5,000 unlabelled.

- **Status:** VERIFIED · **Distinct:** N (release of TOCR-079) · **Parent:** TOCR-079
- **Language / script:** Telugu / Telugu
- **Content:** Image (scene, video frames); Scene text recognition; granularity Word; Real
- **Size:** 25,000 (20,000 labelled) (word crops)
- **Labels:** Yes (train/val) - Word transcription
- **Licence:** NOT STATED (page research line refers to MLT) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download; needs: None
- **Source:** CVIT / ILOCR, IIIT Hyderabad; Competition organisers
- **Link:** https://ilocr.iiit.ac.in/icpr_2024_wirindic/dataset.html
- **Download:** https://ilocr.iiit.ac.in/icpr_2024_wirindic/assets/dataset/Telugu/{train,val,test}.zip
- **Overlap:** Competition packaging of TOCR-079; 95 of 193 MIST Telugu test frames are WIRIndic source frames (TOCR-081).
- **Quality:** Audit: ~44% of crops cut part of the word; only 4,580 distinct words.

### TOCR-082 - Bharat Scene Text Dataset (BSTD)

6,582 scene images with polygon/word annotations in 11 Indian languages + English; supports detection, script ID, cropped word recognition, end-to-end.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (11 Indian + English) / Telugu
- **Content:** Image (scene); Scene text detection, script ID, recognition; granularity Word (+scenes); Real
- **Size:** Telugu 2,760 cropped words (2,215 train / 545 test) (word crops)
- **Labels:** Yes - Polygons + word transcription + script
- **Licence:** Apache-2.0 (repository; no separate data licence) (commercial: Likely allowed; redistribution: Likely allowed)
- **Access:** Open download; needs: None (Google Drive)
- **Source:** IIT Jodhpur (Bhashini); A. De, A. S. Penamakuri, R. Yadav, A. Rathore, H. Shah, D. Sharma, S. Agarwal, P. Kumar, A. Mishra
- **Link:** https://github.com/Bhashini-IITJ/BharatSceneTextDataset
- **Paper:** https://arxiv.org/abs/2511.23071
- **Download:** https://drive.google.com/file/d/1d8yOLWrStRTmB8nIJG3mi-w5P9IzB_z8 (recognition.zip, 791 MB); detection.zip (~17 GB)
- **Quality:** 457/2,760 labels use ౦ for ం (fixable); audit 13/16 correct.

### TOCR-083 - HF gated copy: Bhashini-IITJ/Bharat-Scene-Text-Dataset

Gated Hugging Face copy of BSTD.

- **Status:** GATED · **Distinct:** N (mirror) · **Parent:** TOCR-082
- **Language / script:** Multilingual / Telugu
- **Content:** Image (scene); Scene text; granularity Word (+scenes); Real
- **Size:** See TOCR-082 (images)
- **Labels:** Yes - As TOCR-082
- **Licence:** other (HF) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Gated (auto); needs: HF login + accept terms
- **Source:** IIT Jodhpur; Bhashini-IITJ
- **Link:** https://huggingface.co/datasets/Bhashini-IITJ/Bharat-Scene-Text-Dataset
- **Overlap:** Mirror of TOCR-082.

### TOCR-085 - Kaggle: Kannada-Centric Multilingual Meme Dataset (surajx7x)

10,392 meme images (mostly Kannada, some English/Tamil/Telugu) with OCR text and language annotations.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (Kannada-majority; some Telugu) / Telugu
- **Content:** Image (born-digital memes); Born-digital text OCR / language ID; granularity Image; Real
- **Size:** 10,392 total; Telugu share UNKNOWN (images)
- **Labels:** Yes - OCR text + language (annotations.json; origin NOT VERIFIED)
- **Licence:** Unknown (Kaggle) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; surajx7x
- **Link:** https://www.kaggle.com/datasets/surajx7x/new-dataset
- **Notes:** Born-digital images grouped with scene text; Telugu subset not identified.

### TOCR-213 - ICDAR 2025 Competition on Multi-lingual Roadside Scene Text Recognition (MLT-RSTR) - Telugu

Full roadside scene images in 10 Indic languages with word polygons, transcriptions and language labels; tasks cover detection, recognition and language ID.

- **Status:** INACCESSIBLE · **Distinct:** UNKNOWN (suspected same collection as TOCR-079)
- **Language / script:** Multilingual (10 Indic incl. Telugu) / Telugu
- **Content:** Image (roadside scenes); Scene text detection + recognition + language ID; granularity Word polygons in full scenes; Real
- **Size:** UNKNOWN (scene images)
- **Labels:** Yes (validation set) - Polygon + transcription + language (JSON)
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** All validation/test zips HTTP 404 (2026-11-11); Telugu charlist downloads; needs: Competition registration
- **Source:** CVIT / ILOCR, IIIT Hyderabad; Competition organisers
- **Link:** https://ilocr.iiit.ac.in/icdar_2025_MLT-RSTR/dataset.html
- **Download:** https://ilocr.iiit.ac.in/icdar_2025_MLT-RSTR/assets/dataset/Val/Val.zip (HTTP 404 on 2026-11-11)
- **Overlap:** Roadside collection; suspected same source as IIIT-IndicSTR-Word / WIRIndic (TOCR-079/080).


## OCR image-text: synthetic (24)

_Computer-rendered Telugu text images; the label is the exact text that was rendered._

### TOCR-086 - IIIT-Synthetic-M-Telugu

Synthetic printed Telugu word images rendered with 62 Unicode fonts; page says pre-training use only.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered printed words); Printed word recognition (pre-training); granularity Word; Synthetic
- **Size:** 138,585 (61,142 unique words) (word images)
- **Labels:** Yes - Rendered text (exact)
- **Licence:** NOT STATED (no licence section on any IIIT-Synthetic page) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download; needs: None
- **Source:** ILOCR, IIIT Hyderabad; ILOCR team
- **Link:** https://ilocr.iiit.ac.in/dataset/40/
- **Download:** https://ilocr.iiit.ac.in/public/printed/phase-0/v0.5/telugu/IIIT-Synthetic-M-Telugu/train.zip (169 MB; page link wrongly points to /hindi/)

### TOCR-087 - IIIT-Synthetic-R-Telugu

Synthetic printed Telugu word images rendered with 300 fonts; train/val/test.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered printed words); Printed word recognition; granularity Word (often 2 joined words); Synthetic
- **Size:** 612,500 (428,750 / 61,250 / 122,500) (word images)
- **Labels:** Yes - Rendered text (leading space in labels)
- **Licence:** NOT STATED (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download; needs: None
- **Source:** ILOCR, IIIT Hyderabad; ILOCR team
- **Link:** https://ilocr.iiit.ac.in/dataset/55/
- **Download:** https://ilocr.iiit.ac.in/public/printed/phase-0/v0.5/telugu/IIIT-Synthetic-R-Telugu/{train,val,test}.zip (2.05 GB)
- **Overlap:** 1,270 near-identical image+label groups across official train/test.

### TOCR-088 - IIIT-Synthetic-IndicSTR-Telugu

Synthetic scene-style Telugu word images (backgrounds, distortions).

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (synthetic scene words); Scene text recognition (pre-training); granularity Word; Synthetic
- **Size:** 2,999,658 (2,000,000 / 499,658 / 500,000) (word images)
- **Labels:** Yes - Rendered text
- **Licence:** NOT STATED (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download; needs: None
- **Source:** ILOCR, IIIT Hyderabad; ILOCR team
- **Link:** https://ilocr.iiit.ac.in/dataset/68/
- **Download:** https://ilocr.iiit.ac.in/public/scenetext/phase-0/v0.5/telugu/IIIT-Synthetic-Telugu/{train,val,test}.zip (6.3 GB)
- **Overlap:** Likely the Telugu part of the IndicSTR12 synthetic release (TOCR-089: "3M per language").
- **Quality:** ~25% of audited images near-unreadable; 99.8% of test words appear in train.

### TOCR-089 - IndicSTR12 synthetic (CVIT synthetic.tar.gz, 13 languages)

Synthetic scene-text word images for 13 Indian languages; paper states more than 3 million per language.

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (suspected same as TOCR-088)
- **Language / script:** Multilingual (13 incl. Telugu) / Telugu
- **Content:** Image (synthetic scene words); Scene text recognition (pre-training); granularity Word; Synthetic
- **Size:** >3M per language (paper); Telugu count NOT VERIFIED (word images)
- **Labels:** Yes - Rendered text
- **Licence:** NOT STATED (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (size verified via HEAD only); needs: None
- **Source:** CVIT, IIIT Hyderabad; Harsh Lunia, Ajoy Mondal, C. V. Jawahar
- **Link:** https://cvit.iiit.ac.in/research/projects/cvit-projects/indicstr
- **Paper:** https://arxiv.org/abs/2403.08007
- **Download:** https://cvit.iiit.ac.in/images/datasets/IndicSTR12/synthetic.tar.gz (62.7 GB, HTTP 200)
- **Overlap:** Suspected same Telugu data as TOCR-088 (3M Telugu images both) - NOT VERIFIED.

### TOCR-090 - Kaggle mirror: telugu scene text iiit (+ -val) (gottumukkalamadhuri)

Kaggle uploads with IIIT-Synthetic-IndicSTR file naming (e.g. 0_0.0_102.jpeg).

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-088
- **Language / script:** Telugu / Telugu
- **Content:** Image (synthetic scene words); Scene text recognition; granularity Word; Synthetic
- **Size:** 6,306.9 MB + 1,041.5 MB (ILOCR zips: 4.2+1.05+1.05 GB) (bytes)
- **Labels:** Yes (assumed) - Rendered text
- **Licence:** Apache-2.0 tag (not the uploader's to grant) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; gottumukkalamadhuri
- **Link:** https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-scene-text-iiit
- **Overlap:** Mirror of TOCR-088.

### TOCR-091 - Kaggle mirror (mislabelled): "telugu handwritten dataset" (gottumukkalamadhuri)

Titled handwritten, but file names (Aaradhana_0.0_1.png ...) are IIIT-Synthetic-R-Telugu printed synthetic images.

- **Status:** VERIFIED · **Distinct:** N (mirror) · **Parent:** TOCR-087
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered printed words); Printed word recognition; granularity Word; Synthetic
- **Size:** 3,715 MB (bytes)
- **Labels:** Yes (assumed) - Rendered text
- **Licence:** Apache-2.0 tag (not the uploader's to grant) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; gottumukkalamadhuri
- **Link:** https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-handwritten-dataset
- **Overlap:** Mirror of TOCR-087, despite the "handwritten" title.

### TOCR-092 - Chitralekha - synthetic Telugu word images

Rendered Telugu word images, one config per font (Noto, Pothana2000, Ramabhadra, Mandali, Gidugu ...), with splits.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered words); Word recognition (pre-training); granularity Word; Synthetic
- **Size:** 61,898,021 rows across font configs (~790K per font) (word images)
- **Labels:** Yes - Rendered text
- **Licence:** MIT (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** Individual; gksriharsha
- **Link:** https://huggingface.co/datasets/gksriharsha/chitralekha
- **Existing catalogue:** TEL-OCR-006

### TOCR-093 - harsha-desaraju/telugu-synthetic-line-images

2.5M rendered Telugu (and Sanskrit-in-Telugu) line images with font and fragment metadata.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered lines); Line recognition (pre-training); granularity Line; Synthetic
- **Size:** 2,500,000 (10 train shards + 5,000 val) (line images)
- **Labels:** Yes - Rendered text
- **Licence:** MIT (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/telugu-synthetic-line-images
- **Existing catalogue:** TEL-OCR-007

### TOCR-094 - harsha-desaraju/Telugu-text-image (rendered news chunks)

Andhra Jyothy news text rendered in Telugu fonts, with source text and an OCR read of the render.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered text blocks); Block recognition; granularity Text chunk; Synthetic
- **Size:** 113,592 (rendered chunks)
- **Labels:** Yes - Source text (+OCR text)
- **Licence:** None declared; news text is publisher copyright (commercial: Not established; redistribution: Not established)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/Telugu-text-image

### TOCR-095 - Telugu Document Image-Text Pairs (amancapy/telugu-scans)

20,000 generated "scan-like" Telugu document page images paired with their text; generator code on GitHub.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered pages); Page OCR (image-to-sequence); granularity Page; Synthetic
- **Size:** 20,000 pairs (4,708 MB) (page image-text pairs)
- **Labels:** Yes - Page text (doc{i}.png <-> {i}.txt)
- **Licence:** CC BY-NC 4.0 (Kaggle) (commercial: Not allowed; redistribution: Allowed (non-commercial))
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; amancapy
- **Link:** https://www.kaggle.com/datasets/amancapy/telugu-scans
- **Overlap:** Re-listed by GTS.ai with a CC BY 4.0 claim (TOCR-096).

### TOCR-096 - GTS.ai "Telugu Document Image Dataset" (and Zenodo brochure records)

Vendor listing of the same 20,000 image-text pairs; the page's download links to the Kaggle original; Zenodo holds only a 419 KB brochure PDF.

- **Status:** VERIFIED · **Distinct:** N (re-listing) · **Parent:** TOCR-095
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered pages); Page OCR; granularity Page; Synthetic
- **Size:** 20,000 (claim = Kaggle original) (page image-text pairs)
- **Labels:** Yes - Page text
- **Licence:** CC BY 4.0 claimed on Zenodo - conflicts with original CC BY-NC 4.0 (commercial: Treat as non-commercial (original licence); redistribution: See original)
- **Access:** Brochure only on Zenodo; data via Kaggle; needs: Links to Kaggle
- **Source:** Globose Technology Solutions (GTS.ai); Globose Technology Solutions
- **Link:** https://gts.ai/dataset-download/telugu-document-image-dataset/
- **Overlap:** Re-listing of TOCR-095; not independent data.
- **Existing catalogue:** TEL-OCR-014

### TOCR-097 - NayanaOCR Corpus 2025 - Telugu

Synthetic/rendered Telugu documents with layout regions and VQA for document VLM training.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (22; te config) / Telugu
- **Content:** Image (rendered documents); Document OCR + layout + VQA; granularity Page (regions); Synthetic (translated/rendered)
- **Size:** 45,735 Telugu pages (37.8 GB) (page images)
- **Labels:** Yes - Region boxes + text + VQA
- **Licence:** CC BY-NC 4.0 (commercial: Not allowed; redistribution: Allowed (non-commercial))
- **Access:** Open (HF); needs: None
- **Source:** CognitiveLab; Adithya Kolavi et al. (Nayana)
- **Link:** https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025
- **Overlap:** Built from NayanaDocs-Indic-45k (gated, TOCR-098).
- **Existing catalogue:** TEL-OCR-008

### TOCR-098 - Nayana gated OCR/VQA family (Telugu configs)

Family of gated Hugging Face repositories from the Nayana project with Telugu-named files: source documents, 1M-page document OCR, translated DocMatix/PubMed pages and benchmarks.

- **Status:** GATED · **Distinct:** Y (gated family, counted once)
- **Language / script:** Multilingual (incl. Telugu) / Telugu
- **Content:** Image (documents); Document OCR / VQA / retrieval; granularity Page; Mostly synthetic (rendered/translated)
- **Size:** Telugu repos: Nayana-DocOCR-te-14k-v2-arxiv, Nayana-DocQA-te-10k-v1-docmatix, Nayana-DocOCR-ml-mr-ta-te-or-pa-15k-v1-pubmed, Nayana-DocOCR-mr-ta-te-or-pa-15k-v1-docmatix (+ multi-Indic in-14k and Indic-1m repos) (pages)
- **Labels:** Yes (per repo names) - NOT VERIFIED (gated)
- **Licence:** Mostly none declared / CC BY-NC (OCRBench) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Gated (manual); needs: HF login + manual approval
- **Source:** CognitiveLab; Nayana team
- **Link:** https://huggingface.co/Nayana-cognitivelab
- **Overlap:** Parents/variants of TOCR-097 and TOCR-099.

### TOCR-100 - Synthdog-Multilingual-100 - Telugu

SynthDoG-rendered document images with Wikipedia text in 100 languages (GoNotoKurrent font); 10,000 per non-Latin language.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (100; te) / Telugu
- **Content:** Image (rendered documents); Document OCR pre-training; granularity Page; Synthetic
- **Size:** 10,000 Telugu (per card; not counted) (page images)
- **Labels:** Yes - Rendered text (jsonl)
- **Licence:** Apache-2.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (images in one 11.3 GB tar.gz); needs: None
- **Source:** WueNLP (University of Wurzburg); Gregor Geigle et al.
- **Link:** https://huggingface.co/datasets/WueNLP/Synthdog-Multilingual-100
- **Paper:** https://gregor-ge.github.io/Centurio/

### TOCR-101 - Synthetic captchas library - Telugu 4-character

100,000 synthetic captcha images of 4 random Telugu characters with labels.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (26 scripts) / Telugu
- **Content:** Image (synthetic captchas); Character-sequence recognition; granularity 4 characters; Synthetic
- **Size:** 100,000 Telugu (images)
- **Labels:** Yes - labels.csv
- **Licence:** CC BY 4.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** Individual; remiai3
- **Link:** https://huggingface.co/datasets/remiai3/synthetic-captchas-library
- **Quality:** Random letters, not words; captcha noise.

### TOCR-102 - OCR Synthetic Benchmark Dataset for Indic Languages (EkStep / Tarento)

Synthetic OCR benchmark of 90K images with ground truth for 23 Indic languages.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Multilingual (23 incl. Telugu per paper) / Telugu
- **Content:** Image (rendered); OCR benchmark; granularity UNKNOWN; Synthetic
- **Size:** 90K images, 23 languages; Telugu table row 419 / 1,888 / 1,519 synthetic (column units not given) plus a real subset (images)
- **Labels:** Yes - Ground-truth text
- **Licence:** Paper CC BY 4.0; data UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No download link found; needs: UNKNOWN
- **Source:** EkStep Foundation; Tarento Technologies; Naresh Saini et al.
- **Link:** https://arxiv.org/abs/2205.02543
- **Paper:** https://arxiv.org/abs/2205.02543
- **Notes:** Paper calls it publicly available but gives no download link (arXiv HTML and GitHub searched 2026-11-11). Scene-text lines in 8 languages incl. Telugu were labelled with Google Vision OCR (machine labels).

### TOCR-103 - Kaggle: Final_Telugu_Manuscript_Data (yvenkatasriramreddy)

8.2 GB of PNG + TXT pairs named "chaos_mixed_NNNNN" in a 10k_Data folder; likely generated manuscript-style pages.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (manuscript-style pages); Page OCR; granularity Page; UNKNOWN (likely synthetic)
- **Size:** 8,181.8 MB; ~10K+ pairs (folder name) (image-text pairs)
- **Labels:** Yes - Text file per image
- **Licence:** CC0-1.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; Y. Venkata Sriram Reddy
- **Link:** https://www.kaggle.com/datasets/yvenkatasriramreddy/final-telugu-manuscript-data

### TOCR-105 - Telugu_OCR_Tesseract_Training (font box/tif training files)

Tesseract training files (tif + box) for many Telugu fonts to OCR old literature.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered text pages); Tesseract training; granularity Line/page; Synthetic
- **Size:** 363 MB repo; 293 files (files)
- **Labels:** Yes - Box files
- **Licence:** GPL-3.0 (commercial: Allowed under GPL; redistribution: Allowed under GPL)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; saikrishnawanted
- **Link:** https://github.com/saikrishnawanted/Telugu_OCR_Tesseract_Training

### TOCR-180 - Kaggle: rs synth indic data (ocrteamriad)

Synthetic Indic OCR records; Telugu presence NOT VERIFIED (no description).

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Multilingual (Telugu NOT VERIFIED) / Telugu
- **Content:** Image; OCR; granularity UNKNOWN; UNKNOWN
- **Size:** 23,294 MB of TFRecords (bytes)
- **Labels:** UNKNOWN - UNKNOWN
- **Licence:** Unknown / other (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; UNKNOWN
- **Link:** https://www.kaggle.com/datasets/ocrteamriad/rs-synth-indic-data
- **Notes:** 596 TFRecord shards with no language names in file paths; Telugu presence still NOT VERIFIED.

### TOCR-183 - PLATTER ScrabbleGAN synthetic Telugu handwritten pages

Synthetic handwritten Telugu words generated with ScrabbleGAN (trained on IIIT-INDIC-HW-WORDS) and composed into pages for detector pre-training.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (synthetic handwriting pages); Handwritten text detection pre-training; granularity Page / word; Synthetic (GAN)
- **Size:** 500,000 words on 11,879 pages (Table 2) (words / pages)
- **Labels:** Yes (generated) - Word boxes + text
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Not released (no link found); needs: No public link found
- **Source:** IIT Bombay; Kasuba et al.
- **Link:** https://arxiv.org/abs/2502.06172
- **Paper:** https://arxiv.org/abs/2502.06172
- **Overlap:** Generated from TOCR-002.

### TOCR-184 - GlotOCR Bench - Telugu (Telu)

OCR benchmark of real multilingual texts rendered as clean and old-document images across 100+ Unicode scripts; Telugu is one script config.

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Multilingual (100+ scripts; Telu config) / Telugu
- **Content:** Image (rendered text, clean + degraded); OCR evaluation; granularity Text block; Synthetic rendering of real text
- **Size:** UNKNOWN rows; Telugu file v1.0/Telu_000.parquet is 39.0 MB (image-text pairs)
- **Labels:** Yes - Source text (img_plain + img_old_document)
- **Licence:** other ("open-evaluation"): evaluation only, no training or redistribution (commercial: UNKNOWN; redistribution: Not allowed)
- **Access:** Gated (automatic); needs: HF login + tick "evaluation only" box
- **Source:** CIS, LMU Munich; CIS LMU (cisnlp)
- **Link:** https://huggingface.co/datasets/cis-lmu/GlotOCR-bench
- **Paper:** https://arxiv.org/abs/2604.12978
- **Quality:** Evaluation-only licence: cannot be used as training data.

### TOCR-185 - BhartiOCR - Telugu

Controlled synthetic OCR/document corpus: 28.5M image-text pairs, 71 Indian languages, 18 scripts, with a physical-degradation pipeline (paper textures, stamps, folds).

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Multilingual (71; telugu config) / Telugu
- **Content:** Image (synthetic documents); OCR pre-training; granularity Text block / line (per card); Synthetic
- **Size:** 500,000 Telugu pairs in 100 WebDataset shards (data/telugu/) (image-text pairs)
- **Labels:** Yes - Rendered text
- **Licence:** other: software/metadata Apache-2.0; fonts OFL/GPL+FE/Apache; source text multi-licence (commercial: Depends on source-text licences; redistribution: Depends on source-text licences)
- **Access:** Gated (manual); needs: HF login + manual approval
- **Source:** Individual (Faizaniqbal); HF user Faizaniqbal (real name NOT VERIFIED)
- **Link:** https://huggingface.co/datasets/Faizaniqbal/BhartiOCR

### TOCR-186 - IIIT-H Word Recognition Synthetic Dataset (Telugu)

Font-rendered word images of the 1,000 words in the IIIT-H Word Recognition Dataset, in 28 fonts, without degradation.

- **Status:** INACCESSIBLE · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered words, TIF); Word recognition; granularity Word; Synthetic
- **Size:** 28,000 word images (1,000 words x 28 fonts; 268 MB) (word images)
- **Labels:** Yes - Word label (1,000 classes)
- **Licence:** None stated (cite DAS 2010) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Download 404; page only on the Wayback Machine (researchweb.iiit.ac.in no longer resolves); needs: None when live
- **Source:** CVIT, IIIT Hyderabad; Pramod Sankar K., C. V. Jawahar, R. Manmatha
- **Link:** https://web.archive.org/web/20221127093102/https://researchweb.iiit.ac.in/~pramod_sankar/CandD.html
- **Paper:** DAS 2010: Nearest Neighbor based Collection OCR (Pramod Sankar K., Jawahar, Manmatha)
- **Download:** http://cvit.iiit.ac.in/docsearch/synthetic1000.tar (HTTP 404 on 2026-11-11)
- **Overlap:** Same 1,000-word vocabulary as TOCR-044.

### TOCR-223 - Tiny Multilingual CAPTCHA Library - Telugu (remiai3/tiny-captcha-library)

Synthetic 4-character CAPTCHA images with labels for 44 scripts; 10,000 per script.

- **Status:** VERIFIED · **Distinct:** N (smaller release of TOCR-101 generator)
- **Language / script:** Multilingual (44 scripts incl. Telugu) / Telugu
- **Content:** Image (synthetic CAPTCHAs); CAPTCHA / short text recognition; granularity 4-character string; Synthetic
- **Size:** 10,000 Telugu (images.zip 27.4 MB + labels.csv) (images)
- **Labels:** Yes - Text label (labels.csv)
- **Licence:** CC BY 4.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** remiai3; remiai3
- **Link:** https://huggingface.co/datasets/remiai3/tiny-captcha-library
- **Overlap:** Smaller release of the same generator as TOCR-101 (100,000 Telugu).


## Machine-labelled OCR (not human ground truth) (5)

_Image-text pairs whose text came from an OCR engine or an AI model, not a person. Use with care._

### TOCR-056 - harsha-desaraju/consensus-labelling

The 2.44M book line crops read by three OCR engines with an agreement tier and consensus text.

- **Status:** VERIFIED · **Distinct:** N (labels on TOCR-055) · **Parent:** TOCR-055
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed lines); Line recognition (silver labels); granularity Line; Real images, machine labels
- **Size:** 2,442,885 (line crops)
- **Labels:** Machine-generated - 3-engine OCR consensus (tier 1 = all agree ~1.8% in sampled shards)
- **Licence:** other (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/consensus-labelling

### TOCR-057 - harsha-desaraju/telugu-pdf-line-image-text

Tier 1-4 subset of the consensus-labelled book lines.

- **Status:** VERIFIED · **Distinct:** N (filter of TOCR-056) · **Parent:** TOCR-056
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed lines); Line recognition (silver labels); granularity Line; Real images, machine labels
- **Size:** 233,530 (230,000 / 3,530) (line crops)
- **Labels:** Machine-generated - OCR consensus text + tier
- **Licence:** MIT tag (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/telugu-pdf-line-image-text

### TOCR-063 - kailasa-ngpt/gemini-3.7-flash-ocr (Telugu pages)

Book page images with OCR text produced by a Gemini model (Devanagari, Tamil, Telugu).

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (Sanskrit/Hindi/Tamil/Telugu scripts) / Telugu
- **Content:** Image (book pages); Page OCR (silver labels); granularity Page; Real images, machine labels
- **Size:** 68 Telugu-script pages (13,117 total) (page images)
- **Labels:** Machine-generated - Gemini OCR output
- **Licence:** other (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Kailasa (uploader); kailasa-ngpt
- **Link:** https://huggingface.co/datasets/kailasa-ngpt/gemini-3.7-flash-ocr-26-aug-2026

### TOCR-084 - Indic-CIB: Indic Citizen Information Board dataset

Photos of rural citizen-information boards (e.g. MGNREGA) in 6 Indic languages with machine-generated OCR/table/QA annotations.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (hi, mr, te, kn, ta, ml) / Telugu
- **Content:** Image (scene boards); Board OCR, table extraction, VQA; granularity Image; Real
- **Size:** 1K-10K total; Telugu share NOT VERIFIED (images)
- **Labels:** Machine-generated - OCR text / tables / QA (machine-generated per card)
- **Licence:** Apache-2.0 (commercial: Allowed by tag; redistribution: Allowed by tag)
- **Access:** Open (HF); needs: None
- **Source:** Individual / research group; Litap007
- **Link:** https://huggingface.co/datasets/Litap007/indic-citizen-information-board
- **Notes:** HF filter on language column found no Telugu label; first rows are Hindi. Telugu share still NOT VERIFIED.

### TOCR-208 - ULCA (Bhashini) OCR corpus - Telugu (Project Anuvaad)

Telugu OCR corpora contributed to the national ULCA/Bhashini repository by Project Anuvaad (EkStep/Tarento): education domain and government press releases; collection method "web-scraping-ocr".

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (document pages / crops) + OCR text; Printed OCR; granularity UNKNOWN; Real (web-scraped documents)
- **Size:** 224,614 (education) + 1,243 (government press releases) (records (unit as reported by ULCA metrics; NOT VERIFIED))
- **Labels:** Yes - Text from OCR ("web-scraping-ocr"); human correction NOT VERIFIED
- **Licence:** UNKNOWN (ULCA requires permissive licences for contributions) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Listed in ULCA public metrics (2026-11-11); download not attempted; needs: ULCA account + dataset search request
- **Source:** Project Anuvaad (EkStep Foundation / Tarento) via ULCA, MeitY; Project Anuvaad
- **Link:** https://bhashini.gov.in/ulca/datasets
- **Overlap:** Same group as the EkStep synthetic benchmark (TOCR-102); overlap NOT VERIFIED.
- **Notes:** Evidence: evidence/discovery/ulca_reportdata.json. ULCA lists 28 OCR corpora across 12 languages; only these two are Telugu.


## Character / glyph classification (34)

_Single characters, vowel signs or digits sorted into classes. Good for character recognisers, not for word/line OCR._

### TOCR-021 - HPL Isolated Handwritten Telugu Character Dataset (HP Labs India)

Online (UNIPEN pen trajectories) and offline (bi-level TIFF rendered from the online data) isolated Telugu characters by native writers, with train/test subsets.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Online pen trajectories + offline bi-level images; Isolated character recognition; granularity Character; Real
- **Size:** ~270 samples x 166 characters (~45K); train ~170/char, test ~60/char (character samples)
- **Labels:** Yes - Character class with Unicode mapping
- **Licence:** HP Labs dataset licence (LipiTk site) (commercial: NOT VERIFIED; redistribution: NOT VERIFIED)
- **Access:** Landing page live; download host is an old IISc domain (see link check); needs: None
- **Source:** HP Labs India (hosted by MILE Lab, IISc); HP Labs India Pen-based Applications group
- **Link:** https://lipitk.sourceforge.net/datasets/teluguchardata.htm
- **Paper:** Prashanth L. et al., Elastic Matching of Online Handwritten Tamil and Telugu Scripts Using Local Features, ICDAR 2007
- **Download:** http://mile.ee.iisc.ernet.in/hpl/TelugCharacters/{Online,Offline}/hpl-telugu-iso-char-*.rar
- **Existing catalogue:** TEL-OCR-004

### TOCR-022 - Offline Handwritten Telugu Characters (Negi & M Rao, University of Hyderabad)

Scanned sheets of handwritten Telugu characters in boxes: 11 sheet layouts, 937 unique characters, 83 writers, 913 sheets (582 MB zip).

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned handwriting sheets); Character recognition; granularity Character (sheet layouts); Real
- **Size:** 913 sheets x ~90 characters (~82,000 characters); 937 classes (sheets / character cells)
- **Labels:** Yes (via sheet layout) - Character class per box (layout file)
- **Licence:** Creative Commons Attribution (IEEE page) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Gated (login); needs: Free IEEE DataPort account
- **Source:** University of Hyderabad; Atul Negi, Anish M. Rao
- **Link:** https://ieee-dataport.org/documents/offline-handwritten-telugu-characters
- **Paper:** https://doi.org/10.1109/indicon47234.2019.9028977
- **Overlap:** Same authors as UoH DSpace record (catalogue TEL-OCR-011); treated as one dataset.
- **Existing catalogue:** TEL-OCR-011

### TOCR-023 - UHTelHwCC: Telugu off-line handwritten character dataset (University of Hyderabad)

Paper describes creation of a Telugu offline handwritten character dataset (line removal, text-line and character extraction, labelling).

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real
- **Size:** UNKNOWN (character images)
- **Labels:** Yes (per paper) - Character class
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No public download found; needs: Contact authors
- **Source:** University of Hyderabad; NOT VERIFIED
- **Link:** https://doi.org/10.1007/978-3-031-07005-1_22
- **Paper:** https://doi.org/10.1007/978-3-031-07005-1_22
- **Overlap:** May extend TOCR-022 (same institution); not confirmed.

### TOCR-024 - Telugu Handwritten Character Dataset (Velpuru et al.)

Handwritten Telugu characters covering vowels, consonants, othulu and guninthamulu, labelled and mapped to Unicode (335.47 MB).

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real
- **Size:** UNKNOWN sample count (335.47 MB; up to 1,924 character classes described) (character images)
- **Labels:** Yes - Character class -> Unicode label
- **Licence:** CC BY 4.0 (DataCite) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Gated; needs: IEEE DataPort subscription/login
- **Source:** Academic (authors); Muni Sekhar Velpuru, Tejasree G, Ravi Kumar M
- **Link:** https://ieee-dataport.org/open-access/telugu-handwritten-character-dataset
- **Paper:** https://doi.org/10.1007/978-981-16-7330-6_74 ; https://doi.org/10.1145/3520439
- **Overlap:** Possibly the source of the three identical Kaggle uploads (TOCR-025) - NOT VERIFIED.

### TOCR-025 - Kaggle: "Final Dataset of Telugu Handwritten Characters" (3 identical uploads)

Telugu handwritten character images organised as Achulu/Hallulu/Guninthalu folders with Test1 etc.; uploaded three times with identical structure and size.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y (one dataset; uploads are mirrors)
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real
- **Size:** 353.7 MB each; sample count NOT VERIFIED (character images)
- **Labels:** Yes (folder labels) - Character class (folder)
- **Licence:** Unknown / Apache-2.0 (sarath02003) / Unknown - original licence not stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individuals; UNKNOWN (original creator not stated)
- **Link:** https://www.kaggle.com/datasets/sarath02003/telugu-handwritten
- **Overlap:** Three uploads are the same files (identical paths & size); origin suspected IEEE TOCR-024 (not verified).

### TOCR-026 - Telugu Handwritten Vowels (Muppalaneni et al.)

1,116 images of the 16 handwritten Telugu vowels (achchulu) drawn on a paint mobile app by writers aged 8-36; train 875 / test 241.

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (digital-ink drawn on phone, saved as JPG); Character recognition; granularity Character; Real
- **Size:** 1,116 (train 875 / test 241) (character images)
- **Labels:** Yes - Vowel class
- **Licence:** Creative Commons Attribution (DataCite) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Gated; needs: IEEE DataPort login
- **Source:** Academic (authors); Naresh Babu Muppalaneni, Prathima Chilukuri, D. R. Kumar Raja
- **Link:** https://ieee-dataport.org/documents/telugu-handwritten-vowels
- **Paper:** https://doi.org/10.3138/jmbs-27676-sujjuri

### TOCR-027 - Handwritten Telugu Gunintam క (Ka)

Handwritten samples of the guninthalu (vowel-sign combinations) of the consonant క.

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real
- **Size:** 516 samples (listing states 463 train / 103 test - figures do not add up) (character images)
- **Labels:** Yes - Character class
- **Licence:** Creative Commons Attribution (DataCite) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** DOI target 404s but ieee-dataport.org/node/1880 resolves (301) to the listing; login needed for files; needs: IEEE DataPort login
- **Source:** Academic (authors); Naresh Babu Muppalaneni, Repudi Ramesh
- **Link:** https://ieee-dataport.org/node/1880

### TOCR-028 - AsTel - Offline Assamese and Telugu Handwritten Characters

Offline handwritten character images collected with a paint mobile app: vowels, consonants and compound characters; 625 Telugu classes.

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Assamese; Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real
- **Size:** 625 Telugu classes (sample count NOT VERIFIED) (character images)
- **Labels:** Yes - Character class
- **Licence:** CC BY 4.0 (DataCite) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Gated (page HTTP 403 to scripts); needs: IEEE DataPort login
- **Source:** Academic (authors); Prarthana Dutta, Naresh Babu Muppalaneni
- **Link:** https://ieee-dataport.org/documents/astel-offline-assamese-and-telugu-handwritten-characters
- **Paper:** https://doi.org/10.1007/s13369-025-10169-y

### TOCR-029 - Handwritten Telugu Alphabet Dataset: Vowels and Consonants (Varnamala)

A single 300-dpi JPG grid of handwritten Telugu vowels and consonants; users crop cells themselves.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting, one sheet); Character recognition; granularity Character grid; Real
- **Size:** 1 image (52 characters) (sheet)
- **Labels:** Implicit (grid order) - None beyond layout
- **Licence:** CC BY 4.0 (DataCite) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Gated; needs: IEEE DataPort login
- **Source:** Individual; Arjun Ganadi
- **Link:** https://ieee-dataport.org/documents/handwritten-telugu-alphabet-dataset-vowels-and-consonants-varnamala-ocr-and-pattern
- **Quality:** Too small for training; illustrative only.
- **Existing catalogue:** TEL-OCR-012

### TOCR-030 - Sapta Lipi HCR: Handwritten Character Dataset for Seven Indic Scripts

Handwritten vowels, consonants and numerals for seven Indic scripts including Telugu; 100 samples per class, binarised 28x28.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (7 scripts incl. Telugu, Kannada, Malayalam, Bengali, Devanagari) / Multiple incl. Telugu
- **Content:** Image (handwriting, binarised); Character recognition; granularity Character; Real
- **Size:** 42,600 files total; Telugu share NOT VERIFIED (100 per class) (character images)
- **Labels:** Yes - Class folders
- **Licence:** CC BY 4.0 (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Open (Mendeley); needs: None
- **Source:** Academic (Mendeley depositor); NOT VERIFIED
- **Link:** https://data.mendeley.com/datasets/r5vjyykm3x/1

### TOCR-031 - Handwritten Notations of Digits and Fractions in Telugu Script

4,000 32x32 images of 8 Telugu fraction symbols (500 per class) from 80 writers, plus raw page scans and unprocessed crops.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Digit/fraction symbol recognition; granularity Character; Real
- **Size:** 4,000 (8 classes x 500); 80 writers (symbol images)
- **Labels:** Yes - Class folders
- **Licence:** CC BY-NC-SA 4.0 (commercial: Not allowed; redistribution: Allowed (non-commercial, share-alike))
- **Access:** Open (Mendeley); needs: None
- **Source:** Academic; Lakshmi Sravani Vempati
- **Link:** https://data.mendeley.com/datasets/mpjbr7nfv9/1

### TOCR-032 - CMATERdb 3.4.1 - Handwritten Telugu Numerals

Balanced set of 3,000 handwritten Telugu numerals (300 per digit), 32x32 RGB; TFDS split 2,500 train / 500 test.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Digit recognition; granularity Character (digit); Real
- **Size:** 3,000 (train 2,500 / test 500 in TFDS) (digit images)
- **Labels:** Yes - Digit class
- **Licence:** NOT STATED by original; GitHub mirror says Apache-2.0 (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open via TFDS / mirror; needs: None
- **Source:** CMATER Lab, Jadavpur University; Nibaran Das et al.
- **Link:** https://www.tensorflow.org/datasets/catalog/cmaterdb
- **Paper:** https://doi.org/10.1016/j.asoc.2011.11.030
- **Overlap:** Source for Telugu digits in MNIST-MIX (TOCR-033) and Kaggle hdr-datasets (TOCR-034); axlevisu repo "numbers" (3,000) likely the same.

### TOCR-033 - MNIST-MIX (Telugu digits subset)

Multi-language handwritten digit benchmark combining 10 scripts; Telugu part taken from CMATERdb.

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (derivative) · **Parent:** TOCR-032
- **Language / script:** Multilingual (10 languages incl. Telugu) / Telugu
- **Content:** Image (handwriting); Digit recognition; granularity Character (digit); Real
- **Size:** 3,000 Telugu digits (from CMATERdb) (digit images)
- **Labels:** Yes - Digit class
- **Licence:** NOT VERIFIED (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Paper live; needs: See paper
- **Source:** Academic; Weiwei Jiang
- **Link:** https://arxiv.org/abs/2004.03848
- **Paper:** https://arxiv.org/abs/2004.03848
- **Overlap:** Derivative of TOCR-032.

### TOCR-034 - Kaggle: Multilingual Handwritten Digits Datasets (Telugu-optimized.npz)

Augmented digit sets for English, Hindi, Telugu, Arabic (10,000 per digit); Telugu from CMATERdb (3K originals).

- **Status:** VERIFIED · **Distinct:** N (derivative) · **Parent:** TOCR-032
- **Language / script:** Multilingual / Telugu
- **Content:** Image (handwriting, augmented); Digit recognition; granularity Character (digit); Real + augmentation
- **Size:** 100,000 per language after augmentation (80K/20K) (digit arrays)
- **Labels:** Yes - Digit class (npz)
- **Licence:** Unknown (Kaggle) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; ayu8sh
- **Link:** https://www.kaggle.com/datasets/ayu8sh/hdr-datasets
- **Overlap:** Augmented derivative of TOCR-032.

### TOCR-035 - Kaggle: Telugu Vowel Dataset (6 vowels)

Handwritten samples of six Telugu vowels with a CSV feature version.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real
- **Size:** 8.7 MB; sample count NOT VERIFIED (character images)
- **Labels:** Yes - Class folders + CSV
- **Licence:** GPL-2.0 (Kaggle) (commercial: Allowed under GPL; redistribution: Allowed under GPL)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; Syam Kakarla
- **Link:** https://www.kaggle.com/datasets/syamkakarla/telugu-6-vowel-dataset

### TOCR-036 - Kaggle: Handwritten Telugu Characters (bhaveshkarapu)

Images of handwritten Telugu characters in class folders (trainingdata/<class>/).

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real (assumed)
- **Size:** 13.0 MB; sample count NOT VERIFIED (character images)
- **Labels:** Yes - Class folders
- **Licence:** Unknown (Kaggle) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; Bhavesh Karapu
- **Link:** https://www.kaggle.com/datasets/bhaveshkarapu/handwritten-telugu-characters

### TOCR-037 - Telugu letters dataset (645 classes; IJRES 2024)

Journal article presents a Telugu character dataset of 645 letters (18 achus, 38 hallus, 35 othulu, 34x16 guninthamulu, 10 digits).

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real (per paper)
- **Size:** 645 classes; sample count UNKNOWN (character images)
- **Labels:** Yes (per paper) - Character class
- **Licence:** Article CC BY 4.0; data licence UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Only the article is deposited (Zenodo); no data files; needs: Contact authors
- **Source:** Academic; Josyula Siva Phaniram, Mukkamalla Babu Reddy
- **Link:** https://zenodo.org/records/10530992
- **Paper:** https://doi.org/10.11591/ijres.v13.i1.pp217-226

### TOCR-038 - GitHub axlevisu/CNN-Telugu-OCR data folder

Repository containing 45,217 Telugu character images ("64characters"), 3,000 numeral images and 19,034 Devanagari characters.

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (compilation of TOCR-021 + TOCR-032)
- **Language / script:** Telugu / Telugu
- **Content:** Image (characters); Character recognition; granularity Character; UNKNOWN (source not documented)
- **Size:** 45,217 Telugu character images (64 classes) + 3,000 numerals (character images)
- **Labels:** Yes (folders) - Class folders
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; axlevisu
- **Link:** https://github.com/axlevisu/CNN-Telugu-OCR
- **Overlap:** 45,217 characters = HP Labs offline Telugu set count (TOCR-021, also copied in TOCR-224); 3,000 numerals = CMATERdb Telugu (TOCR-032).

### TOCR-039 - GitHub srikarym/OCR_Telugu_code - final_dataset.hdf5 (Google Drive)

Telugu character OCR project; README links a Google Drive HDF5 dataset of main characters and vattu/gunintam.

- **Status:** INACCESSIBLE · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (characters); Character recognition; granularity Character; UNKNOWN
- **Size:** UNKNOWN (character images)
- **Labels:** Yes (per README) - Character class (HDF5)
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Drive link returns HTTP 404 (2026-11-11); needs: Google Drive link
- **Source:** Individual / academic project; srikarym
- **Link:** https://github.com/srikarym/OCR_Telugu_code
- **Download:** https://drive.google.com/file/d/1ucYy_Emht9MRLjQPaUydSKZzN1ZQ77dd/view (NOT VERIFIED)

### TOCR-040 - GitHub Mitradatta/Telugu-Character-Recognition - self-collected dataset (not released)

Project states it collected ~250 handwritten samples per Telugu character from people of different ages; data not in the repository.

- **Status:** INACCESSIBLE · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Character recognition; granularity Character; Real
- **Size:** ~250 per character (claimed) (character images)
- **Labels:** UNKNOWN - UNKNOWN
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Data not public (repo has README only); needs: Not released
- **Source:** Individual; Mitradatta
- **Link:** https://github.com/Mitradatta/Telugu-Character-Recognition

### TOCR-047 - UHTelPCC: Telugu Printed Character Dataset (University of Hyderabad)

Printed Telugu character images extracted from books printed 1950-1990, with train/test split and KNN/MLP/CNN baselines (99.68% CNN).

- **Status:** INACCESSIBLE · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed characters); Printed character recognition; granularity Character; Real
- **Size:** ~70,000 samples in 325 classes with train/val/test split (paper abstract via search index; NOT VERIFIED against data) (character images)
- **Labels:** Yes - Character class
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Project page 404; repository 503; needs: Contact authors
- **Source:** University of Hyderabad (SCIS); Rakesh Kummari, Chakravarthy Bhagvati
- **Link:** http://scis.uohyd.ac.in/~chakcs/UHTelPCC.html
- **Paper:** https://doi.org/10.1007/978-981-13-9187-3_3

### TOCR-048 - UHIndicPCwS: University of Hyderabad Indic Printed Character with Style

Printed character images for six scripts (Tamil, Telugu, Kannada, Malayalam, Gujarati, Odia) in one Python pickle with class labels.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (6 scripts incl. Telugu) / Telugu
- **Content:** Image arrays (printed characters); Printed character recognition; granularity Character; Real (assumed)
- **Size:** UNKNOWN (Telugu share not stated) (character images)
- **Labels:** Yes - Class labels (scriptname_classnumber)
- **Licence:** NOT STATED (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open download (HTTP 200); needs: None
- **Source:** University of Hyderabad (SCIS); NOT VERIFIED (Bhagvati group)
- **Link:** https://scis.uohyd.ac.in/~chakcs/datasets/UHIndicPCwS.html
- **Download:** https://scis.uohyd.ac.in/~chakcs/datasets/UHIndicPCwS.pkl (572 MB)
- **Quality:** Python pickle - must not be loaded with pickle.load from untrusted source; inspect safely.

### TOCR-104 - banti_training (Telugu OCR glyph training data)

Glyph images used to train the banti Telugu OCR CNN (Achanta & Hastie).

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (glyphs); Glyph classification; granularity Glyph; UNKNOWN (rendered/segmented)
- **Size:** 467 image files (data48 + numbers) (glyph images / sheets)
- **Labels:** Yes (folder/naming) - Glyph class
- **Licence:** None stated (code repos Apache-2.0) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Stanford (authors); Rakesh Achanta, Trevor Hastie
- **Link:** https://github.com/rakeshvar/banti_training
- **Paper:** https://arxiv.org/abs/1509.05962
- **Overlap:** Paper describes 460 classes x 160 samples; repo may hold a subset.

### TOCR-107 - Telugu character database (Konkimalla et al., ICIP 2018)

Database of Telugu characters covering all vattu/gunintam combinations: 17,387 categories, ~560 samples each (6.76M train / 0.97M val).

- **Status:** UNVERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (32x32 characters); Character recognition; granularity Character; UNKNOWN (likely rendered)
- **Size:** 17,387 classes; 6,757,044 train + 972,309 val (+test) (character images)
- **Labels:** Yes - Character class
- **Licence:** UNKNOWN (paper promises code release) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Original data location not found; needs: UNKNOWN
- **Source:** IIT Hyderabad; Chandra Prakash Konkimalla, Sumohana Channappayya et al.
- **Link:** https://arxiv.org/abs/1711.07245
- **Paper:** https://arxiv.org/abs/1711.07245
- **Overlap:** Same abstract appears on IEEE DataPort a1kv-rj60 (TOCR-108) under a different author.

### TOCR-108 - "OCR Telugu Image Dataset" (IEEE DataPort a1kv-rj60)

IEEE DataPort entry whose abstract repeats the Konkimalla et al. 17,387-class database description.

- **Status:** GATED · **Distinct:** N (suspected re-upload) · **Parent:** TOCR-107
- **Language / script:** Telugu / Telugu
- **Content:** Image (characters); Character recognition; granularity Character; UNKNOWN
- **Size:** UNKNOWN (abstract cites 6,757,044 train / 972,309 val) (character images)
- **Labels:** UNKNOWN - UNKNOWN
- **Licence:** CC BY 4.0 (DataCite) (commercial: As stated; redistribution: As stated)
- **Access:** Gated; needs: IEEE DataPort login
- **Source:** Boon IT Solutions (per search snippet); Kadavakollu Venkateswara Rao
- **Link:** https://ieee-dataport.org/documents/ocr-telugu-image-dataset
- **Overlap:** Suspected re-upload of TOCR-107 (identical abstract, different author); one search engine described it as handwritten shopping lists - contents NOT VERIFIED.
- **Quality:** DataCite abstract repeats the 17,387-class description; search engines describe the listing as ~100 handwritten shopping-list photos with a ~17 KB file. Contents NOT VERIFIED.

### TOCR-119 - Telugu palm-leaf character crops (Sriram1908/TeluguManuscriptOCRandTextReconstruction)

Segmented palm-leaf character images mapped to their characters, plus handwritten samples, used for a manuscript OCR project.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (palm-leaf characters); Character recognition; granularity Character; Real (+ own handwriting)
- **Size:** 1,777 images (mappings/*) (character images)
- **Labels:** Yes (folder mapping) - Character class
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; Sriram1908
- **Link:** https://github.com/Sriram1908/TeluguManuscriptOCRandTextReconstruction

### TOCR-120 - Telugu palm-leaf 3D character dataset (2016 paper)

Paper builds a 3D (depth) dataset of Telugu palm-leaf text including compound characters for recognition.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** 3D profile / image (palm leaf); Character recognition; granularity Character; Real
- **Size:** UNKNOWN (characters)
- **Labels:** Yes (per paper) - Character class
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No public release found; needs: Contact authors
- **Source:** Academic (GRIET-hosted PDF); NOT VERIFIED
- **Link:** https://www.griet.ac.in/images/1-s2.0-S2215098616303627-main.pdf
- **Paper:** https://doi.org/10.1016/j.jestch.2016.06.006 (NOT VERIFIED)

### TOCR-143 - On-line Handwriting Recognition of Indian Scripts - The First Benchmark (ICFHR 2010)

Online handwriting benchmark from ISI Kolkata / HP Labs; scripts and Telugu inclusion NOT VERIFIED.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Indian scripts (Telugu NOT VERIFIED) / Telugu
- **Content:** Online pen trajectories; Online handwriting recognition; granularity Character / word; Real
- **Size:** UNKNOWN (UNKNOWN)
- **Labels:** Yes (per paper) - NOT VERIFIED
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No release found; needs: UNKNOWN
- **Source:** ISI Kolkata; HP Labs India; T. Mondal, U. Bhattacharya, S. K. Parui, K. Das, D. Mandalapu
- **Link:** https://dblp.org/rec/conf/icfhr/MondalBPDM10
- **Paper:** https://doi.org/10.1109/ICFHR.2010.39

### TOCR-188 - Handwritten Telugu character corpus (JASTT 2025, unreleased)

33,496 handwritten Telugu characters collected from schoolchildren and adults; the authors say it will be released separately.

- **Status:** INACCESSIBLE · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwritten characters); Character recognition; granularity Character; Real
- **Size:** 33,496 characters (character images)
- **Labels:** Yes (per paper) - Character class
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Announced for later release; needs: Not released
- **Source:** Sri Vasavi Engg. College; Sreenidhi IST; Vardhaman CE; IIIT Nagpur et al.; Mukkoti Vishnu Vardhan, E Jayakiran Reddy, N Srinivas Reddy et al.
- **Link:** https://jastt.org/index.php/jasttpath/article/view/267
- **Paper:** https://jastt.org/index.php/jasttpath/article/view/267
- **Overlap:** Experiments in the paper use Kaggle 6-vowel set (TOCR-035), not this corpus.

### TOCR-212 - Telugu palm-leaf character database (Amrita, 2012)

Paper describes a data acquisition system and a database of isolated Telugu characters from palm-leaf manuscripts.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (palm-leaf characters); Character recognition; granularity Character; Real
- **Size:** UNKNOWN (character images)
- **Labels:** Yes (per paper) - Character class
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No public release found; needs: Contact authors
- **Source:** Amrita Vishwa Vidyapeetham; NOT VERIFIED
- **Link:** https://www.amrita.edu/publication/a-data-acquisition-and-analysis-system-for-palm-leaf-documents-in-telugu/
- **Overlap:** Related palm-leaf work: TOCR-117, 118, 119, 120, 228.

### TOCR-224 - GitHub medini-r/teluguChar (copy of HP Labs offline Telugu characters)

45,217 TIFF character images in hpl-telugu-iso-char-offline/usr_* folders.

- **Status:** VERIFIED · **Distinct:** N (mirror of TOCR-021) · **Parent:** TOCR-021
- **Language / script:** Telugu / Telugu
- **Content:** Image (characters); Character recognition; granularity Character; Real
- **Size:** 45,217 images (character images)
- **Labels:** Yes (file naming) - Character class in file name
- **Licence:** None stated (HP Labs licence applies) (commercial: Per HP Labs licence; redistribution: Not the uploader's to grant)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; medini-r
- **Link:** https://github.com/medini-r/teluguChar
- **Overlap:** Copy of HP Labs offline set (TOCR-021); same count as TOCR-038.

### TOCR-225 - GitHub madhav007VDEV/telugu-ocr-realtime - character image set

650 images in 13 class folders (50 each) used to train a small Telugu character model.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (characters); Character recognition; granularity Character; UNKNOWN
- **Size:** 650 images (13 classes x 50) (character images)
- **Labels:** Yes (folder = class index) - Class index (mapping to letters NOT VERIFIED)
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; madhav007VDEV
- **Link:** https://github.com/madhav007VDEV/telugu-ocr-realtime

### TOCR-228 - GitHub keerthan-381 - Telugu palm-leaf handwritten character crops (DATA_LABELS_FINAL.zip)

Zip of 9,131 character images from Telugu palm-leaf document images, organised for character classification.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (palm-leaf characters); Character recognition; granularity Character; Real
- **Size:** 9,131 images (zip central directory, 8.7 MB) (character images)
- **Labels:** Yes (folder labels, per name) - Character class (NOT VERIFIED)
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual (student project); keerthan-381
- **Link:** https://github.com/keerthan-381/HandWritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images
- **Overlap:** Same project title as rejected code-only repo TOCR-174; possibly related to TOCR-119 palm-leaf crops.

### TOCR-229 - GitHub aceveggie/TeluguTFRecords - Telugu character data in MNIST format

Telugu character images stored as MNIST-style idx files and TFRecords (train-images-idx3-ubyte 13.2 MB; t10k files).

- **Status:** PARTIALLY VERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (characters, idx/TFRecord); Character recognition; granularity Character; UNKNOWN
- **Size:** UNKNOWN (image size not stated) (character images)
- **Labels:** Yes (idx label files) - Class index
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; aceveggie
- **Link:** https://github.com/aceveggie/TeluguTFRecords
- **Overlap:** Source of the characters NOT VERIFIED (possibly HP Labs TOCR-021).


## Layout / detection (no transcription) (11)

_Boxes or regions (text blocks, tables, lines) without the text itself. Not OCR transcription data._

### TOCR-016 - TEXTRON INDIC datasets - Telugu handwritten pages

Word bounding-box annotations for 85 handwritten Telugu pages (from PHDIndic_11) for text detection.

- **Status:** VERIFIED · **Distinct:** N (annotation layer on TOCR-015) · **Parent:** TOCR-015
- **Language / script:** Multilingual (Devanagari, Kannada, Telugu handwritten) / Telugu
- **Content:** Image (handwritten pages); Text detection; granularity Word boxes on pages; Real
- **Size:** 85 Telugu pages (page images)
- **Labels:** Yes (boxes only) - "text x y w h" word boxes; no transcription
- **Licence:** GPL-3.0 (HF tag) (commercial: Allowed under GPL; redistribution: Allowed under GPL)
- **Access:** Open (HF); needs: None
- **Source:** IIT Bombay LEAP OCR team; Dhruv Kudale, Badri Vishal Kasuba et al.
- **Link:** https://huggingface.co/datasets/badrivishalk/TEXTRON_INDIC_DATASETS
- **Overlap:** Pages from PHDIndic_11.

### TOCR-019 - Roboflow Universe: teluguocr/telugu-handwritten-ocr

Small Roboflow computer-vision project labelled "Telugu handwritten OCR" (3 classes per search snippet).

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Object detection / classification (3 classes); granularity UNKNOWN; Real (assumed)
- **Size:** 386 images (workspace listing) (images)
- **Labels:** Yes (object detection, 3 classes per earlier snippet) - Boxes (classes NOT VERIFIED)
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Page returns HTTP 403 to automated clients; needs: Roboflow account
- **Source:** Individual (Roboflow user teluguocr); UNKNOWN
- **Link:** https://universe.roboflow.com/teluguocr/telugu-handwritten-ocr

### TOCR-020 - Roboflow Universe: centurion-university-n60kx/telugu-handwritten

Roboflow object-detection project of Telugu handwriting by a Centurion University account.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Object detection; granularity UNKNOWN; Real (assumed)
- **Size:** UNKNOWN (images)
- **Labels:** Yes (boxes) - NOT VERIFIED - NOT VERIFIED
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** HTTP 403 to automated clients; needs: Roboflow account
- **Source:** Centurion University (account); UNKNOWN
- **Link:** https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten

### TOCR-081 - MIST - Multilingual Incidental Scene Text (Telugu frames)

GoPro road-scene frames with polygon text annotations and script tags in 11 scripts.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (11 scripts) / Telugu
- **Content:** Image (scene); Scene text detection; script ID; granularity Scene (polygons); Real
- **Size:** ~12K scenes total; 193 Telugu-tagged test frames (scene images)
- **Labels:** Yes (polygons + script; no transcription in sampled files) - Polygons, script, care flag
- **Licence:** Research use; ask authors for commercial (commercial: Not without permission; redistribution: Raw imagery: ask authors)
- **Access:** Open (HF); needs: None
- **Source:** CVIT, IIIT Hyderabad; Saumya Mundra, Ajoy Mondal, C. V. Jawahar
- **Link:** https://huggingface.co/datasets/Saumya-Mundra/MIST-Dataset
- **Overlap:** Same road footage as TOCR-079/080.

### TOCR-109 - IndicDLP - Telugu pages (document layout parsing)

119,806 human-annotated document images in 11 Indic languages + English across 12 domains, with 42 layout region classes; no transcriptions.

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Multilingual (12) / Telugu
- **Content:** Image (documents: novels, textbooks, newspapers, forms ...); Document layout parsing; granularity Page regions; Real
- **Size:** 119,806 total; Telugu 7.2% (~8,600 pages, computed from README share) (page images)
- **Labels:** Yes (layout only) - Region boxes, 42 classes (YOLO/COCO)
- **Licence:** MIT (repo) / CC BY 4.0 (Zenodo) (commercial: Allowed; redistribution: Allowed)
- **Access:** Gated on HF; AIKosh/Zenodo routes; needs: HF: login + accept terms; AIKosh download
- **Source:** IIT Madras (AI4Bharat); IIIT Hyderabad; Oikantik Nath, Sahithi Kukkala, Mitesh Khapra, Ravi Kiran Sarvadevabhatla
- **Link:** https://cvit.iiit.ac.in/research/projects/cvit-projects/indicdlp
- **Paper:** https://arxiv.org/abs/2512.20236
- **Download:** https://aikosh.indiaai.gov.in/home/datasets/details/indicdlp.html (via AIKosh)
- **Overlap:** Block OCR eval set (TOCR-060) and dlp-sample (TOCR-110) derived from it.
- **Existing catalogue:** TEL-OCR-015

### TOCR-110 - onath/dlp-sample (IndicDLP sample, telugu config)

Small public sample of IndicDLP pages with layout labels, configs per language and domain.

- **Status:** VERIFIED · **Distinct:** N (sample) · **Parent:** TOCR-109
- **Language / script:** Multilingual / Telugu
- **Content:** Image (documents); Layout parsing; granularity Page regions; Real
- **Size:** 36 Telugu pages (12/12/12) (page images)
- **Labels:** Yes (layout) - Region boxes
- **Licence:** CC BY 4.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** IIT Madras; Oikantik Nath
- **Link:** https://huggingface.co/datasets/onath/dlp-sample
- **Overlap:** Sample of TOCR-109.

### TOCR-111 - Indiscapes / Indiscapes2 (historical Indic manuscript layout)

Region-level layout annotations (text lines, holes, decorations, page boundaries) on historical Indic palm-leaf and paper manuscripts.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (Sanskrit and other Indic; Telugu share NOT VERIFIED) / Multiple (Telugu presence NOT VERIFIED)
- **Content:** Image (manuscripts); Layout parsing; granularity Page regions; Real
- **Size:** UNKNOWN (Telugu) (manuscript pages)
- **Labels:** Yes (layout) - Instance polygons
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Project site live; needs: UNKNOWN
- **Source:** CVIT/IHDIA, IIIT Hyderabad; Abhishek Prusty, Sowmya Aitha, Ravi Kiran Sarvadevabhatla et al.
- **Link:** https://ihdia.iiit.ac.in/
- **Paper:** https://arxiv.org/abs/1912.07025
- **Existing catalogue:** TEL-OCR-013

### TOCR-112 - MUSTARD - Telugu tables (table structure recognition)

Printed/scanned/scene tables from magazines in 13 languages labelled with OTSL structure sequences; ~100 Telugu tables.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (13) / Telugu
- **Content:** Image (tables); Table structure recognition; granularity Table; Real
- **Size:** ~100 Telugu tables (table images)
- **Labels:** Yes (structure only) - OTSL tokens (no cell text)
- **Licence:** MIT (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** IIT Bombay LEAP OCR team; Dhruv Kudale, Badri Vishal Kasuba et al.
- **Link:** https://huggingface.co/datasets/badrivishalk/MUSTARD
- **Paper:** https://arxiv.org/abs/2503.11932

### TOCR-191 - Roboflow Universe: iitbresearchwork/telugu-ocr

Telugu OCR object-detection project (1 class) from an IIT Bombay research workspace that also hosts Tamil/Kannada OCR and "PhDIndic11" projects.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image; Text detection; granularity Word boxes (1 class); Real (NOT VERIFIED)
- **Size:** UNKNOWN (images)
- **Labels:** Yes (1 class) - Boxes, no transcription (per listing)
- **Licence:** CC BY 4.0 (listing) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Page blocks scripts (HTTP 403); facts from search snippets; needs: Roboflow account
- **Source:** IIT Bombay research workspace (iitbresearchwork); iitbresearchwork
- **Link:** https://universe.roboflow.com/iitbresearchwork/telugu-ocr
- **Overlap:** Suspected word-box annotation of PHDIndic_11 Telugu pages (TOCR-015): same workspace has "Malayalam PhDIndic11" and PLATTER used PHDIndic_11 Telugu word boxes; NOT VERIFIED.

### TOCR-192 - Roboflow Universe: vihaveai/telugu-info-detector

Telugu text/info detection project; listing mentions related "telugu-words", "kannada-words" and "part-of-mcq" sets.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image; Text detection; granularity Region; UNKNOWN
- **Size:** UNKNOWN (images)
- **Labels:** Yes (detection) - Boxes (classes NOT VERIFIED)
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Page blocks scripts (HTTP 403); needs: Roboflow account
- **Source:** Vihave AI; vihaveai
- **Link:** https://universe.roboflow.com/vihaveai/telugu-info-detector

### TOCR-194 - Roboflow Universe: centurion-university-n60kx/telugu-handwritten-project (+ teugu-words-labelling)

Small Telugu handwritten object-detection projects from the same Centurion University workspace as TOCR-020.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Handwritten text detection; granularity Word / character boxes (NOT VERIFIED); Real
- **Size:** 13 images (telugu-handwritten-project) (images)
- **Labels:** Yes (detection) - Boxes
- **Licence:** CC BY 4.0 (listing) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Page blocks scripts (HTTP 403); needs: Roboflow account
- **Source:** Centurion University (workspace); centurion-university-n60kx
- **Link:** https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten-project
- **Overlap:** Same workspace as TOCR-020; may share images.


## Script identification (10)

_Images labelled only with which script/language they contain._

### TOCR-015 - PHDIndic_11 - Telugu pages

Page-level handwritten document images in 11 official Indic scripts (1,458 pages by 463 writers) for handwritten script identification.

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Multilingual (11 scripts incl. Telugu) / Telugu
- **Content:** Image (scanned handwriting, TIFF); Script identification; granularity Page; Real
- **Size:** 1,458 pages total; Telugu 85 pages with 5,503 word boxes (PLATTER, arXiv 2502.06172, Table 3) (page images)
- **Labels:** Script label only - Script class
- **Licence:** Creative Commons Attribution (IEEE page) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Gated (login); needs: Free IEEE DataPort account
- **Source:** Aliah University; West Bengal State University; Jadavpur University; Univ. South Dakota; Obaidullah Sk, Chayan Halder, K. C. Santosh, Nibaran Das, Kaushik Roy
- **Link:** https://ieee-dataport.org/open-access/phdindic11-page-level-handwritten-document-image-dataset-11-official-indic-scripts
- **Paper:** https://doi.org/10.1007/s11042-017-4373-y
- **Overlap:** Telugu pages reused in TEXTRON (TOCR-016) and HW-WILD (TOCR-010).

### TOCR-113 - MDIW-13 - Multi-lingual Document Image database for script identification

1,135 printed and handwritten documents in 13 scripts incl. Telugu, segmented into 13,979 lines and 86,655 words.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (13 scripts) / Telugu
- **Content:** Image (printed + handwritten documents); Script identification; granularity Document / line / word; Real
- **Size:** 1,135 documents total; Telugu share NOT VERIFIED (document images)
- **Labels:** Script labels - Script class
- **Licence:** CC BY 4.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (Zenodo); needs: None
- **Source:** Academic consortium; Miguel A. Ferrer et al.
- **Link:** https://doi.org/10.5281/zenodo.6376096
- **Paper:** https://arxiv.org/abs/2405.18924
- **Existing catalogue:** TEL-OCR-016

### TOCR-114 - Kaggle: Indian Scripts (12-script image classification)

10,000+ images (250x250) of 12 Indian scripts incl. Telugu in train/test folders for script classification.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (12) / Telugu
- **Content:** Image; Script identification; granularity Image; UNKNOWN
- **Size:** 13,792 total (Kaggle); Telugu share NOT VERIFIED (images)
- **Labels:** Script label - Folder
- **Licence:** CC0-1.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; Abhishek Subhash Swami
- **Link:** https://www.kaggle.com/datasets/abhisheksubhashswami/indian-scripts
- **Notes:** Kaggle file-list API returned only the first ~1,200 files (Brahmi, Assamese, Devanagari test folders); Telugu folder size still NOT VERIFIED.

### TOCR-115 - Kaggle: english hindi telugu text images (akash034)

Screenshots of English, Hindi and Telugu text in language folders.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** English; Hindi; Telugu / Telugu
- **Content:** Image (screenshots); Script / language identification; granularity Image; Real (screenshots)
- **Size:** 153.2 MB; count NOT VERIFIED (images)
- **Labels:** Language folder only - Language label
- **Licence:** Unknown (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; akash034
- **Link:** https://www.kaggle.com/datasets/akash034/english-hindi-telugu-text-images

### TOCR-116 - lipika-eval (font/script identification images)

Rendered text images labelled with font family and script for 13 scripts; 351 Telugu images.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (13 scripts) / Telugu
- **Content:** Image (rendered); Font / script identification; granularity Image; Synthetic
- **Size:** 351 Telugu (6,876 total) (images)
- **Labels:** Font + script labels - No transcription
- **Licence:** Apache-2.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** Loopdesk AI; loopdesk-ai
- **Link:** https://huggingface.co/datasets/loopdesk-ai/lipika-eval

### TOCR-187 - Multilingual multimodal scene-text dataset (NIT Silchar, ICON 2023) - Telugu

Scene images in Assamese, English, Malayalam and Telugu with text boxes labelled by language, built for YOLOv5 language detection.

- **Status:** UNVERIFIED · **Distinct:** Y
- **Language / script:** Assamese; English; Malayalam; Telugu / Telugu
- **Content:** Image (scene / web images; some created with Canva); Text detection with language labels; granularity Text region; Real + designed images
- **Size:** 1,000 Telugu images (4,000 total) (images)
- **Labels:** Yes - Bounding box + language class (no transcription)
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No release link in paper; needs: Contact authors
- **Source:** NIT Silchar; Nihar Jyoti Basisth, Eisha Halder, Tushar Sachan, Advaitha Vetagiri, Partha Pakray
- **Link:** https://aclanthology.org/2023.icon-1.16.pdf
- **Paper:** https://aclanthology.org/2023.icon-1.16.pdf

### TOCR-193 - Roboflow Universe: fives-data-tpoav/telugu

Single-class ("Telugu") detection dataset; no description.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image; Telugu text detection; granularity Region; UNKNOWN
- **Size:** UNKNOWN (images)
- **Labels:** Yes (1 class) - Boxes labelled "Telugu"
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Page blocks scripts (HTTP 403); needs: Roboflow account
- **Source:** Individual workspace; fives-data-tpoav
- **Link:** https://universe.roboflow.com/fives-data-tpoav/telugu

### TOCR-210 - CVSI-2015 - ICDAR 2015 Competition on Video Script Identification (Telugu)

Cropped word images from video frames (mostly overlaid news/sports captions, some scene text) in 10 scripts incl. Telugu, for script identification.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (10 scripts incl. Telugu) / Telugu
- **Content:** Image (video-frame word crops); Script identification; granularity Word; Real
- **Size:** >=1,000 word images per script (60/10/30 train/val/test) (word images)
- **Labels:** Script label only - Script class (no transcription)
- **Licence:** Research only; commercial use not allowed (organiser terms) (commercial: Not allowed; redistribution: UNKNOWN)
- **Access:** Organiser page reset connections to scripts (2026-11-11); facts from indexed page text; needs: Registration with organisers
- **Source:** Griffith University; ISI Kolkata (organisers); Nabin Sharma, Ranju Mandal, Rabi Sharma, Umapada Pal, Michael Blumenstein
- **Link:** https://www.ict.griffith.edu.au/cvsi2015/Dataset.php
- **Paper:** ICDAR 2015 competition report (Sharma, Mandal, Sharma, Pal, Blumenstein) - DOI NOT VERIFIED

### TOCR-219 - Handwritten Indic script identification data (offline + online, Bhunia et al. 2018)

Character- and word-level handwritten samples in English + 6 Indic scripts (search-indexed text lists Telugu) in offline and online form.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Multilingual (7 scripts; Telugu per search snippet, NOT VERIFIED in abstract) / Telugu
- **Content:** Image + online pen data; Script identification; granularity Character / word; Real
- **Size:** ~10,000 Telugu samples (search snippet; NOT VERIFIED) (samples)
- **Labels:** Script label - Script class
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No release link in paper; needs: Contact authors
- **Source:** ISI Kolkata; IIT Roorkee (NOT VERIFIED); Ayan Kumar Bhunia, Subham Mukherjee, Aneeshan Sain, Ankan Kumar Bhunia, Partha Pratim Roy, Umapada Pal
- **Link:** https://arxiv.org/abs/1802.08568
- **Paper:** https://arxiv.org/abs/1802.08568

### TOCR-220 - Handwritten script identification text lines (Singh et al., 2020)

800 handwritten text lines in Gujarati, Kannada, Malayalam, Oriya, Tamil, Telugu, Urdu and Roman.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Multilingual (8 scripts incl. Telugu) / Telugu
- **Content:** Image (handwritten lines); Script identification; granularity Line; Real
- **Size:** 800 lines total; Telugu share UNKNOWN (text lines)
- **Labels:** Script label - Script class
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No release link; needs: Contact authors
- **Source:** Jadavpur University (NOT VERIFIED); Pawan Kumar Singh, Iman Chatterjee, Ram Sarkar, Mita Nasipuri
- **Link:** https://arxiv.org/abs/2009.07433
- **Paper:** https://arxiv.org/abs/2009.07433


## Text-in-image benchmark (VQA / document understanding) (9)

_Question-answer or retrieval sets built on text-heavy images. Tests reading, but labels are not transcriptions._

### TOCR-099 - NayanaBench (Telugu)

Multilingual document VQA benchmark combining OCR, layout and QA; 200 examples per language including Telugu.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (22) / Telugu
- **Content:** Image (documents); Document VQA / OCR evaluation; granularity Page; Synthetic/rendered (NOT VERIFIED)
- **Size:** 200 Telugu examples (QA items)
- **Labels:** Yes - QA + OCR/layout
- **Licence:** None declared (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** CognitiveLab; Nayana team
- **Link:** https://huggingface.co/datasets/Nayana-cognitivelab/NayanaBench

### TOCR-128 - HW-MLVQA (handwritten multilingual document VQA)

1,600 handwritten pages with 2,400 QA pairs for evaluating OCR-aware VQA; language list does not mention Telugu in the paper text.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Multilingual (Telugu NOT VERIFIED) / Telugu
- **Content:** Image (handwriting); Handwritten document VQA; granularity Page; Real
- **Size:** 1,600 pages total; Telugu UNKNOWN (pages)
- **Labels:** QA pairs - Question-answer
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No dataset link in paper; no HF repo found (searched 2026-11-11); needs: UNKNOWN
- **Source:** CVIT, IIIT Hyderabad; Aniket Pal, Ajoy Mondal, Minesh Mathew, C. V. Jawahar
- **Link:** https://arxiv.org/abs/2507.15655
- **Paper:** https://arxiv.org/abs/2507.15655

### TOCR-130 - IndicVisionBench (OCR task)

~5K images and 37K QA pairs across English + 10 Indian languages covering OCR, multimodal MT and VQA.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (English + 10 Indian incl. te tag) / Telugu
- **Content:** Image; OCR + VQA + MMT evaluation; granularity Image; Real
- **Size:** ~5K images total; Telugu: 89 OCR pages (Wikisource), 69 VQA-Indic, 106 parallel VQA (images)
- **Labels:** Yes - OCR text / QA
- **Licence:** None declared on HF (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Krutrim AI Labs; Krutrim AI Labs
- **Link:** https://huggingface.co/datasets/krutrim-ai-labs/IndicVisionBench
- **Paper:** https://arxiv.org/abs/2511.04727
- **Overlap:** Copies: AtharvImmverse/IndicVisionBench; lalit-03/IndicVisionBench (gated). OCR track Telugu pages likely the same 89 Wikisource pages as ORB-Indic (TOCR-172); both derive from TOCR-049.

### TOCR-131 - MInfoVisQA (multilingual infographic VQA)

Localised chart/table renders in 24 languages with QA (evaluation split only).

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (24 incl. te) / Telugu
- **Content:** Image (rendered charts/tables); Visual QA; granularity Image; Synthetic (rendered)
- **Size:** 8,960 rows; 384 with Telugu images (image_language=te) (images)
- **Labels:** QA - Question-answer
- **Licence:** other (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Academic; arnodjiang
- **Link:** https://huggingface.co/datasets/arnodjiang/MInfoVisQA

### TOCR-132 - adaption-multilingual-doc-qa (magazines VQA remaster)

Multilingual QA on magazine page images asking for specific details (page numbers, names, dates).

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (45; te tag) / Telugu
- **Content:** Image (magazine pages); Document QA; granularity Page; Real (NOT VERIFIED)
- **Size:** 8,801 QA items; 135 on Telugu pages (page_language); no Telugu questions (qa_language) (QA items)
- **Labels:** QA - Prompt/completion
- **Licence:** CC BY 4.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Reubencf
- **Link:** https://huggingface.co/datasets/Reubencf/adaption-multilingual-doc-qa

### TOCR-133 - nvidia/miracl-vision - Telugu

Screenshots of Telugu Wikipedia articles for visual document retrieval, with queries and relevance labels.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (18; te configs) / Telugu
- **Content:** Image (rendered web pages); Visual document retrieval; granularity Page; Rendered real pages
- **Size:** 15,429 Telugu page images; 480 queries (page images)
- **Labels:** Retrieval qrels (text is the article, not a transcription) - qrels
- **Licence:** CC BY-SA 4.0 (commercial: Allowed (share-alike); redistribution: Allowed (share-alike))
- **Access:** Open (HF); needs: None
- **Source:** NVIDIA; NVIDIA
- **Link:** https://huggingface.co/datasets/nvidia/miracl-vision

### TOCR-134 - indic-citizen-information-board-pmgsy

Document QA / extraction set on PMGSY citizen boards in 6 languages.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (6; Telugu confirmed) / Telugu
- **Content:** Image (boards); Document QA / extraction; granularity Image; Real
- **Size:** 6,117 boards; Telugu 1,020 (709 train / 104 val / 207 test) (images)
- **Labels:** Machine-generated (per sibling card) - QA / text
- **Licence:** CC BY 4.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Litap007
- **Link:** https://huggingface.co/datasets/Litap007/indic-citizen-information-board-pmgsy
- **Overlap:** Sibling of TOCR-084.

### TOCR-190 - NayanaIR-CrossBench (multilingual visual document retrieval)

Cross-lingual visual document retrieval benchmark (part of the M3DR framework); corpus page images, queries and relevance labels in 20 languages incl. Telugu.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (20; te tag) / Telugu
- **Content:** Image (document pages); Visual document retrieval; granularity Page; UNKNOWN (likely rendered/translated)
- **Size:** UNKNOWN Telugu share (page images)
- **Labels:** Retrieval qrels - Queries + qrels (no transcription)
- **Licence:** None declared (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Cognitive Lab; Cognitive Lab
- **Link:** https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-CrossBench
- **Overlap:** Same group as Nayana sets (TOCR-097/098/099).

### TOCR-222 - NayanaIR-MonoBench-te (Telugu visual document retrieval)

Telugu monolingual visual document retrieval benchmark: page images, Telugu queries, relevance judgements.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (document pages); Visual document retrieval; granularity Page; UNKNOWN
- **Size:** 1,000 page images; 200 queries; 293 qrels (page images)
- **Labels:** Retrieval labels + answers - Queries, qrels, answers (no transcription)
- **Licence:** None declared (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Cognitive Lab; Cognitive Lab
- **Link:** https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-MonoBench-te
- **Overlap:** Same family as TOCR-190 (NayanaIR-CrossBench).


## Image-only (no transcription) (12)

_Telugu text images without any text labels._

### TOCR-010 - IIIT-INDIC-HW-WILD Telugu (SemiHastakshar unlabelled corpus)

Unlabelled handwritten Telugu word crops gathered from public notes/answer sheets plus crops of IIITS-THDB and PHDIndic_11.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (9 Indic incl. Telugu) / Telugu
- **Content:** Image (handwriting, in the wild); Semi-supervised HTR (unlabelled pool); granularity Word; Real
- **Size:** Telugu 301,170 (257,976 in repo + 43,194 rebuilt from source datasets) (word images)
- **Labels:** No - None (unlabelled by design)
- **Licence:** CC BY 4.0 for own images; source terms for rebuilt crops (commercial: Allowed for own images; redistribution: Allowed for own images)
- **Access:** Open (HF); needs: None
- **Source:** IIIT Hyderabad; Lalitha Evani et al.
- **Link:** https://lalithaevani.github.io/SemiHastakshar-page/
- **Paper:** https://doi.org/10.1145/3774521.3774605
- **Overlap:** Contains crops from IIITS-THDB (TOCR-014) and PHDIndic_11 (TOCR-015).

### TOCR-012 - FutureBeeAI Telugu Handwritten Sticky Notes OCR Image Dataset

Commercial set of 2,000+ phone photos of handwritten Telugu sticky notes from 200+ contributors, with metadata; transcription offered as a paid add-on.

- **Status:** COMMERCIAL · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (camera-captured handwriting); Handwritten OCR (after annotation); granularity Image (note); Real
- **Size:** 2,000+ (vendor claim) (images)
- **Labels:** No (metadata only; bounding boxes/transcription available as custom service) - Metadata CSV
- **Licence:** Commercial licence (vendor: "available for commercial use") (commercial: Allowed under purchase; redistribution: NOT ALLOWED (commercial))
- **Access:** Paid; needs: Purchase / sales contact
- **Source:** FutureBeeAI (vendor); FutureBeeAI
- **Link:** https://www.futurebeeai.com/dataset/ocr-dataset/telugu-sticky-notes-ocr-image-dataset
- **Notes:** Vendor marketing page; contents not independently inspected.

### TOCR-013 - FutureBeeAI Telugu Shopping List OCR Image Dataset

Commercial set of 2,000+ phone photos of handwritten Telugu shopping lists with metadata.

- **Status:** COMMERCIAL · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (camera-captured handwriting); Handwritten OCR (after annotation); granularity Image (list); Real
- **Size:** 2,000+ (vendor claim) (images)
- **Labels:** No (transcription paid add-on) - Metadata CSV
- **Licence:** Commercial licence (commercial: Allowed under purchase; redistribution: NOT ALLOWED)
- **Access:** Paid; needs: Purchase
- **Source:** FutureBeeAI (vendor); FutureBeeAI
- **Link:** https://www.futurebeeai.com/dataset/ocr-dataset/telugu-shopping-list-ocr-image-dataset

### TOCR-014 - IIITS-THDB (IIIT Sri City Telugu Handwriting Database)

450 handwritten Telugu pages (150 writers x 3 pages) collected for writer identification.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned handwriting); Writer identification; granularity Page; Real
- **Size:** 450 pages (150 writers) (page images)
- **Labels:** Writer IDs only - Writer label (no transcription confirmed)
- **Licence:** Non-commercial research and education only (project page) (commercial: Not allowed; redistribution: NOT ALLOWED)
- **Access:** Open (Drive links; not test-downloaded); needs: None stated
- **Source:** IIIT Sri City; Gadde, Reddy, Pulabaigari, Pal
- **Link:** https://chrizandr.github.io/IIITS-THDB/
- **Paper:** https://digitalcommons.isical.ac.in/conf-articles/110
- **Download:** Google Drive links on project page (NOT VERIFIED)
- **Overlap:** 37,787 word crops reused (unlabelled) in TOCR-010.

### TOCR-054 - harsha-desaraju/Telugu-book-text-images

Page images from Telugu book PDFs (file name + page number), no transcription.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (book pages); Unlabelled page images; granularity Page; Real
- **Size:** 232,500 (207,500 / 12,500 / 12,500) (page images)
- **Labels:** No - Provenance only
- **Licence:** MIT tag (source books modern; rights unclear) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/Telugu-book-text-images
- **Existing catalogue:** TEL-OCR-007

### TOCR-055 - harsha-desaraju/telugu-book-line-images (+ -sample)

2.44M unlabelled line crops cut from the book page set (5,000-row sample repo also published).

- **Status:** VERIFIED · **Distinct:** N (derivative of TOCR-054) · **Parent:** TOCR-054
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed lines); Unlabelled line crops; granularity Line; Real
- **Size:** 2,442,885 (+5,000 sample) (line crops)
- **Labels:** No - None
- **Licence:** MIT tag (rights of books unclear) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/telugu-book-line-images
- **Overlap:** Same crops as TOCR-056/057.

### TOCR-064 - Telugu document image classification set (Ramu, 2025)

Paper tests models on 500 handwritten + 500 printed Telugu document images; data not deposited.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (document pages); Handwritten vs printed classification; granularity Page; Real
- **Size:** 1,000 (per paper) (page images)
- **Labels:** Class label (per paper) - Handwritten/printed
- **Licence:** Article CC BY 4.0; data UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Article only; needs: Contact author
- **Source:** Academic; I. Ramu
- **Link:** https://zenodo.org/records/16778120
- **Paper:** https://doi.org/10.5281/zenodo.16778120

### TOCR-065 - FutureBeeAI Telugu Newspaper, Magazine and Books OCR Image Dataset

5,000 images equally split across Telugu newspapers, books and magazines, with metadata.

- **Status:** COMMERCIAL · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed); Printed OCR (after annotation); granularity Page; Real
- **Size:** 5,000 (vendor claim) (images)
- **Labels:** No (transcription paid add-on) - Metadata
- **Licence:** Commercial licence (commercial: Allowed under purchase; redistribution: NOT ALLOWED)
- **Access:** Paid; needs: Purchase
- **Source:** FutureBeeAI (vendor); FutureBeeAI
- **Link:** https://www.futurebeeai.com/dataset/ocr-dataset/telugu-newspaper-book-magazine-ocr-image-dataset

### TOCR-066 - FutureBeeAI Telugu Product Image OCR Dataset

2,000 front-of-pack product images with Telugu text, with metadata.

- **Status:** COMMERCIAL · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (product photos); Scene/product text OCR (after annotation); granularity Image; Real
- **Size:** 2,000 (vendor claim) (images)
- **Labels:** No (paid add-on) - Metadata
- **Licence:** Commercial licence (commercial: Allowed under purchase; redistribution: NOT ALLOWED)
- **Access:** Paid; needs: Purchase
- **Source:** FutureBeeAI (vendor); FutureBeeAI
- **Link:** https://www.futurebeeai.com/dataset/ocr-dataset/telugu-product-image-ocr-dataset

### TOCR-195 - Kaggle: telugu_palm_leafs (chintuimmandi) - palm-leaf binarisation pairs

36 Telugu palm-leaf images each paired with a ground-truth binarised image (NN_in.png / NN_gt.png).

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (suspected copy of TOCR-118 data)
- **Language / script:** Telugu / Telugu
- **Content:** Image (palm-leaf manuscripts); Binarisation; granularity Page; Real
- **Size:** 36 image / ground-truth pairs (72 PNG files, 230.5 MB) (image pairs)
- **Labels:** Yes - Binarised ground-truth image (no text)
- **Licence:** Unknown (Kaggle) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; chintuimmandi
- **Link:** https://www.kaggle.com/datasets/chintuimmandi/telugu-palm-leafs
- **Overlap:** Same size and task as the "Preserving Telugu Manuscripts" binarisation set (TOCR-118, 36 images); suspected to be its data release (NOT VERIFIED).

### TOCR-221 - stefania-radu/rendered_wikipedia_te (rendered Telugu Wikipedia text images)

Telugu Wikipedia text rendered to image patches (PIXEL-style pixel-language-model pre-training); images only, no text column.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered text); Pixel-based language model pre-training; granularity Text patch sequence; Synthetic
- **Size:** 225,693 rows (viewer) / 250,770 (card) (rendered images)
- **Labels:** No - None (pixel_values only)
- **Licence:** None declared (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF, 4.6 GB); needs: None
- **Source:** Individual; stefania-radu
- **Link:** https://huggingface.co/datasets/stefania-radu/rendered_wikipedia_te
- **Overlap:** Rendered from Telugu Wikipedia text (TOCR-139).

### TOCR-230 - GitHub Saisugandhasri - binarised Telugu character images (contrastive dataset construction)

Code for an unsupervised contrastive framework to build a Telugu character dataset, with 54 binarised source images and outputs.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (binarised document images); Character dataset construction (clustering); granularity Page / character; Real
- **Size:** 54 binarised images (+ outputs.zip 20.7 MB) (images)
- **Labels:** No (unsupervised) - Cluster outputs
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; Saisugandhasri
- **Link:** https://github.com/Saisugandhasri/A-novel-unsupervised-contrastive-learning-framework-for-Telugu-script-character-dataset-construction


## Image-only (transcription NOT VERIFIED) (14)

_Images where labels may exist but could not be confirmed._

### TOCR-011 - Assamese and Telugu Handwritten Text Dataset

Mobile-camera photos (300 dpi) of handwritten Assamese and Telugu essays/short stories, 5-10 lines each; intended for language recognition and line/word/character segmentation.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Assamese; Telugu / Telugu; Bengali-Assamese
- **Content:** Image (camera-captured handwriting); Segmentation; language identification; (recognition if text provided); granularity Page (5-10 lines); Real
- **Size:** 222 Telugu samples (200 Assamese) (page images)
- **Labels:** NOT VERIFIED - NOT VERIFIED (DataCite description mentions no transcriptions)
- **Licence:** CC BY 4.0 (DataCite) (commercial: Allowed with attribution; redistribution: Allowed with attribution)
- **Access:** Gated (landing page blocks automated clients; DataCite record verified); needs: IEEE DataPort account (login to download)
- **Source:** NIT Silchar (authors); Prarthana Dutta, Naresh Babu Muppalaneni
- **Link:** https://ieee-dataport.org/documents/assamese-and-telugu-handwritten-text-dataset
- **Notes:** Metadata from DataCite API; page returned HTTP 403 to scripts.

### TOCR-018 - GitHub JayanthKalluri/TeluguWordRecognizer - "handwritten_telugu_word_dataset" (Google Drive)

Project README points to a Google Drive folder of handwritten Telugu word images used for training.

- **Status:** UNVERIFIED · **Distinct:** UNKNOWN
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwriting); Handwritten word recognition; granularity Word; Real (assumed)
- **Size:** UNKNOWN (word images)
- **Labels:** NOT VERIFIED - NOT VERIFIED
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Not checked (Drive folder); needs: Google Drive link
- **Source:** Individual; Jayanth Kalluri
- **Link:** https://github.com/JayanthKalluri/TeluguWordRecognizer
- **Download:** https://drive.google.com/drive/folders/1OWdHJhDH-x6n257ck4avON7eIybb5aIR (NOT VERIFIED)
- **Overlap:** Possibly a copy of IIIT-HW-Telugu (not confirmed).
- **Notes:** Same author has JayanthKalluri/TeluguSentenceRecognizer (handwritten sentence OCR; ground_truth.txt and model only, no images).

### TOCR-046 - Telugu Image Corpus - OCR (TDIL / C-DAC Noida OCR Consortium)

500 greyscale 300-dpi TIFF scans of Telugu text, by-products of the national OCR project; listed as research-only.

- **Status:** INACCESSIBLE · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned printed pages); Printed OCR (images); granularity Page; Real
- **Size:** 500 (search-snippet description) (page images)
- **Labels:** NOT VERIFIED - NOT VERIFIED (described as images)
- **Licence:** Research only (search snippet) (commercial: Not allowed (reported); redistribution: UNKNOWN)
- **Access:** Site TLS certificate expired (2026-11-11); page not readable; needs: TDIL registration (reported)
- **Source:** C-DAC Noida OCR Consortium / TDIL, MeitY; OCR Consortium
- **Link:** https://tdil-dc.in/index.php?lang=en&option=com_download&task=showresourceDetails&toolid=264

### TOCR-068 - GitHub Pumapumapumas/ml-class-project - scanned Telugu pages

Class project comparing Tesseract and vision LLMs on scanned Telugu pages; 30 external page images.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned pages); Page OCR evaluation; granularity Page; Real
- **Size:** 30 (page images)
- **Labels:** NOT VERIFIED - NOT VERIFIED
- **Licence:** MIT (repo) (commercial: Allowed by repo licence (page rights unclear); redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Course project; UNKNOWN
- **Link:** https://github.com/Pumapumapumas/ml-class-project
- **Quality:** Very small.

### TOCR-069 - GitHub ChillarAnand/likitham - ocropy Telugu line samples

~25 ocropy line images (dataset/chalam) and a 76 KB training_samples.zip from a Telugu book.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (printed lines); Line recognition; granularity Line; Real
- **Size:** ~25 lines (line images)
- **Labels:** NOT VERIFIED - ocropy GT (NOT VERIFIED)
- **Licence:** No licence file (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; Chillar Anand
- **Link:** https://github.com/ChillarAnand/likitham
- **Quality:** Tiny; source book author (Chalam, d. 1979) likely still in copyright.

### TOCR-106 - chaitusvk/telugu_ocr_multi_line - generated line images

Small set of generated multi-line Telugu images used for a CRNN project.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (rendered lines); Line recognition; granularity Line; Synthetic
- **Size:** 246 images (images)
- **Labels:** NOT VERIFIED - NOT VERIFIED
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; chaitusvk
- **Link:** https://github.com/chaitusvk/telugu_ocr_multi_line
- **Quality:** Tiny.

### TOCR-118 - Telugu palm-leaf binarisation dataset ("Preserving Telugu Manuscripts")

Described as the first open Telugu palm-leaf dataset for digitisation/OCR research: 36 images of Telugu palm leaves for binarisation.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (palm-leaf manuscripts); Binarisation; granularity Page; Real
- **Size:** 36 images (README) (images)
- **Labels:** Binarisation (per paper; NOT VERIFIED) - NOT VERIFIED
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Repo live (7 files, no images); SSRN page HTTP 403 to scripts; needs: Images not in repo; link NOT VERIFIED
- **Source:** Academic (SSRN preprint); NOT VERIFIED (Bhavani Pisini et al.)
- **Link:** https://github.com/Bhavani-Pisini/Image-Binarization-Project
- **Paper:** https://doi.org/10.2139/ssrn.4903434
- **Overlap:** Kaggle telugu_palm_leafs (TOCR-195) has 36 image/ground-truth pairs and is suspected to be this dataset.

### TOCR-196 - Kaggle: IITJ Multilingual OCR Dataset (mayank7239)

Word crops in per-language folders, file names carry quadrilateral coordinates; listing shows Assamese and other folders.

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (suspected copy of TOCR-082)
- **Language / script:** Multilingual (Telugu folder NOT VERIFIED) / Multiple (Telugu NOT VERIFIED)
- **Content:** Image (scene word crops); Scene text recognition; granularity Word; Real
- **Size:** 441.8 MB; file listing capped at 400 files (word crops)
- **Labels:** UNKNOWN - Labels not seen in listing
- **Licence:** CC0-1.0 (Kaggle tag) (commercial: Tag says allowed; upstream terms apply; redistribution: Upstream terms apply)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual (title cites IIT Jodhpur); mayank7239
- **Link:** https://www.kaggle.com/datasets/mayank7239/iitj-multilingual-ocr-dataset
- **Overlap:** Suspected re-upload of Bharat Scene Text crops (TOCR-082, IIT Jodhpur).

### TOCR-214 - Telugu Meme Dataset (domain and troll identification, NITK)

Telugu memes (image + embedded text) labelled for domain, troll / non-troll and emotion.

- **Status:** UNVERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (born-digital memes); Meme classification; granularity Image; Real
- **Size:** UNKNOWN (memes)
- **Labels:** Class labels; embedded-text transcription NOT VERIFIED - Troll / domain / emotion labels
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Repository page HTTP 502; no public download found; needs: Contact authors / shared task
- **Source:** NIT Karnataka (NITK); N. Lohith, S. Adnan Raqeeb, Poreddy Sai Manoj Reddy, Chekuri Venkata Sunil Kumar, M. Anand Kumar
- **Link:** https://doi.org/10.1007/978-3-031-58495-4_2
- **Paper:** https://doi.org/10.1007/978-3-031-58495-4_2

### TOCR-215 - LT-EDI 2024 shared task: troll meme classification - Telugu

Gold-standard Telugu (and Kannada) troll / non-troll meme data for the LT-EDI 2024 "Multitask Meme Classification" shared task.

- **Status:** UNVERIFIED · **Distinct:** N (suspected same data as TOCR-214) · **Parent:** TOCR-214
- **Language / script:** Telugu / Telugu
- **Content:** Image (memes); Troll meme classification; granularity Image; Real
- **Size:** UNKNOWN (Telugu size not given in overview) (memes)
- **Labels:** Class labels - Troll / non-troll
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Not checked (CodaLab-style release); needs: Shared-task registration
- **Source:** LT-EDI 2024 organisers; Bharathi Raja Chakravarthi, Saranya Rajiakodi et al. (incl. M. Anand Kumar)
- **Link:** https://aclanthology.org/2024.ltedi-1.13.pdf
- **Paper:** https://doi.org/10.18653/v1/2024.ltedi-1.13
- **Overlap:** Shared co-organiser with TOCR-214; suspected same Telugu memes.

### TOCR-217 - TelMeMood - multimodal Telugu meme sentiment dataset

Telugu memes (image + text) annotated for sentiment.

- **Status:** UNVERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (memes); Meme sentiment analysis; granularity Image; Real
- **Size:** UNKNOWN (memes)
- **Labels:** Sentiment labels; text transcription NOT VERIFIED - Sentiment
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No public link found; needs: Contact authors
- **Source:** UNKNOWN; NOT VERIFIED
- **Link:** https://doi.org/10.1109/isacc65211.2025.10969246
- **Paper:** https://doi.org/10.1109/isacc65211.2025.10969246

### TOCR-218 - Benchmark dataset for hateful memes detection in Telugu

Telugu memes annotated for hateful content (Springer 2026).

- **Status:** UNVERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (memes); Hateful meme classification; granularity Image; Real
- **Size:** UNKNOWN (memes)
- **Labels:** Labels; text transcription NOT VERIFIED - Hate labels
- **Licence:** UNKNOWN (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** No public link found (Crossref record only); needs: Contact authors
- **Source:** UNKNOWN; NOT VERIFIED
- **Link:** https://doi.org/10.1007/978-3-032-13803-3_27
- **Paper:** https://doi.org/10.1007/978-3-032-13803-3_27

### TOCR-226 - GitHub ntbnaren7/telugu-fra-synthesizer - synthetic Telugu Forest Rights Act documents

Generator + 200 rendered Telugu government-form images (FRA claim documents) for document OCR/extraction experiments.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (synthetic forms); Document OCR / form extraction; granularity Page; Synthetic
- **Size:** 200 page images (+ fra_telugu_docs.zip, 26.4 MB) (page images)
- **Labels:** Not found (no ground-truth files in repo) - None verified
- **Licence:** MIT (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; ntbnaren7
- **Link:** https://github.com/ntbnaren7/telugu-fra-synthesizer
- **Notes:** The generator can presumably emit the rendered text; only images are committed.

### TOCR-227 - GitHub pavankarthik1/Telugu-Hand-Written-character-recognition - handwritten word images

112 handwritten Telugu word images (data/words) used with an SimpleHTR-style model.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (handwritten words); Handwritten word recognition; granularity Word; Real
- **Size:** 112 word images (word images)
- **Labels:** NOT VERIFIED - NOT VERIFIED
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** Individual; pavankarthik1
- **Link:** https://github.com/pavankarthik1/Telugu-Hand-Written-character-recognition


## Scanned archive (image-only) (10)

_Large collections of scanned books, newspapers or manuscripts. Raw material only - no ground truth._

### TOCR-117 - Telugu Palm Leaf Manuscripts (GOML Chennai scans on Internet Archive)

Page images (with machine OCR attempts) of Telugu palm-leaf manuscripts from the Government Oriental Manuscripts Library.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (palm-leaf manuscripts); Historical document images (no ground truth); granularity Page; Real
- **Size:** 1,863 manuscripts (~437 GB) (manuscripts)
- **Labels:** No (machine OCR only) - None (IA OCR text is machine output)
- **Licence:** Public Domain Mark 1.0 (commercial: Allowed; redistribution: Allowed)
- **Access:** Open (archive.org); needs: None
- **Source:** GOML Chennai / Tamil Virtual Academy (mirrored on IA); Institution
- **Link:** https://archive.org/details/telugu-palm-leaf
- **Existing catalogue:** TEL-MSS-001

### TOCR-122 - Internet Archive - Telugu-language items

All archive.org items with language Telugu: scanned books, periodicals, manuscripts; IA machine OCR where present.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scans) + machine OCR text; Unlabelled scans; granularity Page; Real
- **Size:** See catalogue TEL-DLIB-001 (items)
- **Labels:** No (machine OCR only) - IA OCR (machine)
- **Licence:** Varies per item (commercial: Varies; redistribution: Varies)
- **Access:** Open; needs: None
- **Source:** Internet Archive; Various
- **Link:** https://archive.org/search?query=language%3A%28Telugu+OR+tel%29
- **Existing catalogue:** TEL-DLIB-001

### TOCR-123 - Digital Library of India (DLI) - Telugu books

Scanned Telugu books from the Digital Library of India collection on archive.org.

- **Status:** VERIFIED · **Distinct:** N (part of TOCR-122) · **Parent:** TOCR-122
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned books); Unlabelled scans; granularity Page; Real
- **Size:** 18,221 items (catalogue) (books)
- **Labels:** No - None
- **Licence:** Mostly no licence stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open; needs: None
- **Source:** Digital Library of India / Internet Archive; Various
- **Link:** https://archive.org/search?query=collection%3Adigitallibraryindia
- **Existing catalogue:** TEL-DLIB-002

### TOCR-124 - Telugu newspapers e-paper archive (newspapers-telugu, archive.org)

Daily Telugu e-paper editions 2017-2026 on archive.org.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image/PDF (newspaper pages); Unlabelled page images; granularity Page; Real
- **Size:** 5,028 issues (catalogue) (issues)
- **Labels:** No - None
- **Licence:** Newspaper copyright (no licence field) (commercial: Not allowed; redistribution: NOT ALLOWED)
- **Access:** Open; needs: None
- **Source:** Internet Archive (uploader collection); Various publishers
- **Link:** https://archive.org/details/newspapers-telugu
- **Existing catalogue:** TEL-PERIOD-001

### TOCR-125 - Historic Telugu magazines on archive.org (Bharathi, Andhra Patrika, Andhra Mahila ...)

Scanned historic Telugu periodicals.

- **Status:** VERIFIED · **Distinct:** N (part of TOCR-122) · **Parent:** TOCR-122
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned periodicals); Unlabelled scans; granularity Page; Real
- **Size:** See catalogue TEL-PERIOD-002 (issues)
- **Labels:** No - None
- **Licence:** Varies (commercial: Varies; redistribution: Varies)
- **Access:** Open; needs: None
- **Source:** Internet Archive; Various
- **Link:** https://archive.org/search?query=title%3A%28%22andhra+patrika%22%29
- **Existing catalogue:** TEL-PERIOD-002

### TOCR-126 - AP Press Academy digitised old newspapers (pre-1977)

Government of Andhra Pradesh archive of digitised old newspapers and periodicals in several languages incl. Telugu.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu; others / Telugu
- **Content:** Image (newspaper pages); Unlabelled scans; granularity Page; Real
- **Size:** ~1.6 million pages all languages (reported 2005) (pages)
- **Labels:** No - None
- **Licence:** UNKNOWN (Government of AP) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Host did not resolve (DNS) on 2026-11-11; may be temporary; needs: Web viewer
- **Source:** Andhra Pradesh Press Academy; Government of AP
- **Link:** https://pressacademyarchives.ap.nic.in/
- **Existing catalogue:** TEL-PERIOD-005

### TOCR-127 - Kaggle: Telugu Chandamama Books (harishml)

PDF scans of Chandamama Telugu issues (1947 onward), titled "Chandamama Telugu OCR Dataset Books".

- **Status:** VERIFIED · **Distinct:** N (copy) · **Parent:** TOCR-129
- **Language / script:** Telugu / Telugu
- **Content:** PDF scans (magazine); Unlabelled scans; granularity Page; Real
- **Size:** 1,070 MB of issue PDFs (PDF issues)
- **Labels:** No - None
- **Licence:** Unknown; magazine copyright (commercial: Not established; redistribution: Not established)
- **Access:** Open listing; needs: Kaggle account
- **Source:** Individual; Harish ML
- **Link:** https://www.kaggle.com/datasets/harishml/telugu-chandamama-books
- **Overlap:** Subset copy of Chandamama archive (TOCR-129).

### TOCR-129 - Chandamama (Telugu edition) 1947-2012 scans

Scanned issues of the Telugu Chandamama children's magazine on archive.org.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned magazine); Unlabelled scans; granularity Page; Real
- **Size:** 1,628 Telugu issues (~180 GB, catalogue) (issues)
- **Labels:** No - None
- **Licence:** No licence field; magazine copyright (commercial: Not established; redistribution: Not established)
- **Access:** Open; needs: None
- **Source:** Chandamama archive (uploaded to archive.org); Chandamama publications
- **Link:** https://archive.org/search?query=collection%3Achandamama-magazine
- **Overlap:** Source of TOCR-058 and TOCR-127.
- **Existing catalogue:** TEL-PERIOD-003

### TOCR-209 - British Library AAS card catalogues: Telugu (digitised microfilm)

Digitised microfilm images of the British Library Asian and African Studies Telugu card catalogue.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu; English / Telugu
- **Content:** Image (catalogue card scans); Unlabelled scans (catalogue cards); granularity Card / page; Real
- **Size:** UNKNOWN (card images)
- **Labels:** No (text not verified) - None verified
- **Licence:** UNKNOWN (no rights field in DataCite) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** DataCite record live; files not opened; needs: None (BL research repository)
- **Source:** British Library; British Library
- **Link:** https://bl.iro.bl.uk/work/0249413b-6469-4c28-bb03-c4b3f9dd7403

### TOCR-211 - British Library Endangered Archives EAP038 - pre-1947 Telugu printed books and periodicals

Digitised (microfilm/scan) Telugu books and periodicals from Andhra Pradesh libraries, mostly 1869-1947 (e.g. Prajasakthi, Navasakthi issues).

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Image (scanned pages); Unlabelled scans; granularity Page; Real
- **Size:** 2,164 catalogued items; ~159,260 images (per search-indexed project text) (items / page images)
- **Labels:** No - None
- **Licence:** EAP terms (non-commercial research use; NOT VERIFIED) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Project and catalogue pages indexed; live page returned empty to scripts (2026-11-11); needs: None (online viewer)
- **Source:** British Library Endangered Archives Programme; EAP038 project team
- **Link:** https://eap.bl.uk/project/EAP038


## Text-only corpus (OCR language modelling) (10)

_Plain Telugu text with no images. Useful for OCR language models, spell-checking and rendering synthetic data - never image-text data._

### TOCR-121 - Transcription of Benjamin Schultze's Telugu-English Conversation Book

Scholarly transcription of an early 18th-century Telugu-English conversation book (Max Weber Stiftung / perspectivia).

- **Status:** UNVERIFIED · **Distinct:** Y
- **Language / script:** Telugu; English / Telugu
- **Content:** Text (+ facsimile NOT VERIFIED); Historical transcription; granularity Page / text; Real
- **Size:** UNKNOWN (pages)
- **Labels:** Transcription - Text transcription
- **Licence:** CC BY-ND 4.0 (DataCite) (commercial: Allowed (no derivatives); redistribution: Allowed (no derivatives))
- **Access:** Landing page served a bot check to scripts; needs: None
- **Source:** Max Weber Stiftung (perspectivia.net); NOT VERIFIED
- **Link:** https://perspectivia.net/receive/pnet_mods_00006709
- **Notes:** Would become an image-text historical set only if page facsimiles are provided - not confirmed.

### TOCR-135 - Telugu Wikisource text dump (wikimedia/wikisource 20231101.te; tewikisource XML)

Text-only Telugu corpus useful for OCR language models / post-correction. Text of TOCR-049 without images.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Text only; Language modelling for OCR (not OCR data); granularity Text; Real text
- **Size:** Proofread texts (see TOCR-049 for pages) (text)
- **Labels:** Not applicable - None (no images)
- **Licence:** CC BY-SA 3.0 / GFDL (HF tag); live Wikisource text is CC BY-SA 4.0 (commercial: See licence; redistribution: See licence)
- **Access:** Open; needs: None (CulturaX gated)
- **Source:** See catalogue; See catalogue
- **Link:** https://huggingface.co/datasets/wikimedia/wikisource
- **Existing catalogue:** TEL-LIT-001

### TOCR-136 - Sangraha - Telugu

Text-only Telugu corpus useful for OCR language models / post-correction. Large cleaned pretraining text.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Text only; Language modelling for OCR (not OCR data); granularity Text; Real text
- **Size:** verified/tel 15.10 GB (text)
- **Labels:** Not applicable - None (no images)
- **Licence:** CC BY 4.0 (commercial: See licence; redistribution: See licence)
- **Access:** Open; needs: None (CulturaX gated)
- **Source:** See catalogue; See catalogue
- **Link:** https://huggingface.co/datasets/ai4bharat/sangraha
- **Existing catalogue:** TEL-TXT-005

### TOCR-137 - IndicCorp v2 - Telugu

Text-only Telugu corpus useful for OCR language models / post-correction. Web/news text.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Text only; Language modelling for OCR (not OCR data); granularity Text; Real text
- **Size:** te.txt 15.76 GB (text)
- **Labels:** Not applicable - None (no images)
- **Licence:** CC0 1.0 (per README) (commercial: See licence; redistribution: See licence)
- **Access:** Open; needs: None (CulturaX gated)
- **Source:** See catalogue; See catalogue
- **Link:** https://huggingface.co/datasets/ai4bharat/IndicCorpV2
- **Existing catalogue:** TEL-TXT-004

### TOCR-138 - CulturaX - Telugu

Text-only Telugu corpus useful for OCR language models / post-correction. Gated on HF.

- **Status:** GATED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Text only; Language modelling for OCR (not OCR data); granularity Text; Real text
- **Size:** UNKNOWN (gated) (text)
- **Labels:** Not applicable - None (no images)
- **Licence:** mC4/OSCAR terms (commercial: See licence; redistribution: See licence)
- **Access:** Gated on HF (login + accept terms, automatic); needs: HF account + accept terms
- **Source:** See catalogue; See catalogue
- **Link:** https://huggingface.co/datasets/uonlp/CulturaX
- **Existing catalogue:** TEL-TXT-006

### TOCR-139 - Telugu Wikipedia dumps (tewiki)

Text-only Telugu corpus useful for OCR language models / post-correction. 

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Text only; Language modelling for OCR (not OCR data); granularity Text; Real text
- **Size:** 130,627 articles (text)
- **Labels:** Not applicable - None (no images)
- **Licence:** CC BY-SA 4.0 (commercial: See licence; redistribution: See licence)
- **Access:** Open; needs: None (CulturaX gated)
- **Source:** See catalogue; See catalogue
- **Link:** https://dumps.wikimedia.org/tewiki/latest/
- **Existing catalogue:** TEL-TXT-001

### TOCR-140 - harsha-desaraju/telugu-ocr-text (+ -uncombined) - source vs OCR text pairs

News text and the OCR read of its rendering, for OCR post-correction; text only.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Text only; OCR post-correction; granularity Document chunk; Synthetic OCR errors
- **Size:** 50,000 (+113,592 uncombined) (text pairs)
- **Labels:** Yes - src_text / ocr_text
- **Licence:** None declared (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual; Harsha Desaraju
- **Link:** https://huggingface.co/datasets/harsha-desaraju/telugu-ocr-text
- **Overlap:** Text side of TOCR-094.

### TOCR-141 - eswardivi/indiccorp_telugu_line

IndicCorp Telugu split into lines (text only).

- **Status:** VERIFIED · **Distinct:** N (derivative of TOCR-137) · **Parent:** TOCR-137
- **Language / script:** Telugu / Telugu
- **Content:** Text only; Rendering source / LM; granularity Line; Real text
- **Size:** 42,916,522 lines (lines)
- **Labels:** Not applicable - None
- **Licence:** None declared (IndicCorp terms) (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (HF); needs: None
- **Source:** Individual; eswardivi
- **Link:** https://huggingface.co/datasets/eswardivi/indiccorp_telugu_line

### TOCR-142 - TeluguOCR/corpora - Telugu Internet Unicode corpora

Telugu Unicode text corpora collected by the TeluguOCR project for language modelling.

- **Status:** VERIFIED · **Distinct:** Y
- **Language / script:** Telugu / Telugu
- **Content:** Text only; Language model for OCR; granularity Text; Real text
- **Size:** ~33 MB repo (text)
- **Labels:** Not applicable - None
- **Licence:** None stated (commercial: UNKNOWN; redistribution: UNKNOWN)
- **Access:** Open (GitHub); needs: None
- **Source:** TeluguOCR project; Rakesh Achanta et al.
- **Link:** https://github.com/TeluguOCR/corpora

### TOCR-197 - HuggingFaceFW/finepdfs - Telugu (tel_Telu)

Text extracted from public PDFs (born-digital extraction or OCR) for LM pre-training; no page images.

- **Status:** PARTIALLY VERIFIED · **Distinct:** Y
- **Language / script:** Multilingual (1,700+; tel_Telu config) / Telugu
- **Content:** Text only; Language modelling for OCR (not OCR data); granularity Document text; Real text (part machine-OCR)
- **Size:** UNKNOWN (Telugu share not computed) (documents)
- **Labels:** Not applicable - None (no images)
- **Licence:** ODC-By 1.0 (commercial: Allowed (source terms apply); redistribution: Allowed with attribution)
- **Access:** Open (HF); needs: None
- **Source:** Hugging Face; HuggingFaceFW
- **Link:** https://huggingface.co/datasets/HuggingFaceFW/finepdfs
- **Quality:** Some text is itself OCR output; useful as PDF-domain language model text only.


## Related resource (not a dataset) (10)

_Tools, models, fonts and portals that help build OCR data. Not counted as datasets._

### TOCR-144 - ILOCR / Bhashini OCR API catalogue (132 Telugu model entries)

Master list of 1,456 consortium OCR APIs; 132 are Telugu (layout, word recognition, pipelines, script detection) from IIITH, IITB, IITD, IITJ, plus Google OCR, Tesseract, EasyOCR, Surya entries. Models, not data; api_detail pages return server errors.

- **Status:** VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** See source (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** NLTM OCR consortium (IIIT Hyderabad); UNKNOWN
- **Link:** https://ilocr.iiit.ac.in/api_list/

### TOCR-145 - Bhashini ULCA - dataset/model portal

National language-data portal that aggregates OCR datasets/models; dataset search needs the web app.

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** See source (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** MeitY Bhashini; UNKNOWN
- **Link:** https://bhashini.gov.in/ulca
- **Existing catalogue:** TEL-SPEECH-018

### TOCR-146 - AIKosh (IndiaAI) dataset platform

Government dataset portal re-hosting Indian datasets incl. IIIT-INDIC-HW-WORDS and IndicDLP.

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** See source (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** IndiaAI Mission, MeitY; UNKNOWN
- **Link:** https://aikosh.indiaai.gov.in/home/datasets
- **Existing catalogue:** TEL-SPEECH-019

### TOCR-147 - Tesseract Telugu models and langdata (tel.traineddata)

Trained Telugu OCR models and training text/wordlists; useful for synthetic data and baselines.

- **Status:** VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** Apache-2.0 (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** Tesseract OCR project; UNKNOWN
- **Link:** https://github.com/tesseract-ocr/tessdata_best/blob/main/tel.traineddata
- **Existing catalogue:** TEL-OCR-009

### TOCR-148 - Telugu Unicode fonts (Noto, Pothana2000, Vemana, Google Fonts Telugu subset)

Fonts used to render synthetic Telugu OCR data.

- **Status:** VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** SIL OFL 1.1 (most) (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** Google Fonts; AndhraBharati; UNKNOWN
- **Link:** https://fonts.google.com/?subset=telugu
- **Notes:** Also uploaded as Kaggle viralbarodia/gujarati-and-telugu-fonts (Noto Sans Telugu, MIT tag).
- **Existing catalogue:** TEL-DIAL-004

### TOCR-149 - IndicPhotoOCR toolkit (BSTD models)

Scene-text detection, script ID and recognition models for 11 Indian languages + English.

- **Status:** VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** See source (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** IIT Jodhpur (Bhashini); UNKNOWN
- **Link:** https://github.com/Bhashini-IITJ/IndicPhotoOCR

### TOCR-150 - TeluguOCR data generators (datagen_initio, datagen_duo)

Scripts to generate millions of rendered Telugu characters/glyphs for banti OCR training.

- **Status:** VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** See source (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** TeluguOCR project; UNKNOWN
- **Link:** https://github.com/TeluguOCR

### TOCR-151 - IndicSceneTextRendering (synthetic scene-text renderer)

Renderer used for IIIT-ILST synthetic word images.

- **Status:** VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** See source (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** CVIT, IIIT Hyderabad; UNKNOWN
- **Link:** https://github.com/mineshmathew/IndicSceneTextRendering

### TOCR-152 - gopalvarun03/Telugu-OCR - Vedic Telugu-script synthetic data generator

Notebooks to render synthetic Telugu-script Vedic text images from 85+ transcription files; generated data not in repo.

- **Status:** PARTIALLY VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** See source (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** Individual; UNKNOWN
- **Link:** https://github.com/gopalvarun03/Telugu-OCR

### TOCR-153 - harsha-desaraju/TeluguOCR (pipeline + model)

Code that builds the harsha-desaraju Wikisource line, synthetic line and consensus datasets; model card on HF.

- **Status:** VERIFIED · **Distinct:** N (not a dataset)
- **Language / script:** Telugu / Telugu
- **Content:** Not a dataset; Supporting resource; granularity Not applicable; Not applicable
- **Size:** Not applicable (Not applicable)
- **Labels:** Not applicable - Not applicable
- **Licence:** MIT (commercial: See source; redistribution: See source)
- **Access:** Open; needs: None
- **Source:** Individual; UNKNOWN
- **Link:** https://github.com/harsha-desaraju/TeluguOCR


## Rejected (44)

_Candidates that turned out to have no Telugu, no images, or no data. Kept so nobody re-checks them._

### TOCR-154 - 3D Telugu Character Recognition (IEEE DataPort yz7d-cz45)

Rejected candidate - see notes.

- **Why rejected:** Accelerometer x/y/z sensor CSVs for in-air writing of 5 characters - no images.
- **Link:** https://ieee-dataport.org/documents/3d-telugu-character-recognition

### TOCR-155 - HSC-IndicDB (Mendeley dkmxgd8n79)

Rejected candidate - see notes.

- **Why rejected:** Description names Bengali, Devanagari, Kannada, Malayalam; Telugu not mentioned.
- **Link:** https://data.mendeley.com/datasets/dkmxgd8n79/1

### TOCR-156 - Learn Telugu letters Alphabets with Audio (Mendeley 98rd3nx2n4)

Rejected candidate - see notes.

- **Why rejected:** Audio pronunciation learning resource, not OCR data.
- **Link:** https://data.mendeley.com/datasets/98rd3nx2n4/1

### TOCR-157 - AI-powered multilingual OCR system for historical documents (Zenodo 20604818)

Rejected candidate - see notes.

- **Why rejected:** Typed as dataset but is a technical specification report; no data.
- **Link:** https://doi.org/10.5281/zenodo.20604818

### TOCR-158 - nvidia/OCR-Synthetic-Multilingual-v1 (and Kaggle 24K starter subset)

Rejected candidate - see notes.

- **Why rejected:** Languages en, ja, ko, ru, zh only - no Telugu.
- **Link:** https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1

### TOCR-159 - ICDAR RRC MLT-2017 / MLT-2019

Rejected candidate - see notes.

- **Why rejected:** Indian scripts are Bangla and Devanagari only - no Telugu.
- **Link:** https://rrc.cvc.uab.es/?ch=15

### TOCR-160 - MITDI - Mixed-lingual Indic Texts in Digital Images (MTAP 2022)

Rejected candidate - see notes.

- **Why rejected:** English, Bangla, Hindi only.
- **Link:** https://doi.org/10.1007/s11042-022-12596-7

### TOCR-161 - Transfer Learning for STR in Indian Languages - released real data (Gunna et al. 2021)

Rejected candidate - see notes.

- **Why rejected:** Released real data is Gujarati and Tamil only; Telugu results use IIIT-ILST.
- **Link:** https://cvit.iiit.ac.in/research/projects/cvit-projects/transfer-learning-for-scene-text-recognition-in-indian-languages

### TOCR-162 - interfaze-ai/ocr-mlt-50m

Rejected candidate - see notes.

- **Why rejected:** 60 rows across 50 languages; no meaningful Telugu content.
- **Link:** https://huggingface.co/datasets/interfaze-ai/ocr-mlt-50m

### TOCR-163 - AbhishekBhandari/Indic-post-ocr-correction

Rejected candidate - see notes.

- **Why rejected:** Gujarati, Hindi, Marathi only.
- **Link:** https://huggingface.co/datasets/AbhishekBhandari/Indic-post-ocr-correction

### TOCR-164 - Aus-23/indic-synthetic-scene-text-1000

Rejected candidate - see notes.

- **Why rejected:** Marathi, Hindi, Gujarati, Bengali only.
- **Link:** https://huggingface.co/datasets/Aus-23/indic-synthetic-scene-text-1000

### TOCR-165 - Crossmodal-3600 caption sets (floschne/xm3600, xm3600_1k, dinhanhx/crossmodal-3600, PangeaBench-xm100, ai-enthusiasm-community/XM3600)

Rejected candidate - see notes.

- **Why rejected:** Telugu image captions, not text in images.
- **Link:** https://huggingface.co/datasets/floschne/xm3600

### TOCR-166 - WIT (wikimedia/wit_base, VedaLabs/wit_base)

Rejected candidate - see notes.

- **Why rejected:** Image-caption pairs; no Telugu found in sample; not OCR.
- **Link:** https://huggingface.co/datasets/wikimedia/wit_base

### TOCR-167 - CC3M-35L / COCO-35L (ai-enthusiasm-community)

Rejected candidate - see notes.

- **Why rejected:** Translated captions, not OCR.
- **Link:** https://huggingface.co/datasets/ai-enthusiasm-community/CC3M-35L

### TOCR-168 - visheratin/laion-coco-nllb

Rejected candidate - see notes.

- **Why rejected:** Translated captions, not OCR.
- **Link:** https://huggingface.co/datasets/visheratin/laion-coco-nllb

### TOCR-169 - ARTPARK-IISc Vaani (and benchmarks)

Rejected candidate - see notes.

- **Why rejected:** Speech dataset with prompt images; not OCR.
- **Link:** https://huggingface.co/datasets/ARTPARK-IISc/Vaani

### TOCR-170 - DRISHTIKON (13ari / Vipashyana)

Rejected candidate - see notes.

- **Why rejected:** Cultural VQA; no Telugu text found in sample; not OCR.
- **Link:** https://huggingface.co/datasets/13ari/DRISHTIKON

### TOCR-171 - neulab/CulturalGround and other cultural VQA sets (symile-m3, global-piqa, mvl-sib, ArogyaBodha, IndicMMVet, IndicPope, IndicLLaVABench, Kaleidoscope)

Rejected candidate - see notes.

- **Why rejected:** General VQA/QA with Telugu questions; images are not text-centric.
- **Link:** https://huggingface.co/datasets/neulab/CulturalGround

### TOCR-173 - Shaip OCR training data

Rejected candidate - see notes.

- **Why rejected:** Custom-collection vendor page; no Telugu OCR product listed.
- **Link:** https://www.shaip.com/solutions/optical-character-recognition-ocr-machine-learning/

### TOCR-174 - GitHub UthejKaramalapudi/Handwritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images

Rejected candidate - see notes.

- **Why rejected:** Code only; no images in repository.
- **Link:** https://github.com/UthejKaramalapudi/Handwritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images

### TOCR-175 - GitHub Harathi123/Telugu-Character-Recognition-using-CNN

Rejected candidate - see notes.

- **Why rejected:** Reuses HP Labs data (TOCR-021); no new data.
- **Link:** https://github.com/Harathi123/Telugu-Character-Recognition-using-CNN

### TOCR-176 - GitHub alfahimmohammad/Telugu-Handwritten-Text-Recognition

Rejected candidate - see notes.

- **Why rejected:** Reuses CVIT IIIT-HW-Telugu (TOCR-001); no new data.
- **Link:** https://github.com/alfahimmohammad/Telugu-Handwritten-Text-Recognition

### TOCR-177 - GitHub jaganmohanreddy2106/Telugu-Handwritten-Digit-Recognition

Rejected candidate - see notes.

- **Why rejected:** 10 example digit images only; no dataset.
- **Link:** https://github.com/jaganmohanreddy2106/Telugu-Handwritten-Digit-Recognition

### TOCR-178 - Telugu Alphabets 52-letter chart (Zenodo 20079705)

Rejected candidate - see notes.

- **Why rejected:** Single educational chart image; record now HTTP 410 (removed).
- **Link:** https://doi.org/10.5281/zenodo.20079705

### TOCR-179 - Telugu NLP / news / lyrics Kaggle sets (text-only, non-OCR)

Rejected candidate - see notes.

- **Why rejected:** Text classification/NLP corpora surfaced by Kaggle search; not OCR and not needed as OCR LM sources.
- **Link:** https://www.kaggle.com/datasets/sudalairajkumar/telugu-nlp

### TOCR-198 - SignboardText (IEEE DataPort 10.21227/5k09-4k21)

Rejected candidate - see notes.

- **Why rejected:** Vietnamese/English signboards (UIT, VNU-HCM); surfaced in Telugu scene-text searches but has no Telugu.
- **Link:** https://ieee-dataport.org/documents/signboardtext-0

### TOCR-199 - CATALIST / CATALISTd video scene text (IIT Bombay, on AIKosh)

Rejected candidate - see notes.

- **Why rejected:** English, Hindi and Marathi only.
- **Link:** https://catalist-2021.github.io

### TOCR-200 - DohaScript handwritten Hindi (arXiv 2602.18089)

Rejected candidate - see notes.

- **Why rejected:** Hindi only.
- **Link:** https://arxiv.org/abs/2602.18089

### TOCR-201 - IIEST-Indic-HW writer identification dataset

Rejected candidate - see notes.

- **Why rejected:** Bengali and Hindi only.
- **Link:** https://doi.org/10.1145/3774521.3774586

### TOCR-202 - EpiSAM / Shilalekhya stone-inscription datasets (IHDIA)

Rejected candidate - see notes.

- **Why rejected:** Single Indic script not named; no Telugu evidence on project pages or HF card.
- **Link:** https://ihdia.iiit.ac.in/episam/

### TOCR-203 - arikatokachi/indic-synthetic-documents (+v2)

Rejected candidate - see notes.

- **Why rejected:** Languages en, bn, hi, ta only (folders and tags).
- **Link:** https://huggingface.co/datasets/arikatokachi/indic-synthetic-documents

### TOCR-204 - Nexdata 500,000 Images Multilingual OCR Dataset in 21 Languages

Rejected candidate - see notes.

- **Why rejected:** Commercial sample; listed languages do not include Telugu.
- **Link:** https://huggingface.co/datasets/Nexdata-kr/500000-Images-Multilingual-OCR-Dataset-in-21-Languages

### TOCR-205 - DataCluster Labs Multilingual OCR Annotation Dataset (Kaggle + HF)

Rejected candidate - see notes.

- **Why rejected:** Vendor sample with he/th/ja/ar; no Telugu files.
- **Link:** https://huggingface.co/datasets/Dataclusterlabspvtltd/Multilingual_OCR_Annotation_Dataset

### TOCR-206 - A Benchmark and Dataset for Post-OCR Text Correction in Sanskrit (AIKosh)

Rejected candidate - see notes.

- **Why rejected:** Sanskrit text only (Devanagari); no Telugu.
- **Link:** https://aikosh.indiaai.gov.in/home/datasets/details/a_benchmark_and_dataset_for_post_ocr_text_correction_in_sanskrit.html

### TOCR-207 - Indic-VizVQA-v2 (Kaggle armaansingh2340)

Rejected candidate - see notes.

- **Why rejected:** Translated VizWiz/VQAv2 questions; images are not text-centric.
- **Link:** https://www.kaggle.com/datasets/armaansingh2340/indic-vizvqa-v2

### TOCR-231 - HKS-NVC: Handwritten Kadamba Script numerals, vowels, consonants (IEEE DataPort 10.21227/nhvr-w717)

Rejected candidate - see notes.

- **Why rejected:** Kadamba script (ancestor of Kannada-Telugu), not Telugu.
- **Link:** https://doi.org/10.21227/nhvr-w717

### TOCR-232 - GitHub NamineniBrahmani/multilingual-ocr

Rejected candidate - see notes.

- **Why rejected:** Six scripts (Nandinagari, Malayalam, Kannada, Devanagari, Sarada, Bengali); no Telugu folder.
- **Link:** https://github.com/NamineniBrahmani/multilingual-ocr

### TOCR-233 - GitHub bitreaper42/DC_Indic scene-text evaluation set

Rejected candidate - see notes.

- **Why rejected:** ground_truth.json has only English and Hindi regions.
- **Link:** https://github.com/bitreaper42/DC_Indic

### TOCR-234 - GitHub darshanrao/Ancient-Hand-Writtten-Recognition-Under-Data-Deficiency

Rejected candidate - see notes.

- **Why rejected:** Tamil and Sanskrit data only.
- **Link:** https://github.com/darshanrao/Ancient-Hand-Writtten-Recognition-Under-Data-Deficiency

### TOCR-235 - HASOC 2025 multimodal meme task (FIRE 2025)

Rejected candidate - see notes.

- **Why rejected:** Hindi, Gujarati, Bangla and Bodo memes; no Telugu.
- **Link:** https://ceur-ws.org/Vol-4173/

### TOCR-236 - Synbols synthetic glyph datasets (ServiceNow)

Rejected candidate - see notes.

- **Why rejected:** No Telugu alphabet in the generator (code search 2026-11-11).
- **Link:** https://github.com/ServiceNow/synbols

### TOCR-237 - Tamil handwritten palm-leaf manuscript dataset (THPLMD)

Rejected candidate - see notes.

- **Why rejected:** Tamil only; surfaces in Telugu palm-leaf searches.
- **Link:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10864864/

### TOCR-238 - Hamburg palm-leaf manuscript word datasets (fdr.uni-hamburg.de)

Rejected candidate - see notes.

- **Why rejected:** Tamil manuscripts; no Telugu.
- **Link:** https://b2find.eudat.eu/dataset/f0497ec0-a60f-5710-96b4-2bf9adef6f56

### TOCR-239 - IIST BCI Telugu datasets (EEG; IEEE DataPort)

Rejected candidate - see notes.

- **Why rejected:** Brain-signal recordings of Telugu speech/commands, not images.
- **Link:** https://doi.org/10.21227/32qq-c421
