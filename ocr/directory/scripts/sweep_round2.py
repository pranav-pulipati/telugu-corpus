"""Round-2 metadata sweeps (no data download): broader 'telugu' queries on Kaggle, Hugging Face, DataCite and Mendeley.

usage: python3 -I sweep_round2.py OUTFILE
"""
import json, re, sys, time, urllib.parse, urllib.request

UA = {'User-Agent': 'telugu-ocr-directory-research/1.0'}


def get(url, tries=4):
    err = ''
    for k in range(tries):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read())
        except urllib.error.HTTPError as e:
            err = f'HTTP {e.code}'
            if e.code in (429, 503):
                time.sleep(15 * (k + 1)); continue
            return {'_error': err}
        except Exception as e:  # noqa: BLE001
            err = str(e)[:100]; time.sleep(4 * (k + 1))
    return {'_error': err}


out = {'queried': time.strftime('%Y-%m-%d'), 'log': [], 'kaggle': {}, 'hf': {}, 'datacite': {}, 'mendeley': {}}

# Kaggle: page through broad queries
for q in ['telugu', 'telugu images', 'telugu handwritten', 'telugu ocr', 'indic ocr', 'indian languages ocr', 'indic handwritten', 'indian script',
          'dravidian', 'south indian languages images', 'telugu text', 'telugu characters', 'telugu letters', 'telugu words', 'telugu newspaper',
          'telugu book', 'telugu manuscript', 'palm leaf', 'indic scene text', 'multilingual ocr']:
    n = 0
    for page in range(1, 11):
        r = get('https://www.kaggle.com/api/v1/datasets/list?' + urllib.parse.urlencode({'search': q, 'page': page}))
        if not isinstance(r, list) or not r:
            break
        for d in r:
            ref = d.get('ref') or d.get('datasetRef')
            out['kaggle'].setdefault(ref, {'title': d.get('title'), 'subtitle': d.get('subtitle'), 'size': d.get('totalBytes'), 'queries': []})['queries'].append(q)
            n += 1
        time.sleep(1)
    out['log'].append({'platform': 'kaggle', 'query': q, 'hits': n})

# Hugging Face: Telugu-tagged datasets with image modality, plus new search terms
for url, label in [('https://huggingface.co/api/datasets?filter=language:te&filter=modality:image&limit=1000&full=false', 'language:te + modality:image'),
                   ('https://huggingface.co/api/datasets?filter=language:te&filter=modality:document&limit=1000&full=false', 'language:te + modality:document'),
                   ('https://huggingface.co/api/datasets?filter=language:tel&limit=1000&full=false', 'language:tel')]:
    r = get(url)
    n = 0
    for d in (r if isinstance(r, list) else []):
        out['hf'].setdefault(d['id'], {'queries': []})['queries'].append(label); n += 1
    out['log'].append({'platform': 'hf', 'query': label, 'hits': n})
for q in ['Telu', 'telugu-hw', 'telugu handwriting', 'tel_telu', 'indic-hw', 'indic handwritten', 'hastakshar', 'chips', 'glotocr', 'indic doc',
          'indic document', 'indic-ocr-bench', 'ocr indic', 'indic printed', 'indic scene', 'indic-str', 'devanagari telugu', 'dravidian ocr',
          'ocr multilingual', 'multilingual ocr', 'scene text multilingual', 'document parsing indic', 'indic vqa', 'telugu image', 'telugu vision',
          'telugu doc', 'telugu books', 'telugu newspaper', 'telugu manuscript', 'palm leaf', 'olai', 'tala patra', 'shilalekh', 'inscription']:
    r = get('https://huggingface.co/api/datasets?' + urllib.parse.urlencode({'search': q, 'limit': 200}))
    n = 0
    for d in (r if isinstance(r, list) else []):
        out['hf'].setdefault(d['id'], {'queries': []})['queries'].append(q); n += 1
    out['log'].append({'platform': 'hf', 'query': q, 'hits': n})
    time.sleep(0.3)

# DataCite: every record mentioning Telugu (all resource types), paged
n, url = 0, 'https://api.datacite.org/dois?' + urllib.parse.urlencode({'query': 'telugu', 'page[size]': 1000})
while url and n < 20000:
    r = get(url)
    for d in r.get('data', []) if isinstance(r, dict) else []:
        a = d['attributes']
        out['datacite'][d['id']] = {'title': (a.get('titles') or [{}])[0].get('title'), 'type': (a.get('types') or {}).get('resourceTypeGeneral'),
                                    'publisher': a.get('publisher'), 'year': a.get('publicationYear'), 'url': a.get('url'),
                                    'desc': ((a.get('descriptions') or [{}])[0].get('description') or '')[:400]}
        n += 1
    url = (r.get('links') or {}).get('next') if isinstance(r, dict) else None
    time.sleep(0.5)
out['log'].append({'platform': 'datacite', 'query': 'telugu (all types)', 'hits': n})

# Mendeley Data public search
for q in ['telugu', 'telugu handwritten', 'telugu character', 'indic handwritten', 'indian script', 'palm leaf manuscript']:
    r = get('https://data.mendeley.com/api/research-data/search?' + urllib.parse.urlencode({'search': q, 'type': 'DATASET', 'size': 100}))
    items = r.get('results', []) if isinstance(r, dict) else []
    for it in items:
        out['mendeley'].setdefault(it.get('id') or it.get('containerURI') or it.get('title'), {'title': it.get('title'), 'doi': it.get('doi'),
                                                                                             'desc': (it.get('description') or '')[:400], 'queries': []})['queries'].append(q)
    out['log'].append({'platform': 'mendeley', 'query': q, 'hits': len(items), 'error': r.get('_error') if isinstance(r, dict) else None})

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
for p in ('kaggle', 'hf', 'datacite', 'mendeley'):
    print(p, len(out[p]))
