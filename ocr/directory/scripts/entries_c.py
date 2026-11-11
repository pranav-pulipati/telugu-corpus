"""Directory records, part C: layout/detection, script ID, manuscripts & archives, text-in-image benchmarks,
text-only corpora, related resources (not datasets) and rejected candidates."""
from common import E

R = []

# ------------------------------------------------------------------ layout / detection / script identification
R.append(E(
    id='TOCR-015', name='PHDIndic_11 - Telugu pages', aliases='IEEE DataPort 10.21227/p2p9-er60', version='2017/2018',
    desc='Page-level handwritten document images in 11 official Indic scripts (1,458 pages by 463 writers) for handwritten script identification.',
    url='https://ieee-dataport.org/open-access/phdindic11-page-level-handwritten-document-image-dataset-11-official-indic-scripts', paper='https://doi.org/10.1007/s11042-017-4373-y',
    doi='10.21227/p2p9-er60', inst='Aliah University; West Bengal State University; Jadavpur University; Univ. South Dakota', authors='Obaidullah Sk, Chayan Halder, K. C. Santosh, Nibaran Das, Kaushik Roy',
    lang='Multilingual (11 scripts incl. Telugu)', modality='Image (scanned handwriting, TIFF)', task='Script identification', gran='Page', rs='Real', count='1,458 pages total; Telugu share NOT VERIFIED',
    unit='page images', ann='Script label only', ann_type='Script class', lic='Creative Commons Attribution (IEEE page)', comm='Allowed with attribution', redis='Allowed with attribution',
    access_req='Free IEEE DataPort account', access='Gated (login)', ver='GATED', overlap='Telugu pages reused in TEXTRON (TOCR-016) and HW-WILD (TOCR-010).', cat='Script identification', distinct='Y'))

R.append(E(
    id='TOCR-109', name='IndicDLP - Telugu pages (document layout parsing)', version='2025 (ICDAR, Best Student Paper runner-up)',
    desc='119,806 human-annotated document images in 11 Indic languages + English across 12 domains, with 42 layout region classes; no transcriptions.',
    url='https://cvit.iiit.ac.in/research/projects/cvit-projects/indicdlp', download='https://aikosh.indiaai.gov.in/home/datasets/details/indicdlp.html (via AIKosh)',
    hf='https://huggingface.co/datasets/ai4bharat/indicdlp (gated)', github='https://github.com/AI4Bharat/IndicDLP', archive='https://doi.org/10.5281/zenodo.15881917', paper='https://arxiv.org/abs/2512.20236',
    doi='10.1007/978-3-032-04614-7_2', inst='IIT Madras (AI4Bharat); IIIT Hyderabad', authors='Oikantik Nath, Sahithi Kukkala, Mitesh Khapra, Ravi Kiran Sarvadevabhatla',
    lang='Multilingual (12)', modality='Image (documents: novels, textbooks, newspapers, forms ...)', task='Document layout parsing', gran='Page regions', rs='Real',
    count='119,806 total; Telugu 7.2% (~8,600 pages, computed from README share)', unit='page images', ann='Yes (layout only)', ann_type='Region boxes, 42 classes (YOLO/COCO)',
    lic='MIT (repo) / CC BY 4.0 (Zenodo)', comm='Allowed', redis='Allowed', access_req='HF: login + accept terms; AIKosh download', access='Gated on HF; AIKosh/Zenodo routes', ver='GATED',
    overlap='Block OCR eval set (TOCR-060) and dlp-sample (TOCR-110) derived from it.', cat='Layout / detection (no transcription)', distinct='Y', catalogue='TEL-OCR-015'))

R.append(E(
    id='TOCR-110', name='onath/dlp-sample (IndicDLP sample, telugu config)', parent='TOCR-109', desc='Small public sample of IndicDLP pages with layout labels, configs per language and domain.',
    hf='https://huggingface.co/datasets/onath/dlp-sample', url='https://huggingface.co/datasets/onath/dlp-sample', inst='IIT Madras', authors='Oikantik Nath', lang='Multilingual', modality='Image (documents)',
    task='Layout parsing', gran='Page regions', rs='Real', count='36 Telugu pages (12/12/12)', unit='page images', ann='Yes (layout)', ann_type='Region boxes', lic='CC BY 4.0', comm='Allowed', redis='Allowed',
    access_req='None', access='Open (HF)', ver='VERIFIED', overlap='Sample of TOCR-109.', cat='Layout / detection (no transcription)', distinct='N (sample)'))

R.append(E(
    id='TOCR-111', name='Indiscapes / Indiscapes2 (historical Indic manuscript layout)', version='2019 (ICDAR) / 2023',
    desc='Region-level layout annotations (text lines, holes, decorations, page boundaries) on historical Indic palm-leaf and paper manuscripts.',
    url='https://ihdia.iiit.ac.in/', paper='https://arxiv.org/abs/1912.07025', inst='CVIT/IHDIA, IIIT Hyderabad', authors='Abhishek Prusty, Sowmya Aitha, Ravi Kiran Sarvadevabhatla et al.',
    lang='Multilingual (Sanskrit and other Indic; Telugu share NOT VERIFIED)', script='Multiple (Telugu presence NOT VERIFIED)', modality='Image (manuscripts)', task='Layout parsing', gran='Page regions', rs='Real',
    count='UNKNOWN (Telugu)', unit='manuscript pages', ann='Yes (layout)', ann_type='Instance polygons', lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='UNKNOWN', access='Project site live',
    ver='PARTIALLY VERIFIED', cat='Layout / detection (no transcription)', distinct='Y', catalogue='TEL-OCR-013'))

R.append(E(
    id='TOCR-112', name='MUSTARD - Telugu tables (table structure recognition)', aliases='CheneyWong/SPRINT-MUSTARD; bevaya/MUSTARD (copies)', version='2024 (ICDAR, SPRINT)',
    desc='Printed/scanned/scene tables from magazines in 13 languages labelled with OTSL structure sequences; ~100 Telugu tables.', hf='https://huggingface.co/datasets/badrivishalk/MUSTARD',
    github='https://github.com/IITB-LEAP-OCR/SPRINT', paper='https://arxiv.org/abs/2503.11932', url='https://huggingface.co/datasets/badrivishalk/MUSTARD', inst='IIT Bombay LEAP OCR team',
    authors='Dhruv Kudale, Badri Vishal Kasuba et al.', lang='Multilingual (13)', modality='Image (tables)', task='Table structure recognition', gran='Table', rs='Real', count='~100 Telugu tables',
    unit='table images', ann='Yes (structure only)', ann_type='OTSL tokens (no cell text)', lic='MIT', comm='Allowed', redis='Allowed', access_req='None', access='Open (HF)', ver='VERIFIED',
    cat='Layout / detection (no transcription)', distinct='Y'))

R.append(E(
    id='TOCR-113', name='MDIW-13 - Multi-lingual Document Image database for script identification', version='2022/2024', desc='1,135 printed and handwritten documents in 13 scripts incl. Telugu, segmented into 13,979 lines and 86,655 words.',
    archive='https://doi.org/10.5281/zenodo.6376096', url='https://doi.org/10.5281/zenodo.6376096', paper='https://arxiv.org/abs/2405.18924', doi='10.1007/s12559-023-10193-w', inst='Academic consortium',
    authors='Miguel A. Ferrer et al.', lang='Multilingual (13 scripts)', modality='Image (printed + handwritten documents)', task='Script identification', gran='Document / line / word', rs='Real',
    count='1,135 documents total; Telugu share NOT VERIFIED', unit='document images', ann='Script labels', ann_type='Script class', lic='CC BY 4.0', comm='Allowed', redis='Allowed', access_req='None',
    access='Open (Zenodo)', ver='VERIFIED', cat='Script identification', distinct='Y', catalogue='TEL-OCR-016'))

R.append(E(
    id='TOCR-114', name='Kaggle: Indian Scripts (12-script image classification)', desc='10,000+ images (250x250) of 12 Indian scripts incl. Telugu in train/test folders for script classification.',
    kaggle='https://www.kaggle.com/datasets/abhisheksubhashswami/indian-scripts', url='https://www.kaggle.com/datasets/abhisheksubhashswami/indian-scripts', inst='Individual', authors='Abhishek Subhash Swami',
    lang='Multilingual (12)', modality='Image', task='Script identification', gran='Image', rs='UNKNOWN', count='13,792 total (Kaggle); Telugu share NOT VERIFIED', unit='images', ann='Script label', ann_type='Folder',
    lic='CC0-1.0', comm='Allowed', redis='Allowed', access_req='Kaggle account', access='Open listing', ver='VERIFIED', cat='Script identification', distinct='Y'))

R.append(E(
    id='TOCR-115', name='Kaggle: english hindi telugu text images (akash034)', desc='Screenshots of English, Hindi and Telugu text in language folders.',
    kaggle='https://www.kaggle.com/datasets/akash034/english-hindi-telugu-text-images', url='https://www.kaggle.com/datasets/akash034/english-hindi-telugu-text-images', inst='Individual', authors='akash034',
    lang='English; Hindi; Telugu', modality='Image (screenshots)', task='Script / language identification', gran='Image', rs='Real (screenshots)', count='153.2 MB; count NOT VERIFIED', unit='images',
    ann='Language folder only', ann_type='Language label', lic='Unknown', comm='UNKNOWN', redis='UNKNOWN', access_req='Kaggle account', access='Open listing', ver='PARTIALLY VERIFIED', cat='Script identification', distinct='Y'))

R.append(E(
    id='TOCR-116', name='lipika-eval (font/script identification images)', desc='Rendered text images labelled with font family and script for 13 scripts; 351 Telugu images.',
    hf='https://huggingface.co/datasets/loopdesk-ai/lipika-eval', url='https://huggingface.co/datasets/loopdesk-ai/lipika-eval', inst='Loopdesk AI', authors='loopdesk-ai', lang='Multilingual (13 scripts)',
    modality='Image (rendered)', task='Font / script identification', gran='Image', rs='Synthetic', count='351 Telugu (6,876 total)', unit='images', ann='Font + script labels', ann_type='No transcription',
    lic='Apache-2.0', comm='Allowed', redis='Allowed', access_req='None', access='Open (HF)', ver='VERIFIED', cat='Script identification', distinct='Y'))

# ------------------------------------------------------------------ manuscripts & scanned archives
R.append(E(
    id='TOCR-117', name='Telugu Palm Leaf Manuscripts (GOML Chennai scans on Internet Archive)', desc='Page images (with machine OCR attempts) of Telugu palm-leaf manuscripts from the Government Oriental Manuscripts Library.',
    url='https://archive.org/details/telugu-palm-leaf', archive='https://archive.org/details/telugu-palm-leaf', inst='GOML Chennai / Tamil Virtual Academy (mirrored on IA)', authors='Institution',
    modality='Image (palm-leaf manuscripts)', task='Historical document images (no ground truth)', gran='Page', rs='Real', count='1,863 manuscripts (~437 GB)', unit='manuscripts', ann='No (machine OCR only)',
    ann_type='None (IA OCR text is machine output)', lic='Public Domain Mark 1.0', comm='Allowed', redis='Allowed', access_req='None', access='Open (archive.org)', ver='VERIFIED', cat='Scanned archive (image-only)', distinct='Y',
    catalogue='TEL-MSS-001'))

R.append(E(
    id='TOCR-118', name='Telugu palm-leaf binarisation dataset ("Preserving Telugu Manuscripts")', aliases='Bhavani-Pisini/Image-Binarization-Project',
    desc='Described as the first open Telugu palm-leaf dataset for digitisation/OCR research: 36 images of Telugu palm leaves for binarisation.',
    github='https://github.com/Bhavani-Pisini/Image-Binarization-Project', url='https://github.com/Bhavani-Pisini/Image-Binarization-Project', paper='https://doi.org/10.2139/ssrn.4903434',
    doi='10.2139/ssrn.4903434', inst='Academic (SSRN preprint)', authors='NOT VERIFIED (Bhavani Pisini et al.)', modality='Image (palm-leaf manuscripts)', task='Binarisation', gran='Page', rs='Real',
    count='36 images (README)', unit='images', ann='Binarisation (per paper; NOT VERIFIED)', ann_type='NOT VERIFIED', lic='None stated', comm='UNKNOWN', redis='UNKNOWN', access_req='Images not in repo; link NOT VERIFIED',
    access='Repo live (7 files, no images); SSRN page HTTP 403 to scripts', ver='PARTIALLY VERIFIED', overlap='Repo and SSRN preprint assumed to describe the same dataset (title/description match).',
    cat='Image-only (transcription NOT VERIFIED)', distinct='Y'))

R.append(E(
    id='TOCR-119', name='Telugu palm-leaf character crops (Sriram1908/TeluguManuscriptOCRandTextReconstruction)', desc='Segmented palm-leaf character images mapped to their characters, plus handwritten samples, used for a manuscript OCR project.',
    github='https://github.com/Sriram1908/TeluguManuscriptOCRandTextReconstruction', url='https://github.com/Sriram1908/TeluguManuscriptOCRandTextReconstruction', inst='Individual', authors='Sriram1908',
    modality='Image (palm-leaf characters)', task='Character recognition', gran='Character', rs='Real (+ own handwriting)', count='1,777 images (mappings/*)', unit='character images', ann='Yes (folder mapping)', ann_type='Character class',
    lic='None stated', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-120', name='Telugu palm-leaf 3D character dataset (2016 paper)', desc='Paper builds a 3D (depth) dataset of Telugu palm-leaf text including compound characters for recognition.',
    url='https://www.griet.ac.in/images/1-s2.0-S2215098616303627-main.pdf', paper='https://doi.org/10.1016/j.jestch.2016.06.006 (NOT VERIFIED)', inst='Academic (GRIET-hosted PDF)', authors='NOT VERIFIED',
    modality='3D profile / image (palm leaf)', task='Character recognition', gran='Character', rs='Real', count='UNKNOWN', unit='characters', ann='Yes (per paper)', ann_type='Character class', lic='UNKNOWN', comm='UNKNOWN',
    redis='UNKNOWN', access_req='Contact authors', access='No public release found', ver='UNVERIFIED', cat='Character / glyph classification', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-121', name='Transcription of Benjamin Schultze\'s Telugu-English Conversation Book', desc='Scholarly transcription of an early 18th-century Telugu-English conversation book (Max Weber Stiftung / perspectivia).',
    url='https://perspectivia.net/receive/pnet_mods_00006709', inst='Max Weber Stiftung (perspectivia.net)', authors='NOT VERIFIED', lang='Telugu; English', modality='Text (+ facsimile NOT VERIFIED)',
    task='Historical transcription', gran='Page / text', rs='Real', count='UNKNOWN', unit='pages', ann='Transcription', ann_type='Text transcription', lic='CC BY-ND 4.0 (DataCite)', comm='Allowed (no derivatives)',
    redis='Allowed (no derivatives)', access_req='None', access='Landing page served a bot check to scripts', ver='UNVERIFIED', cat='Text-only corpus (OCR language modelling)', distinct='Y',
    notes='Would become an image-text historical set only if page facsimiles are provided - not confirmed.'))

R.append(E(
    id='TOCR-122', name='Internet Archive - Telugu-language items', desc='All archive.org items with language Telugu: scanned books, periodicals, manuscripts; IA machine OCR where present.',
    url='https://archive.org/search?query=language%3A%28Telugu+OR+tel%29', inst='Internet Archive', authors='Various', modality='Image (scans) + machine OCR text', task='Unlabelled scans',
    gran='Page', rs='Real', count='See catalogue TEL-DLIB-001', unit='items', ann='No (machine OCR only)', ann_type='IA OCR (machine)', lic='Varies per item', comm='Varies', redis='Varies', access_req='None',
    access='Open', ver='VERIFIED', cat='Scanned archive (image-only)', distinct='Y', catalogue='TEL-DLIB-001'))

R.append(E(
    id='TOCR-123', name='Digital Library of India (DLI) - Telugu books', parent='TOCR-122', desc='Scanned Telugu books from the Digital Library of India collection on archive.org.',
    url='https://archive.org/search?query=collection%3Adigitallibraryindia', inst='Digital Library of India / Internet Archive', authors='Various', modality='Image (scanned books)', task='Unlabelled scans',
    gran='Page', rs='Real', count='18,221 items (catalogue)', unit='books', ann='No', ann_type='None', lic='Mostly no licence stated', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open',
    ver='VERIFIED', cat='Scanned archive (image-only)', distinct='N (part of TOCR-122)', catalogue='TEL-DLIB-002'))

R.append(E(
    id='TOCR-124', name='Telugu newspapers e-paper archive (newspapers-telugu, archive.org)', desc='Daily Telugu e-paper editions 2017-2026 on archive.org.',
    url='https://archive.org/details/newspapers-telugu', inst='Internet Archive (uploader collection)', authors='Various publishers', modality='Image/PDF (newspaper pages)', task='Unlabelled page images',
    gran='Page', rs='Real', count='5,028 issues (catalogue)', unit='issues', ann='No', ann_type='None', lic='Newspaper copyright (no licence field)', comm='Not allowed', redis='NOT ALLOWED', access_req='None',
    access='Open', ver='VERIFIED', cat='Scanned archive (image-only)', distinct='Y', catalogue='TEL-PERIOD-001'))

R.append(E(
    id='TOCR-125', name='Historic Telugu magazines on archive.org (Bharathi, Andhra Patrika, Andhra Mahila ...)', parent='TOCR-122', desc='Scanned historic Telugu periodicals.',
    url='https://archive.org/search?query=title%3A%28%22andhra+patrika%22%29', inst='Internet Archive', authors='Various', modality='Image (scanned periodicals)', task='Unlabelled scans', gran='Page', rs='Real',
    count='See catalogue TEL-PERIOD-002', unit='issues', ann='No', ann_type='None', lic='Varies', comm='Varies', redis='Varies', access_req='None', access='Open', ver='VERIFIED',
    cat='Scanned archive (image-only)', distinct='N (part of TOCR-122)', catalogue='TEL-PERIOD-002'))

R.append(E(
    id='TOCR-126', name='AP Press Academy digitised old newspapers (pre-1977)', desc='Government of Andhra Pradesh archive of digitised old newspapers and periodicals in several languages incl. Telugu.',
    url='https://pressacademyarchives.ap.nic.in/', inst='Andhra Pradesh Press Academy', authors='Government of AP', lang='Telugu; others', modality='Image (newspaper pages)', task='Unlabelled scans',
    gran='Page', rs='Real', count='~1.6 million pages all languages (reported 2005)', unit='pages', ann='No', ann_type='None', lic='UNKNOWN (Government of AP)', comm='UNKNOWN', redis='UNKNOWN', access_req='Web viewer',
    access='Host did not resolve (DNS) on 2026-11-11; may be temporary', ver='PARTIALLY VERIFIED', cat='Scanned archive (image-only)', distinct='Y', catalogue='TEL-PERIOD-005'))

R.append(E(
    id='TOCR-127', name='Kaggle: Telugu Chandamama Books (harishml)', parent='TOCR-129', desc='PDF scans of Chandamama Telugu issues (1947 onward), titled "Chandamama Telugu OCR Dataset Books".',
    kaggle='https://www.kaggle.com/datasets/harishml/telugu-chandamama-books', url='https://www.kaggle.com/datasets/harishml/telugu-chandamama-books', inst='Individual', authors='Harish ML',
    modality='PDF scans (magazine)', task='Unlabelled scans', gran='Page', rs='Real', count='1,070 MB of issue PDFs', unit='PDF issues', ann='No', ann_type='None', lic='Unknown; magazine copyright', comm='Not established',
    redis='Not established', access_req='Kaggle account', access='Open listing', ver='VERIFIED', overlap='Subset copy of Chandamama archive (TOCR-129).', cat='Scanned archive (image-only)', distinct='N (copy)'))

R.append(E(
    id='TOCR-129', name='Chandamama (Telugu edition) 1947-2012 scans', desc='Scanned issues of the Telugu Chandamama children\'s magazine on archive.org.',
    url='https://archive.org/search?query=collection%3Achandamama-magazine', inst='Chandamama archive (uploaded to archive.org)', authors='Chandamama publications', modality='Image (scanned magazine)',
    task='Unlabelled scans', gran='Page', rs='Real', count='1,628 Telugu issues (~180 GB, catalogue)', unit='issues', ann='No', ann_type='None', lic='No licence field; magazine copyright', comm='Not established',
    redis='Not established', access_req='None', access='Open', ver='VERIFIED', overlap='Source of TOCR-058 and TOCR-127.', cat='Scanned archive (image-only)', distinct='Y', catalogue='TEL-PERIOD-003'))

# ------------------------------------------------------------------ text-in-image benchmarks
R.append(E(
    id='TOCR-128', name='HW-MLVQA (handwritten multilingual document VQA)', version='2025', desc='1,600 handwritten pages with 2,400 QA pairs for evaluating OCR-aware VQA; language list does not mention Telugu in the paper text.',
    url='https://arxiv.org/abs/2507.15655', paper='https://arxiv.org/abs/2507.15655', inst='CVIT, IIIT Hyderabad', authors='Aniket Pal, Ajoy Mondal, Minesh Mathew, C. V. Jawahar',
    lang='Multilingual (Telugu NOT VERIFIED)', modality='Image (handwriting)', task='Handwritten document VQA', gran='Page', rs='Real', count='1,600 pages total; Telugu UNKNOWN', unit='pages',
    ann='QA pairs', ann_type='Question-answer', lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='UNKNOWN', access='No dataset link in paper HTML', ver='UNVERIFIED',
    cat='Text-in-image benchmark (VQA / document understanding)', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-130', name='IndicVisionBench (OCR task)', version='2025 (ICLR 2026)', desc='~5K images and 37K QA pairs across English + 10 Indian languages covering OCR, multimodal MT and VQA.',
    hf='https://huggingface.co/datasets/krutrim-ai-labs/IndicVisionBench', github='https://github.com/ola-krutrim/IndicVisionBench', url='https://huggingface.co/datasets/krutrim-ai-labs/IndicVisionBench',
    paper='https://arxiv.org/abs/2511.04727', inst='Krutrim AI Labs', authors='Krutrim AI Labs', lang='Multilingual (English + 10 Indian incl. te tag)', modality='Image', task='OCR + VQA + MMT evaluation',
    gran='Image', rs='Real', count='~5K images total; Telugu share NOT VERIFIED', unit='images', ann='Yes', ann_type='OCR text / QA', lic='None declared on HF', comm='UNKNOWN', redis='UNKNOWN', access_req='None',
    access='Open (HF)', ver='PARTIALLY VERIFIED', overlap='Copies: AtharvImmverse/IndicVisionBench; lalit-03/IndicVisionBench (gated).', cat='Text-in-image benchmark (VQA / document understanding)', distinct='Y'))

R.append(E(
    id='TOCR-131', name='MInfoVisQA (multilingual infographic VQA)', desc='Localised chart/table renders in 24 languages with QA (evaluation split only).', hf='https://huggingface.co/datasets/arnodjiang/MInfoVisQA',
    url='https://huggingface.co/datasets/arnodjiang/MInfoVisQA', inst='Academic', authors='arnodjiang', lang='Multilingual (24 incl. te)', modality='Image (rendered charts/tables)', task='Visual QA', gran='Image',
    rs='Synthetic (rendered)', count='3,072 visuals total; Telugu share NOT VERIFIED', unit='images', ann='QA', ann_type='Question-answer', lic='other', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)',
    ver='PARTIALLY VERIFIED', cat='Text-in-image benchmark (VQA / document understanding)', distinct='Y'))

R.append(E(
    id='TOCR-132', name='adaption-multilingual-doc-qa (magazines VQA remaster)', desc='Multilingual QA on magazine page images asking for specific details (page numbers, names, dates).',
    hf='https://huggingface.co/datasets/Reubencf/adaption-multilingual-doc-qa', url='https://huggingface.co/datasets/Reubencf/adaption-multilingual-doc-qa', inst='Individual', authors='Reubencf',
    lang='Multilingual (45; te tag)', modality='Image (magazine pages)', task='Document QA', gran='Page', rs='Real (NOT VERIFIED)', count='1K-10K total; Telugu share NOT VERIFIED', unit='QA items', ann='QA',
    ann_type='Prompt/completion', lic='CC BY 4.0', comm='Allowed', redis='Allowed', access_req='None', access='Open (HF)', ver='PARTIALLY VERIFIED', cat='Text-in-image benchmark (VQA / document understanding)', distinct='Y'))

R.append(E(
    id='TOCR-133', name='nvidia/miracl-vision - Telugu', desc='Screenshots of Telugu Wikipedia articles for visual document retrieval, with queries and relevance labels.',
    hf='https://huggingface.co/datasets/nvidia/miracl-vision', url='https://huggingface.co/datasets/nvidia/miracl-vision', inst='NVIDIA', authors='NVIDIA', lang='Multilingual (18; te configs)',
    modality='Image (rendered web pages)', task='Visual document retrieval', gran='Page', rs='Rendered real pages', count='15,429 Telugu page images; 480 queries', unit='page images', ann='Retrieval qrels (text is the article, not a transcription)',
    ann_type='qrels', lic='CC BY-SA 4.0', comm='Allowed (share-alike)', redis='Allowed (share-alike)', access_req='None', access='Open (HF)', ver='VERIFIED',
    cat='Text-in-image benchmark (VQA / document understanding)', distinct='Y'))

R.append(E(
    id='TOCR-134', name='indic-citizen-information-board-pmgsy', desc='Document QA / extraction set on PMGSY citizen boards in 6 languages.', hf='https://huggingface.co/datasets/Litap007/indic-citizen-information-board-pmgsy',
    url='https://huggingface.co/datasets/Litap007/indic-citizen-information-board-pmgsy', inst='Individual', authors='Litap007', lang='Multilingual (6; te tag)', modality='Image (boards)', task='Document QA / extraction',
    gran='Image', rs='Real', count='1K-10K; earlier sampling found no Telugu rows', unit='images', ann='Machine-generated (per sibling card)', ann_type='QA / text', lic='CC BY 4.0', comm='Allowed', redis='Allowed',
    access_req='None', access='Open (HF)', ver='PARTIALLY VERIFIED', overlap='Sibling of TOCR-084.', cat='Text-in-image benchmark (VQA / document understanding)', distinct='Y'))

# ------------------------------------------------------------------ text-only corpora (never image-text)
for rid, name, url, cnt, lic, cat_id, note in [
        ('TOCR-135', 'Telugu Wikisource text dump (wikimedia/wikisource 20231101.te; tewikisource XML)', 'https://huggingface.co/datasets/wikimedia/wikisource', 'Proofread texts (see TOCR-049 for pages)', 'CC BY-SA', 'TEL-LIT-001', 'Text of TOCR-049 without images.'),
        ('TOCR-136', 'Sangraha - Telugu', 'https://huggingface.co/datasets/ai4bharat/sangraha', 'verified/tel 15.10 GB', 'CC BY 4.0', 'TEL-TXT-005', 'Large cleaned pretraining text.'),
        ('TOCR-137', 'IndicCorp v2 - Telugu', 'https://huggingface.co/datasets/ai4bharat/IndicCorpV2', 'te.txt 15.76 GB', 'CC0 1.0 (per README)', 'TEL-TXT-004', 'Web/news text.'),
        ('TOCR-138', 'CulturaX - Telugu', 'https://huggingface.co/datasets/uonlp/CulturaX', 'UNKNOWN (gated)', 'mC4/OSCAR terms', 'TEL-TXT-006', 'Gated on HF.'),
        ('TOCR-139', 'Telugu Wikipedia dumps (tewiki)', 'https://dumps.wikimedia.org/tewiki/latest/', '130,627 articles', 'CC BY-SA 4.0', 'TEL-TXT-001', ''),
]:
    R.append(E(id=rid, name=name, url=url, hf=url if 'huggingface' in url else 'NONE', desc=f'Text-only Telugu corpus useful for OCR language models / post-correction. {note}',
               inst='See catalogue', authors='See catalogue', modality='Text only', task='Language modelling for OCR (not OCR data)', gran='Text', rs='Real text', count=cnt, unit='text',
               ann='Not applicable', ann_type='None (no images)', lic=lic, comm='See licence', redis='See licence', access_req='None (CulturaX gated)', access='Open', ver='VERIFIED',
               cat='Text-only corpus (OCR language modelling)', distinct='Y', catalogue=cat_id))

# per-row corrections from the HF API check (2026-11-11)
for _r in R:
    if _r['id'] == 'TOCR-138':
        _r.update(access='Gated on HF (login + accept terms, automatic)', access_req='HF account + accept terms', ver='GATED')
    if _r['id'] == 'TOCR-135':
        _r.update(lic='CC BY-SA 3.0 / GFDL (HF tag); live Wikisource text is CC BY-SA 4.0')

R.append(E(
    id='TOCR-140', name='harsha-desaraju/telugu-ocr-text (+ -uncombined) - source vs OCR text pairs', desc='News text and the OCR read of its rendering, for OCR post-correction; text only.',
    hf='https://huggingface.co/datasets/harsha-desaraju/telugu-ocr-text', url='https://huggingface.co/datasets/harsha-desaraju/telugu-ocr-text', inst='Individual', authors='Harsha Desaraju', modality='Text only',
    task='OCR post-correction', gran='Document chunk', rs='Synthetic OCR errors', count='50,000 (+113,592 uncombined)', unit='text pairs', ann='Yes', ann_type='src_text / ocr_text', lic='None declared',
    comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='VERIFIED', overlap='Text side of TOCR-094.', cat='Text-only corpus (OCR language modelling)', distinct='Y'))

R.append(E(
    id='TOCR-141', name='eswardivi/indiccorp_telugu_line', parent='TOCR-137', desc='IndicCorp Telugu split into lines (text only).', hf='https://huggingface.co/datasets/eswardivi/indiccorp_telugu_line',
    url='https://huggingface.co/datasets/eswardivi/indiccorp_telugu_line', inst='Individual', authors='eswardivi', modality='Text only', task='Rendering source / LM', gran='Line', rs='Real text',
    count='42,916,522 lines', unit='lines', ann='Not applicable', ann_type='None', lic='None declared (IndicCorp terms)', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='VERIFIED',
    cat='Text-only corpus (OCR language modelling)', distinct='N (derivative of TOCR-137)'))

R.append(E(
    id='TOCR-142', name='TeluguOCR/corpora - Telugu Internet Unicode corpora', desc='Telugu Unicode text corpora collected by the TeluguOCR project for language modelling.', github='https://github.com/TeluguOCR/corpora',
    url='https://github.com/TeluguOCR/corpora', inst='TeluguOCR project', authors='Rakesh Achanta et al.', modality='Text only', task='Language model for OCR', gran='Text', rs='Real text', count='~33 MB repo',
    unit='text', ann='Not applicable', ann_type='None', lic='None stated', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (GitHub)', ver='VERIFIED', cat='Text-only corpus (OCR language modelling)', distinct='Y'))

R.append(E(
    id='TOCR-143', name='On-line Handwriting Recognition of Indian Scripts - The First Benchmark (ICFHR 2010)', desc='Online handwriting benchmark from ISI Kolkata / HP Labs; scripts and Telugu inclusion NOT VERIFIED.',
    url='https://dblp.org/rec/conf/icfhr/MondalBPDM10', paper='https://doi.org/10.1109/ICFHR.2010.39', doi='10.1109/ICFHR.2010.39', inst='ISI Kolkata; HP Labs India',
    authors='T. Mondal, U. Bhattacharya, S. K. Parui, K. Das, D. Mandalapu', lang='Indian scripts (Telugu NOT VERIFIED)', modality='Online pen trajectories', task='Online handwriting recognition',
    gran='Character / word', rs='Real', count='UNKNOWN', unit='UNKNOWN', ann='Yes (per paper)', ann_type='NOT VERIFIED', lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='UNKNOWN', access='No release found',
    ver='UNVERIFIED', cat='Character / glyph classification', distinct='UNKNOWN'))

# ------------------------------------------------------------------ related resources (not datasets; not counted)
def REL(rid, name, url, desc, lic='See source', catalogue='NONE', ver='VERIFIED', inst='See source', github='NONE', hf='NONE'):
    return E(id=rid, name=name, url=url, desc=desc, lic=lic, inst=inst, github=github, hf=hf, modality='Not a dataset', task='Supporting resource', gran='Not applicable',
             rs='Not applicable', count='Not applicable', unit='Not applicable', ann='Not applicable', ann_type='Not applicable', comm='See source', redis='See source', access_req='None',
             access='Open', ver=ver, cat='Related resource (not a dataset)', distinct='N (not a dataset)', catalogue=catalogue)


R.append(REL('TOCR-144', 'ILOCR / Bhashini OCR API catalogue (132 Telugu model entries)', 'https://ilocr.iiit.ac.in/api_list/',
             'Master list of 1,456 consortium OCR APIs; 132 are Telugu (layout, word recognition, pipelines, script detection) from IIITH, IITB, IITD, IITJ, plus Google OCR, Tesseract, EasyOCR, Surya entries. Models, not data; api_detail pages return server errors.',
             inst='NLTM OCR consortium (IIIT Hyderabad)'))
R.append(REL('TOCR-145', 'Bhashini ULCA - dataset/model portal', 'https://bhashini.gov.in/ulca', 'National language-data portal that aggregates OCR datasets/models; dataset search needs the web app.',
             catalogue='TEL-SPEECH-018', ver='PARTIALLY VERIFIED', inst='MeitY Bhashini'))
R.append(REL('TOCR-146', 'AIKosh (IndiaAI) dataset platform', 'https://aikosh.indiaai.gov.in/home/datasets', 'Government dataset portal re-hosting Indian datasets incl. IIIT-INDIC-HW-WORDS and IndicDLP.',
             catalogue='TEL-SPEECH-019', ver='PARTIALLY VERIFIED', inst='IndiaAI Mission, MeitY'))
R.append(REL('TOCR-147', 'Tesseract Telugu models and langdata (tel.traineddata)', 'https://github.com/tesseract-ocr/tessdata_best/blob/main/tel.traineddata',
             'Trained Telugu OCR models and training text/wordlists; useful for synthetic data and baselines.', lic='Apache-2.0', catalogue='TEL-OCR-009', inst='Tesseract OCR project'))
R.append(REL('TOCR-148', 'Telugu Unicode fonts (Noto, Pothana2000, Vemana, Google Fonts Telugu subset)', 'https://fonts.google.com/?subset=telugu',
             'Fonts used to render synthetic Telugu OCR data.', lic='SIL OFL 1.1 (most)', catalogue='TEL-DIAL-004', inst='Google Fonts; AndhraBharati'))
R.append(REL('TOCR-149', 'IndicPhotoOCR toolkit (BSTD models)', 'https://github.com/Bhashini-IITJ/IndicPhotoOCR', 'Scene-text detection, script ID and recognition models for 11 Indian languages + English.',
             github='https://github.com/Bhashini-IITJ/IndicPhotoOCR', inst='IIT Jodhpur (Bhashini)'))
R.append(REL('TOCR-150', 'TeluguOCR data generators (datagen_initio, datagen_duo)', 'https://github.com/TeluguOCR', 'Scripts to generate millions of rendered Telugu characters/glyphs for banti OCR training.',
             github='https://github.com/TeluguOCR/datagen_initio', inst='TeluguOCR project'))
R.append(REL('TOCR-151', 'IndicSceneTextRendering (synthetic scene-text renderer)', 'https://github.com/mineshmathew/IndicSceneTextRendering', 'Renderer used for IIIT-ILST synthetic word images.',
             github='https://github.com/mineshmathew/IndicSceneTextRendering', inst='CVIT, IIIT Hyderabad'))
R.append(REL('TOCR-152', 'gopalvarun03/Telugu-OCR - Vedic Telugu-script synthetic data generator', 'https://github.com/gopalvarun03/Telugu-OCR',
             'Notebooks to render synthetic Telugu-script Vedic text images from 85+ transcription files; generated data not in repo.', github='https://github.com/gopalvarun03/Telugu-OCR',
             ver='PARTIALLY VERIFIED', inst='Individual'))
R.append(REL('TOCR-153', 'harsha-desaraju/TeluguOCR (pipeline + model)', 'https://github.com/harsha-desaraju/TeluguOCR',
             'Code that builds the harsha-desaraju Wikisource line, synthetic line and consensus datasets; model card on HF.', lic='MIT', github='https://github.com/harsha-desaraju/TeluguOCR', inst='Individual'))

# ------------------------------------------------------------------ rejected candidates (kept for transparency)
def REJ(rid, name, url, reason, inst='See source'):
    return E(id=rid, name=name, url=url, desc='Rejected candidate - see notes.', inst=inst, modality='See notes', task='See notes', gran='Not applicable', rs='Not applicable',
             count='Not applicable', unit='Not applicable', ann='Not applicable', ann_type='Not applicable', access='See notes', ver='REJECTED', cat='Rejected', distinct='N', notes=reason)


for rid, name, url, reason in [
    ('TOCR-154', '3D Telugu Character Recognition (IEEE DataPort yz7d-cz45)', 'https://ieee-dataport.org/documents/3d-telugu-character-recognition', 'Accelerometer x/y/z sensor CSVs for in-air writing of 5 characters - no images.'),
    ('TOCR-155', 'HSC-IndicDB (Mendeley dkmxgd8n79)', 'https://data.mendeley.com/datasets/dkmxgd8n79/1', 'Description names Bengali, Devanagari, Kannada, Malayalam; Telugu not mentioned.'),
    ('TOCR-156', 'Learn Telugu letters Alphabets with Audio (Mendeley 98rd3nx2n4)', 'https://data.mendeley.com/datasets/98rd3nx2n4/1', 'Audio pronunciation learning resource, not OCR data.'),
    ('TOCR-157', 'AI-powered multilingual OCR system for historical documents (Zenodo 20604818)', 'https://doi.org/10.5281/zenodo.20604818', 'Typed as dataset but is a technical specification report; no data.'),
    ('TOCR-158', 'nvidia/OCR-Synthetic-Multilingual-v1 (and Kaggle 24K starter subset)', 'https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1', 'Languages en, ja, ko, ru, zh only - no Telugu.'),
    ('TOCR-159', 'ICDAR RRC MLT-2017 / MLT-2019', 'https://rrc.cvc.uab.es/?ch=15', 'Indian scripts are Bangla and Devanagari only - no Telugu.'),
    ('TOCR-160', 'MITDI - Mixed-lingual Indic Texts in Digital Images (MTAP 2022)', 'https://doi.org/10.1007/s11042-022-12596-7', 'English, Bangla, Hindi only.'),
    ('TOCR-161', 'Transfer Learning for STR in Indian Languages - released real data (Gunna et al. 2021)', 'https://cvit.iiit.ac.in/research/projects/cvit-projects/transfer-learning-for-scene-text-recognition-in-indian-languages', 'Released real data is Gujarati and Tamil only; Telugu results use IIIT-ILST.'),
    ('TOCR-162', 'interfaze-ai/ocr-mlt-50m', 'https://huggingface.co/datasets/interfaze-ai/ocr-mlt-50m', '60 rows across 50 languages; no meaningful Telugu content.'),
    ('TOCR-163', 'AbhishekBhandari/Indic-post-ocr-correction', 'https://huggingface.co/datasets/AbhishekBhandari/Indic-post-ocr-correction', 'Gujarati, Hindi, Marathi only.'),
    ('TOCR-164', 'Aus-23/indic-synthetic-scene-text-1000', 'https://huggingface.co/datasets/Aus-23/indic-synthetic-scene-text-1000', 'Marathi, Hindi, Gujarati, Bengali only.'),
    ('TOCR-165', 'Crossmodal-3600 caption sets (floschne/xm3600, xm3600_1k, dinhanhx/crossmodal-3600, PangeaBench-xm100, ai-enthusiasm-community/XM3600)', 'https://huggingface.co/datasets/floschne/xm3600', 'Telugu image captions, not text in images.'),
    ('TOCR-166', 'WIT (wikimedia/wit_base, VedaLabs/wit_base)', 'https://huggingface.co/datasets/wikimedia/wit_base', 'Image-caption pairs; no Telugu found in sample; not OCR.'),
    ('TOCR-167', 'CC3M-35L / COCO-35L (ai-enthusiasm-community)', 'https://huggingface.co/datasets/ai-enthusiasm-community/CC3M-35L', 'Translated captions, not OCR.'),
    ('TOCR-168', 'visheratin/laion-coco-nllb', 'https://huggingface.co/datasets/visheratin/laion-coco-nllb', 'Translated captions, not OCR.'),
    ('TOCR-169', 'ARTPARK-IISc Vaani (and benchmarks)', 'https://huggingface.co/datasets/ARTPARK-IISc/Vaani', 'Speech dataset with prompt images; not OCR.'),
    ('TOCR-170', 'DRISHTIKON (13ari / Vipashyana)', 'https://huggingface.co/datasets/13ari/DRISHTIKON', 'Cultural VQA; no Telugu text found in sample; not OCR.'),
    ('TOCR-171', 'neulab/CulturalGround and other cultural VQA sets (symile-m3, global-piqa, mvl-sib, ArogyaBodha, IndicMMVet, IndicPope, IndicLLaVABench, Kaleidoscope)', 'https://huggingface.co/datasets/neulab/CulturalGround', 'General VQA/QA with Telugu questions; images are not text-centric.'),
    ('TOCR-172', 'krutrim-ai-labs/ocr_rotation_bench', 'https://huggingface.co/datasets/krutrim-ai-labs/ocr_rotation_bench', 'Page-rotation classification; no Telugu in sampled rows.'),
    ('TOCR-173', 'Shaip OCR training data', 'https://www.shaip.com/solutions/optical-character-recognition-ocr-machine-learning/', 'Custom-collection vendor page; no Telugu OCR product listed.'),
    ('TOCR-174', 'GitHub UthejKaramalapudi/Handwritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images', 'https://github.com/UthejKaramalapudi/Handwritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images', 'Code only; no images in repository.'),
    ('TOCR-175', 'GitHub Harathi123/Telugu-Character-Recognition-using-CNN', 'https://github.com/Harathi123/Telugu-Character-Recognition-using-CNN', 'Reuses HP Labs data (TOCR-021); no new data.'),
    ('TOCR-176', 'GitHub alfahimmohammad/Telugu-Handwritten-Text-Recognition', 'https://github.com/alfahimmohammad/Telugu-Handwritten-Text-Recognition', 'Reuses CVIT IIIT-HW-Telugu (TOCR-001); no new data.'),
    ('TOCR-177', 'GitHub jaganmohanreddy2106/Telugu-Handwritten-Digit-Recognition', 'https://github.com/jaganmohanreddy2106/Telugu-Handwritten-Digit-Recognition', '10 example digit images only; no dataset.'),
    ('TOCR-178', 'Telugu Alphabets 52-letter chart (Zenodo 20079705)', 'https://doi.org/10.5281/zenodo.20079705', 'Single educational chart image; record now HTTP 410 (removed).'),
    ('TOCR-179', 'Telugu NLP / news / lyrics Kaggle sets (text-only, non-OCR)', 'https://www.kaggle.com/datasets/sudalairajkumar/telugu-nlp', 'Text classification/NLP corpora surfaced by Kaggle search; not OCR and not needed as OCR LM sources.'),
]:
    R.append(REJ(rid, name, url, reason))

for rid, name, url, cnt, note in [
    ('TOCR-180', 'Kaggle: rs synth indic data (ocrteamriad)', 'https://www.kaggle.com/datasets/ocrteamriad/rs-synth-indic-data', '23,294 MB of TFRecords', 'Synthetic Indic OCR records; Telugu presence NOT VERIFIED (no description).'),
    ('TOCR-181', 'Kaggle: OCR Stress Test v2 Multilingual Benchmark (harishk2209)', 'https://www.kaggle.com/datasets/harishk2209/ocr-stress-test-v2', '183.6 MB', 'Indic folders include gu, tamil ...; Telugu presence NOT VERIFIED (file list fetch failed).'),
]:
    R.append(E(id=rid, name=name, kaggle=url, url=url, desc=note, inst='Individual', modality='Image', task='OCR', gran='UNKNOWN', rs='UNKNOWN', count=cnt, unit='bytes',
               ann='UNKNOWN', ann_type='UNKNOWN', lic='Unknown / other', access_req='Kaggle account', access='Open listing', ver='UNVERIFIED',
               lang='Multilingual (Telugu NOT VERIFIED)', cat='OCR image-text: synthetic' if 'synth' in name else 'OCR image-text: printed', distinct='UNKNOWN'))
