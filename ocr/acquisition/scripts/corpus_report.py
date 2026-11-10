"""Aggregate statistics from data/corpus_work/assign/*.parquet -> scripts/_corpus_stats.json and DATASET_MANIFEST.csv.

python -I ocr/acquisition/scripts/corpus_report.py
"""
import collections, csv, json, os, statistics, sys
import pyarrow.parquet as pq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus_sources import SOURCES, DATA  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
WORK = os.path.join(DATA, 'corpus_work')


def main():
    stats = {}
    shards = json.load(open(os.path.join(WORK, 'shard_checksums.json'))) if os.path.exists(os.path.join(WORK, 'shard_checksums.json')) else []
    bench = json.load(open(os.path.join(WORK, 'benchmark_test_pages.json')))
    bench_pages = {'hwpage:' + p for p in bench['icdar2024_test_pages']}
    for s, spec in SOURCES.items():
        p = os.path.join(WORK, 'assign', f'{s}.parquet')
        if not os.path.exists(p):
            stats[s] = dict(source=s, collection=spec[1], input_items=0, note='no image-text pairs on disk'); continue
        t = pq.read_table(p, columns=['drop', 'split', 'text', 'text_flags', 'text_changes', 'width', 'height', 'group_id', 'orig_split']).to_pydict()
        n = len(t['drop'])
        kept = [i for i in range(n) if not t['drop'][i]]
        drops = collections.Counter(t['drop'][i] for i in range(n) if t['drop'][i])
        splits = collections.Counter(t['split'][i] for i in kept)
        changes = collections.Counter(c for i in kept for c in t['text_changes'][i].split(',') if c)
        flags = collections.Counter(c for i in kept for c in t['text_flags'][i].split(',') if c)
        lens = [len(t['text'][i]) for i in kept]
        ws = [t['width'][i] for i in kept]; hs = [t['height'][i] for i in kept]
        groups = collections.defaultdict(set)
        for i in kept:
            groups[t['split'][i]].add(t['group_id'][i])
        vocab = collections.defaultdict(set)
        for i in kept:
            vocab[t['split'][i]].add(t['text'][i])
        test_in_train = (len(vocab['test'] & vocab['train']) / len(vocab['test'])) if vocab.get('test') and vocab.get('train') else None
        moved = sum(1 for i in kept if t['orig_split'][i] not in ('unsplit', t['split'][i]) and not (t['orig_split'][i] == 'validation' and t['split'][i] == 'val'))
        stats[s] = dict(source=s, collection=spec[1], granularity=spec[2], label_type=spec[3], licence=spec[4], licence_status=spec[5],
                        redistributable=spec[6], role=spec[7], url=spec[8], input_items=n, kept=len(kept), dropped=n - len(kept),
                        drop_reasons=dict(drops), splits=dict(splits), groups_per_split={k: len(v) for k, v in groups.items()},
                        label_changes=dict(changes), kept_flags=dict(flags), unique_labels=len(set(t['text'][i] for i in kept)),
                        median_label_chars=statistics.median(lens) if lens else None,
                        median_width=statistics.median(ws) if ws else None, median_height=statistics.median(hs) if hs else None,
                        test_label_types_seen_in_train=round(test_in_train, 3) if test_in_train is not None else None,
                        moved_from_official_split=moved,
                        icdar2024_test_page_items_in_test=sum(1 for i in kept if t['group_id'][i] in bench_pages and t['split'][i] == 'test'),
                        icdar2024_test_page_items_outside_test=sum(1 for i in kept if t['group_id'][i] in bench_pages and t['split'][i] != 'test'),
                        shards=[x for x in shards if os.path.basename(x['shard']).rsplit('-', 1)[0] == s])
    json.dump(stats, open(os.path.join(ROOT, 'scripts', '_corpus_stats.json'), 'w'), ensure_ascii=False, indent=1)

    # DATASET_MANIFEST.csv : one row per source x split (exact kept counts), with licence + checksums of its shards
    rows = []
    for s, st in stats.items():
        if not st.get('kept'):
            rows.append(dict(source=s, collection=st['collection'], split='', samples=0, granularity=SOURCES[s][2], label_type=SOURCES[s][3],
                             licence=SOURCES[s][4], licence_status=SOURCES[s][5], redistributable=SOURCES[s][6], role=SOURCES[s][7],
                             annotation_quality='', shards='', shard_sha256='', source_url=SOURCES[s][8],
                             notes='texts acquired; page images not yet fetched - not counted' if s == 'wikisource_te_pages' else ''))
            continue
        for sp, k in sorted(st['splits'].items()):
            sh = [x for x in st['shards'] if f"/{sp}/" in x['shard']]
            rows.append(dict(source=s, collection=st['collection'], split=sp, samples=k, granularity=st['granularity'], label_type=st['label_type'],
                             licence=st['licence'], licence_status=st['licence_status'], redistributable=st['redistributable'], role=st['role'],
                             annotation_quality='see TRAINING_READINESS_REPORT.md', shards=len(sh),
                             shard_sha256=';'.join(f"{os.path.basename(x['shard'])}={x['sha256']}" for x in sh),
                             source_url=st['url'], notes=''))
    with open(os.path.join(ROOT, 'DATASET_MANIFEST.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    tot = collections.Counter()
    for st in stats.values():
        for sp, k in (st.get('splits') or {}).items():
            tot[(st['collection'], sp)] += k
    for k in sorted(tot):
        print(k, tot[k])


if __name__ == '__main__':
    main()
