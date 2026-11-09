#!/usr/bin/env python3
"""Check reachability of every URL in the catalogue (collection_url, license_evidence_url, evidence_urls).

Writes evidence/link_check.json  {url: {status, final_url, error, date}}; build.py folds it into VERIFICATION_LOG.csv.
Polite: max 2 concurrent requests per host, HEAD first then GET fallback.
Run:  .venv/bin/python scripts/link_check.py
"""
import csv, json, os, sys, threading, datetime, urllib.request, urllib.parse, collections
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "Mozilla/5.0 (compatible; telugu-corpus-catalogue/1.0; research link check)"
host_locks = collections.defaultdict(lambda: threading.Semaphore(2))


import ssl
INSECURE = ssl.create_default_context(); INSECURE.check_hostname = False; INSECURE.verify_mode = ssl.CERT_NONE


def encode(url):
    """Percent-encode non-ASCII characters and spaces so urllib can request Telugu-titled URLs."""
    return urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%~")


def check(url):
    host = urllib.parse.urlparse(url).netloc
    today = datetime.date.today().isoformat()
    with host_locks[host]:
        for method in ("HEAD", "GET", "GET-insecure"):
            try:
                req = urllib.request.Request(encode(url), method=method.split("-")[0], headers={"User-Agent": UA})
                ctx = INSECURE if method == "GET-insecure" else None
                with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
                    out = {"status": r.status, "final_url": r.geturl(), "date": today}
                    if ctx:
                        out["error"] = "reachable only with TLS verification disabled (invalid certificate)"
                    return url, out
            except urllib.error.HTTPError as e:
                if method == "HEAD" and e.code in (403, 404, 405, 429, 500, 501):
                    continue
                return url, {"status": e.code, "final_url": url, "error": str(e.reason)[:80], "date": today}
            except Exception as e:  # timeouts, DNS, TLS
                if method == "HEAD" or (method == "GET" and "CERTIFICATE" in str(e)):
                    continue
                return url, {"status": 0, "final_url": url, "error": type(e).__name__ + ": " + str(e)[:80], "date": today}


def main():
    urls = set()
    with open(os.path.join(ROOT, "MASTER_CATALOGUE.csv"), encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            for u in [r["collection_url"], r["license_evidence_url"]] + r["evidence_urls"].split(" | "):
                u = u.strip()
                if u.startswith("http"):
                    urls.add(u)
    with ThreadPoolExecutor(12) as ex:
        res = dict(ex.map(check, sorted(urls)))
    path = os.path.join(ROOT, "evidence", "link_check.json")
    json.dump(res, open(path, "w"), indent=1, ensure_ascii=False)
    c = collections.Counter((v["status"] // 100) * 100 if v["status"] else 0 for v in res.values())
    print(f"{len(res)} URLs checked: " + ", ".join(f"{k or 'no-response'}: {n}" for k, n in sorted(c.items())))
    for u, v in sorted(res.items()):
        if not (200 <= v["status"] < 400):
            print(f"  {v['status']}\t{u}\t{v.get('error','')}")


if __name__ == "__main__":
    main()
