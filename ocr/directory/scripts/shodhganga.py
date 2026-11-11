"""Search Shodhganga (INFLIBNET Indian theses repository, DSpace 7 API at sgbeta.inflibnet.ac.in) for Telugu OCR theses.

Metadata only. Saves every hit plus the query log to OUTFILE.
usage: python3 -I shodhganga.py OUTFILE
"""
import json, re, sys, time, urllib.parse, urllib.request

UA = {'User-Agent': 'telugu-ocr-directory-research/1.0', 'Accept': 'application/json'}
API = 'https://sgbeta.inflibnet.ac.in/server/api/discover/search/objects'
QUERIES = ['telugu character recognition', 'telugu handwritten', 'telugu ocr', 'telugu optical character', 'telugu script recognition',
           'telugu text recognition', 'telugu document image', 'telugu palm leaf', 'telugu manuscript recognition', 'telugu printed text',
           'telugu word recognition', 'telugu scene text', 'telugu text extraction', 'telugu document analysis', 'telugu handwriting',
           'indic script recognition', 'indian script ocr', 'south indian script recognition', 'dravidian character recognition',
           'multi script document', 'telugu numeral', 'telugu inscription', 'telugu video text', 'telugu font recognition']


def meta(o, key):
    return ' | '.join(v.get('value', '') for v in (o.get('metadata') or {}).get(key, []))


out = {'queried': time.strftime('%Y-%m-%d'), 'queries': [], 'hits': {}}
for q in QUERIES:
    n, total = 0, None
    for page in range(5):
        url = API + '?' + urllib.parse.urlencode({'query': q, 'dsoType': 'ITEM', 'size': 40, 'page': page})
        try:
            d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
        except Exception as e:  # noqa: BLE001
            out['queries'].append({'query': q, 'page': page, 'error': str(e)[:100]}); break
        sr = d.get('_embedded', {}).get('searchResult', {})
        total = (sr.get('page') or {}).get('totalElements')
        objs = sr.get('_embedded', {}).get('objects', [])
        for ob in objs:
            it = ob.get('_embedded', {}).get('indexableObject', {})
            h = out['hits'].setdefault(it.get('uuid'), {
                'title': meta(it, 'dc.title'), 'handle': it.get('handle'), 'year': meta(it, 'dc.date.awarded') or meta(it, 'dc.date.issued'),
                'university': meta(it, 'dc.publisher.institution') or meta(it, 'dc.publisher'), 'researcher': meta(it, 'dc.creator.researcher') or meta(it, 'dc.contributor.author'),
                'abstract': (meta(it, 'dc.description.abstract') or meta(it, 'dc.description'))[:1500], 'queries': []})
            h['queries'].append(q); n += 1
        if len(objs) < 40:
            break
        time.sleep(0.5)
    out['queries'].append({'query': q, 'hits': n, 'total': total})
    print(q, n, total, flush=True)
    time.sleep(0.5)
rel = {k: v for k, v in out['hits'].items() if re.search(r'telugu', v['title'] + v['abstract'], re.I)}
out['telugu_relevant'] = sorted(rel)
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print('unique', len(out['hits']), 'mention Telugu', len(rel))
