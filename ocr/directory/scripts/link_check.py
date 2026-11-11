"""Record the HTTP status of every URL in telugu_ocr_final.csv (HEAD, else a 1 KB ranged GET; no bulk downloads).

Usage: python3 link_check.py telugu_ocr_final.csv ocr/directory/evidence/link_check.csv
"""
import csv, re, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

FIELDS = ['Official webpage URL', 'Direct download URL', 'Hugging Face URL', 'GitHub URL', 'Kaggle URL', 'Zenodo / Figshare / archive URL', 'Research paper URL']
UA = {'User-Agent': 'Mozilla/5.0 (research link check)'}


def first_url(s):
    m = re.search(r'https?://[^\s)(;,]+', s)
    if not m or '{' in m.group(0):          # templated download paths are not single URLs
        return None
    return m.group(0).rstrip('.')


def status(url):
    for method in ('HEAD', 'GET'):
        try:
            req = urllib.request.Request(url, method=method, headers=dict(UA, **({'Range': 'bytes=0-1023'} if method == 'GET' else {})))
            with urllib.request.urlopen(req, timeout=25) as r:
                if method == 'GET':
                    r.read(1024)
                return str(r.status), r.geturl()
        except urllib.error.HTTPError as e:
            if method == 'HEAD' and e.code in (403, 405, 400, 404, 429, 501):
                continue
            return str(e.code), url
        except Exception as e:  # noqa: BLE001
            if method == 'HEAD':
                continue
            return 'ERR ' + type(e).__name__ + ': ' + str(e)[:80], url
    return 'ERR', url


def main(src, dst):
    rows = list(csv.DictReader(open(src, encoding='utf-8')))
    jobs = []
    for r in rows:
        for f in FIELDS:
            u = first_url(r[f])
            if u:
                jobs.append((r['Dataset ID'], f, u))
    uniq = sorted({u for _, _, u in jobs})
    with ThreadPoolExecutor(8) as ex:
        res = dict(zip(uniq, ex.map(status, uniq)))
    with open(dst, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Dataset ID', 'Field', 'URL', 'HTTP status', 'Final URL'])
        for i, fld, u in jobs:
            w.writerow([i, fld, u, *res[u]])
    bad = [(i, fld, u, res[u][0]) for i, fld, u in jobs if not res[u][0].startswith(('2', '3'))]
    print(len(jobs), 'links,', len(uniq), 'unique,', len(bad), 'non-2xx')
    for b in bad:
        print(*b, sep=' | ')


if __name__ == '__main__':
    main(*sys.argv[1:3])
