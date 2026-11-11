"""Directory records, part A: handwritten (word/line/page), handwritten characters & digits.

Each record is a dict; keys are mapped to the 36 required CSV columns (+2 classification columns) by build_directory.py.
Facts come from the evidence files under ocr/directory/evidence/ and the phase-1/2 OCR acquisition work
(ocr/acquisition/). Anything not confirmed from an official source is written as UNKNOWN or NOT VERIFIED.
"""
from common import E

R = []

# ------------------------------------------------------------------ IIIT Hyderabad handwritten word family
R.append(E(
    id='TOCR-001', name='IIIT-HW-Telugu', aliases='IIIT-HW-TELUGU; Telugu handwritten word dataset (CVIT 2018); IIIT-HW-Telugu_v1',
    version='v1 (2018); two archives on CVIT page: IIIT-HW-Telugu.zip and IIIT-HW-Telugu_v1.tar.gz',
    desc='Original CVIT release of offline handwritten Telugu word images with word transcriptions, written by multiple writers on boxed forms.',
    url='https://cvit.iiit.ac.in/research/projects/cvit-projects/indic-hw-data',
    download='https://cvit.iiit.ac.in/images/Projects/wordlevel-Indicscripts/IIIT-HW-Telugu.zip ; https://cvit.iiit.ac.in/images/Projects/wordlevel-Indicscripts/IIIT-HW-Telugu_v1.tar.gz',
    paper='https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2018/spotting-recognition-handwritten.pdf',
    doi='NOT VERIFIED (ICFHR 2018 paper)', inst='CVIT, IIIT Hyderabad', authors='Kartik Dutta, Praveen Krishnan, Minesh Mathew, C. V. Jawahar',
    modality='Image (offline handwriting, scanned forms)', task='Handwritten word recognition; word spotting', gran='Word', rs='Real',
    count='>120,000 (official page: "over 120K handwritten words")', unit='word images',
    ann='Yes', ann_type='Word-level Unicode transcription', lic='NOT STATED on the CVIT page', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None (direct download)', access='Open download (page live 2026-11-11)', ver='VERIFIED',
    overlap='Parent of TOCR-002 (ILOCR v0.5 re-release, same word list/writers) and of the IHTR 2022/2023 Telugu tracks.',
    quality='See TOCR-002 for measured label quality of the re-release.', cat='OCR image-text: handwritten', distinct='Y',
    catalogue='TEL-OCR-002 (as part of)'))

R.append(E(
    id='TOCR-002', name='IIIT-INDIC-HW-WORDS-Telugu (ILOCR v0.5)', aliases='IIIT-INDIC-HW-WORDS Telugu; ILOCR dataset 23',
    parent='TOCR-001', version='v0.5 (ILOCR NLTM release)',
    desc='Handwritten Telugu word images from boxed forms, with official train/val/test splits, label files and training vocabulary.',
    url='https://ilocr.iiit.ac.in/dataset/23/',
    download='https://ilocr.iiit.ac.in/public/handwritten/phase-0/v0.5/telugu/IIIT-INDIC-HW-WORDS-Telugu/{train,val,test}.zip',
    paper='https://doi.org/10.1007/978-3-030-86337-1_30', doi='10.1007/978-3-030-86337-1_30', inst='CVIT / NLTM OCR consortium, IIIT Hyderabad',
    authors='Santhoshini Gongidi, C. V. Jawahar', modality='Image (offline handwriting)', task='Handwritten word recognition', gran='Word', rs='Real',
    count='126,413 images (88,534 / 19,980 / 17,899); 118,516 labelled (train gt has 80,637 lines)', unit='word images',
    ann='Yes', ann_type='Word transcription (tab-separated gt.txt) + vocabulary', lic='CC BY 4.0 (stated on dataset page)', comm='Allowed with attribution',
    redis='Allowed with attribution', access_req='None', access='Open download (zips HTTP 200, 2026-11-10)', ver='VERIFIED',
    overlap='Same content as IHTR-2023 Telugu train (80,637/80,637 identical path+label pairs, TOCR-005); derived from TOCR-001; Kaggle/HF mirrors exist (TOCR-018).',
    quality='Phase-2 audit: 15/16 labels correct; 35 labels have invalid sign order (legacy encoding, e.g. కనే్నసి); 17 blank crops; official splits writer-disjoint.',
    cat='OCR image-text: handwritten', distinct='N (newer release of TOCR-001; family counted once)', catalogue='TEL-OCR-002',
    notes='Train zip holds 7,897 images with no label line.'))

R.append(E(
    id='TOCR-003', name='IIIT-INDIC-HW-WORDS (multi-script umbrella)', aliases='IIIT-INDIC-HW-WORDS 10 scripts',
    version='2021 (ICDAR)', desc='Umbrella benchmark of handwritten word images in 10 Indic scripts; Telugu portion is the earlier IIIT-HW-Telugu release.',
    url='https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-indic-hw-words', paper='https://doi.org/10.1007/978-3-030-86337-1_30',
    doi='10.1007/978-3-030-86337-1_30', inst='CVIT, IIIT Hyderabad', authors='Santhoshini Gongidi, C. V. Jawahar',
    lang='Multilingual (10 Indic scripts incl. Telugu)', script='Multiple incl. Telugu', modality='Image (offline handwriting)',
    task='Handwritten word recognition', gran='Word', rs='Real', count='872K new instances in 8 scripts + earlier Devanagari & Telugu sets; Telugu subset = TOCR-001/002',
    unit='word images', ann='Yes', ann_type='Word transcription', lic='NOT STATED on CVIT page (ILOCR per-language pages: CC BY 4.0)', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None', access='Open download (per-language zips on CVIT page; Telugu not re-hosted there)', ver='VERIFIED',
    overlap='Telugu part is TOCR-001/002; not counted separately.', quality='See TOCR-002.', cat='OCR image-text: handwritten', distinct='N (umbrella; Telugu = TOCR-001)'))

R.append(E(
    id='TOCR-004', name='IHTR 2022 Telugu track (ICFHR 2022 competition)', aliases='ICFHR 2022 Indic Handwriting Text Recognition',
    parent='TOCR-001', version='2022', desc='Competition packaging of IIIT-INDIC-HW Telugu words (train 80,637 / val 19,980 / test 18,898 per competition page).',
    url='https://cvit.iiit.ac.in/ihtr2022/dataset.html', download='https://cvit.iiit.ac.in/ihtr2022/assets/dataset/{trainingset,validationset,testset}.zip (all-language zips, 27.8 / 4.8 / 10.9 GB)',
    inst='CVIT, IIIT Hyderabad', authors='Competition organisers (CVIT)', modality='Image (offline handwriting)', task='Handwritten word recognition',
    gran='Word', rs='Real', count='Train 80,637 / Val 19,980 / Test 18,898 (competition page table)', unit='word images', ann='Yes (train/val); test labels not released',
    ann_type='Word transcription', lic='NOT STATED', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open download (HTTP 200, 2026-11-10)',
    ver='PARTIALLY VERIFIED', overlap='Benchmark repackaging of TOCR-001/002; not independent data.', cat='OCR image-text: handwritten', distinct='N (derivative)'))

R.append(E(
    id='TOCR-005', name='IHTR 2023 Telugu track (ICDAR 2023 competition)', aliases='ICDAR 2023 IHTR',
    parent='TOCR-002', version='2023', desc='Competition packaging of IIIT-INDIC-HW Telugu: train 80,637, val 1,000, test 5,000 (test unlabelled).',
    url='https://ilocr.iiit.ac.in/ihtr/dataset.html', download='https://ilocr.iiit.ac.in/ihtr/assets/dataset/trainingset/telugu.zip ; testset/Telugu.zip ; validationset.zip',
    inst='CVIT / ILOCR, IIIT Hyderabad', authors='Competition organisers', modality='Image (offline handwriting)', task='Handwritten word recognition',
    gran='Word', rs='Real', count='Train 80,637 / Val 1,000 / Test 5,000', unit='word images', ann='Yes (train/val); test unlabelled', ann_type='Word transcription',
    lic='NOT STATED', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open download (HTTP 200, 2026-11-10)', ver='VERIFIED',
    overlap='Train = TOCR-002 train exactly (80,637/80,637 identical path+label pairs, checked 2026-11-10).', cat='OCR image-text: handwritten', distinct='N (duplicate)'))

R.append(E(
    id='TOCR-006', name='IIIT-Indic-HW-UC Telugu (Unconstrained Camera-captured Indic Offline Handwriting)', aliases='IIIT-Indic-HW-UC; ucciohd',
    version='2024', desc='Camera-captured handwritten Telugu pages segmented into word crops with transcriptions; official word-level splits plus extra manually annotated folders.',
    url='https://cvit.iiit.ac.in/usodi/ucciohd.php', download='https://cvit.iiit.ac.in/images/datasets/indic_handwritten/telugu.zip (4.82 GB)',
    paper='https://doi.org/10.1007/978-3-031-78495-8_21', doi='10.1007/978-3-031-78495-8_21', inst='CVIT, IIIT Hyderabad', authors='Ajoy Mondal, C. V. Jawahar',
    modality='Image (camera-captured handwriting)', task='Handwritten word recognition', gran='Word (page annotations behind it)', rs='Real',
    count='314,243 labelled crops in zip; 200,000 in official splits (150K/20K/30K); 280,226 after cleaning (phase 2)', unit='word images',
    ann='Yes', ann_type='Word transcription; 33,306 placeholder "NA" labels', lic='NOT STATED on project page', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None (direct download)', access='Open download (zip CRC-checked 2026-11-10)', ver='VERIFIED',
    overlap='Superset of the ICDAR 2024 HWD page collection: contains all 700 PLHWTR/IHWWR test pages and 2,062 IHWWR train pages (TOCR-007/008).',
    quality='Audit 14/16 correct; official splits leak (all 4,597 identifiable pages split across train/val/test).', cat='OCR image-text: handwritten', distinct='Y'))

R.append(E(
    id='TOCR-007', name='IHWWR-1.0 Telugu (ICDAR 2024 HWD Task A)', aliases='ICDAR 2024 Competition on Recognition and VQA on Handwritten Documents - isolated word',
    parent='TOCR-006', version='1.0 (2024)', desc='Word crops from camera-captured handwritten Telugu pages; labelled training set and unlabelled test set.',
    url='https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html',
    download='https://ilocr.iiit.ac.in/icdar_2024_hwd/assets/dataset/IHWR-1.0/Training-Set/Word_Level_Telugu_Training_Set.zip ; .../Test-Set/Word_Level_Telugu_Test_Set.zip',
    paper='https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2024/Competition_on_Recognition_and_VQA_on_Handwritten_Documents.pdf',
    inst='CVIT / ILOCR, IIIT Hyderabad', authors='Competition organisers (Ajoy Mondal et al.)', modality='Image (camera-captured handwriting)',
    task='Handwritten word recognition', gran='Word', rs='Real', count='Train 77,625 (labelled; 63,341 Telugu words, 14,284 punctuation/digit crops) / Test 9,585 (unlabelled)',
    unit='word images', ann='Yes (train only)', ann_type='Word transcription', lic='NOT STATED on competition page', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None', access='Open download (HTTP 200)', ver='VERIFIED',
    overlap='Word crops of PLHWTR pages (TOCR-008); 2,062 of 3,476 pages also in HW-UC (TOCR-006) with different segmentation.', quality='Audit 16/16 correct after removing punctuation-only crops.',
    cat='OCR image-text: handwritten', distinct='N (subset/re-crop of TOCR-006/008 pages)'))

R.append(E(
    id='TOCR-008', name='PLHWTR-1.0 Telugu (ICDAR 2024 HWD Task B)', aliases='Page-level handwritten text recognition 1.0',
    parent='TOCR-006', version='1.0 (2024)', desc='Page images of camera-captured Telugu handwriting with page-level text of the prompted sentences (train); test pages unlabelled.',
    url='https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html',
    download='https://ilocr.iiit.ac.in/icdar_2024_hwd/assets/dataset/PLHWTR-1.0/Training-Set/Page_Level_Telugu_Training_Set.zip (3.0 GB) ; Test-Set (742 MB)',
    inst='CVIT / ILOCR, IIIT Hyderabad', authors='Competition organisers', modality='Image (camera-captured handwriting)', task='Page-level handwritten text recognition',
    gran='Page', rs='Real', count='Train 3,496 pages (text) / Test 700 pages (no labels)', unit='page images', ann='Yes (train)', ann_type='Page text (no word boxes in released train zip)',
    lic='NOT STATED', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open download', ver='VERIFIED',
    overlap='Same pages as IHWWR (TOCR-007); all 700 test pages inside HW-UC (TOCR-006).', quality='Writer page numbers not transcribed; some lines run off the photo.',
    cat='OCR image-text: handwritten', distinct='N (same pages as TOCR-006)'))

R.append(E(
    id='TOCR-009', name='ICDAR 2025 IHDR Telugu (Indic Handwritten Document Recognition)', aliases='ICDAR 2025 Competition on Indic Handwritten Document Recognition',
    version='2025', desc='Telugu validation/test pages for word detection (Task A) and page recognition (Task B) in a 10-language competition.',
    url='https://ilocr.iiit.ac.in/icdar_2025_Indic_HDR/dataset.html', download='https://ilocr.iiit.ac.in/icdar_2025_Indic_HDR/assets/dataset/Task-{A,B}/{Validation,Test}/Telugu-*.zip (all return HTTP 404)',
    inst='CVIT / ILOCR, IIIT Hyderabad', authors='Competition organisers', modality='Image (camera-captured handwriting)', task='Handwritten word detection; page recognition',
    gran='Page', rs='Real', count='UNKNOWN (10,000 pages across 10 languages per site)', unit='page images', ann='Yes for validation (boxes / page text) per site', ann_type='Word boxes; page transcription',
    lic='Site: "freely available for academic and research purposes"', comm='UNKNOWN', redis='UNKNOWN', access_req='Contact organisers',
    access='Telugu zips HTTP 404 (checked 2026-11-10); charlist zip still downloads', ver='INACCESSIBLE',
    overlap='Site lists HW-UC, IHWWR, PLHWTR, IHTR as pre-training sets; likely same collection effort.', cat='OCR image-text: handwritten', distinct='Y (distinct, currently inaccessible)'))

R.append(E(
    id='TOCR-010', name='IIIT-INDIC-HW-WILD Telugu (SemiHastakshar unlabelled corpus)', aliases='Indic-HW-Wild',
    version='2025', desc='Unlabelled handwritten Telugu word crops gathered from public notes/answer sheets plus crops of IIITS-THDB and PHDIndic_11.',
    url='https://lalithaevani.github.io/SemiHastakshar-page/', hf='https://huggingface.co/datasets/evanilalitha/IIIT-INDIC-HW-WILD',
    github='https://github.com/LalithaEvani/SemiHastakshar', paper='https://doi.org/10.1145/3774521.3774605', doi='10.1145/3774521.3774605',
    inst='IIIT Hyderabad', authors='Lalitha Evani et al.', lang='Multilingual (9 Indic incl. Telugu)', modality='Image (handwriting, in the wild)',
    task='Semi-supervised HTR (unlabelled pool)', gran='Word', rs='Real', count='Telugu 301,170 (257,976 in repo + 43,194 rebuilt from source datasets)',
    unit='word images', ann='No', ann_type='None (unlabelled by design)', lic='CC BY 4.0 for own images; source terms for rebuilt crops', comm='Allowed for own images',
    redis='Allowed for own images', access_req='None', access='Open (HF)', ver='VERIFIED',
    overlap='Contains crops from IIITS-THDB (TOCR-014) and PHDIndic_11 (TOCR-015).', cat='Image-only (no transcription)', distinct='Y'))

R.append(E(
    id='TOCR-011', name='Assamese and Telugu Handwritten Text Dataset', aliases='IEEE DataPort 10.21227/3ycm-px23',
    version='2024', desc='Mobile-camera photos (300 dpi) of handwritten Assamese and Telugu essays/short stories, 5-10 lines each; intended for language recognition and line/word/character segmentation.',
    url='https://ieee-dataport.org/documents/assamese-and-telugu-handwritten-text-dataset', doi='10.21227/3ycm-px23', inst='NIT Silchar (authors)',
    authors='Prarthana Dutta, Naresh Babu Muppalaneni', lang='Assamese; Telugu', script='Telugu; Bengali-Assamese', modality='Image (camera-captured handwriting)',
    task='Segmentation; language identification; (recognition if text provided)', gran='Page (5-10 lines)', rs='Real', count='222 Telugu samples (200 Assamese)', unit='page images',
    ann='NOT VERIFIED', ann_type='NOT VERIFIED (DataCite description mentions no transcriptions)', lic='CC BY 4.0 (DataCite)', comm='Allowed with attribution',
    redis='Allowed with attribution', access_req='IEEE DataPort account (login to download)', access='Gated (landing page blocks automated clients; DataCite record verified)',
    ver='PARTIALLY VERIFIED', cat='Image-only (transcription NOT VERIFIED)', distinct='Y', notes='Metadata from DataCite API; page returned HTTP 403 to scripts.'))

R.append(E(
    id='TOCR-012', name='FutureBeeAI Telugu Handwritten Sticky Notes OCR Image Dataset', version='Last updated Sep 2023',
    desc='Commercial set of 2,000+ phone photos of handwritten Telugu sticky notes from 200+ contributors, with metadata; transcription offered as a paid add-on.',
    url='https://www.futurebeeai.com/dataset/ocr-dataset/telugu-sticky-notes-ocr-image-dataset', inst='FutureBeeAI (vendor)', authors='FutureBeeAI',
    modality='Image (camera-captured handwriting)', task='Handwritten OCR (after annotation)', gran='Image (note)', rs='Real', count='2,000+ (vendor claim)', unit='images',
    ann='No (metadata only; bounding boxes/transcription available as custom service)', ann_type='Metadata CSV', lic='Commercial licence (vendor: "available for commercial use")',
    comm='Allowed under purchase', redis='NOT ALLOWED (commercial)', access_req='Purchase / sales contact', access='Paid', ver='COMMERCIAL',
    cat='Image-only (no transcription)', distinct='Y', notes='Vendor marketing page; contents not independently inspected.'))

R.append(E(
    id='TOCR-013', name='FutureBeeAI Telugu Shopping List OCR Image Dataset', version='Last updated Sep 2023',
    desc='Commercial set of 2,000+ phone photos of handwritten Telugu shopping lists with metadata.',
    url='https://www.futurebeeai.com/dataset/ocr-dataset/telugu-shopping-list-ocr-image-dataset', inst='FutureBeeAI (vendor)', authors='FutureBeeAI',
    modality='Image (camera-captured handwriting)', task='Handwritten OCR (after annotation)', gran='Image (list)', rs='Real', count='2,000+ (vendor claim)', unit='images',
    ann='No (transcription paid add-on)', ann_type='Metadata CSV', lic='Commercial licence', comm='Allowed under purchase', redis='NOT ALLOWED',
    access_req='Purchase', access='Paid', ver='COMMERCIAL', cat='Image-only (no transcription)', distinct='Y'))

R.append(E(
    id='TOCR-014', name='IIITS-THDB (IIIT Sri City Telugu Handwriting Database)', version='2018 (ICDAR)',
    desc='450 handwritten Telugu pages (150 writers x 3 pages) collected for writer identification.',
    url='https://chrizandr.github.io/IIITS-THDB/', download='Google Drive links on project page (NOT VERIFIED)', paper='https://digitalcommons.isical.ac.in/conf-articles/110',
    inst='IIIT Sri City', authors='Gadde, Reddy, Pulabaigari, Pal', modality='Image (scanned handwriting)', task='Writer identification', gran='Page', rs='Real',
    count='450 pages (150 writers)', unit='page images', ann='Writer IDs only', ann_type='Writer label (no transcription confirmed)',
    lic='Non-commercial research and education only (project page)', comm='Not allowed', redis='NOT ALLOWED', access_req='None stated', access='Open (Drive links; not test-downloaded)',
    ver='PARTIALLY VERIFIED', overlap='37,787 word crops reused (unlabelled) in TOCR-010.', cat='Image-only (no transcription)', distinct='Y'))

R.append(E(
    id='TOCR-016', name='TEXTRON INDIC datasets - Telugu handwritten pages', aliases='TEXTRON (WACV 2024)', parent='TOCR-015',
    desc='Word bounding-box annotations for 85 handwritten Telugu pages (from PHDIndic_11) for text detection.',
    hf='https://huggingface.co/datasets/badrivishalk/TEXTRON_INDIC_DATASETS', url='https://huggingface.co/datasets/badrivishalk/TEXTRON_INDIC_DATASETS',
    inst='IIT Bombay LEAP OCR team', authors='Dhruv Kudale, Badri Vishal Kasuba et al.', lang='Multilingual (Devanagari, Kannada, Telugu handwritten)',
    modality='Image (handwritten pages)', task='Text detection', gran='Word boxes on pages', rs='Real', count='85 Telugu pages', unit='page images',
    ann='Yes (boxes only)', ann_type='"text x y w h" word boxes; no transcription', lic='GPL-3.0 (HF tag)', comm='Allowed under GPL', redis='Allowed under GPL',
    access_req='None', access='Open (HF)', ver='VERIFIED', overlap='Pages from PHDIndic_11.', cat='Layout / detection (no transcription)', distinct='N (annotation layer on TOCR-015)'))

R.append(E(
    id='TOCR-017', name='Kaggle mirror: IIT-INDIC-HW-WORDS Dataset (himanshukumarrajak/indic-data)', parent='TOCR-003',
    desc='38.6 GB Kaggle upload of IIIT handwritten word datasets (IIIT-HW-Dev and others, 9 scripts per description).',
    kaggle='https://www.kaggle.com/datasets/himanshukumarrajak/indic-data', url='https://www.kaggle.com/datasets/himanshukumarrajak/indic-data',
    inst='Individual uploader', authors='himanshukumarrajak', lang='Multilingual', modality='Image (offline handwriting)', task='Handwritten word recognition', gran='Word', rs='Real',
    count='38,572.8 MB total; Telugu share NOT VERIFIED', unit='bytes', ann='Yes', ann_type='Word transcription', lic='Unknown (Kaggle)', comm='UNKNOWN', redis='UNKNOWN (upstream terms apply)',
    access_req='Kaggle account to download', access='Open listing (Kaggle API)', ver='PARTIALLY VERIFIED', overlap='Mirror of IIIT datasets (TOCR-001..003).',
    cat='OCR image-text: handwritten', distinct='N (mirror)'))

R.append(E(
    id='TOCR-018', name='GitHub JayanthKalluri/TeluguWordRecognizer - "handwritten_telugu_word_dataset" (Google Drive)',
    desc='Project README points to a Google Drive folder of handwritten Telugu word images used for training.',
    github='https://github.com/JayanthKalluri/TeluguWordRecognizer', url='https://github.com/JayanthKalluri/TeluguWordRecognizer',
    download='https://drive.google.com/drive/folders/1OWdHJhDH-x6n257ck4avON7eIybb5aIR (NOT VERIFIED)', inst='Individual', authors='Jayanth Kalluri',
    modality='Image (handwriting)', task='Handwritten word recognition', gran='Word', rs='Real (assumed)', count='UNKNOWN', unit='word images', ann='NOT VERIFIED', ann_type='NOT VERIFIED',
    lic='None stated', comm='UNKNOWN', redis='UNKNOWN', access_req='Google Drive link', access='Not checked (Drive folder)', ver='UNVERIFIED',
    overlap='Possibly a copy of IIIT-HW-Telugu (not confirmed).', cat='Image-only (transcription NOT VERIFIED)', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-019', name='Roboflow Universe: teluguocr/telugu-handwritten-ocr', desc='Small Roboflow computer-vision project labelled "Telugu handwritten OCR" (3 classes per search snippet).',
    url='https://universe.roboflow.com/teluguocr/telugu-handwritten-ocr', inst='Individual (Roboflow user teluguocr)', authors='UNKNOWN',
    modality='Image (handwriting)', task='Object detection / classification (3 classes)', gran='UNKNOWN', rs='Real (assumed)', count='UNKNOWN', unit='images',
    ann='Yes (class boxes, per snippet)', ann_type='Bounding boxes (3 classes) - NOT VERIFIED', lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN',
    access_req='Roboflow account', access='Page returns HTTP 403 to automated clients', ver='UNVERIFIED', cat='Layout / detection (no transcription)', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-020', name='Roboflow Universe: centurion-university-n60kx/telugu-handwritten', desc='Roboflow object-detection project of Telugu handwriting by a Centurion University account.',
    url='https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten', inst='Centurion University (account)', authors='UNKNOWN',
    modality='Image (handwriting)', task='Object detection', gran='UNKNOWN', rs='Real (assumed)', count='UNKNOWN', unit='images', ann='Yes (boxes) - NOT VERIFIED', ann_type='NOT VERIFIED',
    lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='Roboflow account', access='HTTP 403 to automated clients', ver='UNVERIFIED',
    cat='Layout / detection (no transcription)', distinct='UNKNOWN'))

# ------------------------------------------------------------------ handwritten characters / digits
R.append(E(
    id='TOCR-021', name='HPL Isolated Handwritten Telugu Character Dataset (HP Labs India)', aliases='hpl-telugu-iso-char; LipiTk Telugu',
    version='1.0 (July 2009)', desc='Online (UNIPEN pen trajectories) and offline (bi-level TIFF rendered from the online data) isolated Telugu characters by native writers, with train/test subsets.',
    url='https://lipitk.sourceforge.net/datasets/teluguchardata.htm',
    download='http://mile.ee.iisc.ernet.in/hpl/TelugCharacters/{Online,Offline}/hpl-telugu-iso-char-*.rar',
    paper='Prashanth L. et al., Elastic Matching of Online Handwritten Tamil and Telugu Scripts Using Local Features, ICDAR 2007', inst='HP Labs India (hosted by MILE Lab, IISc)',
    authors='HP Labs India Pen-based Applications group', modality='Online pen trajectories + offline bi-level images', task='Isolated character recognition', gran='Character', rs='Real',
    count='~270 samples x 166 characters (~45K); train ~170/char, test ~60/char', unit='character samples', ann='Yes', ann_type='Character class with Unicode mapping',
    lic='HP Labs dataset licence (LipiTk site)', comm='NOT VERIFIED', redis='NOT VERIFIED', access_req='None', access='Landing page live; download host is an old IISc domain (see link check)',
    ver='PARTIALLY VERIFIED', cat='Character / glyph classification', distinct='Y', catalogue='TEL-OCR-004'))

R.append(E(
    id='TOCR-022', name='Offline Handwritten Telugu Characters (Negi & M Rao, University of Hyderabad)', aliases='UoH offline handwritten Telugu character dataset; IEEE DataPort 10.21227/zhbj-g291 (+8 version DOIs)',
    version='2019 (9 DOIs: zhbj-g291, m269-yp79, wbpn-pb74, ztth-v821, ergx-ha74, j2c4-j091, vnyr-6m82, zw1h-ra81, 9b0k-k581)',
    desc='Scanned sheets of handwritten Telugu characters in boxes: 11 sheet layouts, 937 unique characters, 83 writers, 913 sheets (582 MB zip).',
    url='https://ieee-dataport.org/documents/offline-handwritten-telugu-characters', archive='https://dspace.uohyd.ac.in/handle/1/8547 (HTTP 503 on 2026-11-11)',
    paper='https://doi.org/10.1109/indicon47234.2019.9028977', doi='10.21227/zhbj-g291', inst='University of Hyderabad', authors='Atul Negi, Anish M. Rao',
    modality='Image (scanned handwriting sheets)', task='Character recognition', gran='Character (sheet layouts)', rs='Real', count='913 sheets x ~90 characters (~82,000 characters); 937 classes',
    unit='sheets / character cells', ann='Yes (via sheet layout)', ann_type='Character class per box (layout file)', lic='Creative Commons Attribution (IEEE page)', comm='Allowed with attribution',
    redis='Allowed with attribution', access_req='Free IEEE DataPort account', access='Gated (login)', ver='GATED',
    overlap='Same authors as UoH DSpace record (catalogue TEL-OCR-011); treated as one dataset.', cat='Character / glyph classification', distinct='Y', catalogue='TEL-OCR-011'))

R.append(E(
    id='TOCR-023', name='UHTelHwCC: Telugu off-line handwritten character dataset (University of Hyderabad)', version='2022 (CVIP)',
    desc='Paper describes creation of a Telugu offline handwritten character dataset (line removal, text-line and character extraction, labelling).',
    url='https://doi.org/10.1007/978-3-031-07005-1_22', paper='https://doi.org/10.1007/978-3-031-07005-1_22', doi='10.1007/978-3-031-07005-1_22',
    inst='University of Hyderabad', authors='NOT VERIFIED', modality='Image (handwriting)', task='Character recognition', gran='Character', rs='Real', count='UNKNOWN', unit='character images',
    ann='Yes (per paper)', ann_type='Character class', lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='Contact authors', access='No public download found', ver='UNVERIFIED',
    overlap='May extend TOCR-022 (same institution); not confirmed.', cat='Character / glyph classification', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-024', name='Telugu Handwritten Character Dataset (Velpuru et al.)', aliases='IEEE DataPort 10.21227/mw6a-d662; versions fp04-fq60, 98y6-mh43, xxr4-v037',
    version='2020', desc='Handwritten Telugu characters covering vowels, consonants, othulu and guninthamulu, labelled and mapped to Unicode (335.47 MB).',
    url='https://ieee-dataport.org/open-access/telugu-handwritten-character-dataset', paper='https://doi.org/10.1007/978-981-16-7330-6_74 ; https://doi.org/10.1145/3520439',
    doi='10.21227/mw6a-d662', inst='Academic (authors)', authors='Muni Sekhar Velpuru, Tejasree G, Ravi Kumar M', modality='Image (handwriting)', task='Character recognition',
    gran='Character', rs='Real', count='UNKNOWN sample count (335.47 MB; up to 1,924 character classes described)', unit='character images', ann='Yes', ann_type='Character class -> Unicode label',
    lic='CC BY 4.0 (DataCite)', comm='Allowed with attribution', redis='Allowed with attribution', access_req='IEEE DataPort subscription/login', access='Gated', ver='GATED',
    overlap='Possibly the source of the three identical Kaggle uploads (TOCR-025) - NOT VERIFIED.', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-025', name='Kaggle: "Final Dataset of Telugu Handwritten Characters" (3 identical uploads)',
    aliases='pavankalyand515/data-telugu-handwritten; sarath02003/telugu-handwritten; nithin1729s/telugu-letters',
    desc='Telugu handwritten character images organised as Achulu/Hallulu/Guninthalu folders with Test1 etc.; uploaded three times with identical structure and size.',
    kaggle='https://www.kaggle.com/datasets/pavankalyand515/data-telugu-handwritten ; https://www.kaggle.com/datasets/sarath02003/telugu-handwritten ; https://www.kaggle.com/datasets/nithin1729s/telugu-letters',
    url='https://www.kaggle.com/datasets/sarath02003/telugu-handwritten', inst='Individuals', authors='UNKNOWN (original creator not stated)', modality='Image (handwriting)',
    task='Character recognition', gran='Character', rs='Real', count='353.7 MB each; sample count NOT VERIFIED', unit='character images', ann='Yes (folder labels)', ann_type='Character class (folder)',
    lic='Unknown / Apache-2.0 (sarath02003) / Unknown - original licence not stated', comm='UNKNOWN', redis='UNKNOWN', access_req='Kaggle account', access='Open listing', ver='PARTIALLY VERIFIED',
    overlap='Three uploads are the same files (identical paths & size); origin suspected IEEE TOCR-024 (not verified).', cat='Character / glyph classification', distinct='Y (one dataset; uploads are mirrors)'))

R.append(E(
    id='TOCR-026', name='Telugu Handwritten Vowels (Muppalaneni et al.)', aliases='IEEE DataPort 10.21227/hrkp-ba24 (+5 version DOIs)', version='2019',
    desc='1,116 images of the 16 handwritten Telugu vowels (achchulu) drawn on a paint mobile app by writers aged 8-36; train 875 / test 241.',
    url='https://ieee-dataport.org/documents/telugu-handwritten-vowels', paper='https://doi.org/10.3138/jmbs-27676-sujjuri', doi='10.21227/hrkp-ba24',
    inst='Academic (authors)', authors='Naresh Babu Muppalaneni, Prathima Chilukuri, D. R. Kumar Raja', modality='Image (digital-ink drawn on phone, saved as JPG)', task='Character recognition',
    gran='Character', rs='Real', count='1,116 (train 875 / test 241)', unit='character images', ann='Yes', ann_type='Vowel class', lic='Creative Commons Attribution (DataCite)',
    comm='Allowed with attribution', redis='Allowed with attribution', access_req='IEEE DataPort login', access='Gated', ver='GATED', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-027', name='Handwritten Telugu Gunintam క (Ka)', aliases='IEEE DataPort 10.21227/phg6-m127; 10.21227/c03b-8207', version='2019',
    desc='Handwritten samples of the guninthalu (vowel-sign combinations) of the consonant క.', url='https://doi.org/10.21227/phg6-m127', doi='10.21227/phg6-m127',
    inst='Academic (authors)', authors='Naresh Babu Muppalaneni, Repudi Ramesh', modality='Image (handwriting)', task='Character recognition', gran='Character', rs='Real',
    count='UNKNOWN', unit='character images', ann='Yes', ann_type='Character class', lic='Creative Commons Attribution (DataCite)', comm='Allowed with attribution', redis='Allowed with attribution',
    access_req='IEEE DataPort login', access='Both DOIs redirect (HTTP 302) to the IEEE landing page, which returns 404 (2026-11-11); may still open in a browser', ver='INACCESSIBLE', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-028', name='AsTel - Offline Assamese and Telugu Handwritten Characters', aliases='IEEE DataPort 10.21227/gn0b-de42', version='2024',
    desc='Offline handwritten character images collected with a paint mobile app: vowels, consonants and compound characters; 625 Telugu classes.',
    url='https://ieee-dataport.org/documents/astel-offline-assamese-and-telugu-handwritten-characters', paper='https://doi.org/10.1007/s13369-025-10169-y', doi='10.21227/gn0b-de42',
    inst='Academic (authors)', authors='Prarthana Dutta, Naresh Babu Muppalaneni', lang='Assamese; Telugu', modality='Image (handwriting)', task='Character recognition', gran='Character', rs='Real',
    count='625 Telugu classes (sample count NOT VERIFIED)', unit='character images', ann='Yes', ann_type='Character class', lic='CC BY 4.0 (DataCite)', comm='Allowed with attribution',
    redis='Allowed with attribution', access_req='IEEE DataPort login', access='Gated (page HTTP 403 to scripts)', ver='GATED', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-029', name='Handwritten Telugu Alphabet Dataset: Vowels and Consonants (Varnamala)', aliases='IEEE DataPort 10.21227/qdy8-qb25', version='2026',
    desc='A single 300-dpi JPG grid of handwritten Telugu vowels and consonants; users crop cells themselves.', url='https://ieee-dataport.org/documents/handwritten-telugu-alphabet-dataset-vowels-and-consonants-varnamala-ocr-and-pattern',
    doi='10.21227/qdy8-qb25', inst='Individual', authors='Arjun Ganadi', modality='Image (handwriting, one sheet)', task='Character recognition', gran='Character grid', rs='Real',
    count='1 image (52 characters)', unit='sheet', ann='Implicit (grid order)', ann_type='None beyond layout', lic='CC BY 4.0 (DataCite)', comm='Allowed with attribution', redis='Allowed with attribution',
    access_req='IEEE DataPort login', access='Gated', ver='VERIFIED', quality='Too small for training; illustrative only.', cat='Character / glyph classification', distinct='Y', catalogue='TEL-OCR-012'))

R.append(E(
    id='TOCR-030', name='Sapta Lipi HCR: Handwritten Character Dataset for Seven Indic Scripts', aliases='Mendeley Data r5vjyykm3x', version='v1 (2026-11-06)',
    desc='Handwritten vowels, consonants and numerals for seven Indic scripts including Telugu; 100 samples per class, binarised 28x28.',
    url='https://data.mendeley.com/datasets/r5vjyykm3x/1', doi='10.17632/r5vjyykm3x.1', inst='Academic (Mendeley depositor)', authors='NOT VERIFIED',
    lang='Multilingual (7 scripts incl. Telugu, Kannada, Malayalam, Bengali, Devanagari)', script='Multiple incl. Telugu', modality='Image (handwriting, binarised)', task='Character recognition',
    gran='Character', rs='Real', count='42,600 files total; Telugu share NOT VERIFIED (100 per class)', unit='character images', ann='Yes', ann_type='Class folders', lic='CC BY 4.0',
    comm='Allowed with attribution', redis='Allowed with attribution', access_req='None', access='Open (Mendeley)', ver='VERIFIED', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-031', name='Handwritten Notations of Digits and Fractions in Telugu Script', aliases='Mendeley Data mpjbr7nfv9', version='v1 (2024-08-27)',
    desc='4,000 32x32 images of 8 Telugu fraction symbols (500 per class) from 80 writers, plus raw page scans and unprocessed crops.',
    url='https://data.mendeley.com/datasets/mpjbr7nfv9/1', doi='10.17632/mpjbr7nfv9.1', inst='Academic', authors='Lakshmi Sravani Vempati',
    modality='Image (handwriting)', task='Digit/fraction symbol recognition', gran='Character', rs='Real', count='4,000 (8 classes x 500); 80 writers', unit='symbol images',
    ann='Yes', ann_type='Class folders', lic='CC BY-NC-SA 4.0', comm='Not allowed', redis='Allowed (non-commercial, share-alike)', access_req='None', access='Open (Mendeley)',
    ver='VERIFIED', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-032', name='CMATERdb 3.4.1 - Handwritten Telugu Numerals', aliases='CMATERdb Telugu; TFDS cmaterdb/telugu', version='3.4.1',
    desc='Balanced set of 3,000 handwritten Telugu numerals (300 per digit), 32x32 RGB; TFDS split 2,500 train / 500 test.',
    url='https://www.tensorflow.org/datasets/catalog/cmaterdb', github='https://github.com/prabhuomkar/CMATERdb (mirror)', archive='Original Google Code repository (archived, not live)',
    paper='https://doi.org/10.1016/j.asoc.2011.11.030', doi='10.1016/j.asoc.2011.11.030', inst='CMATER Lab, Jadavpur University', authors='Nibaran Das et al.',
    modality='Image (handwriting)', task='Digit recognition', gran='Character (digit)', rs='Real', count='3,000 (train 2,500 / test 500 in TFDS)', unit='digit images', ann='Yes', ann_type='Digit class',
    lic='NOT STATED by original; GitHub mirror says Apache-2.0', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open via TFDS / mirror', ver='VERIFIED',
    overlap='Source for Telugu digits in MNIST-MIX (TOCR-033) and Kaggle hdr-datasets (TOCR-034); axlevisu repo "numbers" (3,000) likely the same.', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-033', name='MNIST-MIX (Telugu digits subset)', parent='TOCR-032', version='2020', desc='Multi-language handwritten digit benchmark combining 10 scripts; Telugu part taken from CMATERdb.',
    url='https://arxiv.org/abs/2004.03848', paper='https://arxiv.org/abs/2004.03848', doi='10.1088/2633-1357/abad0e', inst='Academic', authors='Weiwei Jiang',
    lang='Multilingual (10 languages incl. Telugu)', modality='Image (handwriting)', task='Digit recognition', gran='Character (digit)', rs='Real', count='3,000 Telugu digits (from CMATERdb)',
    unit='digit images', ann='Yes', ann_type='Digit class', lic='NOT VERIFIED', comm='UNKNOWN', redis='UNKNOWN', access_req='See paper', access='Paper live', ver='PARTIALLY VERIFIED',
    overlap='Derivative of TOCR-032.', cat='Character / glyph classification', distinct='N (derivative)'))

R.append(E(
    id='TOCR-034', name='Kaggle: Multilingual Handwritten Digits Datasets (Telugu-optimized.npz)', parent='TOCR-032', aliases='ayu8sh/hdr-datasets',
    desc='Augmented digit sets for English, Hindi, Telugu, Arabic (10,000 per digit); Telugu from CMATERdb (3K originals).',
    kaggle='https://www.kaggle.com/datasets/ayu8sh/hdr-datasets', url='https://www.kaggle.com/datasets/ayu8sh/hdr-datasets', inst='Individual', authors='ayu8sh',
    lang='Multilingual', modality='Image (handwriting, augmented)', task='Digit recognition', gran='Character (digit)', rs='Real + augmentation', count='100,000 per language after augmentation (80K/20K)',
    unit='digit arrays', ann='Yes', ann_type='Digit class (npz)', lic='Unknown (Kaggle)', comm='UNKNOWN', redis='UNKNOWN', access_req='Kaggle account', access='Open listing', ver='VERIFIED',
    overlap='Augmented derivative of TOCR-032.', cat='Character / glyph classification', distinct='N (derivative)'))

R.append(E(
    id='TOCR-035', name='Kaggle: Telugu Vowel Dataset (6 vowels)', aliases='syamkakarla/telugu-6-vowel-dataset', version='2020-04-23',
    desc='Handwritten samples of six Telugu vowels with a CSV feature version.', kaggle='https://www.kaggle.com/datasets/syamkakarla/telugu-6-vowel-dataset',
    url='https://www.kaggle.com/datasets/syamkakarla/telugu-6-vowel-dataset', github='https://github.com/syamkakarla98/Telugu_Character_Recognition', inst='Individual', authors='Syam Kakarla',
    modality='Image (handwriting)', task='Character recognition', gran='Character', rs='Real', count='8.7 MB; sample count NOT VERIFIED', unit='character images', ann='Yes', ann_type='Class folders + CSV',
    lic='GPL-2.0 (Kaggle)', comm='Allowed under GPL', redis='Allowed under GPL', access_req='Kaggle account', access='Open listing', ver='VERIFIED', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-036', name='Kaggle: Handwritten Telugu Characters (bhaveshkarapu)', desc='Images of handwritten Telugu characters in class folders (trainingdata/<class>/).',
    kaggle='https://www.kaggle.com/datasets/bhaveshkarapu/handwritten-telugu-characters', url='https://www.kaggle.com/datasets/bhaveshkarapu/handwritten-telugu-characters',
    inst='Individual', authors='Bhavesh Karapu', modality='Image (handwriting)', task='Character recognition', gran='Character', rs='Real (assumed)', count='13.0 MB; sample count NOT VERIFIED',
    unit='character images', ann='Yes', ann_type='Class folders', lic='Unknown (Kaggle)', comm='UNKNOWN', redis='UNKNOWN', access_req='Kaggle account', access='Open listing', ver='PARTIALLY VERIFIED',
    cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-037', name='Telugu letters dataset (645 classes; IJRES 2024)', desc='Journal article presents a Telugu character dataset of 645 letters (18 achus, 38 hallus, 35 othulu, 34x16 guninthamulu, 10 digits).',
    url='https://zenodo.org/records/10530992', paper='https://doi.org/10.11591/ijres.v13.i1.pp217-226', doi='10.11591/ijres.v13.i1.pp217-226', inst='Academic',
    authors='Josyula Siva Phaniram, Mukkamalla Babu Reddy', modality='Image (handwriting)', task='Character recognition', gran='Character', rs='Real (per paper)', count='645 classes; sample count UNKNOWN',
    unit='character images', ann='Yes (per paper)', ann_type='Character class', lic='Article CC BY 4.0; data licence UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='Contact authors',
    access='Only the article is deposited (Zenodo); no data files', ver='UNVERIFIED', cat='Character / glyph classification', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-038', name='GitHub axlevisu/CNN-Telugu-OCR data folder', desc='Repository containing 45,217 Telugu character images ("64characters"), 3,000 numeral images and 19,034 Devanagari characters.',
    github='https://github.com/axlevisu/CNN-Telugu-OCR', url='https://github.com/axlevisu/CNN-Telugu-OCR', inst='Individual', authors='axlevisu',
    modality='Image (characters)', task='Character recognition', gran='Character', rs='UNKNOWN (source not documented)', count='45,217 Telugu character images (64 classes) + 3,000 numerals',
    unit='character images', ann='Yes (folders)', ann_type='Class folders', lic='None stated', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED',
    overlap='Numerals likely CMATERdb Telugu (TOCR-032) - same count 3,000.', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-039', name='GitHub srikarym/OCR_Telugu_code - final_dataset.hdf5 (Google Drive)', desc='Telugu character OCR project; README links a Google Drive HDF5 dataset of main characters and vattu/gunintam.',
    github='https://github.com/srikarym/OCR_Telugu_code', url='https://github.com/srikarym/OCR_Telugu_code', download='https://drive.google.com/file/d/1ucYy_Emht9MRLjQPaUydSKZzN1ZQ77dd/view (NOT VERIFIED)',
    inst='Individual / academic project', authors='srikarym', modality='Image (characters)', task='Character recognition', gran='Character', rs='UNKNOWN', count='UNKNOWN', unit='character images',
    ann='Yes (per README)', ann_type='Character class (HDF5)', lic='None stated', comm='UNKNOWN', redis='UNKNOWN', access_req='Google Drive link', access='Drive link returns HTTP 404 (2026-11-11)', ver='INACCESSIBLE',
    cat='Character / glyph classification', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-040', name='GitHub Mitradatta/Telugu-Character-Recognition - self-collected dataset (not released)',
    desc='Project states it collected ~250 handwritten samples per Telugu character from people of different ages; data not in the repository.',
    github='https://github.com/Mitradatta/Telugu-Character-Recognition', url='https://github.com/Mitradatta/Telugu-Character-Recognition', inst='Individual', authors='Mitradatta',
    modality='Image (handwriting)', task='Character recognition', gran='Character', rs='Real', count='~250 per character (claimed)', unit='character images', ann='UNKNOWN', ann_type='UNKNOWN',
    lic='None stated', comm='UNKNOWN', redis='UNKNOWN', access_req='Not released', access='Data not public (repo has README only)', ver='INACCESSIBLE', cat='Character / glyph classification', distinct='UNKNOWN'))
