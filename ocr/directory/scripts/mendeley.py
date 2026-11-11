"""Search Mendeley Data (public research-data search API, metadata only) for Telugu OCR datasets.

usage: python3 -I mendeley.py OUTFILE
"""
import json, sys, time, urllib.parse, urllib.request

UA = {'User-Agent': 'telugu-ocr-directory-research/1.0'}
QUERIES = ['telugu', 'telugu handwritten', 'telugu character', 'telugu ocr', 'telugu script', 'indic handwritten', 'indian script',
           'indic ocr', 'palm leaf manuscript', 'dravidian handwritten', 'south indian script']
out = {'platform': 'mendeley', 'queried': time.strftime('%Y-%m-%d'), 'queries': [], 'hits': {}}
for q in QUERIES:
    n, total = 0, None
    for page in range(1, 31):
        url = 'https://data.mendeley.com/api/research-data/search?' + urllib.parse.urlencode({'query': q, 'size': 10, 'page': page})
        try:
            d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
        except Exception as e:  # noqa: BLE001
            out['queries'].append({'query': q, 'page': page, 'error': str(e)[:80]}); break
        recs, total = d.get('records', []), d.get('total_records')
        for r in recs:
            h = out['hits'].setdefault(r['id'], {'title': r.get('title'), 'doi': r.get('doi'), 'desc': (r.get('description') or '')[:500], 'queries': []})
            h['queries'].append(q); n += 1
        if len(recs) < 10 or n >= (total or 0):
            break
        time.sleep(0.3)
    out['queries'].append({'query': q, 'hits': n, 'total': total})
    print(q, n, total, flush=True)
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print('unique', len(out['hits']))
