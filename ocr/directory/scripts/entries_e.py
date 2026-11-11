"""Directory records, part E: round-3 adversarial completeness pass (2026-11-11).

R       new rows (TOCR-210 onwards), round='Round 3 (2026-11-11)'.
apply() corrections to earlier rows; each changed row gets a 'Round 3 change' note.
Evidence: evidence/manager_simulation_searches.json, evidence/discovery/{hf_full_listing,github_deep,crossref,pwc_archive_telugu}.json,
evidence/discovery/github_round3_inspect.txt and the URLs in each record.
"""
from common import E

ROUND = 'Round 3 (2026-11-11)'
R = []


def N(**kw):
    kw.setdefault('round', ROUND)
    kw.setdefault('changed3', 'New in round 3')
    R.append(E(**kw))


# ------------------------------------------------------------------ competitions, archives, paper-only datasets
N(id='TOCR-210', name='CVSI-2015 - ICDAR 2015 Competition on Video Script Identification (Telugu)', aliases='CVSI 2015', version='2015',
  desc='Cropped word images from video frames (mostly overlaid news/sports captions, some scene text) in 10 scripts incl. Telugu, for script identification.',
  url='https://www.ict.griffith.edu.au/cvsi2015/Dataset.php', paper='ICDAR 2015 competition report (Sharma, Mandal, Sharma, Pal, Blumenstein) - DOI NOT VERIFIED',
  inst='Griffith University; ISI Kolkata (organisers)', authors='Nabin Sharma, Ranju Mandal, Rabi Sharma, Umapada Pal, Michael Blumenstein',
  lang='Multilingual (10 scripts incl. Telugu)', modality='Image (video-frame word crops)', task='Script identification', gran='Word', rs='Real',
  count='>=1,000 word images per script (60/10/30 train/val/test)', unit='word images', ann='Script label only', ann_type='Script class (no transcription)',
  lic='Research only; commercial use not allowed (organiser terms)', comm='Not allowed', redis='UNKNOWN', access_req='Registration with organisers',
  access='Organiser page reset connections to scripts (2026-11-11); facts from indexed page text', ver='PARTIALLY VERIFIED', cat='Script identification', distinct='Y')

N(id='TOCR-211', name='British Library Endangered Archives EAP038 - pre-1947 Telugu printed books and periodicals', aliases='EAP038',
  desc='Digitised (microfilm/scan) Telugu books and periodicals from Andhra Pradesh libraries, mostly 1869-1947 (e.g. Prajasakthi, Navasakthi issues).',
  url='https://eap.bl.uk/project/EAP038', inst='British Library Endangered Archives Programme', authors='EAP038 project team', modality='Image (scanned pages)',
  task='Unlabelled scans', gran='Page', rs='Real', count='2,164 catalogued items; ~159,260 images (per search-indexed project text)', unit='items / page images',
  ann='No', ann_type='None', lic='EAP terms (non-commercial research use; NOT VERIFIED)', comm='UNKNOWN', redis='UNKNOWN', access_req='None (online viewer)',
  access='Project and catalogue pages indexed; live page returned empty to scripts (2026-11-11)', ver='PARTIALLY VERIFIED', cat='Scanned archive (image-only)', distinct='Y')

N(id='TOCR-212', name='Telugu palm-leaf character database (Amrita, 2012)', version='2012', desc='Paper describes a data acquisition system and a database of isolated Telugu characters from palm-leaf manuscripts.',
  url='https://www.amrita.edu/publication/a-data-acquisition-and-analysis-system-for-palm-leaf-documents-in-telugu/', inst='Amrita Vishwa Vidyapeetham', authors='NOT VERIFIED',
  modality='Image (palm-leaf characters)', task='Character recognition', gran='Character', rs='Real', count='UNKNOWN', unit='character images', ann='Yes (per paper)', ann_type='Character class',
  lic='UNKNOWN', access_req='Contact authors', access='No public release found', ver='UNVERIFIED', overlap='Related palm-leaf work: TOCR-117, 118, 119, 120, 228.',
  cat='Character / glyph classification', distinct='UNKNOWN')

N(id='TOCR-213', name='ICDAR 2025 Competition on Multi-lingual Roadside Scene Text Recognition (MLT-RSTR) - Telugu', aliases='MLT-STDR-2025', version='2025',
  desc='Full roadside scene images in 10 Indic languages with word polygons, transcriptions and language labels; tasks cover detection, recognition and language ID.',
  url='https://ilocr.iiit.ac.in/icdar_2025_MLT-RSTR/dataset.html', download='https://ilocr.iiit.ac.in/icdar_2025_MLT-RSTR/assets/dataset/Val/Val.zip (HTTP 404 on 2026-11-11)',
  inst='CVIT / ILOCR, IIIT Hyderabad', authors='Competition organisers', lang='Multilingual (10 Indic incl. Telugu)', modality='Image (roadside scenes)', task='Scene text detection + recognition + language ID',
  gran='Word polygons in full scenes', rs='Real', count='UNKNOWN', unit='scene images', ann='Yes (validation set)', ann_type='Polygon + transcription + language (JSON)',
  lic='UNKNOWN', access_req='Competition registration', access='All validation/test zips HTTP 404 (2026-11-11); Telugu charlist downloads', ver='INACCESSIBLE',
  overlap='Roadside collection; suspected same source as IIIT-IndicSTR-Word / WIRIndic (TOCR-079/080).', cat='OCR image-text: scene text', distinct='UNKNOWN (suspected same collection as TOCR-079)')

N(id='TOCR-214', name='Telugu Meme Dataset (domain and troll identification, NITK)', version='2024', desc='Telugu memes (image + embedded text) labelled for domain, troll / non-troll and emotion.',
  url='https://doi.org/10.1007/978-3-031-58495-4_2', paper='https://doi.org/10.1007/978-3-031-58495-4_2', doi='10.1007/978-3-031-58495-4_2', inst='NIT Karnataka (NITK)',
  authors='N. Lohith, S. Adnan Raqeeb, Poreddy Sai Manoj Reddy, Chekuri Venkata Sunil Kumar, M. Anand Kumar', modality='Image (born-digital memes)', task='Meme classification',
  gran='Image', rs='Real', count='UNKNOWN', unit='memes', ann='Class labels; embedded-text transcription NOT VERIFIED', ann_type='Troll / domain / emotion labels',
  lic='UNKNOWN', access_req='Contact authors / shared task', access='Repository page HTTP 502; no public download found', ver='UNVERIFIED', cat='Image-only (transcription NOT VERIFIED)', distinct='Y')

N(id='TOCR-215', name='LT-EDI 2024 shared task: troll meme classification - Telugu', parent='TOCR-214', version='2024',
  desc='Gold-standard Telugu (and Kannada) troll / non-troll meme data for the LT-EDI 2024 "Multitask Meme Classification" shared task.',
  url='https://aclanthology.org/2024.ltedi-1.13.pdf', paper='https://doi.org/10.18653/v1/2024.ltedi-1.13', doi='10.18653/v1/2024.ltedi-1.13', inst='LT-EDI 2024 organisers',
  authors='Bharathi Raja Chakravarthi, Saranya Rajiakodi et al. (incl. M. Anand Kumar)', modality='Image (memes)', task='Troll meme classification', gran='Image', rs='Real',
  count='UNKNOWN (Telugu size not given in overview)', unit='memes', ann='Class labels', ann_type='Troll / non-troll', lic='UNKNOWN', access_req='Shared-task registration',
  access='Not checked (CodaLab-style release)', ver='UNVERIFIED', overlap='Shared co-organiser with TOCR-214; suspected same Telugu memes.', cat='Image-only (transcription NOT VERIFIED)',
  distinct='N (suspected same data as TOCR-214)')

N(id='TOCR-216', name='IIIT Telugu document test sets (Rasagna 2013 MS thesis)', version='2013', desc='Laser-print, good-real and challenging-real Telugu document image sets with ground truth, used to evaluate document-level Telugu OCR.',
  url='https://cvit.iiit.ac.in/research/thesis/thesis-students/studies-in-recognition-of-telugu-document-images', paper='Rasagna_Thesis2013.pdf on the IIIT thesis server (tickets-felicity.iiit.ac.in; TLS certificate invalid on 2026-11-11)',
  inst='CVIT, IIIT Hyderabad', authors='Venkat Rasagna (supervised by C. V. Jawahar)', modality='Image (printed pages)', task='Printed Telugu OCR evaluation', gran='Page / word', rs='Real + laser-printed',
  count='UNKNOWN (one set ~200 pages per search snippet)', unit='pages', ann='Yes (per thesis)', ann_type='Text ground truth', lic='UNKNOWN', access_req='Contact CVIT',
  access='Internal; no release found', ver='UNVERIFIED', overlap='Likely drawn from the same DLI book pages as TOCR-044/045.', cat='OCR image-text: printed', distinct='UNKNOWN')

N(id='TOCR-217', name='TelMeMood - multimodal Telugu meme sentiment dataset', version='2025', desc='Telugu memes (image + text) annotated for sentiment.',
  url='https://doi.org/10.1109/isacc65211.2025.10969246', paper='https://doi.org/10.1109/isacc65211.2025.10969246', doi='10.1109/isacc65211.2025.10969246', inst='UNKNOWN',
  authors='NOT VERIFIED', modality='Image (memes)', task='Meme sentiment analysis', gran='Image', rs='Real', count='UNKNOWN', unit='memes', ann='Sentiment labels; text transcription NOT VERIFIED',
  ann_type='Sentiment', lic='UNKNOWN', access_req='Contact authors', access='No public link found', ver='UNVERIFIED', cat='Image-only (transcription NOT VERIFIED)', distinct='Y')

N(id='TOCR-218', name='Benchmark dataset for hateful memes detection in Telugu', version='2026', desc='Telugu memes annotated for hateful content (Springer 2026).',
  url='https://doi.org/10.1007/978-3-032-13803-3_27', paper='https://doi.org/10.1007/978-3-032-13803-3_27', doi='10.1007/978-3-032-13803-3_27', inst='UNKNOWN', authors='NOT VERIFIED',
  modality='Image (memes)', task='Hateful meme classification', gran='Image', rs='Real', count='UNKNOWN', unit='memes', ann='Labels; text transcription NOT VERIFIED', ann_type='Hate labels',
  lic='UNKNOWN', access_req='Contact authors', access='No public link found (Crossref record only)', ver='UNVERIFIED', cat='Image-only (transcription NOT VERIFIED)', distinct='Y')

N(id='TOCR-219', name='Handwritten Indic script identification data (offline + online, Bhunia et al. 2018)', version='2018', desc='Character- and word-level handwritten samples in English + 6 Indic scripts (search-indexed text lists Telugu) in offline and online form.',
  url='https://arxiv.org/abs/1802.08568', paper='https://arxiv.org/abs/1802.08568', inst='ISI Kolkata; IIT Roorkee (NOT VERIFIED)',
  authors='Ayan Kumar Bhunia, Subham Mukherjee, Aneeshan Sain, Ankan Kumar Bhunia, Partha Pratim Roy, Umapada Pal', lang='Multilingual (7 scripts; Telugu per search snippet, NOT VERIFIED in abstract)',
  modality='Image + online pen data', task='Script identification', gran='Character / word', rs='Real', count='~10,000 Telugu samples (search snippet; NOT VERIFIED)', unit='samples',
  ann='Script label', ann_type='Script class', lic='UNKNOWN', access_req='Contact authors', access='No release link in paper', ver='UNVERIFIED', cat='Script identification', distinct='UNKNOWN')

N(id='TOCR-220', name='Handwritten script identification text lines (Singh et al., 2020)', version='2020', desc='800 handwritten text lines in Gujarati, Kannada, Malayalam, Oriya, Tamil, Telugu, Urdu and Roman.',
  url='https://arxiv.org/abs/2009.07433', paper='https://arxiv.org/abs/2009.07433', inst='Jadavpur University (NOT VERIFIED)', authors='Pawan Kumar Singh, Iman Chatterjee, Ram Sarkar, Mita Nasipuri',
  lang='Multilingual (8 scripts incl. Telugu)', modality='Image (handwritten lines)', task='Script identification', gran='Line', rs='Real', count='800 lines total; Telugu share UNKNOWN', unit='text lines',
  ann='Script label', ann_type='Script class', lic='UNKNOWN', access_req='Contact authors', access='No release link', ver='UNVERIFIED', cat='Script identification', distinct='UNKNOWN')

# ------------------------------------------------------------------ platform finds (Hugging Face full listing)
N(id='TOCR-221', name='stefania-radu/rendered_wikipedia_te (rendered Telugu Wikipedia text images)', version='2024',
  desc='Telugu Wikipedia text rendered to image patches (PIXEL-style pixel-language-model pre-training); images only, no text column.',
  hf='https://huggingface.co/datasets/stefania-radu/rendered_wikipedia_te', url='https://huggingface.co/datasets/stefania-radu/rendered_wikipedia_te', inst='Individual', authors='stefania-radu',
  modality='Image (rendered text)', task='Pixel-based language model pre-training', gran='Text patch sequence', rs='Synthetic', count='225,693 rows (viewer) / 250,770 (card)', unit='rendered images',
  ann='No', ann_type='None (pixel_values only)', lic='None declared', access_req='None', access='Open (HF, 4.6 GB)', ver='VERIFIED', overlap='Rendered from Telugu Wikipedia text (TOCR-139).',
  cat='Image-only (no transcription)', distinct='Y')

N(id='TOCR-222', name='NayanaIR-MonoBench-te (Telugu visual document retrieval)', version='2025', desc='Telugu monolingual visual document retrieval benchmark: page images, Telugu queries, relevance judgements.',
  hf='https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-MonoBench-te', url='https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-MonoBench-te', inst='Cognitive Lab', authors='Cognitive Lab',
  modality='Image (document pages)', task='Visual document retrieval', gran='Page', rs='UNKNOWN', count='1,000 page images; 200 queries; 293 qrels', unit='page images', ann='Retrieval labels + answers',
  ann_type='Queries, qrels, answers (no transcription)', lic='None declared', access_req='None', access='Open (HF)', ver='VERIFIED', overlap='Same family as TOCR-190 (NayanaIR-CrossBench).',
  cat='Text-in-image benchmark (VQA / document understanding)', distinct='Y')

N(id='TOCR-223', name='Tiny Multilingual CAPTCHA Library - Telugu (remiai3/tiny-captcha-library)', aliases='AtharvImmverse/tiny-captcha-library (copy)', version='2026-01',
  desc='Synthetic 4-character CAPTCHA images with labels for 44 scripts; 10,000 per script.', hf='https://huggingface.co/datasets/remiai3/tiny-captcha-library',
  url='https://huggingface.co/datasets/remiai3/tiny-captcha-library', inst='remiai3', authors='remiai3', lang='Multilingual (44 scripts incl. Telugu)', modality='Image (synthetic CAPTCHAs)',
  task='CAPTCHA / short text recognition', gran='4-character string', rs='Synthetic', count='10,000 Telugu (images.zip 27.4 MB + labels.csv)', unit='images', ann='Yes', ann_type='Text label (labels.csv)',
  lic='CC BY 4.0', comm='Allowed', redis='Allowed', access_req='None', access='Open (HF)', ver='VERIFIED', overlap='Smaller release of the same generator as TOCR-101 (100,000 Telugu).',
  cat='OCR image-text: synthetic', distinct='N (smaller release of TOCR-101 generator)')

# ------------------------------------------------------------------ platform finds (GitHub deep sweep)
N(id='TOCR-224', name='GitHub medini-r/teluguChar (copy of HP Labs offline Telugu characters)', parent='TOCR-021', version='2020',
  desc='45,217 TIFF character images in hpl-telugu-iso-char-offline/usr_* folders.', github='https://github.com/medini-r/teluguChar', url='https://github.com/medini-r/teluguChar',
  inst='Individual', authors='medini-r', modality='Image (characters)', task='Character recognition', gran='Character', rs='Real', count='45,217 images', unit='character images', ann='Yes (file naming)',
  ann_type='Character class in file name', lic='None stated (HP Labs licence applies)', comm='Per HP Labs licence', redis='Not the uploader\'s to grant', access_req='None', access='Open (GitHub)',
  ver='VERIFIED', overlap='Copy of HP Labs offline set (TOCR-021); same count as TOCR-038.', cat='Character / glyph classification', distinct='N (mirror of TOCR-021)')

N(id='TOCR-225', name='GitHub madhav007VDEV/telugu-ocr-realtime - character image set', version='2026', desc='650 images in 13 class folders (50 each) used to train a small Telugu character model.',
  github='https://github.com/madhav007VDEV/telugu-ocr-realtime', url='https://github.com/madhav007VDEV/telugu-ocr-realtime', inst='Individual', authors='madhav007VDEV', modality='Image (characters)',
  task='Character recognition', gran='Character', rs='UNKNOWN', count='650 images (13 classes x 50)', unit='character images', ann='Yes (folder = class index)', ann_type='Class index (mapping to letters NOT VERIFIED)',
  lic='None stated', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED', cat='Character / glyph classification', distinct='Y')

N(id='TOCR-226', name='GitHub ntbnaren7/telugu-fra-synthesizer - synthetic Telugu Forest Rights Act documents', version='2025',
  desc='Generator + 200 rendered Telugu government-form images (FRA claim documents) for document OCR/extraction experiments.',
  github='https://github.com/ntbnaren7/telugu-fra-synthesizer', url='https://github.com/ntbnaren7/telugu-fra-synthesizer', inst='Individual', authors='ntbnaren7',
  modality='Image (synthetic forms)', task='Document OCR / form extraction', gran='Page', rs='Synthetic', count='200 page images (+ fra_telugu_docs.zip, 26.4 MB)', unit='page images',
  ann='Not found (no ground-truth files in repo)', ann_type='None verified', lic='MIT', comm='Allowed', redis='Allowed', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED',
  cat='Image-only (transcription NOT VERIFIED)', distinct='Y', notes='The generator can presumably emit the rendered text; only images are committed.')

N(id='TOCR-227', name='GitHub pavankarthik1/Telugu-Hand-Written-character-recognition - handwritten word images', version='2022',
  desc='112 handwritten Telugu word images (data/words) used with an SimpleHTR-style model.', github='https://github.com/pavankarthik1/Telugu-Hand-Written-character-recognition',
  url='https://github.com/pavankarthik1/Telugu-Hand-Written-character-recognition', inst='Individual', authors='pavankarthik1', modality='Image (handwritten words)', task='Handwritten word recognition',
  gran='Word', rs='Real', count='112 word images', unit='word images', ann='NOT VERIFIED', ann_type='NOT VERIFIED', lic='None stated', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED',
  cat='Image-only (transcription NOT VERIFIED)', distinct='Y')

N(id='TOCR-228', name='GitHub keerthan-381 - Telugu palm-leaf handwritten character crops (DATA_LABELS_FINAL.zip)', version='2023',
  desc='Zip of 9,131 character images from Telugu palm-leaf document images, organised for character classification.',
  github='https://github.com/keerthan-381/HandWritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images',
  url='https://github.com/keerthan-381/HandWritten_Charcater_Classificaition_For_Telugu_Palmleaf_Document_Images', inst='Individual (student project)', authors='keerthan-381',
  modality='Image (palm-leaf characters)', task='Character recognition', gran='Character', rs='Real', count='9,131 images (zip central directory, 8.7 MB)', unit='character images',
  ann='Yes (folder labels, per name)', ann_type='Character class (NOT VERIFIED)', lic='None stated', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED',
  overlap='Same project title as rejected code-only repo TOCR-174; possibly related to TOCR-119 palm-leaf crops.', cat='Character / glyph classification', distinct='Y')

N(id='TOCR-229', name='GitHub aceveggie/TeluguTFRecords - Telugu character data in MNIST format', version='2017',
  desc='Telugu character images stored as MNIST-style idx files and TFRecords (train-images-idx3-ubyte 13.2 MB; t10k files).', github='https://github.com/aceveggie/TeluguTFRecords',
  url='https://github.com/aceveggie/TeluguTFRecords', inst='Individual', authors='aceveggie', modality='Image (characters, idx/TFRecord)', task='Character recognition', gran='Character', rs='UNKNOWN',
  count='UNKNOWN (image size not stated)', unit='character images', ann='Yes (idx label files)', ann_type='Class index', lic='None stated', access_req='None', access='Open (GitHub)',
  ver='PARTIALLY VERIFIED', overlap='Source of the characters NOT VERIFIED (possibly HP Labs TOCR-021).', cat='Character / glyph classification', distinct='UNKNOWN')

N(id='TOCR-230', name='GitHub Saisugandhasri - binarised Telugu character images (contrastive dataset construction)', version='2025',
  desc='Code for an unsupervised contrastive framework to build a Telugu character dataset, with 54 binarised source images and outputs.',
  github='https://github.com/Saisugandhasri/A-novel-unsupervised-contrastive-learning-framework-for-Telugu-script-character-dataset-construction',
  url='https://github.com/Saisugandhasri/A-novel-unsupervised-contrastive-learning-framework-for-Telugu-script-character-dataset-construction', inst='Individual', authors='Saisugandhasri',
  modality='Image (binarised document images)', task='Character dataset construction (clustering)', gran='Page / character', rs='Real', count='54 binarised images (+ outputs.zip 20.7 MB)', unit='images',
  ann='No (unsupervised)', ann_type='Cluster outputs', lic='None stated', access_req='None', access='Open (GitHub)', ver='PARTIALLY VERIFIED', cat='Image-only (no transcription)', distinct='Y')

# ------------------------------------------------------------------ new rejected candidates
for rid, name, url, reason in [
    ('TOCR-231', 'HKS-NVC: Handwritten Kadamba Script numerals, vowels, consonants (IEEE DataPort 10.21227/nhvr-w717)', 'https://doi.org/10.21227/nhvr-w717', 'Kadamba script (ancestor of Kannada-Telugu), not Telugu.'),
    ('TOCR-232', 'GitHub NamineniBrahmani/multilingual-ocr', 'https://github.com/NamineniBrahmani/multilingual-ocr', 'Six scripts (Nandinagari, Malayalam, Kannada, Devanagari, Sarada, Bengali); no Telugu folder.'),
    ('TOCR-233', 'GitHub bitreaper42/DC_Indic scene-text evaluation set', 'https://github.com/bitreaper42/DC_Indic', 'ground_truth.json has only English and Hindi regions.'),
    ('TOCR-234', 'GitHub darshanrao/Ancient-Hand-Writtten-Recognition-Under-Data-Deficiency', 'https://github.com/darshanrao/Ancient-Hand-Writtten-Recognition-Under-Data-Deficiency', 'Tamil and Sanskrit data only.'),
    ('TOCR-235', 'HASOC 2025 multimodal meme task (FIRE 2025)', 'https://ceur-ws.org/Vol-4173/', 'Hindi, Gujarati, Bangla and Bodo memes; no Telugu.'),
    ('TOCR-236', 'Synbols synthetic glyph datasets (ServiceNow)', 'https://github.com/ServiceNow/synbols', 'No Telugu alphabet in the generator (code search 2026-11-11).'),
    ('TOCR-237', 'Tamil handwritten palm-leaf manuscript dataset (THPLMD)', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10864864/', 'Tamil only; surfaces in Telugu palm-leaf searches.'),
    ('TOCR-238', 'Hamburg palm-leaf manuscript word datasets (fdr.uni-hamburg.de)', 'https://b2find.eudat.eu/dataset/f0497ec0-a60f-5710-96b4-2bf9adef6f56', 'Tamil manuscripts; no Telugu.'),
    ('TOCR-239', 'IIST BCI Telugu datasets (EEG; IEEE DataPort)', 'https://doi.org/10.21227/32qq-c421', 'Brain-signal recordings of Telugu speech/commands, not images.'),
]:
    N(id=rid, name=name, url=url, desc='Rejected candidate - see notes.', inst='See source', modality='See notes', task='See notes', gran='Not applicable', rs='Not applicable',
      count='Not applicable', unit='Not applicable', ann='Not applicable', ann_type='Not applicable', access='See notes', ver='REJECTED', cat='Rejected', distinct='N', notes=reason,
      changed3='New in round 3 (rejected)')


# ------------------------------------------------------------------ corrections to earlier rows
def _set(rec, change, **kw):
    for k, v in kw.items():
        if k == 'notes' and rec.get('notes'):
            v = rec['notes'] + ' ' + v
        rec[k] = v
    rec['changed3'] = change if rec['changed3'] == 'NONE' else rec['changed3'] + '; ' + change


def apply(rows):
    by = {r['id']: r for r in rows}
    _set(by['TOCR-009'], 'Links re-checked', access='Telugu zips redirect to cdn.iiit.ac.in and return HTTP 404 (re-checked 2026-11-11); charlist zip still downloads')
    _set(by['TOCR-018'], 'Related repo found', notes='Same author has JayanthKalluri/TeluguSentenceRecognizer (handwritten sentence OCR; ground_truth.txt and model only, no images).')
    _set(by['TOCR-021'], 'LipiTk index page added', aliases=by['TOCR-021']['aliases'] + '; LipiTk HP Labs datasets index https://lipitk.sourceforge.net/hpl-datasets.htm (MILE Lab, IISc hosts downloads)')
    _set(by['TOCR-027'], 'Working landing page and size found', url='https://ieee-dataport.org/node/1880',
         count='516 samples (listing states 463 train / 103 test - figures do not add up)', access='DOI target 404s but ieee-dataport.org/node/1880 resolves (301) to the listing; login needed for files',
         ver='GATED')
    _set(by['TOCR-038'], 'Identified as compilation', overlap='45,217 characters = HP Labs offline Telugu set count (TOCR-021, also copied in TOCR-224); 3,000 numerals = CMATERdb Telugu (TOCR-032).',
         distinct='N (compilation of TOCR-021 + TOCR-032)')
    _set(by['TOCR-041'], 'Internal page set noted', notes='Mozhi crops come from ~1,000 internally scanned pages per language; the full pages were not released.')
    _set(by['TOCR-047'], 'Size from paper abstract', count='~70,000 samples in 325 classes with train/val/test split (paper abstract via search index; NOT VERIFIED against data)')
    _set(by['TOCR-106'], 'Related repo found', aliases='chaitusvk/telugu_ocr_flask (116 labelled test line images: tel_ocr_test_imgs + te_test_labels.txt)')
    _set(by['TOCR-108'], 'Conflicting descriptions recorded', quality='DataCite abstract repeats the 17,387-class description; search engines describe the listing as ~100 handwritten shopping-list photos with a ~17 KB file. Contents NOT VERIFIED.')
    _set(by['TOCR-113'], 'IEEE DataPort copies noted', aliases='MDIW-13 MultiScript Document Database (IEEE DataPort 10.21227/41ff-fm88, 10.21227/656q-hc18)')
    _set(by['TOCR-174'], 'Related repo found', overlap='Sibling project keerthan-381 (TOCR-228) with the same title does publish 9,131 palm-leaf character images.')
