"""Write small, legally redistributable samples (8 per source) from data/unified/ into ocr/acquisition/samples/.

Only sources marked redistributable in corpus_sources.SOURCES are sampled (explicit open licence). Images are copied
byte-for-byte from the unified shards; labels.tsv records uid, split, cleaned text, licence and source URL.
python -I ocr/acquisition/scripts/make_samples.py
"""
import csv, glob, os, random, shutil, sys
import pyarrow.parquet as pq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus_sources import SOURCES  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
UNI = os.path.join(ROOT, 'data', 'unified'); OUT = os.path.join(ROOT, 'samples')

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
for src, spec in SOURCES.items():
    if not spec[6]:
        continue
    files = sorted(glob.glob(os.path.join(UNI, '*', '*', f'{src}-*.parquet')))
    if not files:
        continue
    rnd = random.Random('sample:' + src)
    d = os.path.join(OUT, src); os.makedirs(d)
    picks = []
    chosen = rnd.sample(files, min(4, len(files)))
    per = -(-8 // len(chosen))
    for p in chosen:
        t = pq.read_table(p, columns=['uid', 'image', 'image_format', 'text', 'licence'])
        for i in rnd.sample(range(t.num_rows), min(per, t.num_rows)):
            picks.append((os.path.basename(os.path.dirname(p)), t.slice(i, 1).to_pylist()[0]))
    with open(os.path.join(d, 'labels.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t'); w.writerow(['file', 'uid', 'split', 'text', 'licence', 'source_url'])
        for k, (split, r) in enumerate(picks[:8]):
            name = f"{k:02d}.{'jpg' if r['image_format'] == 'JPEG' else 'png'}"
            open(os.path.join(d, name), 'wb').write(r['image'])
            w.writerow([name, r['uid'], split, r['text'].replace('\n', ' / '), r['licence'], spec[8]])
    print(src, len(picks[:8]))
