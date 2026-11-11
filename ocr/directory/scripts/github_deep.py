"""Round 3: deep GitHub repository search (all pages, up to the API's 1,000-result cap per query) + file-tree check.

Uses the authenticated `gh` CLI. Metadata and file listings only; nothing is cloned.
usage: python3 -I github_deep.py OUTFILE
"""
import json, re, subprocess, sys, time

QUERIES = ['telugu', 'telugu ocr', 'telugu handwritten', 'telugu handwriting', 'telugu character recognition', 'telugu dataset', 'telugu-ocr in:name',
           'telugu text recognition', 'telugu scene text', 'telugu palm leaf', 'telugu manuscript', 'telugu digits', 'telugu letters', 'telugu alphabet',
           'telugu word recognition', 'telugu printed', 'telugu script', 'indic ocr dataset', 'indic handwritten dataset', 'indian language ocr dataset',
           'telugu inscription', 'telugu newspaper ocr', 'telugu synthetic', 'tesseract telugu', 'telugu crnn', 'telugu trocr', 'telugu htr']
OCR = re.compile(r'ocr|handwrit|charact|letter|alphabet|akshar|glyph|digit|numer|script|text.?recog|word.?recog|scene|palm|manuscript|inscript|document|'
                 r'synthetic|crnn|trocr|htr|tesseract|vattu|gunint|recogni', re.I)


def gh(path):
    for k in range(4):
        r = subprocess.run(['gh', 'api', '-H', 'Accept: application/vnd.github+json', path], capture_output=True, text=True)
        if r.returncode == 0:
            return json.loads(r.stdout)
        if 'rate limit' in (r.stderr + r.stdout).lower():
            time.sleep(60); continue
        return {'_error': (r.stderr or r.stdout)[:200]}
    return {'_error': 'rate limited'}


out = {'queried': time.strftime('%Y-%m-%d'), 'queries': [], 'repos': {}}
for q in QUERIES:
    n = total = 0
    for page in range(1, 11):
        d = gh(f'search/repositories?q={q.replace(" ", "+")}&per_page=100&page={page}')
        items = d.get('items', []) if isinstance(d, dict) else []
        total = d.get('total_count', total) if isinstance(d, dict) else total
        for it in items:
            rec = out['repos'].setdefault(it['full_name'], {'description': it.get('description'), 'stars': it.get('stargazers_count'), 'size_kb': it.get('size'),
                                                            'updated': it.get('pushed_at'), 'topics': it.get('topics'), 'queries': []})
            rec['queries'].append(q); n += 1
        if len(items) < 100:
            break
        time.sleep(2.5)
    out['queries'].append({'query': q, 'hits': n, 'total': total})
    print(q, n, total, flush=True)
    time.sleep(2.5)

# file-tree check for OCR-looking repos: count image files and label-like files
for name, rec in out['repos'].items():
    txt = name + ' ' + (rec['description'] or '') + ' ' + ' '.join(rec['topics'] or [])
    rec['ocr_like'] = bool(OCR.search(txt)) and bool(re.search(r'telugu|indic|indian', txt + ' ' + ' '.join(rec['queries']), re.I))
    if not rec['ocr_like']:
        continue
    t = gh(f'repos/{name}/git/trees/HEAD?recursive=1')
    files = [x['path'] for x in t.get('tree', []) if x.get('type') == 'blob'] if isinstance(t, dict) else []
    imgs = [f for f in files if re.search(r'\.(png|jpe?g|tiff?|bmp|gif)$', f, re.I)]
    rec['n_files'] = len(files); rec['n_images'] = len(imgs); rec['truncated'] = bool(t.get('truncated')) if isinstance(t, dict) else None
    rec['label_files'] = [f for f in files if re.search(r'(label|gt|ground.?truth|annot|transcri)[^/]*\.(txt|csv|json|tsv)$', f, re.I)][:10]
    rec['archives'] = [f for f in files if re.search(r'\.(zip|tar|tgz|gz|7z|rar|h5|hdf5|npz|pkl|pickle)$', f, re.I)][:10]
    rec['drive_links'] = None
    time.sleep(0.8)
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print('repos', len(out['repos']), 'ocr-like', sum(r['ocr_like'] for r in out['repos'].values()))
