"""Build the unified, cleaned, leakage-safe Telugu OCR corpus.

Stages (run in order; each writes under ocr/acquisition/data/corpus_work/ or data/unified/):
  scan   <source|all>  decode every image, normalise every label, record QA facts  -> corpus_work/meta/<source>.parquet
  assign               drop rules, duplicate removal, cross-source overlap, grouped splits -> corpus_work/assignments.parquet
  export <source|all>  write kept samples to data/unified/<collection>/<split>/<source>-NNNNN.parquet (+ sha256)
  report               aggregate statistics -> scripts/_corpus_stats.json (used by the markdown reports)

Originals are never modified. Every dropped or changed sample keeps a reason code in the assignments table.
Requires pillow + pyarrow. Run with:  python -I ocr/acquisition/scripts/build_corpus.py scan all
"""
import hashlib, io, json, os, re, sys, unicodedata, collections, statistics
from multiprocessing import Pool
import pyarrow as pa, pyarrow.parquet as pq, pyarrow.compute
from PIL import Image, ImageOps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus_sources import SOURCES, DATA  # noqa: E402

WORK = os.path.join(DATA, 'corpus_work')
OUT = os.path.join(DATA, 'unified')
Image.MAX_IMAGE_PIXELS = 200_000_000

# ------------------------------------------------------------------ text normalisation
TEL_LETTER = 'ఁ-౥'          # Telugu signs + letters (excludes Telugu digits U+0C66-0C6F)
ZW = dict.fromkeys(map(ord, '​‌‍﻿­⁠'), None)
PLACEHOLDERS = {'NA', 'N/A', 'na', '#', '###', 'null', 'NULL', 'None'}


def strip_wikitext(w):
    """Wikisource page wikitext -> plain text (header/footer noinclude blocks removed)."""
    t = re.sub(r'<noinclude>.*?</noinclude>', '', w, flags=re.S)
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.sub(r'<ref[^>]*?/>|<ref[^>]*>.*?</ref>', '', t, flags=re.S)
    t = re.sub(r'\[\[(?:File|Image|దస్త్రం|బొమ్మ):[^\]]*\]\]', '', t)
    t = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', t)
    for _ in range(6):  # innermost templates first
        def tpl(m):
            # keep the last positional argument (the visible text of formatting templates); drop named args
            parts = [p for p in m.group(1).split('|')[1:] if not re.match(r'^\s*[\w -]+\s*=', p)]
            return parts[-1] if parts else ''
        t2 = re.sub(r'\{\{([^{}]*)\}\}', tpl, t)
        if t2 == t:
            break
        t = t2
    t = re.sub(r'^\s*\{\|.*$|^\s*\|\}.*$|^\s*\|-.*$', '', t, flags=re.M)                 # table syntax
    t = re.sub(r'^\s*[|!]\s*(?:[^|\n]*\|(?!\|))?', '', t, flags=re.M)                     # table cells
    t = re.sub(r'<br\s*/?>', '\n', t, flags=re.I)
    t = re.sub(r'</?[a-zA-Z][^>]*>', '', t)
    t = t.replace("'''", '').replace("''", '')
    t = re.sub(r'__[A-Z]+__', '', t)
    return t


def normalise(raw, granularity, source):
    """Return (text, changes:list[str])."""
    changes = []
    t = raw if raw is not None else ''
    if source == 'wikisource_te_pages':
        t = strip_wikitext(t); changes.append('wikitext_stripped')
    if '\\n' in t:
        t = t.replace('\\n', '\n'); changes.append('literal_backslash_n')
    t2 = t.translate(ZW)
    if t2 != t:
        changes.append('zero_width_removed'); t = t2
    t2 = t.replace(' ', ' ').replace('\t', ' ')
    t2 = unicodedata.normalize('NFC', t2)
    if t2 != t.replace(' ', ' ').replace('\t', ' '):
        changes.append('nfc')
    t = t2
    t2 = re.sub(f'(?<=[{TEL_LETTER}])౦', 'ం', t)     # Telugu digit zero used as anusvara
    if t2 != t:
        changes.append('digit_zero_to_anusvara'); t = t2
    if granularity == 'word':
        t2 = re.sub(r'\s+', ' ', t).strip()
    else:
        t2 = '\n'.join(re.sub(r'[ ]+', ' ', ln).strip() for ln in t.splitlines())
        t2 = re.sub(r'\n{3,}', '\n\n', t2).strip()
    if t2 != t:
        changes.append('whitespace'); t = t2
    # NB: quotation marks are kept - printed word crops really contain them (checked on Mozhi/Synthetic-M images)
    return t, changes


def text_flags(t):
    f = []
    if '�' in t:
        f.append('replacement_char')
    has_tel = bool(re.search('[ఀ-౿]', t))
    has_lat = bool(re.search('[A-Za-z]', t))
    has_dig = bool(re.search(r'[0-9౦-౯]', t))
    if not has_tel and not has_lat and not has_dig and t:
        f.append('punctuation_only')
    if has_dig and not has_tel and not has_lat:
        f.append('digits_only')
    if has_lat:
        f.append('latin')
    if re.search('్ర్[క-హ]', t):
        f.append('legacy_ra_order')           # e.g. స్ర్తీ written for స్త్రీ (flag only)
    if re.search('్్|[ా-ౌ][ా-ౌ]', t):
        f.append('invalid_sign_sequence')
    if re.search('[^ఀ-౿ -~\n।॥‘’“”–—…°₹]', t):
        f.append('unexpected_chars')
    return f


def akshara_count(t):
    # base letters (independent vowels + consonants not followed by virama) + Latin letters/digits
    n = len(re.findall('[అ-ఔ]|[క-హ](?!్)', t))
    return n + len(re.findall(r'[A-Za-z0-9౦-౯]', t))


# ------------------------------------------------------------------ image QA (runs in worker processes)
def qa_image(args):
    key, b = args
    r = dict(key=key, src_bytes=len(b), src_md5=hashlib.md5(b).hexdigest())
    try:
        im = Image.open(io.BytesIO(b)); fmt = im.format
        exif_rot = 0
        try:
            exif_rot = im.getexif().get(274, 1) or 1
        except Exception:
            pass
        im.load()
        r.update(fmt=fmt, mode=im.mode, width=im.width, height=im.height, exif_orientation=int(exif_rot))
        g = im.convert('L')
        px = g.resize((min(g.width, 256), min(g.height, 256)))
        st = px.getextrema()
        hist = px.histogram(); n = sum(hist); mean = sum(i * c for i, c in enumerate(hist)) / n
        r['pixel_std'] = round((sum(c * (i - mean) ** 2 for i, c in enumerate(hist)) / n) ** 0.5, 2)
        r['pixel_range'] = st[1] - st[0]
        d = g.resize((9, 8)); p = list(d.tobytes())
        r['dhash'] = int(''.join('1' if p[i * 9 + j] > p[i * 9 + j + 1] else '0' for i in range(8) for j in range(8)), 2) - (1 << 63)
        r['pixel_md5'] = hashlib.md5(g.tobytes() + f'{g.width}x{g.height}'.encode()).hexdigest()
        r['corrupt'] = False
    except Exception as e:
        r.update(corrupt=True, error=str(e)[:120], fmt=None, mode=None, width=0, height=0, exif_orientation=0,
                 pixel_std=0.0, pixel_range=0, dhash=0, pixel_md5='')
    return r


def needs_conversion(m):
    return m['fmt'] not in ('JPEG', 'PNG') or m['mode'] not in ('L', 'RGB') or m['exif_orientation'] not in (0, 1)


def standardise(b):
    im = Image.open(io.BytesIO(b)); im = ImageOps.exif_transpose(im)
    if im.mode in ('RGBA', 'LA', 'P', 'PA'):
        im = im.convert('RGBA'); bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.split()[-1]); im = bg
    elif im.mode not in ('L', 'RGB'):
        im = im.convert('RGB')
    o = io.BytesIO(); im.save(o, 'PNG', optimize=False); return o.getvalue()


# ------------------------------------------------------------------ stage: scan
def chunks(it, n):
    buf = []
    for x in it:
        buf.append(x)
        if len(buf) == n:
            yield buf; buf = []
    if buf:
        yield buf


def scan(source):
    loader, coll, gran = SOURCES[source][0], SOURCES[source][1], SOURCES[source][2]
    os.makedirs(os.path.join(WORK, 'meta'), exist_ok=True)
    rows = []
    with Pool(14) as pool:
        for batch in chunks(loader(), 2000):
            qa = pool.map(qa_image, [(k, b) for k, b, *_ in batch], chunksize=50)
            for (k, b, raw, osplit, grp, extra), q in zip(batch, qa):
                text, ch = normalise(raw, gran, source)
                q.update(source=source, collection=coll, granularity=gran, orig_split=osplit, group_id=grp,
                         raw_text=raw if gran != 'page' else None, text=text, text_changes=','.join(ch),
                         text_flags=','.join(text_flags(text)), n_chars=len(text), n_aksharas=akshara_count(text),
                         extra=json.dumps(extra, ensure_ascii=False))
                rows.append(q)
            print(source, len(rows), flush=True)
    t = pa.Table.from_pylist(rows)
    pq.write_table(t, os.path.join(WORK, 'meta', f'{source}.parquet'))
    print('scanned', source, len(rows))


# ------------------------------------------------------------------ stage: assign
def stable_frac(s):
    return int(hashlib.sha1(s.encode()).hexdigest()[:8], 16) / 0xFFFFFFFF


def grouped_split(groups_sizes, val=0.05, test=0.05, forced_test=()):
    """Assign whole groups to splits; order groups by a stable hash, fill test then val by sample count."""
    total = sum(groups_sizes.values()); out = {}
    for g in forced_test:
        if g in groups_sizes:
            out[g] = 'test'
    ntest = sum(groups_sizes[g] for g in out)
    nval = 0
    for g in sorted(groups_sizes, key=stable_frac):
        if g in out:
            continue
        if ntest < test * total:
            out[g] = 'test'; ntest += groups_sizes[g]
        elif nval < val * total:
            out[g] = 'val'; nval += groups_sizes[g]
        else:
            out[g] = 'train'
    return out


def load_meta(srcs):
    ts = [pq.read_table(os.path.join(WORK, 'meta', f'{s}.parquet')) for s in srcs if os.path.exists(os.path.join(WORK, 'meta', f'{s}.parquet'))]
    cols = ['source', 'collection', 'granularity', 'key', 'orig_split', 'group_id', 'text', 'text_flags', 'text_changes', 'corrupt',
            'pixel_std', 'pixel_range', 'pixel_md5', 'dhash', 'width', 'height', 'n_aksharas', 'n_chars', 'fmt', 'mode', 'exif_orientation', 'extra']
    rows = []
    for t in ts:
        rows += t.select(cols).to_pylist()
    return rows


def assign(srcs):
    rows = load_meta(srcs)
    if not rows:
        return
    bench = json.load(open(os.path.join(WORK, 'benchmark_test_pages.json')))
    icdar_test_pages = {'hwpage:' + p for p in bench['icdar2024_test_pages']}
    hwuc_pages = {r['group_id'] for r in rows if r['source'] == 'hw_uc_telugu' and r['group_id'].startswith('hwpage:')}
    priority = ['hw_uc_telugu', 'hw_words_telugu', 'ihwwr1_telugu', 'mozhi_telugu', 'wikisource_te_pages', 'sarvam_ocr_bench_te',
                'indicdlp_eval_sample_te', 'wirindic_telugu', 'bstd_telugu', 'indicstr12_telugu',
                'synthetic_m_telugu', 'synthetic_r_telugu', 'synthetic_indicstr_telugu']
    rank = {s: i for i, s in enumerate(priority)}
    rows.sort(key=lambda r: (rank[r['source']], r['key']))

    # 1. per-sample drop rules
    for r in rows:
        f = set(filter(None, r['text_flags'].split(',')))
        reason = ''
        if r['corrupt']:
            reason = 'corrupt_image'
        elif not r['text']:
            reason = 'empty_label'
        elif r['text'].strip() in PLACEHOLDERS:
            reason = 'placeholder_label'
        elif 'replacement_char' in f:
            reason = 'broken_encoding'
        elif r['granularity'] == 'word' and r['collection'] != 'synthetic' and 'punctuation_only' in f:
            reason = 'punctuation_only'
        elif r['source'] in ('ihwwr1_telugu', 'hw_uc_telugu') and 'digits_only' in f:
            # visual check: ~4/10 digit crops on these camera pages do not match their label (copied sentence-ID numbers)
            reason = 'digits_only_unreliable'
        elif r['granularity'] == 'word' and r['collection'] != 'synthetic' and (r['pixel_range'] < 16 or r['pixel_std'] < 3):
            reason = 'blank_image'
        elif r['source'] == 'ihwwr1_telugu' and r['group_id'] in hwuc_pages:
            reason = 'overlap_page_in_hw_uc'
        elif r['source'] == 'wikisource_te_pages':
            tel = len(re.findall('[ఀ-౿]', r['text']))
            if r['n_chars'] < 20 or tel / max(1, r['n_chars']) < 0.3:
                reason = 'page_text_too_short_or_not_telugu'
        r['drop'] = reason

    # 2. exact duplicates (identical decoded pixels) inside a collection; conflicting labels are dropped entirely
    by_px = collections.defaultdict(list)
    for r in rows:
        if not r['drop']:
            by_px[(r['collection'], r['pixel_md5'])].append(r)
    for (_, _), grp in by_px.items():
        if len(grp) < 2:
            continue
        if len({g['text'] for g in grp}) > 1:      # same pixels, different text: cannot tell which is right
            for g in grp:
                g['drop'] = 'duplicate_image_conflicting_labels'
        else:
            for g in grp[1:]:
                g['drop'] = 'exact_duplicate_image'

    # 3. near-duplicates across sources (same dHash + same label) in real collections
    by_dh = collections.defaultdict(list)
    for r in rows:
        if not r['drop'] and r['collection'] != 'synthetic':
            by_dh[(r['collection'], r['dhash'], r['text'])].append(r)
    for grp in by_dh.values():
        srcs = {g['source'] for g in grp}
        if len(srcs) > 1:
            for g in grp[1:]:
                if g['source'] != grp[0]['source']:
                    g['drop'] = 'near_duplicate_other_source'

    # 4. splits, by original document unit
    plan = {}
    kept = [r for r in rows if not r['drop']]
    by_source = collections.defaultdict(list)
    for r in kept:
        by_source[r['source']].append(r)
    for s, rs in by_source.items():
        role = SOURCES[s][7]
        if role == 'eval_only':
            for r in rs:
                r['split'] = 'test'; r['split_rule'] = 'evaluation-only source'
            continue
        if role == 'pretrain':
            for r in rs:
                r['split'] = {'val': 'val', 'validation': 'val', 'test': 'test'}.get(r['orig_split'], 'train')
                r['split_rule'] = 'official split kept (synthetic, no source documents)'
            continue
        if s == 'hw_words_telugu':   # official splits are disjoint by writer folder (checked) -> keep
            for r in rs:
                r['split'] = {'val': 'val', 'test': 'test'}.get(r['orig_split'], 'train')
                r['split_rule'] = 'official split kept (writer folders disjoint across splits)'
            continue
        if s == 'bstd_telugu':   # official train/test already scene-disjoint; carve val from train scenes
            sizes = collections.Counter(r['group_id'] for r in rs if r['orig_split'] == 'train')
            g = grouped_split(sizes, val=0.1, test=0.0)
            for r in rs:
                r['split'] = 'test' if r['orig_split'] == 'test' else g[r['group_id']]
                r['split_rule'] = 'official scene-disjoint test kept; val = held-out train scenes'
            continue
        sizes = collections.Counter(r['group_id'] for r in rs)
        small = len(rs) < 30000
        forced = [g for g in sizes if g in icdar_test_pages] if s in ('hw_uc_telugu', 'ihwwr1_telugu') else []
        g = grouped_split(sizes, val=0.1 if small else 0.05, test=0.1 if small else 0.05, forced_test=forced)
        unit = rs[0]['group_id'].split(':')[0]
        for r in rs:
            r['split'] = g[r['group_id']]
            r['split_rule'] = f're-split by {unit}' + ('; ICDAR-2024 test pages forced to test' if forced else '')
    for r in rows:
        if r['drop']:
            r['split'] = ''; r['split_rule'] = ''
        r['uid'] = hashlib.sha1(f"{r['source']}|{r['key']}".encode()).hexdigest()[:16]

    # 5. group-level leakage audit across collections: same group id in two splits must never happen
    gs = collections.defaultdict(set)
    for r in rows:
        if not r['drop']:
            gs[(r['source'], r['group_id'])].add(r['split'])
    leaks = {k: v for k, v in gs.items() if len(v) > 1 and k[1] != 'synthetic'}
    assert not leaks, list(leaks.items())[:5]
    out = pa.Table.from_pylist([{k: r[k] for k in ['uid', 'source', 'key', 'collection', 'granularity', 'group_id', 'orig_split', 'split',
                                                    'split_rule', 'drop', 'text', 'text_flags', 'text_changes', 'n_aksharas', 'width', 'height',
                                                    'fmt', 'mode', 'exif_orientation', 'pixel_md5', 'dhash', 'extra']} for r in rows])
    os.makedirs(os.path.join(WORK, 'assign'), exist_ok=True)
    for s in sorted(set(out.column('source').to_pylist())):
        pq.write_table(out.filter(pa.compute.equal(out['source'], s)), os.path.join(WORK, 'assign', f'{s}.parquet'))
    c = collections.Counter((r['source'], r['drop'] or 'KEPT:' + r['split']) for r in rows)
    for k in sorted(c):
        print(k, c[k])


# ------------------------------------------------------------------ stage: export
def export(source):
    if not os.path.exists(os.path.join(WORK, 'assign', f'{source}.parquet')):
        print('nothing to export for', source); return
    a = pq.read_table(os.path.join(WORK, 'assign', f'{source}.parquet'), columns=['key', 'uid', 'drop', 'split', 'granularity', 'text',
                      'text_flags', 'text_changes', 'width', 'height', 'fmt', 'mode', 'exif_orientation', 'group_id', 'orig_split', 'extra']).to_pylist()
    keep = {r['key']: r for r in a if not r['drop']}
    lic = SOURCES[source]
    loader, coll = lic[0], lic[1]
    writers = {}; buffers = collections.defaultdict(list); counts = collections.Counter()

    def flush(split, final=False):
        buf = buffers[split]
        if not buf or (len(buf) < 5000 and not final):
            return
        d = os.path.join(OUT, coll, split); os.makedirs(d, exist_ok=True)
        n = counts[('shard', split)]; counts[('shard', split)] += 1
        p = os.path.join(d, f'{source}-{n:05d}.parquet')
        pq.write_table(pa.Table.from_pylist(buf), p, compression='zstd')
        buffers[split] = []

    for k, b, raw, osplit, grp, extra in loader():
        r = keep.get(k)
        if not r:
            continue
        conv = r['fmt'] not in ('JPEG', 'PNG') or r['mode'] not in ('L', 'RGB') or r['exif_orientation'] not in (0, 1)
        img = standardise(b) if conv else b
        buffers[r['split']].append(dict(uid=r['uid'], image=img, image_format='PNG' if conv else r['fmt'], text=r['text'],
                                        raw_text=raw if r['granularity'] != 'page' else None,
                                        collection=coll, granularity=r['granularity'], source=source, source_key=k,
                                        group_id=r['group_id'], orig_split=r['orig_split'], label_type=lic[3],
                                        licence=lic[4], licence_status=lic[5], redistributable=lic[6],
                                        text_flags=r['text_flags'], text_changes=r['text_changes'], width=r['width'], height=r['height'],
                                        extra=r['extra']))
        counts[r['split']] += 1
        flush(r['split'])
    for s in list(buffers):
        flush(s, final=True)
    print('exported', source, {k: v for k, v in counts.items() if isinstance(k, str)})


# ------------------------------------------------------------------ stage: checksums / manifest
def checksums():
    rows = []
    for root, _, fs in os.walk(OUT):
        for f in sorted(fs):
            if not f.endswith('.parquet'):
                continue
            p = os.path.join(root, f)
            h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
            n = pq.ParquetFile(p).metadata.num_rows
            rows.append(dict(shard=os.path.relpath(p, DATA), rows=n, bytes=os.path.getsize(p), sha256=h))
    json.dump(rows, open(os.path.join(WORK, 'shard_checksums.json'), 'w'), indent=0)
    print(len(rows), 'shards', sum(r['rows'] for r in rows), 'rows')


if __name__ == '__main__':
    stage, arg = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'all')
    srcs = list(SOURCES) if arg == 'all' else arg.split(',')
    if stage == 'scan':
        for s in srcs:
            scan(s)
    elif stage == 'assign':
        real = [s for s in SOURCES if SOURCES[s][1] != 'synthetic']
        assign(real)                       # real data: cross-source duplicate + overlap checks need all of it together
        for s in SOURCES:                  # synthetic: one source at a time (memory); no shared documents
            if SOURCES[s][1] == 'synthetic' and s in srcs:
                assign([s])
    elif stage == 'export':
        for s in srcs:
            export(s)
    elif stage == 'checksums':
        checksums()
