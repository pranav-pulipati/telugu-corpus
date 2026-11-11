"""Systematic discovery of Telugu OCR datasets across open platform APIs.

Runs a fixed list of query variants against each platform's public search API and saves every raw hit
(id, title, url, snippet) to <out>/<platform>.json plus a query log. Nothing is downloaded except metadata.

usage: python -I discover.py OUTDIR [platform ...]
platforms: hf github zenodo figshare datacite dataverse archive openalex s2 arxiv
"""
import json, os, sys, time, urllib.parse, urllib.request, subprocess, re

OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'telugu-ocr-directory-research/1.0'}

# Query variants requested in the brief (section 3) + Indic / multilingual variants
TOPICS = ['telugu ocr', 'telugu handwritten', 'telugu handwriting', 'telugu handwritten character', 'telugu handwritten word',
          'telugu character recognition', 'telugu printed text', 'telugu text recognition', 'telugu scene text',
          'telugu document image', 'telugu text line', 'telugu word recognition', 'telugu manuscript', 'telugu palm leaf',
          'telugu newspaper ocr', 'telugu synthetic text images', 'telugu document layout', 'telugu script',
          'telugu digits', 'telugu numerals', 'telugu alphabet', 'telugu akshara', 'telugu glyph',
          'indic ocr', 'indic handwritten', 'indic scene text', 'indian language ocr', 'multilingual ocr indic',
          'indic document layout', 'south indian script recognition', 'dravidian script ocr', 'telugu captcha',
          'telugu image text', 'telugu vision language']


def get(url, data=None, headers=None, tries=4):
    err = 'no response'
    for k in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
            return json.loads(urllib.request.urlopen(req, timeout=90).read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                err = f'HTTP {e.code}'; time.sleep(20 * (k + 1)); continue
            return {'_error': f'HTTP {e.code}'}
        except Exception as e:
            time.sleep(5 * (k + 1)); err = str(e)
    return {'_error': err[:120]}


def hf():
    hits, log = {}, []
    for q in TOPICS + ['telugu', 'tel_Telu', 'te-IN', 'iiit hw', 'indicstr', 'mozhi', 'bharat scene text', 'synthdog', 'indic-ocr',
                       'telugu-ocr', 'telugu_ocr', 'handwritten indic', 'nayana', 'indic text image', 'ocr indian', 'ocr te']:
        for kind in ['datasets', 'models']:
            r = get(f'https://huggingface.co/api/{kind}?search={urllib.parse.quote(q)}&limit=200&full=false')
            n = 0
            if isinstance(r, list):
                for d in r:
                    hits.setdefault(f"{kind}/{d['id']}", {'id': d['id'], 'kind': kind, 'queries': []})['queries'].append(q); n += 1
            log.append({'query': q, 'kind': kind, 'hits': n})
            time.sleep(0.3)
    # language-tag listing combined with OCR-ish tasks
    for task in ['image-to-text', 'image-text-to-text', 'object-detection', 'image-classification', 'visual-question-answering', 'document-question-answering']:
        r = get(f'https://huggingface.co/api/datasets?filter=language:te&filter=task_categories:{task}&limit=1000')
        n = 0
        if isinstance(r, list):
            for d in r:
                hits.setdefault(f"datasets/{d['id']}", {'id': d['id'], 'kind': 'datasets', 'queries': []})['queries'].append(f'language:te+task:{task}'); n += 1
        log.append({'query': f'language:te + task_categories:{task}', 'kind': 'datasets', 'hits': n})
    return hits, log


def github():
    hits, log = {}, []
    for q in TOPICS:
        for kind in ['repositories']:
            try:
                r = json.loads(subprocess.run(['gh', 'api', '-X', 'GET', 'search/repositories', '-f', f'q={q}', '-f', 'per_page=100'],
                                              capture_output=True, text=True, timeout=120).stdout or '{}')
            except Exception as e:
                r = {'_error': str(e)}
            items = r.get('items', [])
            for it in items:
                hits.setdefault(it['full_name'], {'id': it['full_name'], 'url': it['html_url'], 'description': it.get('description'),
                                                   'stars': it.get('stargazers_count'), 'size_kb': it.get('size'), 'license': (it.get('license') or {}).get('spdx_id'),
                                                   'updated': it.get('pushed_at'), 'queries': []})['queries'].append(q)
            log.append({'query': q, 'kind': kind, 'total_count': r.get('total_count'), 'returned': len(items)})
            time.sleep(2.5)
    return hits, log


def zenodo():
    hits, log = {}, []
    for q in TOPICS + ['telugu']:
        qq = q   # anonymous Zenodo search allows at most 25 results per page -> page through up to 100
        items, total = [], None
        for page in range(1, 5):
            r = get('https://zenodo.org/api/records?' + urllib.parse.urlencode({'q': qq, 'size': 25, 'page': page}))
            got = (r.get('hits') or {}).get('hits', []) if isinstance(r, dict) else []
            total = (r.get('hits') or {}).get('total') if isinstance(r, dict) else total
            items += got
            if len(got) < 25:
                break
            time.sleep(1)
        r = {'hits': {'total': total}}
        for it in items:
            m = it.get('metadata', {})
            hits.setdefault(str(it['id']), {'id': it['id'], 'title': m.get('title'), 'doi': it.get('doi'), 'type': (m.get('resource_type') or {}).get('type'),
                                             'license': (m.get('license') or {}).get('id'), 'url': it.get('links', {}).get('self_html'),
                                             'desc': re.sub('<[^>]+>', ' ', m.get('description') or '')[:400], 'queries': []})['queries'].append(q)
        log.append({'query': qq, 'hits': len(items), 'total': (r.get('hits') or {}).get('total') if isinstance(r, dict) else None})
        time.sleep(1)
    return hits, log


def figshare():
    hits, log = {}, []
    for q in TOPICS:
        r = get('https://api.figshare.com/v2/articles/search', data=json.dumps({'search_for': q, 'page_size': 100}).encode(),
                headers={'Content-Type': 'application/json'})
        items = r if isinstance(r, list) else []
        for it in items:
            hits.setdefault(str(it['id']), {'id': it['id'], 'title': it.get('title'), 'doi': it.get('doi'), 'url': it.get('url_public_html'),
                                             'type': it.get('defined_type_name'), 'queries': []})['queries'].append(q)
        log.append({'query': q, 'hits': len(items)})
        time.sleep(1)
    return hits, log


def datacite():
    hits, log = {}, []
    for q in TOPICS:
        r = get('https://api.datacite.org/dois?' + urllib.parse.urlencode({'query': q, 'page[size]': 200,
                                                                         'fields[dois]': 'titles,url,publisher,types,descriptions,rightsList,publicationYear,doi'}))
        items = r.get('data', []) if isinstance(r, dict) else []
        for it in items:
            a = it['attributes']
            hits.setdefault(it['id'], {'id': it['id'], 'title': (a.get('titles') or [{}])[0].get('title'), 'url': a.get('url'),
                                        'publisher': a.get('publisher'), 'type': (a.get('types') or {}).get('resourceTypeGeneral'),
                                        'year': a.get('publicationYear'), 'rights': [x.get('rights') for x in a.get('rightsList') or []],
                                        'desc': ((a.get('descriptions') or [{}])[0].get('description') or '')[:400], 'queries': []})['queries'].append(q)
        log.append({'query': q, 'hits': len(items), 'total': (r.get('meta') or {}).get('total') if isinstance(r, dict) else None})
        time.sleep(1)
    return hits, log


def dataverse():
    hits, log = {}, []
    for q in TOPICS:
        r = get('https://dataverse.harvard.edu/api/search?' + urllib.parse.urlencode({'q': q, 'type': 'dataset', 'per_page': 100}))
        items = (r.get('data') or {}).get('items', []) if isinstance(r, dict) else []
        for it in items:
            hits.setdefault(it.get('global_id'), {'id': it.get('global_id'), 'title': it.get('name'), 'url': it.get('url'),
                                                  'desc': (it.get('description') or '')[:400], 'queries': []})['queries'].append(q)
        log.append({'query': q, 'hits': len(items), 'total': (r.get('data') or {}).get('total_count') if isinstance(r, dict) else None})
        time.sleep(1)
    return hits, log


def archive():
    hits, log = {}, []
    for q in ['telugu ocr', 'telugu handwritten', 'telugu dataset', 'telugu character recognition', 'telugu palm leaf',
              'telugu manuscript', 'indic ocr dataset', 'telugu scene text', 'telugu text recognition']:
        r = get('https://archive.org/advancedsearch.php?' + urllib.parse.urlencode(
            {'q': q, 'fl[]': ['identifier', 'title', 'mediatype', 'collection', 'item_size'], 'rows': 200, 'output': 'json'}, doseq=True))
        docs = (r.get('response') or {}).get('docs', []) if isinstance(r, dict) else []
        for d in docs:
            hits.setdefault(d['identifier'], {'id': d['identifier'], 'title': d.get('title'), 'mediatype': d.get('mediatype'),
                                               'url': f"https://archive.org/details/{d['identifier']}", 'queries': []})['queries'].append(q)
        log.append({'query': q, 'hits': len(docs), 'total': (r.get('response') or {}).get('numFound') if isinstance(r, dict) else None})
        time.sleep(1)
    return hits, log


def openalex():
    hits, log = {}, []
    for q in TOPICS:
        if 'telugu' not in q and 'indic' not in q and 'indian' not in q and 'dravidian' not in q:
            continue
        r = get('https://api.openalex.org/works?' + urllib.parse.urlencode({'search': q, 'per-page': 200, 'select': 'id,doi,title,publication_year,primary_location,cited_by_count,type'}))
        items = r.get('results', []) if isinstance(r, dict) else []
        for it in items:
            loc = it.get('primary_location') or {}
            hits.setdefault(it['id'], {'id': it['id'], 'doi': it.get('doi'), 'title': it.get('title'), 'year': it.get('publication_year'),
                                        'venue': ((loc.get('source') or {}).get('display_name')), 'cited_by': it.get('cited_by_count'),
                                        'type': it.get('type'), 'queries': []})['queries'].append(q)
        log.append({'query': q, 'hits': len(items), 'total': (r.get('meta') or {}).get('count') if isinstance(r, dict) else None})
        time.sleep(0.5)
    return hits, log


def s2():
    hits, log = {}, []
    for q in TOPICS:
        if 'telugu' not in q and 'indic' not in q:
            continue
        r = get('https://api.semanticscholar.org/graph/v1/paper/search?' + urllib.parse.urlencode(
            {'query': q + ' dataset', 'limit': 100, 'fields': 'title,year,externalIds,venue,citationCount,abstract,url'}))
        items = r.get('data', []) if isinstance(r, dict) else []
        for it in items:
            hits.setdefault(it['paperId'], {'id': it['paperId'], 'title': it.get('title'), 'year': it.get('year'), 'venue': it.get('venue'),
                                             'ids': it.get('externalIds'), 'cited_by': it.get('citationCount'), 'url': it.get('url'),
                                             'abstract': (it.get('abstract') or '')[:600], 'queries': []})['queries'].append(q)
        log.append({'query': q + ' dataset', 'hits': len(items), 'total': r.get('total') if isinstance(r, dict) else None,
                    'error': r.get('_error') if isinstance(r, dict) else None})
        time.sleep(4)
    return hits, log


def arxiv():
    import xml.etree.ElementTree as ET
    hits, log = {}, []
    for q in ['all:telugu AND all:ocr', 'all:telugu AND all:handwritten', 'all:telugu AND all:"text recognition"',
              'all:telugu AND all:"character recognition"', 'all:telugu AND all:"scene text"', 'all:indic AND all:ocr AND all:dataset',
              'all:indic AND all:handwritten AND all:dataset', 'all:indic AND all:"scene text"', 'all:telugu AND all:document AND all:image',
              'all:"indian languages" AND all:ocr', 'all:indic AND all:"document layout"', 'all:telugu AND all:manuscript']:
        url = 'http://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': q, 'max_results': 100})
        try:
            x = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
            root = ET.fromstring(x); ns = {'a': 'http://www.w3.org/2005/Atom'}
            ents = root.findall('a:entry', ns)
            for e in ents:
                i = e.findtext('a:id', namespaces=ns)
                hits.setdefault(i, {'id': i, 'title': re.sub(r'\s+', ' ', e.findtext('a:title', namespaces=ns) or ''),
                                    'published': e.findtext('a:published', namespaces=ns),
                                    'abstract': re.sub(r'\s+', ' ', e.findtext('a:summary', namespaces=ns) or '')[:600], 'queries': []})['queries'].append(q)
            log.append({'query': q, 'hits': len(ents)})
        except Exception as ex:
            log.append({'query': q, 'error': str(ex)[:100]})
        time.sleep(3.5)
    return hits, log


FUNCS = dict(hf=hf, github=github, zenodo=zenodo, figshare=figshare, datacite=datacite, dataverse=dataverse,
             archive=archive, openalex=openalex, s2=s2, arxiv=arxiv)
if __name__ == '__main__':
    for p in (sys.argv[2:] or FUNCS):
        h, l = FUNCS[p]()
        json.dump({'platform': p, 'queried': time.strftime('%Y-%m-%d'), 'queries': l, 'hits': h},
                  open(os.path.join(OUT, f'{p}.json'), 'w'), ensure_ascii=False, indent=0)
        print(p, 'unique hits', len(h), 'queries', len(l), flush=True)
