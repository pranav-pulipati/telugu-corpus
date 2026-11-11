"""Follow citations of the hub Telugu OCR dataset papers through OpenAlex (metadata only).

For each seed paper, list every work that cites it, keep those whose title/abstract mention Telugu (or Indic + dataset),
and save them to evidence/discovery/citations.json for manual screening.
usage: python3 -I citations.py OUTFILE
"""
import json, re, sys, time, urllib.parse, urllib.request

UA = {'User-Agent': 'telugu-ocr-directory-research/1.0'}
SEEDS = {  # seed label -> search string used to find the OpenAlex work (DOI where known)
    'IIIT-INDIC-HW-WORDS (ICDAR 2021)': 'doi:10.1007/978-3-030-86337-1_30',
    'IIIT-HW-Telugu (ICFHR 2018)': 'title:Towards Spotting and Recognition of Handwritten Words in Indic Scripts',
    'Mozhi / Towards Deployable OCR': 'title:Towards Deployable OCR models for Indic languages',
    'IIIT-ILST benchmark': 'title:Benchmarking Scene Text Recognition in Devanagari, Telugu and Malayalam',
    'IndicSTR12': 'title:IndicSTR12: A Dataset for Indic Scene Text Recognition',
    'Konkimalla Telugu OCR database': 'title:Optical Character Recognition (OCR) for Telugu: Database, Algorithm and Application',
    'UHTelPCC': 'doi:10.1007/978-981-13-9187-3_3',
    'PHDIndic_11': 'doi:10.1007/s11042-017-4373-y',
    'Bharat Scene Text (BSTD)': 'title:Bharat Scene Text: A Novel Comprehensive Dataset and Benchmark for Indian Language Scene Text Understanding',
    'PLATTER / CHIPS': 'title:PLATTER: A Page-Level Handwritten Text Recognition System for Indic Scripts',
    'IndicDLP': 'title:IndicDLP: A Foundational Dataset for Multi-Lingual and Multi-Domain Document Layout Parsing',
    'Indiscapes': 'title:Indiscapes: Instance Segmentation Networks for Layout Parsing of Historical Indic Manuscripts',
    'HP Labs / Lipi Toolkit Telugu': 'title:Online Handwriting Recognition of Telugu Characters',
    'Synthetic data for Indic STR (Synthetic-IndicSTR)': 'title:Transfer Learning for Scene Text Recognition in Indian Languages',
}


def get(url):
    for k in range(5):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
        except Exception as e:  # noqa: BLE001
            err = str(e); time.sleep(3 * (k + 1))
    return {'_error': err}


def find(seed):
    kind, val = seed.split(':', 1)
    if kind == 'doi':
        r = get('https://api.openalex.org/works/https://doi.org/' + val)
        return r if r.get('id') else None
    r = get('https://api.openalex.org/works?' + urllib.parse.urlencode({'filter': 'title.search:' + val.replace(',', ' '), 'per-page': 5}))
    res = r.get('results') or []
    res.sort(key=lambda w: -(w.get('cited_by_count') or 0))
    return res[0] if res else None


def abstract(w):
    inv = w.get('abstract_inverted_index') or {}
    pos = sorted((p, t) for t, ps in inv.items() for p in ps)
    return ' '.join(t for _, t in pos)


out = {'queried': time.strftime('%Y-%m-%d'), 'seeds': {}, 'hits': {}}
for label, seed in SEEDS.items():
    w = find(seed)
    if not w:
        out['seeds'][label] = {'error': 'seed not found'}; continue
    wid = w['id'].rsplit('/', 1)[1]
    n, kept, cursor = 0, 0, '*'
    while cursor:
        r = get('https://api.openalex.org/works?' + urllib.parse.urlencode({'filter': f'cites:{wid}', 'per-page': 200, 'cursor': cursor,
                                                                           'select': 'id,doi,title,publication_year,abstract_inverted_index,primary_location,cited_by_count'}))
        for c in r.get('results', []):
            n += 1
            t, a = c.get('title') or '', abstract(c)
            txt = t + ' ' + a
            if re.search(r'telugu', txt, re.I) or (re.search(r'indic|indian (language|script)', txt, re.I) and re.search(r'dataset|database|corpus|benchmark', txt, re.I)):
                kept += 1
                h = out['hits'].setdefault(c['id'], {'title': t, 'year': c.get('publication_year'), 'doi': c.get('doi'),
                                                     'venue': ((c.get('primary_location') or {}).get('source') or {}).get('display_name'),
                                                     'telugu': bool(re.search(r'telugu', txt, re.I)), 'abstract': a[:700], 'cites': []})
                h['cites'].append(label)
        cursor = (r.get('meta') or {}).get('next_cursor') if r.get('results') else None
        time.sleep(0.2)
    out['seeds'][label] = {'openalex': wid, 'title': w.get('title'), 'cited_by': n, 'kept': kept}
    print(label, wid, 'citing', n, 'kept', kept, flush=True)
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print('unique kept', len(out['hits']), 'with telugu', sum(h['telugu'] for h in out['hits'].values()))
