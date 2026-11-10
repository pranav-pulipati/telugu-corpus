"""Source registry for the unified Telugu OCR corpus.

Every source yields records (key, image_bytes, raw_text, orig_split, group_id) from the ORIGINAL downloads
under ocr/acquisition/data/ (zip members, extracted files or parquet rows). Nothing here modifies the originals.

key       stable id inside the source (zip member path, file path or row id)
group_id  the original document unit used for leakage-safe splitting (page, book, scene, video sequence ...)
"""
import io, json, os, re, zipfile, glob
import pyarrow.parquet as pq

DATA = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))


def _zip_gt(zpath, gt_member, img_prefix, sep='\t'):
    z = zipfile.ZipFile(zpath)
    for line in z.read(gt_member).decode('utf-8-sig').splitlines():
        if not line.strip():
            continue
        p, t = line.split(sep, 1) if sep in line else (line, '')
        yield p.strip(), t, z, img_prefix + p.strip()


def mozhi():
    for s in ['train', 'val', 'test']:
        zp = f'{DATA}/ilocr_mozhi_telugu_official/zips/{s}.zip'
        for p, t, z, m in _zip_gt(zp, f'{s}/{s}_gt.txt', f'{s}/'):
            book_page = re.match(r'images/(\d+)-(\d+)_', p)
            yield m, z.read(m), t, s, 'book:' + book_page.group(1), {'page': book_page.group(1) + '-' + book_page.group(2)}


def hw_words():
    for s in ['train', 'val', 'test']:
        zp = f'{DATA}/ilocr_hw_words_telugu/zips/{s}.zip'
        for p, t, z, m in _zip_gt(zp, f'{s}/{s}_gt.txt', f'{s}/'):
            parts = p.split('/')  # images/<a>/<b>/<n>.jpg
            yield m, z.read(m), t, s, f'form:{parts[1]}/{parts[2]}', {'a': parts[1]}


def ihwwr():
    zp = f'{DATA}/ilocr_ihwwr1_telugu/zips/Word_Level_Telugu_Training_Set.zip'
    z = zipfile.ZipFile(zp)
    for part in '12':
        base = f'Word_Level_Training_Set/Word_Level_Training_Set{part}/'
        for line in z.read(base + f'train{part}.txt').decode('utf-8-sig').splitlines():
            if '\t' not in line:
                continue
            p, t = line.split('\t', 1)
            page = os.path.basename(p).rpartition('_')[0]
            yield base + p, z.read(base + p), t, 'train', 'hwpage:' + page, {}


def hw_uc():
    zp = f'{DATA}/cvit_hw_uc_telugu/zips/telugu.zip'
    z = zipfile.ZipFile(zp)
    names = set(z.namelist())
    seen = set()
    for s in ['train', 'val', 'test']:
        for line in z.read(f'telugu/file/{s}_gt.txt').decode('utf-8-sig').splitlines():
            if '\t' not in line:
                continue
            p, t = line.split('\t', 1)
            m = 'telugu/' + p
            if m not in names:
                continue
            seen.add(m)
            yield m, z.read(m), t, s, _hwuc_group(p), {'folder': p.split('/')[0]}
    # labelled words in the manually annotated folders that are not in the official splits
    for gt in sorted(n for n in names if n.startswith('telugu/2_New_Manually_Annotated/') and n.endswith('/gt.txt')):
        base = gt.rsplit('/', 1)[0] + '/'
        for line in z.read(gt).decode('utf-8-sig').splitlines():
            if '\t' not in line:
                continue
            p, t = line.split('\t', 1)
            m = base + p
            if m in seen or m not in names:
                continue
            seen.add(m)
            yield m, z.read(m), t, 'unsplit', _hwuc_group(m[len('telugu/'):]), {'folder': m.split('/')[1]}


def _hwuc_group(p):
    b = os.path.basename(p)
    if '_' in b:  # <pageid>_<word>.jpg  (same page-id space as IHWWR / PLHWTR)
        return 'hwpage:' + b.rpartition('_')[0]
    # numeric crop ids without page information: bucket consecutive ids (documented approximation).
    # Ids are sparse (part_2 ~1 crop per 11 ids, part_1 ~1 per 100), a 40-word page spans ~440 / ~4,000 ids,
    # so buckets of 10,000 / 50,000 ids keep most pages whole (est. 4-8% of pages straddle a bucket edge).
    n = int(re.sub(r'\D', '', b) or 0)
    width = 50_000 if '1_part_1' in p else 10_000
    return f'hwucbucket:{p.split("/")[1] if p.startswith("2_New") else p.split("/")[0]}/{n // width}'


def wirindic():
    zps = {s: zipfile.ZipFile(f'{DATA}/ilocr_wirindic_telugu/zips/{s}.zip') for s in ['train', 'val']}
    for s, z in zps.items():
        ims = z.read(f'{s}/{s}_images.txt').decode('utf-8-sig').split()
        lbs = z.read(f'{s}/{s}_labels.txt').decode('utf-8-sig').splitlines()
        assert len(ims) == len(lbs)
        for p, t in zip(ims, lbs):
            seq = re.search(r'(\d+_[LR]_GH\d+)_image', p).group(1)
            yield p, z.read(p), t, s, 'video:' + seq, {'frame': re.search(r'(\d+_[LR]_GH\d+_image_\d+)', p).group(1)}


def bstd():
    root = f'{DATA}/bstd_telugu_recognition/extracted'
    for s in ['train', 'test']:
        d = json.load(open(f'{root}/Recognition/{s}_recognition_data.json', encoding='utf-8'))
        for k, v in sorted(d.items()):
            if v.get('language') != 'telugu':
                continue
            yield v['path'], open(f'{root}/{v["path"]}', 'rb').read(), v.get('text') or '', s, 'scene:' + re.sub(r'_\d+\.jpg$', '', k), {}


def indicstr12():
    import hashlib
    mirror = {}
    for s in ['train', 'validation', 'test']:
        for r in pq.read_table(f'{DATA}/hf_darknight054_indicstr12_crops_telugu/{s}.parquet', columns=['image', 'text']).to_pylist():
            mirror[hashlib.md5(r['image']['bytes']).hexdigest()] = r['text']
    for s in ['train', 'test']:
        zp = f'{DATA}/ilocr_indicstr12_telugu/zips/{s}.zip'
        for p, t, z, m in _zip_gt(zp, f'{s}/{s}_gt.txt', f'{s}/'):
            b = z.read(m)
            mt = mirror.get(hashlib.md5(b).hexdigest())
            label, src = t, 'ilocr_v0.5'
            if mt is not None and mt != t and '"' not in mt:   # mirror (CVIT real.zip) carries corrected labels
                label, src = mt, 'cvit_real_zip_correction'
            yield m, b, label, s, 'scene:' + os.path.basename(p).split('_')[0], {'label_source': src, 'original_label': t}


def _parquet(path, text_col, split):
    t = pq.read_table(path, columns=['image', text_col] + (['image_name'] if 'sarvam' in path else []))
    for i, r in enumerate(t.to_pylist()):
        key = r.get('image_name') or f'{os.path.basename(path)}#{i}'
        yield key, r['image']['bytes'], r[text_col] or '', split, 'evalitem:' + key, {}


def sarvam():
    yield from _parquet(f'{DATA}/hf_sarvam_indic_ocr_bench_telugu/test_telugu.parquet', 'gt', 'test')


def indicdlp_sample():
    yield from _parquet(f'{DATA}/hf_onath_indicdlp_eval_sample_telugu/Telugu.parquet', 'text', 'test')


def _syn(folder, splits, gt_name):
    for s in splits:
        zp = f'{DATA}/{folder}/zips/{s}.zip'
        z = zipfile.ZipFile(zp)
        gt = [n for n in z.namelist() if n.endswith(gt_name.format(s=s))][0]
        base = gt.rsplit('/', 1)[0] + '/'
        for line in z.read(gt).decode('utf-8-sig').splitlines():
            if '\t' not in line:
                continue
            p, t = line.split('\t', 1)
            yield base + p, z.read(base + p), t, s, 'synthetic', {}


def syn_m():
    yield from _syn('ilocr_synthetic_m_telugu', ['train'], '{s}_gt.txt')


def syn_r():
    yield from _syn('ilocr_synthetic_r_telugu', ['train', 'val', 'test'], '{s}_gt.txt')


def syn_str():
    yield from _syn('ilocr_synthetic_indicstr_telugu', ['train', 'val', 'test'], '{s}_gt.txt')


def wikisource():
    root = f'{DATA}/wikisource_pages'
    imgs = {}
    if not os.path.exists(f'{root}/images.jsonl'):   # page images not fetched yet -> no pairs (texts alone are not OCR data)
        return
    for line in open(f'{root}/images.jsonl', encoding='utf-8'):
        r = json.loads(line)
        if r.get('ok'):
            imgs[r['title']] = r
    files = json.load(open(f'{root}/files.json'))
    for line in open(f'{root}/texts.jsonl', encoding='utf-8'):
        r = json.loads(line)
        im = imgs.get(r['title'])
        if not im:
            continue
        yield r['title'], open(f'{root}/images/{im["image"]}', 'rb').read(), r['wikitext'], 'unsplit', 'book:' + im['file'], \
            {'level': r['level'], 'revid': r['revid'], 'scan_licence': files[im['file']]['licence']}


# ---------------------------------------------------------------------------------------------
# source_id: (loader, collection, granularity, label_type, licence, licence_status, redistributable, role, provenance URL)
SOURCES = {
    'mozhi_telugu':        (mozhi, 'printed', 'word', 'human', 'CC BY 4.0', 'stated on every other-language Mozhi page; Telugu page broken', True, 'train+eval', 'https://ilocr.iiit.ac.in/public/printed/phase-0/v0.5/telugu/akshara/'),
    'sarvam_ocr_bench_te': (sarvam, 'printed', 'block', 'human_double_reviewed', 'Apache-2.0', 'HF licence tag', True, 'eval_only', 'https://huggingface.co/datasets/sarvamai/indic-ocr-bench'),
    'indicdlp_eval_sample_te': (indicdlp_sample, 'printed', 'block', 'human', 'CC BY 4.0', 'HF licence tag', True, 'eval_only', 'https://huggingface.co/datasets/onath/indicdlp-eval-set-22-sample'),
    'wikisource_te_pages': (wikisource, 'printed', 'page', 'human_proofread', 'Text CC BY-SA 4.0; scan licence per file', 'per-file Commons/Wikisource licence checked', True, 'train+eval', 'https://te.wikisource.org/'),
    'hw_uc_telugu':        (hw_uc, 'handwritten', 'word', 'human', 'not stated', 'NOT CONFIRMED - research use pending confirmation', False, 'train+eval', 'https://cvit.iiit.ac.in/usodi/ucciohd.php'),
    'ihwwr1_telugu':       (ihwwr, 'handwritten', 'word', 'human', 'not stated', 'competition data, no licence on page', False, 'train+eval', 'https://ilocr.iiit.ac.in/icdar_2024_hwd/dataset.html'),
    'hw_words_telugu':     (hw_words, 'handwritten', 'word', 'human', 'CC BY 4.0', 'stated on dataset page', True, 'train+eval', 'https://ilocr.iiit.ac.in/dataset/23/'),
    'wirindic_telugu':     (wirindic, 'scene_text', 'word', 'human', 'not stated', 'competition data, no licence on page', False, 'train+eval', 'https://ilocr.iiit.ac.in/icpr_2024_wirindic/dataset.html'),
    'bstd_telugu':         (bstd, 'scene_text', 'word', 'human', 'Apache-2.0', 'repository licence (no separate data licence)', True, 'train+eval', 'https://github.com/Bhashini-IITJ/BharatSceneTextDataset'),
    'indicstr12_telugu':   (indicstr12, 'scene_text', 'word', 'human', 'CC BY 4.0 (annotations)', 'stated on dataset page; images crawled from the web (third-party copyright)', False, 'train+eval', 'https://ilocr.iiit.ac.in/dataset/36/'),
    'synthetic_m_telugu':  (syn_m, 'synthetic', 'word', 'synthetic_exact', 'not stated', 'no licence section on any IIIT-Synthetic page; page says pre-training only', False, 'pretrain', 'https://ilocr.iiit.ac.in/dataset/40/'),
    'synthetic_r_telugu':  (syn_r, 'synthetic', 'word', 'synthetic_exact', 'not stated', 'no licence section on any IIIT-Synthetic page', False, 'pretrain', 'https://ilocr.iiit.ac.in/dataset/55/'),
    'synthetic_indicstr_telugu': (syn_str, 'synthetic', 'word', 'synthetic_exact', 'not stated', 'no licence section on any IIIT-Synthetic page', False, 'pretrain', 'https://ilocr.iiit.ac.in/dataset/68/'),
}
