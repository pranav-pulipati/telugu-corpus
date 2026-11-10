import json,sys,urllib.request,urllib.parse,os,time
out=sys.argv[2]
def get(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'telugu-corpus-catalogue'}),timeout=60)
        return json.loads(r.read())
    except Exception as e: return {'_error':str(e)[:200]}
for line in open(sys.argv[1]):
    i=line.strip()
    if not i: continue
    q=urllib.parse.quote(i,safe='/')
    info=get(f'https://huggingface.co/api/datasets/{q}?blobs=false')
    tree=get(f'https://huggingface.co/api/datasets/{q}/tree/main?recursive=false')
    splits=get(f'https://datasets-server.huggingface.co/splits?dataset={urllib.parse.quote(i)}')
    size=get(f'https://datasets-server.huggingface.co/size?dataset={urllib.parse.quote(i)}')
    d=dict(id=i,info={k:info.get(k) for k in ['gated','private','disabled','cardData','tags','lastModified','downloads','_error']},
           tree=[(t.get('path'),t.get('type'),t.get('size')) for t in tree] if isinstance(tree,list) else tree,
           splits=splits,size=size)
    json.dump(d,open(os.path.join(out,i.replace('/','__')+'.json'),'w'),ensure_ascii=False,indent=1)
    print(i,'ok' if '_error' not in info else info['_error'])
