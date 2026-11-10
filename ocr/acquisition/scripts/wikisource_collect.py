"""Collect human-proofread Telugu Wikisource pages as (page image, page text) pairs.

Stages (each resumable, results under data/wikisource_pages/):
  list    - all Page: titles in the "proofread" (level 3) and "validated" (level 4) categories
  files   - licence + URL for every scanned book file (File:...pdf/djvu) via imageinfo/extmetadata
  text    - raw wikitext of every listed page (batched 50 titles per API call)
  images  - page thumbnails (only for books whose scan licence is free), --limit N pages, --width W

Usage: python -I wikisource_collect.py list|files|text|images [--limit N] [--width 1280] [--workers 4]
Be polite: generic User-Agent, maxlag, retries with back-off. No login.
"""
import json, os, re, sys, time, urllib.parse, urllib.request, hashlib, random
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'wikisource_pages'))
API = 'https://te.wikisource.org/w/api.php'
# Wikimedia's robot policy (https://w.wiki/4wJS) requires contact details in the User-Agent; bulk image requests
# without them are refused with HTTP 429. Set WIKIMEDIA_CONTACT (an email or project URL you choose) before 'images'.
UA = {'User-Agent': f"telugu-ocr-corpus-research/1.0 ({os.environ.get('WIKIMEDIA_CONTACT', 'no contact set')})"}
CATS = {3: 'వర్గం:అచ్చుదిద్దబడినవి', 4: 'వర్గం:ఆమోదించబడ్డవి'}
FREE = re.compile(r'(public domain|^pd|cc0|cc[- ]by(-sa)?|cc by|gfdl|godl|attribution)', re.I)
os.makedirs(ROOT, exist_ok=True)


PACE = [1.5]   # seconds between API calls (raised automatically after a 429)


def get(url, binary=False, tries=8):
    for k in range(tries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120)
            b = r.read()
            if not binary:
                time.sleep(PACE[0])
            return b if binary else json.loads(b)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 503):
                PACE[0] = min(PACE[0] * 2, 20)
                wait = int(e.headers.get('Retry-After') or 0) or 60 * (k + 1)
            else:
                wait = 5 * (k + 1)
            time.sleep(wait + random.random() * 5)
        except Exception:
            time.sleep(5 * (k + 1))
    return None


def stage_dump():
    """Read Page: namespace texts and proofreading levels from the official XML dump (no API calls)."""
    import bz2, glob as g
    import xml.etree.ElementTree as ET
    path = sorted(g.glob(os.path.join(ROOT, 'dump', 'tewikisource-*-pages-articles.xml.bz2')))[-1]
    pages, n = {}, 0
    with bz2.open(path, 'rb') as fh, open(os.path.join(ROOT, 'texts.jsonl'), 'w', encoding='utf-8') as fo:
        title = ns = text = revid = ts = None
        for ev, el in ET.iterparse(fh, events=('end',)):
            tag = el.tag.rsplit('}', 1)[-1]
            if tag == 'title':
                title = el.text
            elif tag == 'ns':
                ns = el.text
            elif tag == 'id' and revid is None and title and ns == '104' and text is None:
                pass
            elif tag == 'revision':
                revid = el.findtext('{*}id'); ts = el.findtext('{*}timestamp'); text = el.findtext('{*}text') or ''
            elif tag == 'page':
                if ns == '104':
                    m = re.search(r'<pagequality\s+level="(\d)"', text or '')
                    lvl = int(m.group(1)) if m else None
                    if lvl in (3, 4):
                        pages[title] = lvl
                        fo.write(json.dumps(dict(title=title, level=lvl, revid=int(revid), timestamp=ts, wikitext=text, dump=os.path.basename(path)), ensure_ascii=False) + '\n')
                    n += 1
                title = ns = text = revid = ts = None
                el.clear()
    json.dump(pages, open(os.path.join(ROOT, 'pages.json'), 'w'), ensure_ascii=False)
    print('Page: namespace pages', n, 'proofread/validated', len(pages),
          'level3', sum(v == 3 for v in pages.values()), 'level4', sum(v == 4 for v in pages.values()))


def api(**p):
    p.update(format='json', maxlag=5)
    return get(API + '?' + urllib.parse.urlencode(p))


def stage_list():
    out = {}
    for level, cat in CATS.items():
        cont = {}
        while True:
            d = api(action='query', list='categorymembers', cmtitle=cat, cmnamespace=104, cmlimit='max', cmprop='title', **cont)
            for m in d['query']['categorymembers']:
                out[m['title']] = level
            if 'continue' not in d:
                break
            cont = d['continue']
        print(cat, 'running total', len(out), flush=True)
    json.dump(out, open(os.path.join(ROOT, 'pages.json'), 'w'), ensure_ascii=False)


def split_title(t):
    m = re.match(r'^[^:]+:(.+?)(?:/(\d+))?$', t)
    return m.group(1), (int(m.group(2)) if m.group(2) else None)


def stage_files():
    pages = json.load(open(os.path.join(ROOT, 'pages.json')))
    files = sorted({split_title(t)[0] for t in pages})
    outp = os.path.join(ROOT, 'files.json')
    done = json.load(open(outp)) if os.path.exists(outp) else {}
    todo = [f for f in files if f not in done]
    for i in range(0, len(todo), 10):   # 10 titles per call: long Telugu titles exceed URL limits (HTTP 414) at 50
        batch = todo[i:i + 10]
        d = api(action='query', prop='imageinfo', titles='|'.join('File:' + f for f in batch),
                iiprop='url|size|mime|extmetadata', iiextmetadatafilter='LicenseShortName|License|Copyrighted|UsageTerms|Artist|DateTimeOriginal')
        if not d or 'query' not in d:
            print('batch failed, will retry on next run', flush=True); time.sleep(60); continue
        norm = {n['to']: n['from'] for n in d['query'].get('normalized', [])}
        for p in d['query']['pages'].values():
            title = norm.get(p['title'], p['title'])
            f = title.split(':', 1)[1]
            ii = (p.get('imageinfo') or [{}])[0]
            em = ii.get('extmetadata') or {}
            if not isinstance(em, dict):
                em = {}
            lic = (em.get('LicenseShortName') or {}).get('value', '')
            done[f] = dict(url=(ii.get('url') or '').split('?')[0] or None, mime=ii.get('mime'), pages=ii.get('pagecount'), width=ii.get('width'),
                           repository=p.get('imagerepository'), licence=lic,
                           copyrighted=(em.get('Copyrighted') or {}).get('value', ''),
                           usage_terms=re.sub('<[^>]+>', '', (em.get('UsageTerms') or {}).get('value', ''))[:200],
                           free=bool(FREE.search(lic)))  # CC licences are "copyrighted" but free; non-free/unknown -> False
        json.dump(done, open(outp, 'w'), ensure_ascii=False, indent=0)
        print('files', len(done), '/', len(files), flush=True)


def stage_text():
    pages = json.load(open(os.path.join(ROOT, 'pages.json')))
    outp = os.path.join(ROOT, 'texts.jsonl')
    have = set()
    if os.path.exists(outp):
        for line in open(outp, encoding='utf-8'):
            have.add(json.loads(line)['title'])
    todo = [t for t in pages if t not in have]
    with open(outp, 'a', encoding='utf-8') as fo:
        for i in range(0, len(todo), 50):
            batch = todo[i:i + 50]
            d = api(action='query', prop='revisions', titles='|'.join(batch), rvprop='content|ids|timestamp', rvslots='main')
            if not d:
                continue
            norm = {n['to']: n['from'] for n in d['query'].get('normalized', [])}
            for p in d['query']['pages'].values():
                if 'revisions' not in p:
                    continue
                rv = p['revisions'][0]
                t = norm.get(p['title'], p['title'])
                fo.write(json.dumps(dict(title=t, level=pages.get(t, pages.get(p['title'])), revid=rv['revid'], timestamp=rv['timestamp'],
                                         wikitext=rv['slots']['main']['*']), ensure_ascii=False) + '\n')
            fo.flush()
            if (i // 50) % 20 == 0:
                print('text', len(have) + i + len(batch), '/', len(pages), flush=True)


def thumb_url(file_url, page, width, fname):
    # https://upload.wikimedia.org/wikipedia/commons/a/ab/X.pdf -> .../commons/thumb/a/ab/X.pdf/page5-1280px-X.pdf.jpg
    base, tail = file_url.split('/wikipedia/', 1) if '/wikipedia/' in file_url else file_url.split('/wikisource/', 1)
    proj = 'wikipedia' if '/wikipedia/' in file_url else 'wikisource'
    parts = tail.split('/')
    thumb = f'{base}/{proj}/' + '/'.join(parts[:1] + ['thumb'] + parts[1:])
    enc = urllib.parse.quote(fname.replace(' ', '_'))
    return f'{thumb}/page{page}-{width}px-{enc}.jpg'


def stage_images(limit, width, workers):
    pages = json.load(open(os.path.join(ROOT, 'pages.json')))
    files = json.load(open(os.path.join(ROOT, 'files.json')))
    imgdir = os.path.join(ROOT, 'images'); os.makedirs(imgdir, exist_ok=True)
    # validated (level 4) first, then proofread; only free-licence scans
    cand = []
    for t, lvl in pages.items():
        f, n = split_title(t)
        fi = files.get(f)
        if not fi or not fi.get('url') or not fi.get('free') or n is None:
            continue
        cand.append((-lvl, f, n, t))
    cand.sort()
    cand = cand[:limit]
    logp = os.path.join(ROOT, 'images.jsonl')
    have = set()
    if os.path.exists(logp):
        for line in open(logp, encoding='utf-8'):
            have.add(json.loads(line)['title'])

    def work(c):
        _, f, n, t = c
        if t in have:
            return None
        name = hashlib.sha1(t.encode()).hexdigest()[:20] + '.jpg'
        u = thumb_url(files[f]['url'], n, width, f)
        b = get(u, binary=True, tries=6)
        if not b or b[:2] != b'\xff\xd8':
            return dict(title=t, file=f, page=n, ok=False, url=u)
        open(os.path.join(imgdir, name), 'wb').write(b)
        return dict(title=t, file=f, page=n, ok=True, url=u, image=name, bytes=len(b), sha256=hashlib.sha256(b).hexdigest())

    with open(logp, 'a', encoding='utf-8') as fo, ThreadPoolExecutor(workers) as ex:
        for i, r in enumerate(ex.map(work, cand)):
            if r:
                fo.write(json.dumps(r, ensure_ascii=False) + '\n'); fo.flush()
            if i % 500 == 0:
                print('images', i, '/', len(cand), flush=True)


if __name__ == '__main__':
    a = sys.argv[1:]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    {'list': stage_list, 'files': stage_files, 'text': stage_text, 'dump': stage_dump}.get(a[0], lambda: None)()
    if a[0] == 'images':
        if not os.environ.get('WIKIMEDIA_CONTACT'):
            sys.exit('set WIKIMEDIA_CONTACT first (see Wikimedia User-Agent policy)')
        stage_images(opt('--limit', 10 ** 9), opt('--width', 1280), opt('--workers', 4))
