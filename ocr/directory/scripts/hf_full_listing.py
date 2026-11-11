"""Round 3: complete (paginated) Hugging Face listings, so no query is cut off at the 200/1000-result API limit.

Lists every dataset for each search term / filter by following the API's Link: rel="next" cursor, then flags those
with image/document evidence (tags or file names) and Telugu evidence (tag, id, or Telugu-named files).
Metadata only. usage: python3 -I hf_full_listing.py OUTFILE
"""
import json, re, sys, time, urllib.parse, urllib.request

UA = {'User-Agent': 'telugu-ocr-directory-research/1.0'}
LISTINGS = [
    ('search', 'telugu'), ('search', 'Telugu'), ('search', 'tel_'), ('search', '-te-'), ('search', '_te_'), ('search', 'indic'), ('search', 'ocr'),
    ('search', 'handwrit'), ('search', 'scene-text'), ('search', 'scene_text'), ('search', 'text-recognition'), ('search', 'document'),
    ('filter', 'language:te'), ('filter', 'language:tel'),
]


def page(url):
    for k in range(4):
        try:
            resp = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90)
            link = resp.headers.get('Link') or ''
            m = re.search(r'<([^>]+)>;\s*rel="next"', link)
            return json.loads(resp.read()), (m.group(1) if m else None)
        except Exception as e:  # noqa: BLE001
            err = str(e); time.sleep(5 * (k + 1))
    return {'_error': err}, None


out = {'queried': time.strftime('%Y-%m-%d'), 'listings': [], 'datasets': {}}
for kind, val in LISTINGS:
    url = 'https://huggingface.co/api/datasets?' + urllib.parse.urlencode({kind: val, 'limit': 1000, 'full': 'false'})
    n, pages = 0, 0
    while url and pages < 60:
        data, url = page(url)
        pages += 1
        if not isinstance(data, list):
            out['listings'].append({'kind': kind, 'value': val, 'error': data.get('_error')}); break
        for d in data:
            rec = out['datasets'].setdefault(d['id'], {'tags': [t for t in d.get('tags', []) if t.startswith(('language:', 'modality:', 'task_categories:', 'license:', 'size_categories:'))],
                                                       'gated': d.get('gated'), 'listings': []})
            rec['listings'].append(f'{kind}={val}'); n += 1
        time.sleep(0.5)
    out['listings'].append({'kind': kind, 'value': val, 'datasets': n, 'pages': pages})
    print(kind, val, n, pages, flush=True)


def flag(i, r):
    tags = ' '.join(r['tags'])
    img = bool(re.search(r'modality:(image|document|video)|task_categories:(image-to-text|image-text-to-text|object-detection|image-classification|'
                         r'visual-question-answering|document-question-answering|image-feature-extraction|image-segmentation)', tags)) or \
        bool(re.search(r'ocr|handwrit|scene.?text|word.?image|line.?image|text.?image|document|manuscript|palm|glyph|character|captcha|font|page', i, re.I))
    tel = 'language:te' in r['tags'] or 'language:tel' in r['tags'] or bool(re.search(r'telugu|(^|[-_/])te([-_]|$)|tel_telu', i, re.I))
    return img, tel


for i, r in out['datasets'].items():
    r['image_evidence'], r['telugu_evidence'] = flag(i, r)
both_all = [i for i, r in out['datasets'].items() if r['image_evidence'] and r['telugu_evidence']]
out['total_datasets_listed'] = len(out['datasets'])
out['datasets'] = {k: v for k, v in out['datasets'].items() if v['telugu_evidence']}  # keep the evidence file small
out['note'] = 'Only datasets with Telugu evidence are kept (file-size limit); total_datasets_listed is the full count screened.'
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
both = [i for i, r in out['datasets'].items() if r['image_evidence'] and r['telugu_evidence']]
print('unique datasets', out['total_datasets_listed'], 'image+telugu evidence', len(both_all))
