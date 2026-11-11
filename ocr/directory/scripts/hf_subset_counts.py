"""Count the Telugu rows of public multilingual HF datasets via the datasets-server API (no data download).

For each (dataset, config, split, column) it reads column statistics (value frequencies) and, if those are not
available, asks the /filter endpoint for the number of rows whose column equals a Telugu label.
usage: python3 -I hf_subset_counts.py OUTFILE
"""
import json, sys, time, urllib.parse, urllib.request

UA = {'User-Agent': 'telugu-ocr-directory-research/1.0'}
API = 'https://datasets-server.huggingface.co'
TE = ['te', 'tel', 'Telugu', 'telugu', 'te_IN', 'tel_Telu', 'Telu']
JOBS = [  # dataset, config, split, language column
    ('sarvamai/indic-ocr-bench', 'default', 'test', 'language'),
    ('sarvamai/indic-ocr-bench', 'default', 'small_representative', 'language'),
    ('krutrim-ai-labs/IndicVisionBench', 'ocr', 'test', 'language'),
    ('krutrim-ai-labs/IndicVisionBench', 'vqa_indic', 'test', 'language'),
    ('krutrim-ai-labs/IndicVisionBench', 'vqa_parallel', 'test', 'language'),
    ('krutrim-ai-labs/IndicVisionBench', 'vqa_en', 'test', 'language'),
]


def get(url):
    for k in range(4):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read())
        except urllib.error.HTTPError as e:
            try:
                return json.loads(e.read())
            except Exception:  # noqa: BLE001
                return {'error': f'HTTP {e.code}'}
        except Exception as e:  # noqa: BLE001
            err = str(e); time.sleep(3 * (k + 1))
    return {'error': err}


def configs(ds):
    d = get(f'{API}/splits?dataset={urllib.parse.quote(ds)}')
    return [(s['config'], s['split']) for s in d.get('splits', [])]


def count(ds, cfg, split, col):
    q = f'dataset={urllib.parse.quote(ds)}&config={urllib.parse.quote(cfg)}&split={urllib.parse.quote(split)}'
    st = get(f'{API}/statistics?{q}')
    for c in st.get('statistics', []):
        if c['column_name'] == col and (c.get('column_statistics') or {}).get('frequencies'):
            fr = c['column_statistics']['frequencies']
            return {'method': 'statistics', 'frequencies': fr, 'telugu': sum(v for k, v in fr.items() if k in TE),
                    'total': st.get('num_examples')}
    for lab in TE:
        where = urllib.parse.quote(f'"{col}"=\'{lab}\'')
        d = get(f'{API}/filter?{q}&where={where}&length=1')
        if d.get('num_rows_total'):
            return {'method': 'filter', 'label': lab, 'telugu': d['num_rows_total']}
    return {'method': 'filter', 'telugu': 0, 'note': 'no Telugu label matched', 'error': st.get('error')}


if __name__ == '__main__':
    extra = [tuple(a.split('|')) for a in sys.argv[2:]]  # "dataset|config|split|column"
    out = []
    for ds, cfg, split, col in JOBS + extra:
        r = count(ds, cfg, split, col)
        r.update(dataset=ds, config=cfg, split=split, column=col)
        out.append(r)
        print(ds, cfg, split, '->', r.get('telugu'), r.get('method'), (r.get('frequencies') or {}) if len(r.get('frequencies') or {}) < 40 else '', flush=True)
    old = json.load(open(sys.argv[1])) if len(sys.argv) > 1 and __import__('os').path.exists(sys.argv[1]) else []
    key = lambda r: (r['dataset'], r['config'], r['split'])
    merged = {key(r): r for r in old}
    merged.update({key(r): r for r in out})
    json.dump(list(merged.values()), open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
