"""Fetch zip members whose names match a regex, via HTTP ranges, in parallel. usage: URL OUTDIR REGEX"""
import sys,os,re,runpy,struct,zlib,urllib.request,time
from concurrent.futures import ThreadPoolExecutor
url,out,rx=sys.argv[1],sys.argv[2],re.compile(sys.argv[3])
def rng(a,b):
    for k in range(6):
        try: return urllib.request.urlopen(urllib.request.Request(url,headers={'Range':f'bytes={a}-{b}','User-Agent':'Mozilla/5.0'}),timeout=120).read()
        except Exception as e: err=e; time.sleep(2*(k+1))
    raise err
size=int(urllib.request.urlopen(urllib.request.Request(url,method='HEAD',headers={'User-Agent':'Mozilla/5.0'}),timeout=60).headers['Content-Length'])
tail=rng(max(0,size-70000),size-1); i=tail.rfind(b'PK\x05\x06')
_,_,_,_,nent,cdsize,cdoff=struct.unpack('<IHHHHII',tail[i:i+20]); j=tail.rfind(b'PK\x06\x06')
if j!=-1: z=tail[j:]; cdsize=struct.unpack('<Q',z[40:48])[0]; cdoff=struct.unpack('<Q',z[48:56])[0]
cd=rng(cdoff,cdoff+cdsize-1); p=0; ents=[]
while p<len(cd) and cd[p:p+4]==b'PK\x01\x02':
    (_,_,_,meth,_,_,_,csz,usz,fnl,exl,cml,_,_,_,lho)=struct.unpack('<HHHHHHIIIHHHHHII',cd[p+4:p+46]); fn=cd[p+46:p+46+fnl].decode('utf-8','replace'); ex=cd[p+46+fnl:p+46+fnl+exl]
    if 0xFFFFFFFF in (csz,usz,lho):
        q=0
        while q<len(ex):
            hid,hsz=struct.unpack('<HH',ex[q:q+4]); vals=list(struct.unpack('<'+'Q'*(hsz//8),ex[q+4:q+4+8*(hsz//8)]))
            if hid==1:
                if usz==0xFFFFFFFF: usz=vals.pop(0)
                if csz==0xFFFFFFFF: csz=vals.pop(0)
                if lho==0xFFFFFFFF: lho=vals.pop(0)
            q+=4+hsz
    if rx.search(fn) and not fn.endswith('/'): ents.append((fn,meth,csz,lho))
    p+=46+fnl+exl+cml
print('matched',len(ents),flush=True)
def get(e):
    fn,meth,csz,off=e; d=os.path.join(out,fn)
    if os.path.exists(d): return
    h=rng(off,off+30+1024); fnl,exl=struct.unpack('<HH',h[26:30]); st=off+30+fnl+exl
    raw=rng(st,st+csz-1) if csz else b''
    os.makedirs(os.path.dirname(d),exist_ok=True); open(d,'wb').write(zlib.decompress(raw,-15) if meth==8 else raw)
with ThreadPoolExecutor(8) as ex: list(ex.map(get,ents))
print('done',len(ents))
