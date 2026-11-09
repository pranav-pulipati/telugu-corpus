"""Count pages in a MediaWiki namespace via allpages (continuation)."""
import json, sys, urllib.request, urllib.parse
api, ns = sys.argv[1], sys.argv[2]
n=0; cont={}
while True:
    p={"action":"query","list":"allpages","apnamespace":ns,"aplimit":"max","format":"json",**cont}
    with urllib.request.urlopen(urllib.request.Request(api+"?"+urllib.parse.urlencode(p),headers={"User-Agent":"telugu-corpus-catalogue/1.0"}),timeout=60) as r: d=json.load(r)
    n+=len(d["query"]["allpages"])
    if "continue" not in d: break
    cont=d["continue"]
print(api, ns, n)
