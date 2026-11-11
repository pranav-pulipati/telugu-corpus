"""Round 3: Crossref works search (metadata only) for Telugu OCR dataset papers.

usage: python3 -I crossref.py OUTFILE
"""
import json, re, sys, time, urllib.parse, urllib.request

UA = {'User-Agent': 'telugu-ocr-directory-research/1.0 (metadata sweep)'}
QUERIES = ['telugu dataset handwritten', 'telugu character recognition dataset', 'telugu ocr dataset', 'telugu printed character dataset',
           'telugu handwritten database', 'telugu word images dataset', 'telugu scene text dataset', 'telugu palm leaf dataset',
           'telugu manuscript dataset', 'telugu document images', 'indic handwritten dataset', 'indic scene text dataset', 'indic ocr benchmark',
           'indian scripts handwritten database', 'multi-script document database indian', 'telugu numerals dataset', 'telugu online handwriting',
           'telugu text recognition', 'telugu script identification', 'telugu inscription recognition']
out = {'platform': 'crossref', 'queried': time.strftime('%Y-%m-%d'), 'queries': [], 'hits': {}}
for q in QUERIES:
    url = 'https://api.crossref.org/works?' + urllib.parse.urlencode({'query.bibliographic': q, 'rows': 200, 'select': 'DOI,title,type,issued,container-title,publisher'})
    try:
        d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read())['message']
    except Exception as e:  # noqa: BLE001
        out['queries'].append({'query': q, 'error': str(e)[:80]}); continue
    for it in d.get('items', []):
        t = ' '.join(it.get('title') or [])
        h = out['hits'].setdefault(it['DOI'], {'title': t, 'type': it.get('type'), 'year': ((it.get('issued') or {}).get('date-parts') or [[None]])[0][0],
                                               'venue': ' '.join(it.get('container-title') or []), 'publisher': it.get('publisher'), 'queries': []})
        h['queries'].append(q)
    out['queries'].append({'query': q, 'hits': len(d.get('items', [])), 'total': d.get('total-results')})
    print(q, len(d.get('items', [])), d.get('total-results'), flush=True)
    time.sleep(1)
rel = {k: v for k, v in out['hits'].items() if re.search(r'telugu', v['title'], re.I) and re.search(r'data ?set|database|corpus|benchmark|collection', v['title'], re.I)}
out['telugu_dataset_titles'] = sorted(rel)
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print('unique', len(out['hits']), 'telugu dataset titles', len(rel))
