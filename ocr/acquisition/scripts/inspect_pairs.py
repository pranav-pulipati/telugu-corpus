"""Quality stats for image-text pairs. input: JSON list of [image_path_or_None, label, split, image_bytes_or_None] via a loader name."""
import sys,os,json,hashlib,io,statistics,re,unicodedata,collections
from PIL import Image
def tel_frac(s):
    s=[c for c in s if not c.isspace()]
    return sum(0x0C00<=ord(c)<=0x0C7F for c in s)/len(s) if s else 0
def stats(pairs,name):
    n=len(pairs); missing=0; empty=0; latin=0; puretel=0; ws=[];hs=[]; md5=collections.Counter(); labels=collections.Counter(); bad=0; splits=collections.Counter(); nonnfc=0; lens=[]
    for i,(p,lab,sp,b) in enumerate(pairs):
        splits[sp]+=1
        if b is None:
            if p is None or not os.path.exists(p): missing+=1; continue
            b=open(p,'rb').read()
        md5[hashlib.md5(b).hexdigest()]+=1
        if i%max(1,n//2000)==0:
            try: im=Image.open(io.BytesIO(b)); ws.append(im.width); hs.append(im.height)
            except Exception: bad+=1
        lab=lab or ''
        if not lab.strip(): empty+=1; continue
        labels[lab]+=1; lens.append(len(lab))
        if re.search('[A-Za-z]',lab): latin+=1
        if tel_frac(lab)>=0.999: puretel+=1
        if unicodedata.normalize('NFC',lab)!=lab: nonnfc+=1
    dup=sum(v-1 for v in md5.values() if v>1)
    return dict(dataset=name,pairs=n,splits=dict(splits),missing_images=missing,unreadable_sampled=bad,empty_labels=empty,labels_with_latin=latin,
        pure_telugu_labels=puretel,non_nfc_labels=nonnfc,unique_labels=len(labels),duplicate_image_bytes=dup,
        label_len_median=statistics.median(lens) if lens else None,
        img_w_median=statistics.median(ws) if ws else None,img_h_median=statistics.median(hs) if hs else None,
        most_common_labels=labels.most_common(5))
