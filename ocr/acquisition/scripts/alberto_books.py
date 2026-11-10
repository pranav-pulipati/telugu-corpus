import json,urllib.request,urllib.parse,sys
def get(u):
    for k in range(4):
        try: return json.loads(urllib.request.urlopen(u,timeout=120).read())
        except Exception as e: err=e
    return {'_error':str(err)}
top=get('https://huggingface.co/api/datasets/AlbertoChestnut/telugu-ocr/tree/main')
out=[]
for x in top:
    if x['type']!='directory': continue
    L=get('https://huggingface.co/api/datasets/AlbertoChestnut/telugu-ocr/tree/main/'+urllib.parse.quote(x['path']))
    if isinstance(L,dict): out.append(dict(book=x['path'],error=L['_error'])); continue
    jp={f['path'].rsplit('.',1)[0] for f in L if f['path'].lower().endswith(('.jpg','.jpeg','.png'))}
    tx={f['path'].rsplit('.',1)[0] for f in L if f['path'].endswith('.txt')}
    out.append(dict(book=x['path'],images=len(jp),texts=len(tx),pairs=len(jp&tx),img_bytes=sum(f.get('size',0) for f in L if f['path'].lower().endswith(('.jpg','.jpeg','.png')))))
json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,indent=0)
print(len(out),sum(o.get('pairs',0) for o in out))
