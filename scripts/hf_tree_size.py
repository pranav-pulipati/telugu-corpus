"""Sum file sizes in an HF dataset repo whose path matches a Telugu pattern. usage: hf_tree_size.py repo regex"""
import json, re, sys, urllib.request
repo, pat = sys.argv[1], re.compile(sys.argv[2])
def get(u):
    req=urllib.request.Request(u,headers={"User-Agent":"telugu-corpus-catalogue/1.0"})
    with urllib.request.urlopen(req,timeout=120) as r: return json.load(r), r.headers.get("Link","")
url=f"https://huggingface.co/api/datasets/{repo}/tree/main?recursive=true&expand=false&limit=1000"
tot=n=0; ex=[]
while url:
    try: items,link=get(url)
    except Exception as e: print(repo,"ERR",e); sys.exit()
    for it in items:
        if it.get("type")=="file" and pat.search(it["path"]):
            tot+=it.get("size",0); n+=1; ex.append(it["path"])
    m=re.search(r'<([^>]+)>;\s*rel="next"',link); url=m.group(1) if m else None
print(f"{repo}\tfiles={n}\tbytes={tot}\tGB={tot/1e9:.2f}\texamples={ex[:4]}")
