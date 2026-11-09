"""Profile Internet Archive collections: item count, licenseurl distribution, year range, sample titles (Telugu-language items)."""
import json, sys, urllib.request, urllib.parse, collections
def q(query, fields, rows):
    u="https://archive.org/advancedsearch.php?"+urllib.parse.urlencode({"q":query,"rows":rows,"output":"json"})+"".join("&fl[]="+f for f in fields)
    with urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"telugu-corpus-catalogue/1.0"}),timeout=120) as r: return json.load(r)["response"]
out={}
for c in sys.argv[1:]:
    query=f"collection:{c} AND language:(Telugu OR tel)" if not c.startswith("Q:") else c[2:]
    r=q(query,["identifier","title","licenseurl","date","year","mediatype","rights","item_size"],5000)
    docs=r["docs"]; lic=collections.Counter(d.get("licenseurl","(none)") if isinstance(d.get("licenseurl",""),str) else str(d.get("licenseurl")) for d in docs)
    yrs=[int(str(d.get("year") or d.get("date",""))[:4]) for d in docs if str(d.get("year") or d.get("date",""))[:4].isdigit()]
    mt=collections.Counter(d.get("mediatype") for d in docs)
    size=sum(int(d.get("item_size") or 0) for d in docs)
    out[c]={"numFound":r["numFound"],"sampled":len(docs),"licenseurl":lic.most_common(5),"year_min":min(yrs) if yrs else None,"year_max":max(yrs) if yrs else None,"mediatypes":mt.most_common(4),"sampled_bytes":size,"samples":[(d["identifier"],str(d.get("title"))[:70]) for d in docs[:4]]}
    print(json.dumps({c:out[c]},ensure_ascii=False))
json.dump(out,open("ia_collection_profiles.json","w"),ensure_ascii=False,indent=1)
