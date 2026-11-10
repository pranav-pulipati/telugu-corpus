"""Independent validation of data/unified/ (run after build_corpus.py export + checksums).

Checks every shard: sha256 matches corpus_work/shard_checksums.json, every image decodes (full pixel load),
labels are non-empty and Unicode-NFC with no zero-width characters, uids are unique, and no (source, group_id)
appears in more than one split. Writes scripts/_validation.json.
python -I ocr/acquisition/scripts/validate_unified.py
"""
import collections, glob, hashlib, io, json, os, unicodedata
from multiprocessing import Pool
import pyarrow.parquet as pq
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA = os.path.join(ROOT, 'data')


def check_shard(p):
    h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    t = pq.read_table(p, columns=['uid', 'image', 'text', 'source', 'group_id'])
    bad_img = bad_txt = 0; uids = []; groups = set()
    for r in t.to_pylist():
        try:
            im = Image.open(io.BytesIO(r['image'])); im.load()
            if im.mode not in ('L', 'RGB'):
                bad_img += 1
        except Exception:
            bad_img += 1
        x = r['text']
        if not x or unicodedata.normalize('NFC', x) != x or any(c in x for c in '​‌‍﻿'):
            bad_txt += 1
        uids.append(r['uid']); groups.add((r['source'], r['group_id']))
    split = os.path.basename(os.path.dirname(p))
    return dict(shard=os.path.relpath(p, DATA), sha256=h, rows=t.num_rows, bad_images=bad_img, bad_labels=bad_txt, split=split,
                uids=uids, groups=[list(g) for g in groups])


def main():
    shards = sorted(glob.glob(os.path.join(DATA, 'unified', '*', '*', '*.parquet')))
    ref = {r['shard']: r for r in json.load(open(os.path.join(DATA, 'corpus_work', 'shard_checksums.json')))}
    with Pool(14) as pool:
        res = pool.map(check_shard, shards, chunksize=4)
    uid_count = collections.Counter(u for r in res for u in r['uids'])
    gsplits = collections.defaultdict(set)
    for r in res:
        for g in r['groups']:
            if g[1] != 'synthetic':
                gsplits[tuple(g)].add(r['split'])
    out = dict(shards=len(res), rows=sum(r['rows'] for r in res),
               checksum_mismatches=[r['shard'] for r in res if ref.get(r['shard'], {}).get('sha256') != r['sha256']],
               undecodable_or_bad_mode_images=sum(r['bad_images'] for r in res), bad_labels=sum(r['bad_labels'] for r in res),
               duplicate_uids=sum(1 for v in uid_count.values() if v > 1),
               groups_in_more_than_one_split=sum(1 for v in gsplits.values() if len(v) > 1))
    json.dump(out, open(os.path.join(ROOT, 'scripts', '_validation.json'), 'w'), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
