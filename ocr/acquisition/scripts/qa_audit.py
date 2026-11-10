"""Manual audit helper.

  sample  N            pick N random kept items per source (fixed seed) from data/unified/, write contact sheets to
                       data/corpus_work/audit/<source>.png and a blank verdict file qa/manual_audit.csv (if absent)
  summary              Wilson 95% intervals of label error rate per source from qa/manual_audit.csv

Verdicts are filled in by a human reviewer who reads each image: correct / wrong / unreadable,
with the corrected text when wrong.
"""
import csv, io, json, math, os, random, sys, glob
import pyarrow.parquet as pq
from PIL import Image, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
UNI = os.path.join(ROOT, 'data', 'unified')
AUD = os.path.join(ROOT, 'data', 'corpus_work', 'audit')
CSV = os.path.join(ROOT, 'qa', 'manual_audit.csv')


def sample(n):
    os.makedirs(AUD, exist_ok=True); os.makedirs(os.path.dirname(CSV), exist_ok=True)
    by_src = {}
    for p in sorted(glob.glob(os.path.join(UNI, '*', '*', '*.parquet'))):
        src = os.path.basename(p).rsplit('-', 1)[0]
        by_src.setdefault(src, []).append(p)
    rows = []
    for src, files in sorted(by_src.items()):
        rnd = random.Random('audit:' + src)
        # sample shards, then rows, without loading everything
        pool = []
        for p in rnd.sample(files, min(len(files), 6)):
            t = pq.read_table(p, columns=['uid', 'text', 'granularity'])
            idx = rnd.sample(range(t.num_rows), min(t.num_rows, n))
            pool += [(p, i, t.slice(i, 1).to_pylist()[0]) for i in idx]
        pick = rnd.sample(pool, min(n, len(pool)))
        sheet = []
        for k, (p, i, meta) in enumerate(pick):
            img = pq.read_table(p, columns=['image']).slice(i, 1).to_pylist()[0]['image']
            im = Image.open(io.BytesIO(img)).convert('RGB')
            W = 900 if meta['granularity'] != 'word' else 480
            s = min(W / im.width, (700 if meta['granularity'] != 'word' else 110) / im.height, 4)
            im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))))
            c = Image.new('RGB', (W + 40, im.height + 8), 'white'); c.paste(im, (40, 4)); ImageDraw.Draw(c).text((4, 4), str(k), fill='red')
            sheet.append(c)
            rows.append(dict(source=src, item=k, uid=meta['uid'], split=os.path.basename(os.path.dirname(p)), label=meta['text'], verdict='', corrected='', note=''))
        H = sum(c.height for c in sheet); out = Image.new('RGB', (max(c.width for c in sheet), H), 'white'); y = 0
        for c in sheet:
            out.paste(c, (0, y)); y += c.height
        out.save(os.path.join(AUD, f'{src}.png'))
    if not os.path.exists(CSV):
        with open(CSV, 'w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print('audit sheets in', AUD, 'items', len(rows))


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - m) / d, (c + m) / d)


def summary():
    rows = list(csv.DictReader(open(CSV, encoding='utf-8')))
    out = {}
    for src in sorted({r['source'] for r in rows}):
        rs = [r for r in rows if r['source'] == src and r['verdict']]
        wrong = sum(r['verdict'] == 'wrong' for r in rs); unread = sum(r['verdict'] == 'unreadable' for r in rs)
        lo, hi = wilson(wrong, len(rs))
        out[src] = dict(checked=len(rs), correct=sum(r['verdict'] == 'correct' for r in rs), wrong=wrong, unreadable=unread,
                        error_rate=round(wrong / len(rs), 3) if rs else None, ci95=(round(lo, 3), round(hi, 3)))
    json.dump(out, open(os.path.join(ROOT, 'scripts', '_audit_summary.json'), 'w'), indent=1)
    for k, v in out.items():
        print(k, v)


if __name__ == '__main__':
    {'sample': lambda: sample(int(sys.argv[2])), 'summary': summary}[sys.argv[1]]()
