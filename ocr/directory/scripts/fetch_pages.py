"""Fetch official landing pages and keep a compact evidence record (status, final URL, title, key text).

usage: python -I fetch_pages.py URLS_FILE OUT_JSON
URLS_FILE: one URL per line (optionally 'key<TAB>url'). Pages are fetched once, politely; only text is kept.
"""
import json, re, sys, time, html, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) telugu-ocr-directory-research'}
KEYS = r'licen[cs]e|cc[ -]by|creative commons|images?\b|samples?|writers?|classes|categories|download|size:|doi|dataset|train|test|words?|characters?|pages?|access|login|subscri|request|terms'


def fetch(item):
    key, url = item
    rec = {'key': key, 'url': url, 'checked': time.strftime('%Y-%m-%d')}
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
        raw = r.read(3_000_000)
        rec.update(status=r.status, final_url=r.geturl(), content_type=r.headers.get('Content-Type'))
        t = raw.decode('utf-8', 'replace')
        title = re.search(r'<title[^>]*>(.*?)</title>', t, re.S | re.I)
        rec['title'] = html.unescape(title.group(1)).strip()[:200] if title else ''
        txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S | re.I))))
        rec['text_len'] = len(txt)
        sents = re.split(r'(?<=[.!?])\s+', txt)
        rec['evidence'] = [s[:300] for s in sents if re.search(KEYS, s, re.I) and len(s) > 25][:25]
        rec['links'] = sorted(set(l for l in re.findall(r'href="([^"]+)"', t)
                                  if re.search(r'\.(zip|tar|gz|rar|7z|pkl|hdf5|mat)\b|drive\.google|kaggle|zenodo|figshare|github\.com/[^/]+/[^/"]+$|huggingface|doi\.org|download', l, re.I)))[:40]
    except urllib.error.HTTPError as e:
        rec.update(status=e.code, error=str(e)[:120])
    except Exception as e:
        rec.update(status=None, error=str(e)[:120])
    return rec


items = []
for line in open(sys.argv[1]):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    k, u = line.split('\t', 1) if '\t' in line else (line, line)
    items.append((k, u))
with ThreadPoolExecutor(6) as ex:
    res = list(ex.map(fetch, items))
json.dump(res, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
for r in res:
    print(r['status'], '|', r['key'][:40], '|', (r.get('title') or r.get('error') or '')[:90])
