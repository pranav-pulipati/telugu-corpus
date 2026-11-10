import sys,collections,json
from huggingface_hub import HfFileSystem
import pyarrow.parquet as pq
fs=HfFileSystem()
repo,glob,cols=sys.argv[1],sys.argv[2],sys.argv[3].split(',')
files=sorted(fs.glob(f'datasets/{repo}/{glob}'))
cnt={c:collections.Counter() for c in cols}; n=0
maxf=int(sys.argv[4]) if len(sys.argv)>4 else 10**9
for f in files[:maxf]:
    with fs.open(f,'rb',block_size=2**20) as fh:
        t=pq.read_table(fh,columns=cols)
    n+=t.num_rows
    for c in cols:
        for v in t.column(c).to_pylist():
            if isinstance(v,float): v=round(v,1)
            if isinstance(v,str) and len(v)>60: v=v[:60]
            cnt[c][v]+=1
print(json.dumps({'repo':repo,'files_read':min(len(files),maxf),'files_total':len(files),'rows':n,**{c:(cnt[c].most_common(25), 'distinct=%d'%len(cnt[c])) for c in cols}},ensure_ascii=False))
