"""Fetch every Hugging Face dataset tagged language:te (with tags) and save a snapshot."""
import json, re, sys, urllib.request
out = sys.argv[1]
url = "https://huggingface.co/api/datasets?filter=language:te&limit=1000&full=true"
rows = []
while url:
    req = urllib.request.Request(url, headers={"User-Agent": "telugu-corpus-catalogue/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        rows += json.load(r)
        link = r.headers.get("Link", "")
    m = re.search(r'<([^>]+)>;\s*rel="next"', link)
    url = m.group(1) if m else None
    print(len(rows), file=sys.stderr)
json.dump(rows, open(out, "w"), ensure_ascii=False)
print(len(rows))
