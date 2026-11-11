"""Directory records, part D: round-2 discovery (2026-11-11).

R       new rows (TOCR-182 onwards), each marked round='Round 2 (2026-11-11)'.
apply() corrections and new facts for round-1 rows; every changed row gets a short 'Round 2 change' note.
Evidence for every fact is in evidence/discovery/ (round2_sweep.json, citations.json, shodhganga.json,
kaggle_details_round2.txt), evidence/hf_subset_counts.json and the URLs given in each record.
"""
from common import E

ROUND = 'Round 2 (2026-11-11)'
R = []


def N(**kw):
    kw.setdefault('round', ROUND)
    kw.setdefault('changed', 'New in round 2')
    R.append(E(**kw))


# ------------------------------------------------------------------ new datasets with Telugu content
N(id='TOCR-182', name='CHIPS - Corpus of Handwritten Indic Scripts (Telugu pages)', aliases='PLATTER dataset (IIT Bombay)', version='2025 (arXiv 2502.06172)',
  desc='Page-level handwritten Indic OCR dataset labelled for word detection and recognition, released with the PLATTER page-level HTR system; 10 languages.',
  url='https://arxiv.org/abs/2502.06172', paper='https://arxiv.org/abs/2502.06172', github='https://github.com/iitb-research-code/doctr (code only)',
  inst='IIT Bombay', authors='Badri Vishal Kasuba, Dhruv Kudale, Venkatapathy Subramanian, Parag Chaudhuri, Ganesh Ramakrishnan',
  lang='Multilingual (10 Indic; Telugu rows in Table 4)', modality='Image (handwritten pages)', task='Page-level handwritten text detection + recognition', gran='Page (word boxes)',
  rs='Pages built from real handwritten word images (IIIT-INDIC-HW-WORDS); page layout composition NOT VERIFIED', count='Telugu 1,951 train / 504 val / 419 test (2,874 pages); 25,290 pages all languages',
  unit='page images', ann='Yes (per paper)', ann_type='Word boxes + word transcriptions', lic='UNKNOWN (paper says data/code released; no data licence found)', comm='UNKNOWN', redis='UNKNOWN',
  access_req='No public link found', access='No dataset link on arXiv, GitHub or HF (checked 2026-11-11)', ver='INACCESSIBLE',
  overlap='Built from IIIT-INDIC-HW-WORDS word images (TOCR-002); PLATTER also uses PHDIndic_11 Telugu pages (TOCR-015).', cat='OCR image-text: handwritten',
  distinct='UNKNOWN (may be a re-composition of TOCR-002 words)')

N(id='TOCR-183', name='PLATTER ScrabbleGAN synthetic Telugu handwritten pages', version='2025', desc='Synthetic handwritten Telugu words generated with ScrabbleGAN (trained on IIIT-INDIC-HW-WORDS) and composed into pages for detector pre-training.',
  url='https://arxiv.org/abs/2502.06172', paper='https://arxiv.org/abs/2502.06172', github='https://github.com/iitb-research-code/ScrabbleGAN (generator code)', inst='IIT Bombay',
  authors='Kasuba et al.', modality='Image (synthetic handwriting pages)', task='Handwritten text detection pre-training', gran='Page / word', rs='Synthetic (GAN)',
  count='500,000 words on 11,879 pages (Table 2)', unit='words / pages', ann='Yes (generated)', ann_type='Word boxes + text', lic='UNKNOWN', access_req='No public link found',
  access='Not released (no link found)', ver='UNVERIFIED', overlap='Generated from TOCR-002.', cat='OCR image-text: synthetic', distinct='UNKNOWN')

N(id='TOCR-184', name='GlotOCR Bench - Telugu (Telu)', version='v1.0 (2026)', desc='OCR benchmark of real multilingual texts rendered as clean and old-document images across 100+ Unicode scripts; Telugu is one script config.',
  hf='https://huggingface.co/datasets/cis-lmu/GlotOCR-bench', github='https://github.com/cisnlp/glotocr-bench', url='https://huggingface.co/datasets/cis-lmu/GlotOCR-bench',
  paper='https://arxiv.org/abs/2604.12978', inst='CIS, LMU Munich', authors='CIS LMU (cisnlp)', lang='Multilingual (100+ scripts; Telu config)', modality='Image (rendered text, clean + degraded)',
  task='OCR evaluation', gran='Text block', rs='Synthetic rendering of real text', count='UNKNOWN rows; Telugu file v1.0/Telu_000.parquet is 39.0 MB', unit='image-text pairs',
  ann='Yes', ann_type='Source text (img_plain + img_old_document)', lic='other ("open-evaluation"): evaluation only, no training or redistribution', comm='UNKNOWN', redis='Not allowed',
  access_req='HF login + tick "evaluation only" box', access='Gated (automatic)', ver='GATED', cat='OCR image-text: synthetic', distinct='Y',
  quality='Evaluation-only licence: cannot be used as training data.')

N(id='TOCR-185', name='BhartiOCR - Telugu', version='2026 (HF, created 2026-09-09)', desc='Controlled synthetic OCR/document corpus: 28.5M image-text pairs, 71 Indian languages, 18 scripts, with a physical-degradation pipeline (paper textures, stamps, folds).',
  hf='https://huggingface.co/datasets/Faizaniqbal/BhartiOCR', url='https://huggingface.co/datasets/Faizaniqbal/BhartiOCR', inst='Individual (Faizaniqbal)', authors='HF user Faizaniqbal (real name NOT VERIFIED)',
  lang='Multilingual (71; telugu config)', modality='Image (synthetic documents)', task='OCR pre-training', gran='Text block / line (per card)', rs='Synthetic',
  count='500,000 Telugu pairs in 100 WebDataset shards (data/telugu/)', unit='image-text pairs', ann='Yes', ann_type='Rendered text', lic='other: software/metadata Apache-2.0; fonts OFL/GPL+FE/Apache; source text multi-licence',
  comm='Depends on source-text licences', redis='Depends on source-text licences', access_req='HF login + manual approval', access='Gated (manual)', ver='GATED', cat='OCR image-text: synthetic', distinct='Y')

N(id='TOCR-186', name='IIIT-H Word Recognition Synthetic Dataset (Telugu)', version='2010', desc='Font-rendered word images of the 1,000 words in the IIIT-H Word Recognition Dataset, in 28 fonts, without degradation.',
  url='https://web.archive.org/web/20221127093102/https://researchweb.iiit.ac.in/~pramod_sankar/CandD.html', download='http://cvit.iiit.ac.in/docsearch/synthetic1000.tar (HTTP 404 on 2026-11-11)',
  paper='DAS 2010: Nearest Neighbor based Collection OCR (Pramod Sankar K., Jawahar, Manmatha)', inst='CVIT, IIIT Hyderabad', authors='Pramod Sankar K., C. V. Jawahar, R. Manmatha',
  modality='Image (rendered words, TIF)', task='Word recognition', gran='Word', rs='Synthetic', count='28,000 word images (1,000 words x 28 fonts; 268 MB)', unit='word images',
  ann='Yes', ann_type='Word label (1,000 classes)', lic='None stated (cite DAS 2010)', access_req='None when live', access='Download 404; page only on the Wayback Machine (researchweb.iiit.ac.in no longer resolves)',
  ver='INACCESSIBLE', overlap='Same 1,000-word vocabulary as TOCR-044.', cat='OCR image-text: synthetic', distinct='Y')

N(id='TOCR-187', name='Multilingual multimodal scene-text dataset (NIT Silchar, ICON 2023) - Telugu', version='2023', desc='Scene images in Assamese, English, Malayalam and Telugu with text boxes labelled by language, built for YOLOv5 language detection.',
  url='https://aclanthology.org/2023.icon-1.16.pdf', paper='https://aclanthology.org/2023.icon-1.16.pdf', inst='NIT Silchar', authors='Nihar Jyoti Basisth, Eisha Halder, Tushar Sachan, Advaitha Vetagiri, Partha Pakray',
  lang='Assamese; English; Malayalam; Telugu', modality='Image (scene / web images; some created with Canva)', task='Text detection with language labels', gran='Text region', rs='Real + designed images',
  count='1,000 Telugu images (4,000 total)', unit='images', ann='Yes', ann_type='Bounding box + language class (no transcription)', lic='UNKNOWN', access_req='Contact authors', access='No release link in paper',
  ver='UNVERIFIED', cat='Script identification', distinct='Y')

N(id='TOCR-188', name='Handwritten Telugu character corpus (JASTT 2025, unreleased)', version='2025', desc='33,496 handwritten Telugu characters collected from schoolchildren and adults; the authors say it will be released separately.',
  url='https://jastt.org/index.php/jasttpath/article/view/267', paper='https://jastt.org/index.php/jasttpath/article/view/267', inst='Sri Vasavi Engg. College; Sreenidhi IST; Vardhaman CE; IIIT Nagpur et al.',
  authors='Mukkoti Vishnu Vardhan, E Jayakiran Reddy, N Srinivas Reddy et al.', modality='Image (handwritten characters)', task='Character recognition', gran='Character', rs='Real',
  count='33,496 characters', unit='character images', ann='Yes (per paper)', ann_type='Character class', lic='UNKNOWN', access_req='Not released', access='Announced for later release',
  ver='INACCESSIBLE', overlap='Experiments in the paper use Kaggle 6-vowel set (TOCR-035), not this corpus.', cat='Character / glyph classification', distinct='Y')

N(id='TOCR-189', name='UniLipi historical manuscript data - Telugu script', version='2026 (arXiv 2608.28195)', desc='Annotated palm-leaf/paper manuscript pages (50-600 pages per script) and ~2.5M synthetic lines per script for 13 Indic scripts incl. Telugu, for a unified multi-script manuscript OCR.',
  url='https://ihdia.iiit.ac.in/unilipi/', paper='https://arxiv.org/abs/2608.28195', github='https://github.com/lekhya-ai/UniLipi (code)', inst='IHDIA / CVIT, IIIT Hyderabad', authors='UniLipi authors (IIIT Hyderabad)',
  lang='Sanskrit and other languages in Telugu script (13 scripts total)', modality='Image (historical manuscripts + synthetic lines)', task='Historical manuscript line OCR', gran='Line',
  rs='Real + synthetic', count='Telugu: UNKNOWN (50-600 real pages per script; ~2.5M synthetic lines per script)', unit='pages / lines', ann='Yes', ann_type='Line transcription (unified WX romanisation)',
  lic='UNKNOWN', access_req='Not released', access='Project page dataset link is a "coming soon" placeholder (2026-11-11)', ver='INACCESSIBLE', cat='OCR image-text: handwritten', distinct='Y')

N(id='TOCR-190', name='NayanaIR-CrossBench (multilingual visual document retrieval)', desc='Cross-lingual visual document retrieval benchmark (part of the M3DR framework); corpus page images, queries and relevance labels in 20 languages incl. Telugu.',
  hf='https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-CrossBench', url='https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-CrossBench', inst='Cognitive Lab', authors='Cognitive Lab',
  lang='Multilingual (20; te tag)', modality='Image (document pages)', task='Visual document retrieval', gran='Page', rs='UNKNOWN (likely rendered/translated)', count='UNKNOWN Telugu share',
  unit='page images', ann='Retrieval qrels', ann_type='Queries + qrels (no transcription)', lic='None declared', access_req='None', access='Open (HF)', ver='PARTIALLY VERIFIED',
  overlap='Same group as Nayana sets (TOCR-097/098/099).', cat='Text-in-image benchmark (VQA / document understanding)', distinct='Y')

N(id='TOCR-191', name='Roboflow Universe: iitbresearchwork/telugu-ocr', desc='Telugu OCR object-detection project (1 class) from an IIT Bombay research workspace that also hosts Tamil/Kannada OCR and "PhDIndic11" projects.',
  url='https://universe.roboflow.com/iitbresearchwork/telugu-ocr', inst='IIT Bombay research workspace (iitbresearchwork)', authors='iitbresearchwork', modality='Image', task='Text detection',
  gran='Word boxes (1 class)', rs='Real (NOT VERIFIED)', count='UNKNOWN', unit='images', ann='Yes (1 class)', ann_type='Boxes, no transcription (per listing)', lic='CC BY 4.0 (listing)', comm='Allowed with attribution',
  redis='Allowed with attribution', access_req='Roboflow account', access='Page blocks scripts (HTTP 403); facts from search snippets', ver='UNVERIFIED',
  overlap='Suspected word-box annotation of PHDIndic_11 Telugu pages (TOCR-015): same workspace has "Malayalam PhDIndic11" and PLATTER used PHDIndic_11 Telugu word boxes; NOT VERIFIED.',
  cat='Layout / detection (no transcription)', distinct='UNKNOWN')

N(id='TOCR-192', name='Roboflow Universe: vihaveai/telugu-info-detector', desc='Telugu text/info detection project; listing mentions related "telugu-words", "kannada-words" and "part-of-mcq" sets.',
  url='https://universe.roboflow.com/vihaveai/telugu-info-detector', inst='Vihave AI', authors='vihaveai', modality='Image', task='Text detection', gran='Region', rs='UNKNOWN', count='UNKNOWN',
  unit='images', ann='Yes (detection)', ann_type='Boxes (classes NOT VERIFIED)', lic='UNKNOWN', access_req='Roboflow account', access='Page blocks scripts (HTTP 403)', ver='UNVERIFIED',
  cat='Layout / detection (no transcription)', distinct='UNKNOWN')

N(id='TOCR-193', name='Roboflow Universe: fives-data-tpoav/telugu', desc='Single-class ("Telugu") detection dataset; no description.',
  url='https://universe.roboflow.com/fives-data-tpoav/telugu', inst='Individual workspace', authors='fives-data-tpoav', modality='Image', task='Telugu text detection', gran='Region', rs='UNKNOWN',
  count='UNKNOWN', unit='images', ann='Yes (1 class)', ann_type='Boxes labelled "Telugu"', lic='UNKNOWN', access_req='Roboflow account', access='Page blocks scripts (HTTP 403)', ver='UNVERIFIED',
  cat='Script identification', distinct='UNKNOWN')

N(id='TOCR-194', name='Roboflow Universe: centurion-university-n60kx/telugu-handwritten-project (+ teugu-words-labelling)', desc='Small Telugu handwritten object-detection projects from the same Centurion University workspace as TOCR-020.',
  url='https://universe.roboflow.com/centurion-university-n60kx/telugu-handwritten-project', inst='Centurion University (workspace)', authors='centurion-university-n60kx',
  modality='Image (handwriting)', task='Handwritten text detection', gran='Word / character boxes (NOT VERIFIED)', rs='Real', count='13 images (telugu-handwritten-project)', unit='images',
  ann='Yes (detection)', ann_type='Boxes', lic='CC BY 4.0 (listing)', comm='Allowed with attribution', redis='Allowed with attribution', access_req='Roboflow account', access='Page blocks scripts (HTTP 403)',
  ver='UNVERIFIED', overlap='Same workspace as TOCR-020; may share images.', cat='Layout / detection (no transcription)', distinct='UNKNOWN')

N(id='TOCR-195', name='Kaggle: telugu_palm_leafs (chintuimmandi) - palm-leaf binarisation pairs', desc='36 Telugu palm-leaf images each paired with a ground-truth binarised image (NN_in.png / NN_gt.png).',
  kaggle='https://www.kaggle.com/datasets/chintuimmandi/telugu-palm-leafs', url='https://www.kaggle.com/datasets/chintuimmandi/telugu-palm-leafs', inst='Individual', authors='chintuimmandi',
  modality='Image (palm-leaf manuscripts)', task='Binarisation', gran='Page', rs='Real', count='36 image / ground-truth pairs (72 PNG files, 230.5 MB)', unit='image pairs', ann='Yes',
  ann_type='Binarised ground-truth image (no text)', lic='Unknown (Kaggle)', comm='UNKNOWN', redis='UNKNOWN', access_req='Kaggle account', access='Open listing', ver='PARTIALLY VERIFIED',
  overlap='Same size and task as the "Preserving Telugu Manuscripts" binarisation set (TOCR-118, 36 images); suspected to be its data release (NOT VERIFIED).',
  cat='Image-only (no transcription)', distinct='N (suspected copy of TOCR-118 data)')

N(id='TOCR-196', name='Kaggle: IITJ Multilingual OCR Dataset (mayank7239)', desc='Word crops in per-language folders, file names carry quadrilateral coordinates; listing shows Assamese and other folders.',
  kaggle='https://www.kaggle.com/datasets/mayank7239/iitj-multilingual-ocr-dataset', url='https://www.kaggle.com/datasets/mayank7239/iitj-multilingual-ocr-dataset', inst='Individual (title cites IIT Jodhpur)',
  authors='mayank7239', lang='Multilingual (Telugu folder NOT VERIFIED)', script='Multiple (Telugu NOT VERIFIED)', modality='Image (scene word crops)', task='Scene text recognition', gran='Word',
  rs='Real', count='441.8 MB; file listing capped at 400 files', unit='word crops', ann='UNKNOWN', ann_type='Labels not seen in listing', lic='CC0-1.0 (Kaggle tag)', comm='Tag says allowed; upstream terms apply',
  redis='Upstream terms apply', access_req='Kaggle account', access='Open listing', ver='PARTIALLY VERIFIED', overlap='Suspected re-upload of Bharat Scene Text crops (TOCR-082, IIT Jodhpur).',
  cat='Image-only (transcription NOT VERIFIED)', distinct='N (suspected copy of TOCR-082)')

N(id='TOCR-197', name='HuggingFaceFW/finepdfs - Telugu (tel_Telu)', desc='Text extracted from public PDFs (born-digital extraction or OCR) for LM pre-training; no page images.',
  hf='https://huggingface.co/datasets/HuggingFaceFW/finepdfs', url='https://huggingface.co/datasets/HuggingFaceFW/finepdfs', inst='Hugging Face', authors='HuggingFaceFW',
  lang='Multilingual (1,700+; tel_Telu config)', modality='Text only', task='Language modelling for OCR (not OCR data)', gran='Document text', rs='Real text (part machine-OCR)', count='UNKNOWN (Telugu share not computed)',
  unit='documents', ann='Not applicable', ann_type='None (no images)', lic='ODC-By 1.0', comm='Allowed (source terms apply)', redis='Allowed with attribution', access_req='None', access='Open (HF)',
  ver='PARTIALLY VERIFIED', cat='Text-only corpus (OCR language modelling)', distinct='Y', quality='Some text is itself OCR output; useful as PDF-domain language model text only.')

N(id='TOCR-208', name='ULCA (Bhashini) OCR corpus - Telugu (Project Anuvaad)', desc='Telugu OCR corpora contributed to the national ULCA/Bhashini repository by Project Anuvaad (EkStep/Tarento): education domain and government press releases; collection method "web-scraping-ocr".',
  url='https://bhashini.gov.in/ulca/datasets', archive='https://meity-auth.ulcacontrib.org/ulca/data-metric/v0/store/reportdata (public metrics endpoint; POST only, so a browser GET returns 405)', inst='Project Anuvaad (EkStep Foundation / Tarento) via ULCA, MeitY',
  authors='Project Anuvaad', modality='Image (document pages / crops) + OCR text', task='Printed OCR', gran='UNKNOWN', rs='Real (web-scraped documents)', count='224,614 (education) + 1,243 (government press releases)',
  unit='records (unit as reported by ULCA metrics; NOT VERIFIED)', ann='Yes', ann_type='Text from OCR ("web-scraping-ocr"); human correction NOT VERIFIED', lic='UNKNOWN (ULCA requires permissive licences for contributions)',
  access_req='ULCA account + dataset search request', access='Listed in ULCA public metrics (2026-11-11); download not attempted', ver='PARTIALLY VERIFIED',
  overlap='Same group as the EkStep synthetic benchmark (TOCR-102); overlap NOT VERIFIED.', cat='Machine-labelled OCR (not human ground truth)', distinct='Y',
  notes='Evidence: evidence/discovery/ulca_reportdata.json. ULCA lists 28 OCR corpora across 12 languages; only these two are Telugu.')

N(id='TOCR-209', name='British Library AAS card catalogues: Telugu (digitised microfilm)', version='2017', desc='Digitised microfilm images of the British Library Asian and African Studies Telugu card catalogue.',
  url='https://bl.iro.bl.uk/work/0249413b-6469-4c28-bb03-c4b3f9dd7403', doi='10.21250/aascc24', inst='British Library', authors='British Library', lang='Telugu; English',
  modality='Image (catalogue card scans)', task='Unlabelled scans (catalogue cards)', gran='Card / page', rs='Real', count='UNKNOWN', unit='card images', ann='No (text not verified)', ann_type='None verified',
  lic='UNKNOWN (no rights field in DataCite)', access_req='None (BL research repository)', access='DataCite record live; files not opened', ver='PARTIALLY VERIFIED', cat='Scanned archive (image-only)', distinct='Y')

# ------------------------------------------------------------------ new rejected candidates
for rid, name, url, reason in [
    ('TOCR-198', 'SignboardText (IEEE DataPort 10.21227/5k09-4k21)', 'https://ieee-dataport.org/documents/signboardtext-0', 'Vietnamese/English signboards (UIT, VNU-HCM); surfaced in Telugu scene-text searches but has no Telugu.'),
    ('TOCR-199', 'CATALIST / CATALISTd video scene text (IIT Bombay, on AIKosh)', 'https://catalist-2021.github.io', 'English, Hindi and Marathi only.'),
    ('TOCR-200', 'DohaScript handwritten Hindi (arXiv 2602.18089)', 'https://arxiv.org/abs/2602.18089', 'Hindi only.'),
    ('TOCR-201', 'IIEST-Indic-HW writer identification dataset', 'https://doi.org/10.1145/3774521.3774586', 'Bengali and Hindi only.'),
    ('TOCR-202', 'EpiSAM / Shilalekhya stone-inscription datasets (IHDIA)', 'https://ihdia.iiit.ac.in/episam/', 'Single Indic script not named; no Telugu evidence on project pages or HF card.'),
    ('TOCR-203', 'arikatokachi/indic-synthetic-documents (+v2)', 'https://huggingface.co/datasets/arikatokachi/indic-synthetic-documents', 'Languages en, bn, hi, ta only (folders and tags).'),
    ('TOCR-204', 'Nexdata 500,000 Images Multilingual OCR Dataset in 21 Languages', 'https://huggingface.co/datasets/Nexdata-kr/500000-Images-Multilingual-OCR-Dataset-in-21-Languages', 'Commercial sample; listed languages do not include Telugu.'),
    ('TOCR-205', 'DataCluster Labs Multilingual OCR Annotation Dataset (Kaggle + HF)', 'https://huggingface.co/datasets/Dataclusterlabspvtltd/Multilingual_OCR_Annotation_Dataset', 'Vendor sample with he/th/ja/ar; no Telugu files.'),
    ('TOCR-206', 'A Benchmark and Dataset for Post-OCR Text Correction in Sanskrit (AIKosh)', 'https://aikosh.indiaai.gov.in/home/datasets/details/a_benchmark_and_dataset_for_post_ocr_text_correction_in_sanskrit.html', 'Sanskrit text only (Devanagari); no Telugu.'),
    ('TOCR-207', 'Indic-VizVQA-v2 (Kaggle armaansingh2340)', 'https://www.kaggle.com/datasets/armaansingh2340/indic-vizvqa-v2', 'Translated VizWiz/VQAv2 questions; images are not text-centric.'),
]:
    N(id=rid, name=name, url=url, desc='Rejected candidate - see notes.', inst='See source', modality='See notes', task='See notes', gran='Not applicable', rs='Not applicable',
      count='Not applicable', unit='Not applicable', ann='Not applicable', ann_type='Not applicable', access='See notes', ver='REJECTED', cat='Rejected', distinct='N', notes=reason,
      changed='New in round 2 (rejected)')


# ------------------------------------------------------------------ corrections to round-1 rows
def _set(rec, change, **kw):
    rec.update(kw)
    rec['changed'] = change if rec['changed'] == 'NONE' else rec['changed'] + '; ' + change


def apply(rows):
    by = {r['id']: r for r in rows}
    _set(by['TOCR-015'], 'Telugu share found in PLATTER paper', count='1,458 pages total; Telugu 85 pages with 5,503 word boxes (PLATTER, arXiv 2502.06172, Table 3)')
    _set(by['TOCR-019'], 'Size from search snippet', count='386 images (workspace listing)', ann='Yes (object detection, 3 classes per earlier snippet)', ann_type='Boxes (classes NOT VERIFIED)')
    _set(by['TOCR-044'], 'Resolved via archived IIIT page',
         name='IIIT-H Word Recognition Dataset (Telugu)', aliases='IIIT Telugu book collection (Pramod Sankar, Jawahar, Manmatha 2010); thatz1000',
         desc='Printed Telugu word images of 1,000 distinct words sampled from 33 Digital Library of India books; labels hand-corrected (>99% accurate).',
         url='https://web.archive.org/web/20221127093102/https://researchweb.iiit.ac.in/~pramod_sankar/CandD.html', download='http://cvit.iiit.ac.in/docsearch/thatz1000.tar (HTTP 404 on 2026-11-11)',
         count='32,773 word images (5-530 per word; 52 MB TIF)', unit='word images', ann='Yes', ann_type='Word label (1,000 classes)', lic='None stated (cite DAS 2010)',
         access_req='None when live', access='Download 404; page only on the Wayback Machine', ver='INACCESSIBLE', distinct='Y', cat='OCR image-text: printed', rs='Real', gran='Word',
         modality='Image (printed words, TIF)', task='Word recognition')
    _set(by['TOCR-098'], 'Telugu repos listed from HF API',
         count='Telugu repos: Nayana-DocOCR-te-14k-v2-arxiv, Nayana-DocQA-te-10k-v1-docmatix, Nayana-DocOCR-ml-mr-ta-te-or-pa-15k-v1-pubmed, Nayana-DocOCR-mr-ta-te-or-pa-15k-v1-docmatix (+ multi-Indic in-14k and Indic-1m repos)',
         distinct='Y (gated family, counted once)')
    _set(by['TOCR-102'], 'Paper details added', paper='https://arxiv.org/abs/2205.02543',
         count='90K images, 23 languages; Telugu table row 419 / 1,888 / 1,519 synthetic (column units not given) plus a real subset',
         notes='Paper calls it publicly available but gives no download link (arXiv HTML and GitHub searched 2026-11-11). Scene-text lines in 8 languages incl. Telugu were labelled with Google Vision OCR (machine labels).')
    _set(by['TOCR-107'], 'Size confirmed from arXiv 1711.07245', paper='https://arxiv.org/abs/1711.07245')
    _set(by['TOCR-114'], 'File listing checked', notes='Kaggle file-list API returned only the first ~1,200 files (Brahmi, Assamese, Devanagari test folders); Telugu folder size still NOT VERIFIED.')
    _set(by['TOCR-118'], 'Possible data release found', overlap='Kaggle telugu_palm_leafs (TOCR-195) has 36 image/ground-truth pairs and is suspected to be this dataset.')
    _set(by['TOCR-128'], 'Release re-checked', access='No dataset link in paper; no HF repo found (searched 2026-11-11)')
    _set(by['TOCR-130'], 'Telugu share counted via HF API', count='~5K images total; Telugu: 89 OCR pages (Wikisource), 69 VQA-Indic, 106 parallel VQA',
         overlap='Copies: AtharvImmverse/IndicVisionBench; lalit-03/IndicVisionBench (gated). OCR track Telugu pages likely the same 89 Wikisource pages as ORB-Indic (TOCR-172); both derive from TOCR-049.')
    _set(by['TOCR-131'], 'Telugu share counted via HF API', count='8,960 rows; 384 with Telugu images (image_language=te)')
    _set(by['TOCR-132'], 'Telugu share counted via HF API', count='8,801 QA items; 135 on Telugu pages (page_language); no Telugu questions (qa_language)')
    _set(by['TOCR-134'], 'Telugu rows found (earlier note was wrong)', count='6,117 boards; Telugu 1,020 (709 train / 104 val / 207 test)', lang='Multilingual (6; Telugu confirmed)')
    _set(by['TOCR-084'], 'Telugu check', notes='HF filter on language column found no Telugu label; first rows are Hindi. Telugu share still NOT VERIFIED.')
    _set(by['TOCR-148'], 'Kaggle font upload noted', notes='Also uploaded as Kaggle viralbarodia/gujarati-and-telugu-fonts (Noto Sans Telugu, MIT tag).')
    _set(by['TOCR-016'], 'AIKosh mirror noted', aliases='TEXTRON (WACV 2024); AIKosh textron_dataset listing')
    _set(by['TOCR-180'], 'Files checked', notes='596 TFRecord shards with no language names in file paths; Telugu presence still NOT VERIFIED.')
    _set(by['TOCR-181'], 'Files checked', notes='144 images + ground_truth.csv; file names carry no language; Telugu presence still NOT VERIFIED.')
    # ORB-Indic: round-1 rejection was wrong (paper Table 1 lists 89 Telugu pages with ground truth)
    r = by['TOCR-172']
    keep = {k: r[k] for k in ('id', 'verified', 'round')}
    r.clear()
    r.update(E(id='TOCR-172', name='ORB-Indic (krutrim-ai-labs/ocr_rotation_bench) - Telugu pages', aliases='Seeing Straight / ORB rotation benchmark',
               desc='Rotation-robust OCR benchmark: Wikisource page images in 11 Indic languages with human-edited transcriptions, presented at 4 and 8 rotation classes.',
               hf='https://huggingface.co/datasets/krutrim-ai-labs/ocr_rotation_bench', url='https://huggingface.co/datasets/krutrim-ai-labs/ocr_rotation_bench', paper='https://arxiv.org/abs/2511.04161',
               inst='Krutrim AI Labs', authors='Suranjan Goswami, Abhinav Ravi, Raja Kolla, Ali Faraz, Shaharukh Khan, Akash, Chandra Khatri, Shubham Agarwal', lang='Multilingual (11 Indic; Telugu 89)',
               modality='Image (rotated printed pages)', task='Orientation detection + OCR evaluation', gran='Page', rs='Real pages (rotated)', count='966 pages total; Telugu 89 (paper Table 1)',
               unit='page images', ann='Yes', ann_type='Rotation label + page transcription (Wikisource pagetext)', lic='Krutrim Community License 1.0', comm='Per Krutrim licence (NOT VERIFIED)',
               redis='Per Krutrim licence (NOT VERIFIED)', access_req='None', access='Open (HF; Indic files 226 MB + 509 MB)', ver='PARTIALLY VERIFIED',
               overlap='Derived from Telugu Wikisource (TOCR-049); suspected same 89 Telugu pages as IndicVisionBench OCR (TOCR-130).', cat='OCR image-text: printed',
               distinct='N (suspected same pages as TOCR-130; derived from TOCR-049)', notes='Round 1 rejected this row after sampling English rows; the paper confirms Telugu.'))
    r.update(keep)
    r['changed'] = 'Un-rejected: Telugu confirmed in paper'
