import json,sys,glob,os,urllib.request,urllib.parse
P=sys.argv[1]; O=sys.argv[2]
def get(u):
    try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'telugu-corpus-catalogue'}),timeout=90).read())
    except Exception as e: return {'_error':str(e)[:150]}
def tel(s): return sum(0x0C00<=ord(c)<=0x0C7F for c in s)
for f in sorted(glob.glob(P+'/*.json')):
    d=json.load(open(f)); sp=(d['splits'] or {}).get('splits') if isinstance(d['splits'],dict) else None
    if not sp: continue
    pick=[s for s in sp if s['config'].lower() in ('te','telugu','tel','corpus-te','images-te')] or [s for s in sp if 'tel' in s['config'].lower()] or sp[:1]
    res=[]
    for s in pick[:2]:
        r=get('https://datasets-server.huggingface.co/first-rows?'+urllib.parse.urlencode({'dataset':d['id'],'config':s['config'],'split':s['split']}))
        if '_error' in r or 'rows' not in r: res.append((s,r)); continue
        feats=[ (x['name'],str(x['type'])[:60]) for x in r['features']]
        rows=r['rows']; tc=0; samp=[]
        for row in rows[:100]:
            rr=row['row']; txt=' '.join(str(v) for k,v in rr.items() if isinstance(v,str))
            tc+=tel(txt)
        for row in rows[:3]:
            samp.append({k:(v[:160] if isinstance(v,str) else (v.get('src','')[:80] if isinstance(v,dict) else str(v)[:100])) for k,v in row['row'].items()})
        res.append((s,{'features':feats,'n':len(rows),'telugu_chars_in_first_rows':tc,'samples':samp}))
    json.dump(res,open(os.path.join(O,os.path.basename(f)),'w'),ensure_ascii=False,indent=1)
    print('==',d['id'])
    for s,r in res:
        if 'features' in r:
            print('  ',s['config'],s['split'],'| feats',[x[0] for x in r['features']],'| tel chars',r['telugu_chars_in_first_rows'],'/',r['n'],'rows')
            for x in r['samples'][:2]: print('     ',{k:v for k,v in x.items() if not str(v).startswith('https://datasets-server')})
        else: print('  ',s['config'],'ERR',str(r)[:150])
