"""Re-count and check every Telugu OCR dataset downloaded into ocr/acquisition/data/.

Writes:
  ocr/acquisition/VERIFIED_DOWNLOADS.csv   one row per dataset split actually on disk
  ocr/acquisition/samples/<dataset>/       up to 8 image+label pairs per dataset (redistributable licences only)
  ocr/acquisition/scripts/_verify_stats.json  quality numbers used in SAMPLE_INSPECTION_REPORT.md

Run with an environment that has pillow + pyarrow:
  python -I ocr/acquisition/scripts/verify_downloads.py
"""
import csv, hashlib, io, json, os, random, re, shutil, statistics, sys, unicodedata, collections
from PIL import Image
import pyarrow.parquet as pq

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA = os.path.join(ROOT, 'data')
SAMPLES = os.path.join(ROOT, 'samples')
TODAY = '2026-11-10'
random.seed(2026)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def tel_frac(s):
    s = [c for c in s if not c.isspace()]
    return sum(0x0C00 <= ord(c) <= 0x0C7F for c in s) / len(s) if s else 0.0


def read_tsv(path, sep='\t'):
    out = []
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n').rstrip('\r')
        if not line.strip():
            continue
        if sep in line:
            p, t = line.split(sep, 1)
        else:
            p, t = line, ''
        out.append((p, t.strip()))
    return out


# ---- loaders: each yields (split, label, image_path_or_None, image_bytes_or_None) ----

def ilocr_gt(base, splits, gtname='{s}/{s}_gt.txt', imgroot='{s}'):
    for s in splits:
        for p, t in read_tsv(os.path.join(base, gtname.format(s=s))):
            yield s, t, os.path.join(base, imgroot.format(s=s), p), None


def wirindic(base):
    for s in ['train', 'val']:
        ims = open(os.path.join(base, f'{s}/{s}_images.txt'), encoding='utf-8').read().split()
        lbs = open(os.path.join(base, f'{s}/{s}_labels.txt'), encoding='utf-8').read().splitlines()
        assert len(ims) == len(lbs), (s, len(ims), len(lbs))
        for p, t in zip(ims, lbs):
            yield s, t.strip(), os.path.join(base, p), None


def ihwwr(base):
    for part in ['1', '2']:
        d = os.path.join(base, f'Word_Level_Training_Set/Word_Level_Training_Set{part}')
        for p, t in read_tsv(os.path.join(d, f'train{part}.txt')):
            yield 'train', t, os.path.join(d, p), None


def parquet_rows(base, files, text_col, img_col='image'):
    for split, f in files:
        fp = os.path.join(base, f)
        for r in pq.read_table(fp, columns=[img_col, text_col]).to_pylist():
            yield split, (r[text_col] or '').strip(), None, r[img_col]['bytes']


def scene_full(base):
    for split, f in [('train', 'train.parquet'), ('val', 'validation.parquet'), ('test', 'test.parquet')]:
        for r in pq.read_table(os.path.join(base, f), columns=['image', 'text']).to_pylist():
            t = r['text']
            if isinstance(t, str) and t.startswith('['):
                t = ' '.join(re.findall(r"'([^']*)'", t))
            yield split, t, None, r['image']['bytes']


def bstd(base):
    root = os.path.join(base, 'extracted')
    for s in ['train', 'test']:
        d = json.load(open(os.path.join(root, f'Recognition/{s}_recognition_data.json'), encoding='utf-8'))
        for v in d.values():
            if v.get('language') == 'telugu':
                yield s, (v.get('text') or '').strip(), os.path.join(root, v['path']), None


def wikisource(base):
    for f in sorted(os.listdir(base)):
        if f.endswith('.txt'):
            yield 'sample', open(os.path.join(base, f), encoding='utf-8').read().strip(), os.path.join(base, f[:-4] + '.jpg'), None


# name, folder, loader, category, licence, origin, new_to_catalogue, archives(glob-ish list relative to folder), sample_ok
D = [
    dict(id='ACQ-01', name='WIRIndic-Telugu (ICPR 2024 scene-text word recognition)', folder='ilocr_wirindic_telugu',
         load=lambda b: wirindic(os.path.join(b, 'extracted')), category='scene_text', licence='CC BY 4.0 (ILOCR / Bhashini data policy)',
         url='https://ilocr.iiit.ac.in/icpr_2024_wirindic/dataset.html', new='Yes', unlabelled={'test': 5000}),
    dict(id='ACQ-02', name='IHWWR-1.0 Telugu training set (ICDAR 2024 handwritten words)', folder='ilocr_ihwwr1_telugu',
         load=lambda b: ihwwr(os.path.join(b, 'extracted')), category='handwritten_ocr', licence='CC BY 4.0 (ILOCR / Bhashini data policy)',
         url='https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html', new='Yes (but same pages as IIIT-Indic-HW-UC, see overlap report)'),
    dict(id='ACQ-03', name='Bharat Scene Text Dataset (BSTD) - Telugu cropped words', folder='bstd_telugu_recognition',
         load=bstd, category='scene_text', licence='Apache-2.0 (GitHub repo licence); dataset terms not separately stated',
         url='https://github.com/Bhashini-IITJ/BharatSceneTextDataset', new='Yes'),
    dict(id='ACQ-04', name='Sarvam Indic OCR Bench - Telugu rows (test)', folder='hf_sarvam_indic_ocr_bench_telugu',
         load=lambda b: parquet_rows(b, [('test', 'test_telugu.parquet')], 'gt'), category='printed_ocr', licence='Apache-2.0 (HF tag)',
         url='https://huggingface.co/datasets/sarvamai/indic-ocr-bench', new='Yes'),
    dict(id='ACQ-05', name='IndicDLP block-level OCR eval set - public Telugu sample', folder='hf_onath_indicdlp_eval_sample_telugu',
         load=lambda b: parquet_rows(b, [('Telugu', 'Telugu.parquet')], 'text'), category='printed_ocr', licence='CC BY 4.0 (HF tag)',
         url='https://huggingface.co/datasets/onath/indicdlp-eval-set-22-sample', new='Yes (10-row public sample of a private set)'),
    dict(id='ACQ-06', name='IIIT-Synthetic-M-Telugu (synthetic printed words)', folder='ilocr_synthetic_m_telugu',
         load=lambda b: ilocr_gt(os.path.join(b, 'extracted'), ['train']), category='synthetic', licence='CC BY 4.0 (ILOCR / Bhashini data policy); page says pre-training use only',
         url='https://ilocr.iiit.ac.in/dataset/40/', new='Yes'),
    dict(id='ACQ-07', name='Mozhi-Telugu printed words (HF mirror darknight054/indic-mozhi-ocr, verified against official test split)', folder='hf_darknight054_mozhi_telugu',
         load=lambda b: parquet_rows(b, [('train', 'train.parquet'), ('val', 'validation.parquet'), ('test', 'test.parquet')], 'text'),
         category='printed_ocr', licence='Official source: ILOCR/Bhashini CC BY 4.0 policy; mirror declares no licence',
         url='https://huggingface.co/datasets/darknight054/indic-mozhi-ocr', new='No - already catalogued as TEL-OCR-001 (newly acquired, not a new source)'),
    dict(id='ACQ-08', name='Mozhi-Telugu official test split (ILOCR akshara/test.zip)', folder='ilocr_mozhi_telugu_official',
         load=lambda b: ilocr_gt(os.path.join(b, 'extracted'), ['test']), category='printed_ocr', licence='CC BY 4.0 (ILOCR / Bhashini data policy)',
         url='https://ilocr.iiit.ac.in/public/printed/phase-0/v0.5/telugu/akshara/test.zip', new='No - identical to ACQ-07 test split (used only to verify the mirror)', count='No', sample=False),
    dict(id='ACQ-09', name='IndicSTR12-Telugu real scene-text words (ILOCR v0.5)', folder='ilocr_indicstr12_telugu',
         load=lambda b: ilocr_gt(os.path.join(b, 'extracted'), ['train', 'test']), category='scene_text', licence='CC BY 4.0 on annotations (ILOCR policy); images crawled from Google Images - third-party copyright',
         url='https://ilocr.iiit.ac.in/dataset/36/', new='No - catalogued as TEL-OCR-003; also near-duplicate of IIIT-ILST Telugu', sample=False),
    dict(id='ACQ-10', name='IndicSTR12 crops Telugu (HF mirror darknight054/indicstr12-crops)', folder='hf_darknight054_indicstr12_crops_telugu',
         load=lambda b: parquet_rows(b, [('train', 'train.parquet'), ('val', 'validation.parquet'), ('test', 'test.parquet')], 'text'),
         category='scene_text', licence='None declared (mirror of CVIT real.zip)', url='https://huggingface.co/datasets/darknight054/indicstr12-crops',
         new='No - same 1,183 images as ACQ-09 with 87 corrected labels', count='No', sample=False),
    dict(id='ACQ-12', name='IndicSTR12 full scene images Telugu with word boxes (HF mirror darknight054/indicstr12-full)', folder='hf_darknight054_indicstr12_full_telugu',
         load=lambda b: ((s, ' '.join(t) if isinstance(t, list) else (t or ''), p, im) for s, t, p, im in scene_full(b)),
         category='scene_text', licence='None declared (mirror of CVIT real.zip); images crawled from Google Images',
         url='https://huggingface.co/datasets/darknight054/indicstr12-full', new='No - source scenes of ACQ-09/ACQ-10 (detection boxes + text)', count='No', sample=False),
    dict(id='ACQ-11', name='Telugu Wikisource validated pages - 6-page probe', folder='wikisource_validated_pages_sample',
         load=wikisource, category='printed_ocr', licence='Text CC BY-SA 4.0; scans PD/free per Commons file page (check per book)',
         url='https://te.wikisource.org/wiki/వర్గం:ఆమోదించబడ్డవి', new='No - part of TEL-LIT-001 (probe only)', count='No'),
]


def scan(ds):
    base = os.path.join(DATA, ds['folder'])
    rows = list(ds['load'](base))
    splits = collections.Counter(r[0] for r in rows)
    missing = empty = latin = pure = nonnfc = unreadable = 0
    md5 = collections.Counter(); labels = collections.Counter(); ws = []; hs = []; lens = []
    good = []
    step = max(1, len(rows) // 3000)
    for i, (s, t, p, b) in enumerate(rows):
        if b is None:
            if not p or not os.path.exists(p):
                missing += 1
                continue
            b = open(p, 'rb').read()
        md5[hashlib.md5(b).hexdigest()] += 1
        if i % step == 0:
            try:
                im = Image.open(io.BytesIO(b)); ws.append(im.width); hs.append(im.height)
            except Exception:
                unreadable += 1
        if not t:
            empty += 1
            continue
        good.append((s, t, p, b))
        labels[t] += 1; lens.append(len(t))
        latin += bool(re.search('[A-Za-z]', t))
        pure += tel_frac(t) >= 0.999
        nonnfc += unicodedata.normalize('NFC', t) != t
    st = dict(id=ds['id'], dataset=ds['name'], pairs_listed=len(rows), labelled_pairs=len(good), splits=dict(splits),
              missing_images=missing, empty_labels=empty, unreadable_in_sample=unreadable,
              duplicate_images=sum(v - 1 for v in md5.values() if v > 1), unique_labels=len(labels),
              labels_with_latin=latin, pure_telugu_labels=pure, non_nfc_labels=nonnfc,
              median_label_chars=statistics.median(lens) if lens else None,
              median_img_w=statistics.median(ws) if ws else None, median_img_h=statistics.median(hs) if hs else None,
              top_labels=labels.most_common(5))
    return st, good


def write_samples(ds, good):
    out = os.path.join(SAMPLES, ds['folder'])
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    pick = random.sample(good, min(8, len(good)))
    with open(os.path.join(out, 'labels.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['file', 'split', 'label', 'source', 'licence'])
        for k, (s, t, p, b) in enumerate(pick):
            if b is None:
                b = open(p, 'rb').read()
            ext = (os.path.splitext(p)[1] if p else '') or '.' + (Image.open(io.BytesIO(b)).format or 'png').lower().replace('jpeg', 'jpg')
            name = f'{k:02d}{ext}'
            open(os.path.join(out, name), 'wb').write(b)
            w.writerow([name, s, t.replace('\n', ' / ')[:2000], ds['url'], ds['licence']])


def main():
    stats = []; vrows = []
    for ds in D:
        base = os.path.join(DATA, ds['folder'])
        if not os.path.isdir(base):
            print('missing folder', base); continue
        st, good = scan(ds)
        stats.append(st)
        print(json.dumps({k: st[k] for k in ['id', 'pairs_listed', 'labelled_pairs', 'splits', 'missing_images', 'empty_labels', 'duplicate_images']}, ensure_ascii=False))
        if ds.get('sample', True):
            write_samples(ds, good)
        files = []
        for r, _, fs in os.walk(base):
            if os.sep + 'extracted' in r:
                continue
            files += [os.path.join(r, f) for f in fs if f.endswith(('.zip', '.parquet', '.json', '.jpg', '.txt'))]
        if 'extracted' in os.listdir(base) and ds['folder'] == 'bstd_telugu_recognition':
            files = [os.path.join(base, 'extracted/Recognition/train_recognition_data.json'), os.path.join(base, 'extracted/Recognition/test_recognition_data.json')]
        if ds['folder'] == 'wikisource_validated_pages_sample':
            files = [os.path.join(base, '_index.json')]
        byspl = collections.Counter(s for s, *_ in good)
        for s, n in sorted(st['splits'].items()):
            vrows.append(dict(acq_id=ds['id'], dataset=ds['name'], category=ds['category'], split=s,
                              images_on_disk=n, labelled_pairs=byspl.get(s, 0),
                              counts_as_new_data=ds.get('count', 'Yes') if ds['new'].startswith('Yes') else 'No',
                              new_to_catalogue=ds['new'], licence=ds['licence'], source_url=ds['url'],
                              local_path=os.path.relpath(base, os.path.dirname(ROOT)), download_date=TODAY,
                              files_sha256='; '.join(f'{os.path.relpath(f, base)}={sha256(f)[:16]}' for f in sorted(files)[:6]),
                              total_bytes=sum(os.path.getsize(f) for f in files)))
        for s, n in ds.get('unlabelled', {}).items():
            vrows.append(dict(acq_id=ds['id'], dataset=ds['name'], category=ds['category'], split=s + ' (no labels released)',
                              images_on_disk=n, labelled_pairs=0, counts_as_new_data='No (unlabelled)', new_to_catalogue=ds['new'],
                              licence=ds['licence'], source_url=ds['url'], local_path=os.path.relpath(base, os.path.dirname(ROOT)),
                              download_date=TODAY, files_sha256='', total_bytes=''))
    json.dump(stats, open(os.path.join(ROOT, 'scripts', '_verify_stats.json'), 'w'), ensure_ascii=False, indent=1)
    with open(os.path.join(ROOT, 'VERIFIED_DOWNLOADS.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(vrows[0]))
        w.writeheader(); w.writerows(vrows)


if __name__ == '__main__':
    main()
