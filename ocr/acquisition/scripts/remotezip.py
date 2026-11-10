"""Read members of a remote zip via HTTP range requests (no full download).
usage: remotezip.py URL OUTDIR [--list] [--gt-pattern gt] [--n N]
Extracts all small text members matching pattern (gt/vocab files) and first N image members."""
import sys,struct,zlib,os,urllib.request,json,re
url,out=sys.argv[1],sys.argv[2]; N=int(sys.argv[sys.argv.index('--n')+1]) if '--n' in sys.argv else 20
import time
def rng(a,b):
    for k in range(5):
        try:
            r=urllib.request.Request(url,headers={'Range':f'bytes={a}-{b}','User-Agent':'Mozilla/5.0'})
            return urllib.request.urlopen(r,timeout=120).read()
        except Exception as e:
            err=e; time.sleep(3*(k+1))
    raise err
head=urllib.request.urlopen(urllib.request.Request(url,method='HEAD',headers={'User-Agent':'Mozilla/5.0'}),timeout=60)
size=int(head.headers['Content-Length'])
tail=rng(max(0,size-70000),size-1)
i=tail.rfind(b'PK\x05\x06'); eocd=tail[i:]
_,_,_,_,nent,cdsize,cdoff=struct.unpack('<IHHHHII',eocd[:20])
# zip64?
j=tail.rfind(b'PK\x06\x06')
if j!=-1:
    z=tail[j:]; nent=struct.unpack('<Q',z[32:40])[0]; cdsize=struct.unpack('<Q',z[40:48])[0]; cdoff=struct.unpack('<Q',z[48:56])[0]
cd=rng(cdoff,cdoff+cdsize-1)
ents=[];p=0
while p<len(cd) and cd[p:p+4]==b'PK\x01\x02':
    (ver,vneed,flag,meth,mt,md,crc,csz,usz,fnl,exl,cml,dsk,ia,ea,lho)=struct.unpack('<HHHHHHIIIHHHHHII',cd[p+4:p+46])
    fn=cd[p+46:p+46+fnl].decode('utf-8','replace'); ex=cd[p+46+fnl:p+46+fnl+exl]
    if csz==0xFFFFFFFF or usz==0xFFFFFFFF or lho==0xFFFFFFFF:
        q=0
        while q<len(ex):
            hid,hsz=struct.unpack('<HH',ex[q:q+4]); data=ex[q+4:q+4+hsz]; vals=list(struct.unpack('<'+'Q'*(hsz//8),data[:8*(hsz//8)]))
            if hid==1:
                if usz==0xFFFFFFFF: usz=vals.pop(0)
                if csz==0xFFFFFFFF: csz=vals.pop(0)
                if lho==0xFFFFFFFF: lho=vals.pop(0)
            q+=4+hsz
    ents.append(dict(name=fn,meth=meth,csz=csz,usz=usz,off=lho))
    p+=46+fnl+exl+cml
os.makedirs(out,exist_ok=True)
def get(e):
    h=rng(e['off'],e['off']+30+1024)
    fnl,exl=struct.unpack('<HH',h[26:30]); st=e['off']+30+fnl+exl
    raw=rng(st,st+e['csz']-1) if e['csz'] else b''
    return zlib.decompress(raw,-15) if e['meth']==8 else raw
files=[e for e in ents if not e['name'].endswith('/')]
summary=dict(url=url,zip_bytes=size,n_entries=len(ents),n_files=len(files),
  n_images=sum(1 for e in files if re.search(r'\.(jpe?g|png|tif+|bmp)$',e['name'],re.I)),
  text_files=[(e['name'],e['usz']) for e in files if re.search(r'\.(txt|csv|json|tsv)$',e['name'],re.I)][:50])
print(json.dumps(summary,ensure_ascii=False,indent=1))
if '--list' in sys.argv: sys.exit()
json.dump([ (e['name'],e['usz']) for e in files],open(os.path.join(out,'_listing.json'),'w'),ensure_ascii=False)
maxtxt=int(sys.argv[sys.argv.index('--maxtxt')+1]) if '--maxtxt' in sys.argv else 60_000_000
txts=[e for e in files if re.search(r'\.(txt|csv|json|tsv)$',e['name'],re.I)]
imgs=[e for e in files if re.search(r'\.(jpe?g|png|tif+|bmp)$',e['name'],re.I)]
step=max(1,len(imgs)//N); pick=imgs[::step][:N]
dirs={os.path.dirname(e['name']) for e in pick}
# global gt files (few, large-ish) always; per-image/per-folder small txt only near picked images
glob_txt=[e for e in txts if (len(txts)<=20 or e['usz']>=10000 or re.search(r'(gt|vocab|words|label)',os.path.basename(e['name']),re.I)) and e['usz']<maxtxt]
near=[e for e in txts if len(txts)>20 and e not in glob_txt and (os.path.splitext(e['name'])[0] in {os.path.splitext(x['name'])[0] for x in pick})]
for e in glob_txt+near+pick:
    sub='_text' if e in glob_txt or e in near else '_img'
    d=os.path.join(out,sub,e['name']); os.makedirs(os.path.dirname(d),exist_ok=True); open(d,'wb').write(get(e))
json.dump(summary,open(os.path.join(out,'_zipinfo.json'),'w'),ensure_ascii=False,indent=1)
