"""Count pages in a MediaWiki namespace politely (sleep between calls, retry on 429)."""
import json, sys, time, urllib.request, urllib.parse, urllib.error
api, ns = sys.argv[1], sys.argv[2]
n = 0; cont = {}
while True:
    p = {"action": "query", "list": "allpages", "apnamespace": ns, "aplimit": "max", "format": "json", **cont}
    d = None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(api + "?" + urllib.parse.urlencode(p), headers={"User-Agent": "telugu-corpus-catalogue/1.0 (research)"}), timeout=60) as r:
                d = json.load(r); break
        except urllib.error.HTTPError as e:
            time.sleep(10 * (attempt + 1))
    if d is None:
        sys.exit(f"gave up after repeated HTTP errors; partial count {n}")
    n += len(d["query"]["allpages"])
    if "continue" not in d: break
    cont = d["continue"]; time.sleep(0.5)
print(api, ns, n)
