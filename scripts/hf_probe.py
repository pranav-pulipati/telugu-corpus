"""Probe HF datasets: existence, license, gated, last modified, Telugu configs and sizes (datasets-server)."""
import json, sys, urllib.request, urllib.parse
def get(u):
    try:
        req=urllib.request.Request(u,headers={"User-Agent":"telugu-corpus-catalogue/1.0"})
        with urllib.request.urlopen(req,timeout=60) as r: return json.load(r)
    except Exception as e: return {"_error":str(e)}
out={}
for ds in [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]:
    a=get(f"https://huggingface.co/api/datasets/{ds}")
    rec={"id":ds}
    if "_error" in a: rec["error"]=a["_error"]; out[ds]=rec; print(ds,"ERR",a["_error"]); continue
    tags=a.get("tags",[]); card=a.get("cardData") or {}
    rec.update(license=[t[8:] for t in tags if t.startswith("license:")], gated=a.get("gated"), private=a.get("private"),
        lastModified=a.get("lastModified"), downloads=a.get("downloads"), size_cat=[t[15:] for t in tags if t.startswith("size_categories:")],
        tasks=[t[15:] for t in tags if t.startswith("task_categories:")], n_lang=len([t for t in tags if t.startswith("language:")]))
    cfgs=[c.get("config_name") for c in (card.get("configs") or []) if isinstance(c,dict)]
    sz=get("https://datasets-server.huggingface.co/size?dataset="+urllib.parse.quote(ds))
    tel=[]
    if "size" in sz:
        rec["total_rows"]=sz["size"]["dataset"].get("num_rows"); rec["total_bytes"]=sz["size"]["dataset"].get("num_bytes_original_files")
        for c in sz["size"].get("configs",[]):
            n=c["config"].lower()
            if any(k in n for k in ["te","tel","telugu"]) and (("tel" in n) or n in("te",) or n.startswith("te") or n.endswith("te") or "_te" in n or "te_" in n or "-te" in n or "te-" in n or ".te" in n):
                tel.append({"config":c["config"],"rows":c.get("num_rows"),"bytes":c.get("num_bytes_original_files")})
        rec["partial"]=sz.get("partial")
    else:
        rec["size_error"]=sz.get("_error") or sz.get("error")
        tel=[c for c in cfgs if c and ("tel" in c.lower() or c.lower() in ("te",) or "_te" in c.lower() or "te_" in c.lower() or "-te" in c.lower())]
    rec["telugu_configs"]=tel
    out[ds]=rec
    print(json.dumps(rec,ensure_ascii=False)[:600])
json.dump(out,open(sys.argv[2],"w"),ensure_ascii=False,indent=1)
