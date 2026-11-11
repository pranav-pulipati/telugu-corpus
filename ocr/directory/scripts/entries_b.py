"""Directory records, part B: printed (real), scene text, synthetic."""
from common import E

R = []

# ------------------------------------------------------------------ printed, real
R.append(E(
    id='TOCR-041', name='Mozhi-Telugu (printed word images)', aliases='Mozhi; akshara printed dataset; ILOCR dataset 14',
    version='v0.5 (ILOCR); paper 2024/2025 (ICPR)', desc='Word crops from scanned printed Telugu books with human-verified transcriptions; official train/val/test.',
    url='https://cvit.iiit.ac.in/usodi/tdocrmil.php', download='https://ilocr.iiit.ac.in/public/printed/phase-0/v0.5/telugu/akshara/{train,val,test}.zip',
    hf='https://huggingface.co/datasets/darknight054/indic-mozhi-ocr (mirror, TOCR-042)', archive='https://ilocr.iiit.ac.in/dataset/14/ (page returns server error)',
    paper='https://arxiv.org/abs/2205.06740', doi='10.48550/arXiv.2205.06740', inst='CVIT, IIIT Hyderabad', authors='Minesh Mathew, Ajoy Mondal, C. V. Jawahar',
    modality='Image (printed, scanned books)', task='Printed word recognition', gran='Word', rs='Real', count='100,024 (80,337 / 9,811 / 9,876); 28 books',
    unit='word images', ann='Yes', ann_type='Word transcription', lic='CC BY 4.0 (stated on all other-language Mozhi pages; Telugu page broken)', comm='Allowed with attribution (inferred)',
    redis='Allowed with attribution (inferred)', access_req='None', access='Open download (zips HTTP 200; dataset page HTTP 500)', ver='VERIFIED',
    overlap='Official splits leak: all 28 books and 1,362/1,387 test pages also in train (phase-2 check).', quality='Audit 15/16 correct; 940 punctuation-only crops.',
    cat='OCR image-text: printed', distinct='Y', catalogue='TEL-OCR-001'))

R.append(E(
    id='TOCR-042', name='HF mirror: darknight054/indic-mozhi-ocr (telugu config)', parent='TOCR-041', desc='Parquet re-upload of Mozhi with UUID ids (file names dropped).',
    hf='https://huggingface.co/datasets/darknight054/indic-mozhi-ocr', url='https://huggingface.co/datasets/darknight054/indic-mozhi-ocr', inst='Individual uploader', authors='darknight054',
    lang='Multilingual (13 languages; telugu config)', modality='Image (printed)', task='Printed word recognition', gran='Word', rs='Real', count='100,024 Telugu rows', unit='word images',
    ann='Yes', ann_type='Word transcription', lic='None declared (refers to source)', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='VERIFIED',
    overlap='Test split byte-identical to official (9,876/9,876 images and labels).', cat='OCR image-text: printed', distinct='N (mirror)'))

R.append(E(
    id='TOCR-043', name='Multilingual OCR for Indic Scripts - printed page corpus (Mathew, Singh, Jawahar 2016)', version='2016 (DAS)',
    desc='IIIT printed-page corpus used for multilingual Indic OCR (12 Indian languages + English) in DAS 2016; precursor work to Mozhi.',
    url='https://doi.org/10.1109/DAS.2016.68', paper='https://doi.org/10.1109/DAS.2016.68', doi='10.1109/DAS.2016.68', inst='CVIT, IIIT Hyderabad',
    authors='Minesh Mathew, Ajeet Kumar Singh, C. V. Jawahar', lang='Multilingual (12 Indian + English)', modality='Image (printed pages)', task='Printed text recognition; script ID',
    gran='Word / line', rs='Real', count='UNKNOWN', unit='UNKNOWN', ann='Yes (per paper)', ann_type='NOT VERIFIED', lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN',
    access_req='UNKNOWN', access='No public release found', ver='UNVERIFIED', overlap='Possibly superseded by Mozhi (TOCR-041).', cat='OCR image-text: printed', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-044', name='IIIT Telugu book collection (Pramod Sankar, Jawahar, Manmatha 2010)', version='2010 (DAS)',
    desc='33-book Telugu document-image collection used for collection-level OCR / word annotation research at IIIT Hyderabad.',
    url='NOT FOUND', paper='NOT VERIFIED (DAS 2010; "Nearest neighbor based collection OCR")', inst='CVIT, IIIT Hyderabad; UMass', authors='K. Pramod Sankar, C. V. Jawahar, R. Manmatha',
    modality='Image (printed books)', task='Collection OCR; word annotation', gran='Word / page', rs='Real', count='33 books', unit='books', ann='Partial (per paper)', ann_type='NOT VERIFIED',
    lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='UNKNOWN', access='No public release found', ver='UNVERIFIED', cat='OCR image-text: printed', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-045', name='Building Data Sets for Indian Language OCR Research (annotated corpus, 2009)', version='2009',
    desc='Book chapter describing large annotated document-image corpora built for Indian-language OCR (consortium effort; Telugu among target languages).',
    url='https://doi.org/10.1007/978-1-84800-330-9_1', paper='https://doi.org/10.1007/978-1-84800-330-9_1', doi='10.1007/978-1-84800-330-9_1', inst='IIIT Hyderabad and OCR consortium',
    authors='C. V. Jawahar et al.', lang='Multilingual (Indian languages)', modality='Image (printed)', task='Printed OCR ground truth', gran='Page / word', rs='Real', count='UNKNOWN', unit='UNKNOWN',
    ann='Yes (per chapter)', ann_type='NOT VERIFIED', lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='UNKNOWN', access='No public release found', ver='UNVERIFIED',
    overlap='Possibly related to the TDIL OCR image corpus (TOCR-046).', cat='OCR image-text: printed', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-046', name='Telugu Image Corpus - OCR (TDIL / C-DAC Noida OCR Consortium)', aliases='TDIL toolid 264',
    desc='500 greyscale 300-dpi TIFF scans of Telugu text, by-products of the national OCR project; listed as research-only.',
    url='https://tdil-dc.in/index.php?lang=en&option=com_download&task=showresourceDetails&toolid=264', inst='C-DAC Noida OCR Consortium / TDIL, MeitY', authors='OCR Consortium',
    modality='Image (scanned printed pages)', task='Printed OCR (images)', gran='Page', rs='Real', count='500 (search-snippet description)', unit='page images', ann='NOT VERIFIED',
    ann_type='NOT VERIFIED (described as images)', lic='Research only (search snippet)', comm='Not allowed (reported)', redis='UNKNOWN', access_req='TDIL registration (reported)',
    access='Site TLS certificate expired (2026-11-11); page not readable', ver='INACCESSIBLE', cat='Image-only (transcription NOT VERIFIED)', distinct='Y'))

R.append(E(
    id='TOCR-047', name='UHTelPCC: Telugu Printed Character Dataset (University of Hyderabad)', version='2019',
    desc='Printed Telugu character images extracted from books printed 1950-1990, with train/test split and KNN/MLP/CNN baselines (99.68% CNN).',
    url='http://scis.uohyd.ac.in/~chakcs/UHTelPCC.html (HTTP 404)', archive='https://dspace.uohyd.ac.in/handle/1/8703 (HTTP 503 on 2026-11-11)',
    paper='https://doi.org/10.1007/978-981-13-9187-3_3', doi='10.1007/978-981-13-9187-3_3', inst='University of Hyderabad (SCIS)', authors='Rakesh Kummari, Chakravarthy Bhagvati',
    modality='Image (printed characters)', task='Printed character recognition', gran='Character', rs='Real', count='UNKNOWN', unit='character images', ann='Yes', ann_type='Character class',
    lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='Contact authors', access='Project page 404; repository 503', ver='INACCESSIBLE', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-048', name='UHIndicPCwS: University of Hyderabad Indic Printed Character with Style', desc='Printed character images for six scripts (Tamil, Telugu, Kannada, Malayalam, Gujarati, Odia) in one Python pickle with class labels.',
    url='https://scis.uohyd.ac.in/~chakcs/datasets/UHIndicPCwS.html', download='https://scis.uohyd.ac.in/~chakcs/datasets/UHIndicPCwS.pkl (572 MB)', inst='University of Hyderabad (SCIS)',
    authors='NOT VERIFIED (Bhagvati group)', lang='Multilingual (6 scripts incl. Telugu)', modality='Image arrays (printed characters)', task='Printed character recognition', gran='Character', rs='Real (assumed)',
    count='UNKNOWN (Telugu share not stated)', unit='character images', ann='Yes', ann_type='Class labels (scriptname_classnumber)', lic='NOT STATED', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None', access='Open download (HTTP 200)', ver='PARTIALLY VERIFIED', quality='Python pickle - must not be loaded with pickle.load from untrusted source; inspect safely.',
    cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-049', name='Telugu Wikisource - proofread and validated page scans', aliases='te.wikisource Page: namespace (quality levels 3-4)',
    desc='Scanned book pages with human-proofread (level 3) or validated (level 4) Telugu transcriptions; the source of most open Telugu page/line OCR sets.',
    url='https://te.wikisource.org/', download='https://dumps.wikimedia.org/tewikisource/ (text + quality levels); page images via Commons file pages',
    inst='Wikimedia / Telugu Wikisource community', authors='Volunteers', modality='Image (scanned printed books) + text', task='Page-level OCR ground truth', gran='Page', rs='Real',
    count='134,015 proofread/validated pages (79,532 L3 + 54,483 L4) in 2026-11-01 dump; 127,326 on free-licence scans', unit='pages', ann='Yes', ann_type='Page transcription (wiki markup; layout not preserved)',
    lic='Text CC BY-SA 4.0; scans per file (1,146 of 1,231 free)', comm='Allowed (share-alike) for free scans', redis='Allowed (share-alike)', access_req='None (API/dumps; bulk image fetch needs a policy-compliant User-Agent)',
    access='Open', ver='VERIFIED', overlap='Parent of TOCR-050, 051, 052 and harsha line sets; count pages once.', quality='Columns merged, page numbers dropped; needs line alignment for line OCR.',
    cat='OCR image-text: printed', distinct='Y', catalogue='TEL-LIT-001'))

R.append(E(
    id='TOCR-050', name='AlbertoChestnut/telugu-ocr', parent='TOCR-049', desc='Wikisource page scans with page transcriptions organised by book.',
    hf='https://huggingface.co/datasets/AlbertoChestnut/telugu-ocr', url='https://huggingface.co/datasets/AlbertoChestnut/telugu-ocr', inst='Individual', authors='AlbertoChestnut',
    modality='Image (scanned printed pages)', task='Page OCR', gran='Page', rs='Real', count='23,537 page pairs in 219 book folders (README: ~25,565 / 221)', unit='page image-text pairs',
    ann='Yes', ann_type='Page transcription', lic='CC BY-SA 4.0', comm='Allowed (share-alike)', redis='Allowed (share-alike)', access_req='None', access='Open (HF)', ver='VERIFIED',
    overlap='Subset of TOCR-049.', quality='Catalogue figure 458,964 counts text lines, not pairs.', cat='OCR image-text: printed', distinct='N (derivative of TOCR-049)', catalogue='TEL-OCR-005'))

R.append(E(
    id='TOCR-051', name='harsha-desaraju/telugu-wikisource-text-images', parent='TOCR-049', desc='Line crops cut from Wikisource proofread pages and aligned to the page text, with CER-based acceptance flags.',
    hf='https://huggingface.co/datasets/harsha-desaraju/telugu-wikisource-text-images', url='https://huggingface.co/datasets/harsha-desaraju/telugu-wikisource-text-images',
    github='https://github.com/harsha-desaraju/TeluguOCR', inst='Individual', authors='Harsha Desaraju', modality='Image (printed lines)', task='Line recognition', gran='Line', rs='Real',
    count='659,924 rows (accepted subset smaller; flag column)', unit='line crops', ann='Yes', ann_type='Line text (automatic alignment; accepted/reject flags)', lic='CC BY-SA 4.0', comm='Allowed (share-alike)',
    redis='Allowed (share-alike)', access_req='None', access='Open (HF)', ver='VERIFIED', overlap='Derived from TOCR-049.', quality='Labels from automatic alignment, not per-line human review.',
    cat='OCR image-text: printed', distinct='N (derivative of TOCR-049)', catalogue='TEL-OCR-007'))

R.append(E(
    id='TOCR-052', name='harsha-desaraju/telugu-line-ocr-bench', parent='TOCR-049', desc='1,044 Wikisource line crops with human-verified transcriptions for evaluation.',
    hf='https://huggingface.co/datasets/harsha-desaraju/telugu-line-ocr-bench', url='https://huggingface.co/datasets/harsha-desaraju/telugu-line-ocr-bench', inst='Individual', authors='Harsha Desaraju',
    modality='Image (printed lines)', task='Line recognition (benchmark)', gran='Line', rs='Real', count='1,044', unit='line crops', ann='Yes', ann_type='Human-verified line text', lic='CC BY-SA 4.0',
    comm='Allowed (share-alike)', redis='Allowed (share-alike)', access_req='None', access='Open (HF)', ver='VERIFIED', overlap='Derived from TOCR-049.', cat='OCR image-text: printed', distinct='Y (new human verification)', catalogue='TEL-OCR-007'))

R.append(E(
    id='TOCR-053', name='harsha-desaraju/telugu-line-text-image', desc='Line images from Telugu PDFs with text (e.g. Panchatantram), file and page provenance.',
    hf='https://huggingface.co/datasets/harsha-desaraju/telugu-line-text-image', url='https://huggingface.co/datasets/harsha-desaraju/telugu-line-text-image', inst='Individual', authors='Harsha Desaraju',
    modality='Image (printed lines from PDFs)', task='Line recognition', gran='Line', rs='Real (PDF render or scan - NOT VERIFIED)', count='101,046', unit='line crops', ann='Yes', ann_type='Line text (origin of text NOT VERIFIED)',
    lic='MIT tag (source books not licensed by uploader)', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='PARTIALLY VERIFIED', cat='OCR image-text: printed', distinct='Y'))

R.append(E(
    id='TOCR-054', name='harsha-desaraju/Telugu-book-text-images', desc='Page images from Telugu book PDFs (file name + page number), no transcription.',
    hf='https://huggingface.co/datasets/harsha-desaraju/Telugu-book-text-images', url='https://huggingface.co/datasets/harsha-desaraju/Telugu-book-text-images', inst='Individual', authors='Harsha Desaraju',
    modality='Image (book pages)', task='Unlabelled page images', gran='Page', rs='Real', count='232,500 (207,500 / 12,500 / 12,500)', unit='page images', ann='No', ann_type='Provenance only',
    lic='MIT tag (source books modern; rights unclear)', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='VERIFIED', cat='Image-only (no transcription)', distinct='Y', catalogue='TEL-OCR-007'))

R.append(E(
    id='TOCR-055', name='harsha-desaraju/telugu-book-line-images (+ -sample)', parent='TOCR-054', desc='2.44M unlabelled line crops cut from the book page set (5,000-row sample repo also published).',
    hf='https://huggingface.co/datasets/harsha-desaraju/telugu-book-line-images ; https://huggingface.co/datasets/harsha-desaraju/telugu-book-line-images-sample',
    url='https://huggingface.co/datasets/harsha-desaraju/telugu-book-line-images', inst='Individual', authors='Harsha Desaraju', modality='Image (printed lines)', task='Unlabelled line crops', gran='Line',
    rs='Real', count='2,442,885 (+5,000 sample)', unit='line crops', ann='No', ann_type='None', lic='MIT tag (rights of books unclear)', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)',
    ver='VERIFIED', overlap='Same crops as TOCR-056/057.', cat='Image-only (no transcription)', distinct='N (derivative of TOCR-054)'))

R.append(E(
    id='TOCR-056', name='harsha-desaraju/consensus-labelling', parent='TOCR-055', desc='The 2.44M book line crops read by three OCR engines with an agreement tier and consensus text.',
    hf='https://huggingface.co/datasets/harsha-desaraju/consensus-labelling', url='https://huggingface.co/datasets/harsha-desaraju/consensus-labelling', inst='Individual', authors='Harsha Desaraju',
    modality='Image (printed lines)', task='Line recognition (silver labels)', gran='Line', rs='Real images, machine labels', count='2,442,885', unit='line crops', ann='Machine-generated',
    ann_type='3-engine OCR consensus (tier 1 = all agree ~1.8% in sampled shards)', lic='other', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='VERIFIED',
    cat='Machine-labelled OCR (not human ground truth)', distinct='N (labels on TOCR-055)'))

R.append(E(
    id='TOCR-057', name='harsha-desaraju/telugu-pdf-line-image-text', parent='TOCR-056', desc='Tier 1-4 subset of the consensus-labelled book lines.',
    hf='https://huggingface.co/datasets/harsha-desaraju/telugu-pdf-line-image-text', url='https://huggingface.co/datasets/harsha-desaraju/telugu-pdf-line-image-text', inst='Individual', authors='Harsha Desaraju',
    modality='Image (printed lines)', task='Line recognition (silver labels)', gran='Line', rs='Real images, machine labels', count='233,530 (230,000 / 3,530)', unit='line crops', ann='Machine-generated',
    ann_type='OCR consensus text + tier', lic='MIT tag', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='VERIFIED', cat='Machine-labelled OCR (not human ground truth)', distinct='N (filter of TOCR-056)'))

R.append(E(
    id='TOCR-058', name='Divs0910/telugu-ocr-dataset (Chandamama paragraph crops)', aliases='DIVYANSH-TEJA-09 Telugu OCR dataset pipeline', parent='TOCR-129',
    desc='Paragraph crops from scanned Chandamama magazines aligned automatically to text (match_score); built by a GitHub pipeline with ground-truth JSON per issue.',
    hf='https://huggingface.co/datasets/Divs0910/telugu-ocr-dataset', github='https://github.com/DIVYANSH-TEJA-09/telugu-ocr-dataset', url='https://huggingface.co/datasets/Divs0910/telugu-ocr-dataset',
    inst='Individual', authors='Divyansh Teja (inferred from handles)', modality='Image (scanned printed magazine)', task='Paragraph recognition', gran='Paragraph', rs='Real', count='120,321 (pipeline README: ~70,000 paragraphs target)',
    unit='paragraph crops', ann='Yes (automatic alignment)', ann_type='Paragraph text + match score (not human-verified)', lic='None declared; Chandamama is copyrighted', comm='Not established',
    redis='Not established', access_req='None', access='Open (HF, 10.7 GB)', ver='VERIFIED', overlap='Derived from Chandamama archive scans (TOCR-129).', cat='OCR image-text: printed', distinct='Y'))

R.append(E(
    id='TOCR-059', name='Sarvam Indic OCR Bench - Telugu', desc='Text-block crops from real Telugu documents (19th c. to present) with ground truth reviewed twice by language experts.',
    hf='https://huggingface.co/datasets/sarvamai/indic-ocr-bench', url='https://huggingface.co/datasets/sarvamai/indic-ocr-bench', inst='Sarvam AI', authors='Sarvam AI',
    lang='Multilingual (23 languages; Telugu rows identified)', modality='Image (printed blocks)', task='Block-level OCR (evaluation)', gran='Text block', rs='Real', count='300 Telugu test blocks (+51 in small_representative, a subset)',
    unit='block crops', ann='Yes', ann_type='Block transcription, double-reviewed', lic='Apache-2.0 (HF tag)', comm='Allowed by tag (source documents have own copyright)', redis='Allowed by tag',
    access_req='None', access='Open (HF)', ver='VERIFIED', quality='Audit 16/16 (block level); some source pages carry publisher watermarks.', cat='OCR image-text: printed', distinct='Y'))

R.append(E(
    id='TOCR-060', name='IndicDLP block-level OCR eval set (Telugu)', aliases='onath/indicdlp-eval-set-22 (private); onath/indicdlp-eval-set-22-sample (public)', parent='TOCR-109',
    desc='Cropped text blocks from IndicDLP pages with transcriptions; 582 Telugu blocks in the private full set, 10 in the public sample.',
    hf='https://huggingface.co/datasets/onath/indicdlp-eval-set-22-sample', url='https://huggingface.co/datasets/onath/indicdlp-eval-set-22-sample', inst='IIT Madras (author of IndicDLP)', authors='Oikantik Nath',
    lang='Multilingual (23 languages)', modality='Image (printed blocks)', task='Block-level OCR (evaluation)', gran='Text block', rs='Real', count='582 Telugu (private) / 10 Telugu (public sample, one magazine issue)',
    unit='block crops', ann='Yes', ann_type='Block transcription', lic='CC BY 4.0 (sample)', comm='Allowed (sample)', redis='Allowed (sample)', access_req='Full set private; sample open',
    access='Sample open; full set private', ver='PARTIALLY VERIFIED', cat='OCR image-text: printed', distinct='Y'))

R.append(E(
    id='TOCR-061', name='NayanaOCRBench Natural - Telugu', desc='Real Telugu document pages (e.g. TTD Sapthagiri magazine) with OmniDocBench-style layout + markdown/HTML text.',
    hf='https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Natural', url='https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Natural', inst='CognitiveLab', authors='CognitiveLab (Nayana team)',
    lang='Multilingual (22 languages; te config)', modality='Image (real document pages)', task='Page OCR + layout (evaluation)', gran='Page', rs='Real', count='461 Telugu pages', unit='page images',
    ann='Yes', ann_type='Layout boxes + markdown/HTML text', lic='CC BY-NC 4.0', comm='Not allowed', redis='Allowed (non-commercial)', access_req='None', access='Open (HF)', ver='VERIFIED',
    cat='OCR image-text: printed', distinct='Y'))

R.append(E(
    id='TOCR-062', name='OCR-Bench1000-Telugu', desc='Small Telugu OCR evaluation set (images + labels.txt + metadata.jsonl).', hf='https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Telugu',
    url='https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Telugu', inst='Individual', authors='meharuhanzz', modality='Image', task='OCR evaluation', gran='UNKNOWN', rs='UNKNOWN',
    count='1K-10K (HF size category)', unit='images', ann='Yes (labels.txt)', ann_type='Text labels (NOT VERIFIED)', lic='MIT (HF tag)', comm='Allowed by tag', redis='Allowed by tag',
    access_req='HF login + manual approval', access='Gated (manual)', ver='GATED', cat='OCR image-text: printed', distinct='Y', catalogue='TEL-OCR-010'))

R.append(E(
    id='TOCR-063', name='kailasa-ngpt/gemini-3.7-flash-ocr (Telugu pages)', desc='Book page images with OCR text produced by a Gemini model (Devanagari, Tamil, Telugu).',
    hf='https://huggingface.co/datasets/kailasa-ngpt/gemini-3.7-flash-ocr-26-aug-2026', url='https://huggingface.co/datasets/kailasa-ngpt/gemini-3.7-flash-ocr-26-aug-2026', inst='Kailasa (uploader)', authors='kailasa-ngpt',
    lang='Multilingual (Sanskrit/Hindi/Tamil/Telugu scripts)', modality='Image (book pages)', task='Page OCR (silver labels)', gran='Page', rs='Real images, machine labels', count='68 Telugu-script pages (13,117 total)',
    unit='page images', ann='Machine-generated', ann_type='Gemini OCR output', lic='other', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='VERIFIED',
    cat='Machine-labelled OCR (not human ground truth)', distinct='Y'))

R.append(E(
    id='TOCR-064', name='Telugu document image classification set (Ramu, 2025)', desc='Paper tests models on 500 handwritten + 500 printed Telugu document images; data not deposited.',
    url='https://zenodo.org/records/16778120', paper='https://doi.org/10.5281/zenodo.16778120', doi='10.5281/zenodo.16778120', inst='Academic', authors='I. Ramu',
    modality='Image (document pages)', task='Handwritten vs printed classification', gran='Page', rs='Real', count='1,000 (per paper)', unit='page images', ann='Class label (per paper)',
    ann_type='Handwritten/printed', lic='Article CC BY 4.0; data UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='Contact author', access='Article only', ver='UNVERIFIED',
    cat='Image-only (no transcription)', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-065', name='FutureBeeAI Telugu Newspaper, Magazine and Books OCR Image Dataset', version='Aug 2023', desc='5,000 images equally split across Telugu newspapers, books and magazines, with metadata.',
    url='https://www.futurebeeai.com/dataset/ocr-dataset/telugu-newspaper-book-magazine-ocr-image-dataset', inst='FutureBeeAI (vendor)', authors='FutureBeeAI', modality='Image (printed)',
    task='Printed OCR (after annotation)', gran='Page', rs='Real', count='5,000 (vendor claim)', unit='images', ann='No (transcription paid add-on)', ann_type='Metadata', lic='Commercial licence',
    comm='Allowed under purchase', redis='NOT ALLOWED', access_req='Purchase', access='Paid', ver='COMMERCIAL', cat='Image-only (no transcription)', distinct='Y'))

R.append(E(
    id='TOCR-066', name='FutureBeeAI Telugu Product Image OCR Dataset', version='Aug 2023', desc='2,000 front-of-pack product images with Telugu text, with metadata.',
    url='https://www.futurebeeai.com/dataset/ocr-dataset/telugu-product-image-ocr-dataset', inst='FutureBeeAI (vendor)', authors='FutureBeeAI', modality='Image (product photos)',
    task='Scene/product text OCR (after annotation)', gran='Image', rs='Real', count='2,000 (vendor claim)', unit='images', ann='No (paid add-on)', ann_type='Metadata', lic='Commercial licence',
    comm='Allowed under purchase', redis='NOT ALLOWED', access_req='Purchase', access='Paid', ver='COMMERCIAL', cat='Image-only (no transcription)', distinct='Y'))

R.append(E(
    id='TOCR-067', name='GitHub diuguide/telugu-ocr - page images with ground-truth manifest', desc='Course/research repo with 1,924 Telugu page images and a ground-truth manifest for selected pages.',
    github='https://github.com/diuguide/telugu-ocr', url='https://github.com/diuguide/telugu-ocr', inst='Individual / course project', authors='diuguide', modality='Image (scanned pages)',
    task='Page OCR', gran='Page', rs='Real (assumed)', count='1,924 page images; GT for a selected subset', unit='page images', ann='Partial', ann_type='Ground-truth manifest (format NOT VERIFIED)',
    lic='None stated', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED', cat='OCR image-text: printed', distinct='Y'))

R.append(E(
    id='TOCR-068', name='GitHub Pumapumapumas/ml-class-project - scanned Telugu pages', desc='Class project comparing Tesseract and vision LLMs on scanned Telugu pages; 30 external page images.',
    github='https://github.com/Pumapumapumas/ml-class-project', url='https://github.com/Pumapumapumas/ml-class-project', inst='Course project', authors='UNKNOWN', modality='Image (scanned pages)',
    task='Page OCR evaluation', gran='Page', rs='Real', count='30', unit='page images', ann='NOT VERIFIED', ann_type='NOT VERIFIED', lic='MIT (repo)', comm='Allowed by repo licence (page rights unclear)',
    redis='UNKNOWN', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED', quality='Very small.', cat='Image-only (transcription NOT VERIFIED)', distinct='Y'))

R.append(E(
    id='TOCR-069', name='GitHub ChillarAnand/likitham - ocropy Telugu line samples', desc='~25 ocropy line images (dataset/chalam) and a 76 KB training_samples.zip from a Telugu book.',
    github='https://github.com/ChillarAnand/likitham', url='https://github.com/ChillarAnand/likitham', inst='Individual', authors='Chillar Anand', modality='Image (printed lines)', task='Line recognition',
    gran='Line', rs='Real', count='~25 lines', unit='line images', ann='NOT VERIFIED', ann_type='ocropy GT (NOT VERIFIED)', lic='No licence file', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED', quality='Tiny; source book author (Chalam, d. 1979) likely still in copyright.', cat='Image-only (transcription NOT VERIFIED)', distinct='Y'))

# ------------------------------------------------------------------ scene text
R.append(E(
    id='TOCR-070', name='IIIT-ILST - Telugu (scene text)', version='2017 (ICDAR MOCR workshop)', desc='About 1,000 real scene images per script (Devanagari, Telugu, Malayalam) with word boxes (XML) and cropped word images with transcriptions.',
    url='https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-ilst', download='https://cvit.iiit.ac.in/images/datasets/iiit-ilst/IIIT-ILST.zip (639 MB, 3 scripts)',
    github='https://github.com/mineshmathew/IndicSceneTextRendering', paper='https://arxiv.org/abs/2104.04437', doi='10.1109/ICDAR.2017.364', inst='CVIT, IIIT Hyderabad',
    authors='Minesh Mathew, Mohit Jain, C. V. Jawahar', lang='Multilingual (3 scripts)', modality='Image (scene)', task='Scene text detection + recognition', gran='Word (+scene boxes)', rs='Real',
    count='1,211 Telugu cropped words (WordImagesList)', unit='word crops', ann='Yes', ann_type='Word boxes (XML) + transcription', lic='Research only; images may not be redistributed',
    comm='Not allowed', redis='NOT ALLOWED', access_req='None (agree to terms)', access='Open download', ver='VERIFIED', overlap='1,151 of 1,200 IndicSTR12-Telugu words are re-crops of these (TOCR-071/072).',
    cat='OCR image-text: scene text', distinct='Y'))

R.append(E(
    id='TOCR-071', name='IndicSTR12 real (CVIT release, all 12 languages)', aliases='IndicSTR12 real.zip; verified_twice', version='2023 (ICDAR); CVIT real.zip with corrected labels',
    desc='Real scene-text word crops and full scene images for 12 Indian languages crawled from Google Images; Telugu subset 1,183 crops + 298 scenes.',
    url='https://cvit.iiit.ac.in/research/projects/cvit-projects/indicstr', download='https://cvit.iiit.ac.in/images/datasets/IndicSTR12/real.zip (1.38 GB)', github='https://github.com/harshlunia7/IndicSTR12_ICDAR',
    paper='https://arxiv.org/abs/2403.08007', doi='10.1007/978-3-031-41498-5_17', inst='CVIT, IIIT Hyderabad', authors='Harsh Lunia, Ajoy Mondal, C. V. Jawahar', lang='Multilingual (12)',
    modality='Image (scene)', task='Scene text recognition; detection', gran='Word (+scenes)', rs='Real', count='>27,000 word images total; Telugu 1,183 crops (933/117/133) + 298 scenes', unit='word crops',
    ann='Yes', ann_type='Word transcription; boxes for full scenes', lic='CC BY 4.0 on annotations (ILOCR page); paper CC BY-NC-ND; images third-party web content', comm='Risky (image rights)',
    redis='Annotations yes; images unclear', access_req='None', access='Open download', ver='VERIFIED', overlap='Re-crops of IIIT-ILST Telugu (TOCR-070); 86 labels corrected vs ILOCR v0.5 (TOCR-072).',
    quality='Audit 14/16 correct (2 misspellings).', cat='OCR image-text: scene text', distinct='Y', catalogue='TEL-OCR-003'))

R.append(E(
    id='TOCR-072', name='IndicSTR12-Telugu (ILOCR v0.5)', parent='TOCR-071', aliases='ILOCR dataset 36', desc='ILOCR packaging of the Telugu real IndicSTR12 crops with train/test split.',
    url='https://ilocr.iiit.ac.in/dataset/36/', download='https://ilocr.iiit.ac.in/public/scenetext/phase-0/v0.5/telugu/IndicSTR12/{train,test}.zip (8.5 MB)', inst='ILOCR, IIIT Hyderabad',
    authors='Harsh Lunia, Ajoy Mondal, C. V. Jawahar', modality='Image (scene)', task='Scene text recognition', gran='Word', rs='Real', count='1,200 (900 / 300); 660 unique train words', unit='word crops',
    ann='Yes', ann_type='Word transcription', lic='CC BY 4.0 (stated on page)', comm='Annotations allowed; image rights third-party', redis='Annotations allowed', access_req='None', access='Open download',
    ver='VERIFIED', overlap='Official train/test share 154 scenes (leak); same images as TOCR-071 (1,183 byte-identical).', cat='OCR image-text: scene text', distinct='N (release of TOCR-071)'))

for i, (rid, ref, cnt, note) in enumerate([
        ('TOCR-073', 'darknight054/indicstr12-crops', '1,183 Telugu crops', 'byte-identical to CVIT real.zip crops'),
        ('TOCR-074', 'darknight054/indicstr12-full', '298 Telugu scenes with boxes', 'full scenes from real.zip'),
        ('TOCR-075', 'ananya12k/INDICSTR12_REAL_IMAGES', 'real.zip re-upload (1,382,967,649 bytes, identical size)', 'mirror of CVIT real.zip'),
        ('TOCR-076', 'jai23023/indicstr12-signboards (+ -preprocessed, -verified-twice)', '298 Telugu signboards / 1,183 verified-twice crops', 'derivatives reformatted for VLM tuning')]):
    R.append(E(id=rid, name=f'HF mirror/derivative: {ref}', parent='TOCR-071', desc=f'Hugging Face re-upload of IndicSTR12 real data ({note}).',
               hf='https://huggingface.co/datasets/' + ref.split(' ')[0], url='https://huggingface.co/datasets/' + ref.split(' ')[0], inst='Individual uploader', authors=ref.split('/')[0],
               lang='Multilingual (Telugu subset)', modality='Image (scene)', task='Scene text recognition', gran='Word', rs='Real', count=cnt, unit='images', ann='Yes', ann_type='Word transcription',
               lic='As declared on HF (none / MIT / CC BY 4.0) - upstream terms apply', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (HF)', ver='VERIFIED',
               overlap=f'Mirror/derivative of TOCR-071 ({note}).', cat='OCR image-text: scene text', distinct='N (mirror)'))

R.append(E(
    id='TOCR-077', name='Kaggle mirror: IndicSTR12 Indic Scene Text Recognition (prathmeshzade)', parent='TOCR-071', desc='Kaggle re-upload of IndicSTR12 real/verified_twice with annotations.csv.',
    kaggle='https://www.kaggle.com/datasets/prathmeshzade/indicstr12-indic-scene-text-recognition', url='https://www.kaggle.com/datasets/prathmeshzade/indicstr12-indic-scene-text-recognition',
    archive='Kaggle DOI listing (DataCite): https://www.kaggle.com/dsv/13849272', inst='Individual', authors='Prathmesh Zade', lang='Multilingual (12)', modality='Image (scene)', task='Scene text recognition',
    gran='Word', rs='Real', count='1,373 MB (all 12 languages)', unit='bytes', ann='Yes', ann_type='Word transcription', lic='MIT (Kaggle tag; upstream terms apply)', comm='UNKNOWN', redis='UNKNOWN',
    access_req='Kaggle account', access='Open listing', ver='VERIFIED', overlap='Mirror of TOCR-071.', cat='OCR image-text: scene text', distinct='N (mirror)'))

R.append(E(
    id='TOCR-078', name='Kaggle mirror: telugu scene text (srivarshachivukula5)', parent='TOCR-072', desc='Kaggle upload whose file names match the ILOCR IndicSTR12-Telugu crops.',
    kaggle='https://www.kaggle.com/datasets/srivarshachivukula5/telugu-scene-text', url='https://www.kaggle.com/datasets/srivarshachivukula5/telugu-scene-text', inst='Individual', authors='srivarshachivukula5',
    modality='Image (scene)', task='Scene text recognition', gran='Word', rs='Real', count='8.6 MB (ILOCR set is 8.5 MB)', unit='bytes', ann='Yes (assumed, same files)', ann_type='Word transcription',
    lic='Unknown', comm='UNKNOWN', redis='UNKNOWN', access_req='Kaggle account', access='Open listing', ver='VERIFIED', overlap='Mirror of TOCR-072 (identical file naming).', cat='OCR image-text: scene text', distinct='N (mirror)'))

R.append(E(
    id='TOCR-079', name='IIIT-IndicSTR-Word - Telugu (Indic Scene Text on the Roadside)', version='2024', desc='Word crops extracted from GoPro roadside videos in 10 Indian languages; 25,000 words per language.',
    url='https://cvit.iiit.ac.in/usodi/istr.php', download='https://cvit.iiit.ac.in/images/datasets/indic_scene_text_roadside/telugu.tar.gz (167.8 MB)', inst='CVIT, IIIT Hyderabad',
    authors='Ajoy Mondal, Krishna Tulsyan, C. V. Jawahar', lang='Multilingual (10)', modality='Image (scene, video frames)', task='Scene text recognition', gran='Word', rs='Real',
    count='250,000 total (10 languages); Telugu ~25,000', unit='word crops', ann='Yes', ann_type='Word transcription', lic='NOT STATED on page', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None', access='Open download (HTTP 200)', ver='VERIFIED', overlap='Same data as WIRIndic Telugu (TOCR-080): same 10 languages, 25K/language, GoPro roadside, archive size matches.',
    cat='OCR image-text: scene text', distinct='Y'))

R.append(E(
    id='TOCR-080', name='WIRIndic Telugu (ICPR 2024 Word Image Recognition in Indic scene text)', parent='TOCR-079', version='2024',
    desc='Competition release of the roadside Telugu word crops: train 17,500 / val 2,500 labelled, test 5,000 unlabelled.',
    url='https://ilocr.iiit.ac.in/icpr_2024_wirindic/dataset.html', download='https://ilocr.iiit.ac.in/icpr_2024_wirindic/assets/dataset/Telugu/{train,val,test}.zip', inst='CVIT / ILOCR, IIIT Hyderabad',
    authors='Competition organisers', modality='Image (scene, video frames)', task='Scene text recognition', gran='Word', rs='Real', count='25,000 (20,000 labelled)', unit='word crops', ann='Yes (train/val)',
    ann_type='Word transcription', lic='NOT STATED (page research line refers to MLT)', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open download', ver='VERIFIED',
    overlap='Competition packaging of TOCR-079; 95 of 193 MIST Telugu test frames are WIRIndic source frames (TOCR-081).', quality='Audit: ~44% of crops cut part of the word; only 4,580 distinct words.',
    cat='OCR image-text: scene text', distinct='N (release of TOCR-079)'))

R.append(E(
    id='TOCR-081', name='MIST - Multilingual Incidental Scene Text (Telugu frames)', desc='GoPro road-scene frames with polygon text annotations and script tags in 11 scripts.',
    hf='https://huggingface.co/datasets/Saumya-Mundra/MIST-Dataset', url='https://huggingface.co/datasets/Saumya-Mundra/MIST-Dataset', inst='CVIT, IIIT Hyderabad', authors='Saumya Mundra, Ajoy Mondal, C. V. Jawahar',
    lang='Multilingual (11 scripts)', modality='Image (scene)', task='Scene text detection; script ID', gran='Scene (polygons)', rs='Real', count='~12K scenes total; 193 Telugu-tagged test frames',
    unit='scene images', ann='Yes (polygons + script; no transcription in sampled files)', ann_type='Polygons, script, care flag', lic='Research use; ask authors for commercial', comm='Not without permission',
    redis='Raw imagery: ask authors', access_req='None', access='Open (HF)', ver='VERIFIED', overlap='Same road footage as TOCR-079/080.', cat='Layout / detection (no transcription)', distinct='Y'))

R.append(E(
    id='TOCR-082', name='Bharat Scene Text Dataset (BSTD)', aliases='IndicPhotoOCR data', version='2024-2026 (IJDAR 2026)',
    desc='6,582 scene images with polygon/word annotations in 11 Indian languages + English; supports detection, script ID, cropped word recognition, end-to-end.',
    url='https://github.com/Bhashini-IITJ/BharatSceneTextDataset', download='https://drive.google.com/file/d/1d8yOLWrStRTmB8nIJG3mi-w5P9IzB_z8 (recognition.zip, 791 MB); detection.zip (~17 GB)',
    hf='https://huggingface.co/datasets/Bhashini-IITJ/Bharat-Scene-Text-Dataset (gated copy, TOCR-083)', github='https://github.com/Bhashini-IITJ/BharatSceneTextDataset',
    paper='https://arxiv.org/abs/2511.23071', doi='10.1007/s10032-026-00583-9', inst='IIT Jodhpur (Bhashini)', authors='A. De, A. S. Penamakuri, R. Yadav, A. Rathore, H. Shah, D. Sharma, S. Agarwal, P. Kumar, A. Mishra',
    lang='Multilingual (11 Indian + English)', modality='Image (scene)', task='Scene text detection, script ID, recognition', gran='Word (+scenes)', rs='Real', count='Telugu 2,760 cropped words (2,215 train / 545 test)',
    unit='word crops', ann='Yes', ann_type='Polygons + word transcription + script', lic='Apache-2.0 (repository; no separate data licence)', comm='Likely allowed', redis='Likely allowed',
    access_req='None (Google Drive)', access='Open download', ver='VERIFIED', quality='457/2,760 labels use ౦ for ం (fixable); audit 13/16 correct.', cat='OCR image-text: scene text', distinct='Y'))

R.append(E(
    id='TOCR-083', name='HF gated copy: Bhashini-IITJ/Bharat-Scene-Text-Dataset', parent='TOCR-082', desc='Gated Hugging Face copy of BSTD.',
    hf='https://huggingface.co/datasets/Bhashini-IITJ/Bharat-Scene-Text-Dataset', url='https://huggingface.co/datasets/Bhashini-IITJ/Bharat-Scene-Text-Dataset', inst='IIT Jodhpur', authors='Bhashini-IITJ',
    lang='Multilingual', modality='Image (scene)', task='Scene text', gran='Word (+scenes)', rs='Real', count='See TOCR-082', unit='images', ann='Yes', ann_type='As TOCR-082', lic='other (HF)', comm='UNKNOWN',
    redis='UNKNOWN', access_req='HF login + accept terms', access='Gated (auto)', ver='GATED', overlap='Mirror of TOCR-082.', cat='OCR image-text: scene text', distinct='N (mirror)'))

R.append(E(
    id='TOCR-084', name='Indic-CIB: Indic Citizen Information Board dataset', desc='Photos of rural citizen-information boards (e.g. MGNREGA) in 6 Indic languages with machine-generated OCR/table/QA annotations.',
    hf='https://huggingface.co/datasets/Litap007/indic-citizen-information-board', url='https://huggingface.co/datasets/Litap007/indic-citizen-information-board', inst='Individual / research group', authors='Litap007',
    lang='Multilingual (hi, mr, te, kn, ta, ml)', modality='Image (scene boards)', task='Board OCR, table extraction, VQA', gran='Image', rs='Real', count='1K-10K total; Telugu share NOT VERIFIED', unit='images',
    ann='Machine-generated', ann_type='OCR text / tables / QA (machine-generated per card)', lic='Apache-2.0', comm='Allowed by tag', redis='Allowed by tag', access_req='None', access='Open (HF)',
    ver='PARTIALLY VERIFIED', cat='Machine-labelled OCR (not human ground truth)', distinct='Y'))

R.append(E(
    id='TOCR-085', name='Kaggle: Kannada-Centric Multilingual Meme Dataset (surajx7x)', desc='10,392 meme images (mostly Kannada, some English/Tamil/Telugu) with OCR text and language annotations.',
    kaggle='https://www.kaggle.com/datasets/surajx7x/new-dataset', url='https://www.kaggle.com/datasets/surajx7x/new-dataset', inst='Individual', authors='surajx7x',
    lang='Multilingual (Kannada-majority; some Telugu)', modality='Image (born-digital memes)', task='Born-digital text OCR / language ID', gran='Image', rs='Real', count='10,392 total; Telugu share UNKNOWN',
    unit='images', ann='Yes', ann_type='OCR text + language (annotations.json; origin NOT VERIFIED)', lic='Unknown (Kaggle)', comm='UNKNOWN', redis='UNKNOWN', access_req='Kaggle account', access='Open listing',
    ver='PARTIALLY VERIFIED', cat='OCR image-text: scene text', distinct='Y', notes='Born-digital images grouped with scene text; Telugu subset not identified.'))

# ------------------------------------------------------------------ synthetic
R.append(E(
    id='TOCR-086', name='IIIT-Synthetic-M-Telugu', aliases='ILOCR dataset 40', version='v0.5', desc='Synthetic printed Telugu word images rendered with 62 Unicode fonts; page says pre-training use only.',
    url='https://ilocr.iiit.ac.in/dataset/40/', download='https://ilocr.iiit.ac.in/public/printed/phase-0/v0.5/telugu/IIIT-Synthetic-M-Telugu/train.zip (169 MB; page link wrongly points to /hindi/)',
    inst='ILOCR, IIIT Hyderabad', authors='ILOCR team', modality='Image (rendered printed words)', task='Printed word recognition (pre-training)', gran='Word', rs='Synthetic', count='138,585 (61,142 unique words)',
    unit='word images', ann='Yes', ann_type='Rendered text (exact)', lic='NOT STATED (no licence section on any IIIT-Synthetic page)', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open download',
    ver='VERIFIED', cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-087', name='IIIT-Synthetic-R-Telugu', aliases='ILOCR dataset 55', version='v0.5', desc='Synthetic printed Telugu word images rendered with 300 fonts; train/val/test.',
    url='https://ilocr.iiit.ac.in/dataset/55/', download='https://ilocr.iiit.ac.in/public/printed/phase-0/v0.5/telugu/IIIT-Synthetic-R-Telugu/{train,val,test}.zip (2.05 GB)', inst='ILOCR, IIIT Hyderabad',
    authors='ILOCR team', modality='Image (rendered printed words)', task='Printed word recognition', gran='Word (often 2 joined words)', rs='Synthetic', count='612,500 (428,750 / 61,250 / 122,500)', unit='word images',
    ann='Yes', ann_type='Rendered text (leading space in labels)', lic='NOT STATED', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open download', ver='VERIFIED',
    overlap='1,270 near-identical image+label groups across official train/test.', cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-088', name='IIIT-Synthetic-IndicSTR-Telugu', aliases='ILOCR dataset 68; IIIT-Synthetic-Telugu', version='v0.5', desc='Synthetic scene-style Telugu word images (backgrounds, distortions).',
    url='https://ilocr.iiit.ac.in/dataset/68/', download='https://ilocr.iiit.ac.in/public/scenetext/phase-0/v0.5/telugu/IIIT-Synthetic-Telugu/{train,val,test}.zip (6.3 GB)', inst='ILOCR, IIIT Hyderabad',
    authors='ILOCR team', modality='Image (synthetic scene words)', task='Scene text recognition (pre-training)', gran='Word', rs='Synthetic', count='2,999,658 (2,000,000 / 499,658 / 500,000)', unit='word images',
    ann='Yes', ann_type='Rendered text', lic='NOT STATED', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open download', ver='VERIFIED',
    overlap='Likely the Telugu part of the IndicSTR12 synthetic release (TOCR-089: "3M per language").', quality='~25% of audited images near-unreadable; 99.8% of test words appear in train.',
    cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-089', name='IndicSTR12 synthetic (CVIT synthetic.tar.gz, 13 languages)', desc='Synthetic scene-text word images for 13 Indian languages; paper states more than 3 million per language.',
    url='https://cvit.iiit.ac.in/research/projects/cvit-projects/indicstr', download='https://cvit.iiit.ac.in/images/datasets/IndicSTR12/synthetic.tar.gz (62.7 GB, HTTP 200)', paper='https://arxiv.org/abs/2403.08007',
    inst='CVIT, IIIT Hyderabad', authors='Harsh Lunia, Ajoy Mondal, C. V. Jawahar', lang='Multilingual (13 incl. Telugu)', modality='Image (synthetic scene words)', task='Scene text recognition (pre-training)',
    gran='Word', rs='Synthetic', count='>3M per language (paper); Telugu count NOT VERIFIED', unit='word images', ann='Yes', ann_type='Rendered text', lic='NOT STATED', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None', access='Open download (size verified via HEAD only)', ver='PARTIALLY VERIFIED', overlap='Suspected same Telugu data as TOCR-088 (3M Telugu images both) - NOT VERIFIED.',
    cat='OCR image-text: synthetic', distinct='N (suspected same as TOCR-088)'))

R.append(E(
    id='TOCR-090', name='Kaggle mirror: telugu scene text iiit (+ -val) (gottumukkalamadhuri)', parent='TOCR-088', desc='Kaggle uploads with IIIT-Synthetic-IndicSTR file naming (e.g. 0_0.0_102.jpeg).',
    kaggle='https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-scene-text-iiit ; https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-scene-text-iiit-val',
    url='https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-scene-text-iiit', inst='Individual', authors='gottumukkalamadhuri', modality='Image (synthetic scene words)', task='Scene text recognition',
    gran='Word', rs='Synthetic', count='6,306.9 MB + 1,041.5 MB (ILOCR zips: 4.2+1.05+1.05 GB)', unit='bytes', ann='Yes (assumed)', ann_type='Rendered text', lic='Apache-2.0 tag (not the uploader\'s to grant)',
    comm='UNKNOWN', redis='UNKNOWN', access_req='Kaggle account', access='Open listing', ver='VERIFIED', overlap='Mirror of TOCR-088.', cat='OCR image-text: synthetic', distinct='N (mirror)'))

R.append(E(
    id='TOCR-091', name='Kaggle mirror (mislabelled): "telugu handwritten dataset" (gottumukkalamadhuri)', parent='TOCR-087',
    desc='Titled handwritten, but file names (Aaradhana_0.0_1.png ...) are IIIT-Synthetic-R-Telugu printed synthetic images.', kaggle='https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-handwritten-dataset',
    url='https://www.kaggle.com/datasets/gottumukkalamadhuri/telugu-handwritten-dataset', inst='Individual', authors='gottumukkalamadhuri', modality='Image (rendered printed words)', task='Printed word recognition',
    gran='Word', rs='Synthetic', count='3,715 MB', unit='bytes', ann='Yes (assumed)', ann_type='Rendered text', lic='Apache-2.0 tag (not the uploader\'s to grant)', comm='UNKNOWN', redis='UNKNOWN',
    access_req='Kaggle account', access='Open listing', ver='VERIFIED', overlap='Mirror of TOCR-087, despite the "handwritten" title.', cat='OCR image-text: synthetic', distinct='N (mirror)'))

R.append(E(
    id='TOCR-092', name='Chitralekha - synthetic Telugu word images', version='2024', desc='Rendered Telugu word images, one config per font (Noto, Pothana2000, Ramabhadra, Mandali, Gidugu ...), with splits.',
    hf='https://huggingface.co/datasets/gksriharsha/chitralekha', url='https://huggingface.co/datasets/gksriharsha/chitralekha', inst='Individual', authors='gksriharsha', modality='Image (rendered words)',
    task='Word recognition (pre-training)', gran='Word', rs='Synthetic', count='61,898,021 rows across font configs (~790K per font)', unit='word images', ann='Yes', ann_type='Rendered text', lic='MIT',
    comm='Allowed', redis='Allowed', access_req='None', access='Open (HF)', ver='VERIFIED', cat='OCR image-text: synthetic', distinct='Y', catalogue='TEL-OCR-006'))

R.append(E(
    id='TOCR-093', name='harsha-desaraju/telugu-synthetic-line-images', desc='2.5M rendered Telugu (and Sanskrit-in-Telugu) line images with font and fragment metadata.',
    hf='https://huggingface.co/datasets/harsha-desaraju/telugu-synthetic-line-images', url='https://huggingface.co/datasets/harsha-desaraju/telugu-synthetic-line-images', inst='Individual', authors='Harsha Desaraju',
    modality='Image (rendered lines)', task='Line recognition (pre-training)', gran='Line', rs='Synthetic', count='2,500,000 (10 train shards + 5,000 val)', unit='line images', ann='Yes', ann_type='Rendered text',
    lic='MIT', comm='Allowed', redis='Allowed', access_req='None', access='Open (HF)', ver='VERIFIED', cat='OCR image-text: synthetic', distinct='Y', catalogue='TEL-OCR-007'))

R.append(E(
    id='TOCR-094', name='harsha-desaraju/Telugu-text-image (rendered news chunks)', desc='Andhra Jyothy news text rendered in Telugu fonts, with source text and an OCR read of the render.',
    hf='https://huggingface.co/datasets/harsha-desaraju/Telugu-text-image', url='https://huggingface.co/datasets/harsha-desaraju/Telugu-text-image', inst='Individual', authors='Harsha Desaraju',
    modality='Image (rendered text blocks)', task='Block recognition', gran='Text chunk', rs='Synthetic', count='113,592', unit='rendered chunks', ann='Yes', ann_type='Source text (+OCR text)',
    lic='None declared; news text is publisher copyright', comm='Not established', redis='Not established', access_req='None', access='Open (HF)', ver='VERIFIED', cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-095', name='Telugu Document Image-Text Pairs (amancapy/telugu-scans)', version='2023-04-27',
    desc='20,000 generated "scan-like" Telugu document page images paired with their text; generator code on GitHub.',
    kaggle='https://www.kaggle.com/datasets/amancapy/telugu-scans', url='https://www.kaggle.com/datasets/amancapy/telugu-scans', inst='Individual', authors='amancapy', modality='Image (rendered pages)',
    task='Page OCR (image-to-sequence)', gran='Page', rs='Synthetic', count='20,000 pairs (4,708 MB)', unit='page image-text pairs', ann='Yes', ann_type='Page text (doc{i}.png <-> {i}.txt)',
    lic='CC BY-NC 4.0 (Kaggle)', comm='Not allowed', redis='Allowed (non-commercial)', access_req='Kaggle account', access='Open listing', ver='VERIFIED',
    overlap='Re-listed by GTS.ai with a CC BY 4.0 claim (TOCR-096).', cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-096', name='GTS.ai "Telugu Document Image Dataset" (and Zenodo brochure records)', parent='TOCR-095', aliases='Zenodo 10.5281/zenodo.14965381 / 14965382; Globose Technology Solutions',
    desc='Vendor listing of the same 20,000 image-text pairs; the page\'s download links to the Kaggle original; Zenodo holds only a 419 KB brochure PDF.',
    url='https://gts.ai/dataset-download/telugu-document-image-dataset/', archive='https://doi.org/10.5281/zenodo.14965382', doi='10.5281/zenodo.14965382', inst='Globose Technology Solutions (GTS.ai)',
    authors='Globose Technology Solutions', modality='Image (rendered pages)', task='Page OCR', gran='Page', rs='Synthetic', count='20,000 (claim = Kaggle original)', unit='page image-text pairs', ann='Yes',
    ann_type='Page text', lic='CC BY 4.0 claimed on Zenodo - conflicts with original CC BY-NC 4.0', comm='Treat as non-commercial (original licence)', redis='See original',
    access_req='Links to Kaggle', access='Brochure only on Zenodo; data via Kaggle', ver='VERIFIED', overlap='Re-listing of TOCR-095; not independent data.',
    cat='OCR image-text: synthetic', distinct='N (re-listing)', catalogue='TEL-OCR-014'))

R.append(E(
    id='TOCR-097', name='NayanaOCR Corpus 2025 - Telugu', desc='Synthetic/rendered Telugu documents with layout regions and VQA for document VLM training.',
    hf='https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025', url='https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025', inst='CognitiveLab', authors='Adithya Kolavi et al. (Nayana)',
    lang='Multilingual (22; te config)', modality='Image (rendered documents)', task='Document OCR + layout + VQA', gran='Page (regions)', rs='Synthetic (translated/rendered)', count='45,735 Telugu pages (37.8 GB)',
    unit='page images', ann='Yes', ann_type='Region boxes + text + VQA', lic='CC BY-NC 4.0', comm='Not allowed', redis='Allowed (non-commercial)', access_req='None', access='Open (HF)', ver='VERIFIED',
    overlap='Built from NayanaDocs-Indic-45k (gated, TOCR-098).', cat='OCR image-text: synthetic', distinct='Y', catalogue='TEL-OCR-008'))

R.append(E(
    id='TOCR-098', name='Nayana gated OCR/VQA family (Telugu configs)', aliases='Nayana-cognitivelab/NayanaDocs-Indic-45k; Nayana-DocOCR-Indic-1m; Nayana-DocOCR-Indic-annotations; Nayana-DocOCR-mr-ta-te-or-pa-15k-v1-docmatix; Nayana-DocOCR-ml-mr-ta-te-or-pa-15k-v1-pubmed; Nayana-IR-DescVQA-Indic-47k(_or_ta_te); NayanaOCRBench_Synthetic; 1DuBu1/NayanaOCR_Corpus_2025; Nayana-OCRBench-* variants; SectionOCR-SFT',
    desc='Family of gated Hugging Face repositories from the Nayana project with Telugu-named files: source documents, 1M-page document OCR, translated DocMatix/PubMed pages and benchmarks.',
    hf='https://huggingface.co/Nayana-cognitivelab', url='https://huggingface.co/Nayana-cognitivelab', inst='CognitiveLab', authors='Nayana team', lang='Multilingual (incl. Telugu)', modality='Image (documents)',
    task='Document OCR / VQA / retrieval', gran='Page', rs='Mostly synthetic (rendered/translated)', count='UNKNOWN per repo (HF size categories 1K-1M)', unit='pages', ann='Yes (per repo names)',
    ann_type='NOT VERIFIED (gated)', lic='Mostly none declared / CC BY-NC (OCRBench)', comm='UNKNOWN', redis='UNKNOWN', access_req='HF login + manual approval', access='Gated (manual)', ver='GATED',
    overlap='Parents/variants of TOCR-097 and TOCR-099.', cat='OCR image-text: synthetic', distinct='UNKNOWN (counted once as a family)'))

R.append(E(
    id='TOCR-099', name='NayanaBench (Telugu)', aliases='ranjanhr1/nayanabench-rendered; v1v1d/NayanaBench-rendered-split; NayanaBench-with-reading-order (derivatives)',
    desc='Multilingual document VQA benchmark combining OCR, layout and QA; 200 examples per language including Telugu.', hf='https://huggingface.co/datasets/Nayana-cognitivelab/NayanaBench',
    url='https://huggingface.co/datasets/Nayana-cognitivelab/NayanaBench', inst='CognitiveLab', authors='Nayana team', lang='Multilingual (22)', modality='Image (documents)', task='Document VQA / OCR evaluation',
    gran='Page', rs='Synthetic/rendered (NOT VERIFIED)', count='200 Telugu examples', unit='QA items', ann='Yes', ann_type='QA + OCR/layout', lic='None declared', comm='UNKNOWN', redis='UNKNOWN', access_req='None',
    access='Open (HF)', ver='PARTIALLY VERIFIED', cat='Text-in-image benchmark (VQA / document understanding)', distinct='Y'))

R.append(E(
    id='TOCR-100', name='Synthdog-Multilingual-100 - Telugu', desc='SynthDoG-rendered document images with Wikipedia text in 100 languages (GoNotoKurrent font); 10,000 per non-Latin language.',
    hf='https://huggingface.co/datasets/WueNLP/Synthdog-Multilingual-100', url='https://huggingface.co/datasets/WueNLP/Synthdog-Multilingual-100', paper='https://gregor-ge.github.io/Centurio/', inst='WueNLP (University of Wurzburg)',
    authors='Gregor Geigle et al.', lang='Multilingual (100; te)', modality='Image (rendered documents)', task='Document OCR pre-training', gran='Page', rs='Synthetic', count='10,000 Telugu (per card; not counted)',
    unit='page images', ann='Yes', ann_type='Rendered text (jsonl)', lic='Apache-2.0', comm='Allowed', redis='Allowed', access_req='None', access='Open (images in one 11.3 GB tar.gz)', ver='PARTIALLY VERIFIED',
    cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-101', name='Synthetic captchas library - Telugu 4-character', desc='100,000 synthetic captcha images of 4 random Telugu characters with labels.',
    hf='https://huggingface.co/datasets/remiai3/synthetic-captchas-library', url='https://huggingface.co/datasets/remiai3/synthetic-captchas-library', inst='Individual', authors='remiai3', lang='Multilingual (26 scripts)',
    modality='Image (synthetic captchas)', task='Character-sequence recognition', gran='4 characters', rs='Synthetic', count='100,000 Telugu', unit='images', ann='Yes', ann_type='labels.csv', lic='CC BY 4.0',
    comm='Allowed', redis='Allowed', access_req='None', access='Open (HF)', ver='VERIFIED', quality='Random letters, not words; captcha noise.', cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-102', name='OCR Synthetic Benchmark Dataset for Indic Languages (EkStep / Tarento)', version='2022', desc='Synthetic OCR benchmark of 90K images with ground truth for 23 Indic languages.',
    url='https://arxiv.org/abs/2205.02543', paper='https://arxiv.org/abs/2205.02543', doi='10.48550/arXiv.2205.02543', inst='EkStep Foundation; Tarento Technologies', authors='Naresh Saini et al.',
    lang='Multilingual (23 incl. Telugu per paper)', modality='Image (rendered)', task='OCR benchmark', gran='UNKNOWN', rs='Synthetic', count='90K total; Telugu share UNKNOWN', unit='images', ann='Yes',
    ann_type='Ground-truth text', lic='Paper CC BY 4.0; data UNKNOWN', comm='UNKNOWN', redis='UNKNOWN', access_req='UNKNOWN', access='No download link found', ver='UNVERIFIED', cat='OCR image-text: synthetic', distinct='UNKNOWN'))

R.append(E(
    id='TOCR-103', name='Kaggle: Final_Telugu_Manuscript_Data (yvenkatasriramreddy)', desc='8.2 GB of PNG + TXT pairs named "chaos_mixed_NNNNN" in a 10k_Data folder; likely generated manuscript-style pages.',
    kaggle='https://www.kaggle.com/datasets/yvenkatasriramreddy/final-telugu-manuscript-data', url='https://www.kaggle.com/datasets/yvenkatasriramreddy/final-telugu-manuscript-data', inst='Individual',
    authors='Y. Venkata Sriram Reddy', modality='Image (manuscript-style pages)', task='Page OCR', gran='Page', rs='UNKNOWN (likely synthetic)', count='8,181.8 MB; ~10K+ pairs (folder name)', unit='image-text pairs',
    ann='Yes', ann_type='Text file per image', lic='CC0-1.0', comm='Allowed', redis='Allowed', access_req='Kaggle account', access='Open listing', ver='PARTIALLY VERIFIED', cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-104', name='banti_training (Telugu OCR glyph training data)', desc='Glyph images used to train the banti Telugu OCR CNN (Achanta & Hastie).',
    github='https://github.com/rakeshvar/banti_training', url='https://github.com/rakeshvar/banti_training', paper='https://arxiv.org/abs/1509.05962', doi='10.48550/arXiv.1509.05962',
    inst='Stanford (authors)', authors='Rakesh Achanta, Trevor Hastie', modality='Image (glyphs)', task='Glyph classification', gran='Glyph', rs='UNKNOWN (rendered/segmented)', count='467 image files (data48 + numbers)',
    unit='glyph images / sheets', ann='Yes (folder/naming)', ann_type='Glyph class', lic='None stated (code repos Apache-2.0)', comm='UNKNOWN', redis='UNKNOWN', access_req='None', access='Open (GitHub)',
    ver='PARTIALLY VERIFIED', overlap='Paper describes 460 classes x 160 samples; repo may hold a subset.', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-105', name='Telugu_OCR_Tesseract_Training (font box/tif training files)', desc='Tesseract training files (tif + box) for many Telugu fonts to OCR old literature.',
    github='https://github.com/saikrishnawanted/Telugu_OCR_Tesseract_Training', url='https://github.com/saikrishnawanted/Telugu_OCR_Tesseract_Training', inst='Individual', authors='saikrishnawanted',
    modality='Image (rendered text pages)', task='Tesseract training', gran='Line/page', rs='Synthetic', count='363 MB repo; 293 files', unit='files', ann='Yes', ann_type='Box files', lic='GPL-3.0',
    comm='Allowed under GPL', redis='Allowed under GPL', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED', cat='OCR image-text: synthetic', distinct='Y'))

R.append(E(
    id='TOCR-106', name='chaitusvk/telugu_ocr_multi_line - generated line images', desc='Small set of generated multi-line Telugu images used for a CRNN project.',
    github='https://github.com/chaitusvk/telugu_ocr_multi_line', url='https://github.com/chaitusvk/telugu_ocr_multi_line', inst='Individual', authors='chaitusvk', modality='Image (rendered lines)',
    task='Line recognition', gran='Line', rs='Synthetic', count='246 images', unit='images', ann='NOT VERIFIED', ann_type='NOT VERIFIED', lic='None stated', comm='UNKNOWN', redis='UNKNOWN',
    access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED', quality='Tiny.', cat='Image-only (transcription NOT VERIFIED)', distinct='Y'))

R.append(E(
    id='TOCR-107', name='Telugu character database (Konkimalla et al., ICIP 2018)', desc='Database of Telugu characters covering all vattu/gunintam combinations: 17,387 categories, ~560 samples each (6.76M train / 0.97M val).',
    url='https://arxiv.org/abs/1711.07245', paper='https://arxiv.org/abs/1711.07245', doi='10.1109/ICIP.2018.8451438', inst='IIT Hyderabad', authors='Chandra Prakash Konkimalla, Sumohana Channappayya et al.',
    modality='Image (32x32 characters)', task='Character recognition', gran='Character', rs='UNKNOWN (likely rendered)', count='17,387 classes; 6,757,044 train + 972,309 val (+test)', unit='character images', ann='Yes',
    ann_type='Character class', lic='UNKNOWN (paper promises code release)', comm='UNKNOWN', redis='UNKNOWN', access_req='UNKNOWN', access='Original data location not found', ver='UNVERIFIED',
    overlap='Same abstract appears on IEEE DataPort a1kv-rj60 (TOCR-108) under a different author.', cat='Character / glyph classification', distinct='Y'))

R.append(E(
    id='TOCR-108', name='"OCR Telugu Image Dataset" (IEEE DataPort a1kv-rj60)', parent='TOCR-107', version='2023', desc='IEEE DataPort entry whose abstract repeats the Konkimalla et al. 17,387-class database description.',
    url='https://ieee-dataport.org/documents/ocr-telugu-image-dataset', doi='10.21227/a1kv-rj60', inst='Boon IT Solutions (per search snippet)', authors='Kadavakollu Venkateswara Rao',
    modality='Image (characters)', task='Character recognition', gran='Character', rs='UNKNOWN', count='UNKNOWN (abstract cites 6,757,044 train / 972,309 val)', unit='character images', ann='UNKNOWN',
    ann_type='UNKNOWN', lic='CC BY 4.0 (DataCite)', comm='As stated', redis='As stated', access_req='IEEE DataPort login', access='Gated', ver='GATED',
    overlap='Suspected re-upload of TOCR-107 (identical abstract, different author); one search engine described it as handwritten shopping lists - contents NOT VERIFIED.',
    cat='Character / glyph classification', distinct='N (suspected re-upload)'))
