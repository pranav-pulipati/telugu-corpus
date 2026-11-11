"""Screen Hugging Face search hits for Telugu OCR relevance (metadata + README only, no data downloads).

For each dataset: tags (language/task/modality), README mentions of Telugu, configs/files named te/tel/telugu,
image evidence. For models: training datasets listed in the model card (leads). Writes <out>/hf_screen.json.
usage: python -I screen_hf.py DISCOVERY_DIR EXTRA_IDS_FILE
"""
import json, os, re, sys, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

D = sys.argv[1]
extra = [l.strip() for l in open(sys.argv[2])] if len(sys.argv) > 2 and os.path.exists(sys.argv[2]) else []
UA = {'User-Agent': 'telugu-ocr-directory-research/1.0'}
TEL = re.compile(r'telugu|\btel_telu\b|\btel\b|\bte\b(?![-_])|తెలుగు', re.I)
OCRW = re.compile(r'\bocr\b|handwrit|scene.?text|text.?recogn|document image|word image|line image|character recogn|glyph|text image|image-to-text|layout|printed', re.I)


def get(u, raw=False):
    for k in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
            return r.decode('utf-8', 'replace') if raw else json.loads(r)
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 404):
                return {'_error': e.code} if not raw else ''
            time.sleep(5 * (k + 1))
        except Exception:
            time.sleep(5 * (k + 1))
    return {'_error': 'fail'} if not raw else ''


def screen_dataset(i):
    info = get(f'https://huggingface.co/api/datasets/{urllib.parse.quote(i, safe="/")}')
    if not isinstance(info, dict) or '_error' in info:
        return i, {'error': info.get('_error') if isinstance(info, dict) else 'x'}
    tags = info.get('tags') or []
    card = info.get('cardData') or {}
    siblings = [s.get('rfilename', '') for s in info.get('siblings') or []]
    readme = get(f'https://huggingface.co/datasets/{i}/raw/main/README.md', raw=True) or ''
    lang_te = any(t in ('language:te', 'language:tel') for t in tags)
    img = any(t.startswith('modality:image') for t in tags) or any(re.search(r'\.(png|jpe?g|tif+|webp)$', s, re.I) for s in siblings[:5000]) \
        or 'dtype: image' in readme or any(t in tags for t in ['task_categories:image-to-text', 'task_categories:image-text-to-text', 'task_categories:object-detection', 'task_categories:image-classification'])
    tel_files = [s for s in siblings if re.search(r'(^|[/_\-.])(te|tel|telugu|te_IN|tel_Telu)([/_\-.]|$)', s, re.I)][:10]
    tel_readme = len(re.findall(r'telugu|తెలుగు', readme, re.I))
    ocr_kw = len(OCRW.findall(readme)) + len(OCRW.findall(i))
    return i, dict(lang_te=lang_te, image=img, tel_files=tel_files, tel_readme=tel_readme, ocr_kw=ocr_kw, gated=info.get('gated'),
                   license=card.get('license'), tasks=[t.split(':', 1)[1] for t in tags if t.startswith('task_categories:')],
                   n_lang=sum(1 for t in tags if t.startswith('language:')), downloads=info.get('downloads'), likes=info.get('likes'),
                   last_modified=info.get('lastModified'), n_files=len(siblings), readme_len=len(readme),
                   pretty=(card.get('pretty_name') or ''), size_cat=[t.split(':', 1)[1] for t in tags if t.startswith('size_categories:')])


def screen_model(i):
    info = get(f'https://huggingface.co/api/models/{urllib.parse.quote(i, safe="/")}')
    if not isinstance(info, dict) or '_error' in info:
        return i, {'error': 'x'}
    card = info.get('cardData') or {}
    ds = card.get('datasets') or []
    return i, dict(pipeline=info.get('pipeline_tag'), datasets=ds if isinstance(ds, list) else [ds],
                   lang=[t for t in info.get('tags') or [] if t in ('te', 'tel', 'language:te')], tags=(info.get('tags') or [])[:25])


hits = json.load(open(os.path.join(D, 'hf.json')))['hits']
dsets = sorted({v['id'] for v in hits.values() if v['kind'] == 'datasets'} | set(extra))
models = sorted({v['id'] for v in hits.values() if v['kind'] == 'models'})
with ThreadPoolExecutor(6) as ex:
    ds_res = dict(ex.map(screen_dataset, dsets))
    md_res = dict(ex.map(screen_model, models))
json.dump({'datasets': ds_res, 'models': md_res}, open(os.path.join(D, 'hf_screen.json'), 'w'), ensure_ascii=False, indent=0)
cand = {k: v for k, v in ds_res.items() if 'error' not in v and v['image'] and (v['lang_te'] or v['tel_files'] or v['tel_readme'])}
print('datasets screened', len(ds_res), 'image+telugu-evidence candidates', len(cand))
leads = sorted({d for v in md_res.values() for d in v.get('datasets') or []})
print('training datasets named by models', len(leads))
open(os.path.join(D, 'hf_model_dataset_leads.txt'), 'w').write('\n'.join(leads))
