import json,urllib.request,urllib.parse,random,os,sys,re,time
W="https://te.wikisource.org/w/api.php"; out=sys.argv[1]; os.makedirs(out,exist_ok=True)
UA={'User-Agent':'telugu-corpus-catalogue/1.0 (research sampling)'}
def api(**p):
    p.update(format='json')
    for k in range(5):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(W+'?'+urllib.parse.urlencode(p),headers=UA),timeout=60).read())
        except Exception as e: time.sleep(5*(k+1)); err=e
    raise err
random.seed(11)
mem=[]; cont={}
for _ in range(3):
    d=api(action='query',list='categorymembers',cmtitle='వర్గం:ఆమోదించబడ్డవి',cmlimit=500,cmnamespace=104,cmsort='timestamp',**cont)
    mem+=[m['title'] for m in d['query']['categorymembers']]
    if 'continue' not in d: break
    cont=d['continue']
# pick pages from distinct books
books={}
for t in mem:
    b=t.rsplit('/',1)[0]
    books.setdefault(b,[]).append(t)
pick=[random.choice(v) for k,v in random.sample(sorted(books.items()),min(6,len(books)))]
rows=[]
for t in pick:
    d=api(action='query',prop='revisions',titles=t,rvprop='content',rvslots='main')
    pg=next(iter(d['query']['pages'].values())); txt=pg['revisions'][0]['slots']['main']['*']
    m=re.match(r'Page:(.+?)(?:/(\d+))?$',t) or re.match(r'పుట:(.+?)(?:/(\d+))?$',t)
    fname,pno=m.group(1),m.group(2)
    p={'action':'query','prop':'imageinfo','titles':'File:'+fname,'iiprop':'url|size|mime'}
    if pno: p['iiurlparam']=f'page{pno}-1200px'
    ii=api(**p); ip=next(iter(ii['query']['pages'].values())); info=ip.get('imageinfo',[{}])[0]
    url=info.get('thumburl') or info.get('url')
    slug=re.sub(r'[^\w.-]+','_',t)[:120]
    if url:
        b=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read(); open(os.path.join(out,slug+'.jpg'),'wb').write(b)
    body=re.sub(r'<noinclude>.*?</noinclude>','',txt,flags=re.S)
    open(os.path.join(out,slug+'.txt'),'w').write(body)
    rows.append(dict(page=t,file=fname,page_no=pno,image_url=url,mime=info.get('mime'),text_chars=len(body)))
    time.sleep(1)
json.dump(dict(validated_pages_sampled_from=len(mem),books_in_sample=len(books),rows=rows),open(os.path.join(out,'_index.json'),'w'),ensure_ascii=False,indent=1)
print(json.dumps(rows,ensure_ascii=False,indent=1))
