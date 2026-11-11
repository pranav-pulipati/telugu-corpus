"""Build telugu_ocr_final.csv (repo root) and the count tables used by the docs.

Run from anywhere:  python3 ocr/directory/scripts/build_directory.py
"""
import csv, json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import COLUMNS, CATEGORIES, STATUSES  # noqa: E402
import entries_a, entries_b, entries_c, entries_d, entries_e  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
OUT_CSV = os.path.join(ROOT, 'telugu_ocr_final.csv')
OUT_STATS = os.path.join(HERE, '..', 'evidence', 'counts.json')

R = entries_a.R + entries_b.R + entries_c.R + entries_d.R + entries_e.R
entries_d.apply(R)
entries_e.apply(R)
R.sort(key=lambda r: r['id'])

# ---- integrity checks
ids = [r['id'] for r in R]
dupes = [i for i, c in Counter(ids).items() if c > 1]
assert not dupes, f'duplicate IDs: {dupes}'
idset = set(ids)
problems = []
for r in R:
    for ref in re.findall(r'TOCR-\d{3}', r['parent'] + ' ' + r['overlap'] + ' ' + r['distinct'] + ' ' + r['notes']):
        if ref not in idset:
            problems.append((r['id'], ref))
    if r['cat'].startswith('OCR image-text') and r['modality'].lower().startswith('text only'):
        problems.append((r['id'], 'text-only row in image-text category'))
assert not problems, problems

with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow([h for _, h in COLUMNS])
    for r in R:
        w.writerow([r[k] for k, _ in COLUMNS])


def distinct(r):
    return r['distinct'].startswith('Y')


datasets = [r for r in R if r['cat'] not in ('Related resource (not a dataset)', 'Rejected')]
stats = dict(
    total_rows=len(R),
    dataset_rows=len(datasets),
    distinct_datasets=sum(distinct(r) for r in datasets),
    distinct_unknown=sum(r['distinct'].startswith('UNKNOWN') for r in datasets),
    mirrors_or_derivatives=sum(r['distinct'].startswith('N') for r in datasets),
    related_resources=sum(r['cat'] == 'Related resource (not a dataset)' for r in R),
    rejected=sum(r['ver'] == 'REJECTED' for r in R),
    by_status={s: sum(r['ver'] == s for r in datasets) for s in STATUSES},
    by_status_distinct={s: sum(r['ver'] == s and distinct(r) for r in datasets) for s in STATUSES},
    by_category={c: sum(r['cat'] == c for r in R) for c in CATEGORIES},
    by_category_distinct={c: sum(r['cat'] == c and distinct(r) for r in R) for c in CATEGORIES},
    relationships=sum(1 for r in R if r['parent'] != 'NONE' or re.search(r'TOCR-\d{3}', r['overlap'])),
    in_existing_catalogue=sum(r['catalogue'] != 'NONE' for r in R),
    new_in_round2=sum(r['round'].startswith('Round 2') for r in R),
    new_distinct_in_round2=sum(r['round'].startswith('Round 2') and distinct(r) and r['cat'] not in ('Related resource (not a dataset)', 'Rejected') for r in R),
    new_in_round3=sum(r['round'].startswith('Round 3') for r in R),
    new_distinct_in_round3=sum(r['round'].startswith('Round 3') and distinct(r) and r['cat'] not in ('Related resource (not a dataset)', 'Rejected') for r in R),
    changed_in_round3=sum(r['changed3'] not in ('NONE',) and not r['round'].startswith('Round 3') for r in R),
    changed_in_round2=sum(r['changed'] != 'NONE' and not r['round'].startswith('Round 2') for r in R),
)
os.makedirs(os.path.dirname(OUT_STATS), exist_ok=True)
json.dump(stats, open(OUT_STATS, 'w'), indent=1)
print(json.dumps(stats, indent=1))
print('wrote', OUT_CSV)
