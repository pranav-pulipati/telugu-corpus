"""Validate telugu_ocr_final.csv, the generated reports and reproducibility.

Usage (from repo root):  python3 ocr/directory/scripts/validate_directory.py
Exit code 0 = all checks passed. Prints every problem found.
"""
import csv, hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.abspath(os.path.join(HERE, '..'))
ROOT = os.path.abspath(os.path.join(DIR, '..', '..'))
sys.path.insert(0, HERE)
from common import COLUMNS, STATUSES, CATEGORIES  # noqa: E402

CSV = os.path.join(ROOT, 'telugu_ocr_final.csv')
DOCS = ['README.md', 'DATASET_DETAILS.md', 'DISCOVERY_LOG.md', 'DUPLICATE_AND_MIRROR_REPORT.md', 'UNAVAILABLE_AND_GATED_DATASETS.md',
        'LICENSING_AND_ACCESS_REPORT.md', 'COVERAGE_REPORT.md', 'CURRENT_STATE_AUDIT.md']
REQUIRED = ['Dataset ID', 'Official dataset name', 'Alternative names', 'Parent dataset', 'Dataset version', 'Dataset description', 'Official webpage URL',
            'Direct download URL', 'Hugging Face URL', 'GitHub URL', 'Kaggle URL', 'Zenodo / Figshare / archive URL', 'Research paper URL', 'DOI', 'Institution',
            'Authors', 'Language', 'Script', 'Modality', 'Task', 'Granularity', 'Real / synthetic', 'Published sample count', 'Sample count unit',
            'Annotation availability', 'Annotation type', 'Licence', 'Commercial-use permission', 'Redistribution permission', 'Access requirements',
            'Access status', 'Verification status', 'Last verified date', 'Duplicate / overlap notes', 'Dataset quality notes', 'Additional notes']
problems = []


def bad(msg):
    problems.append(msg)


def digest(paths):
    h = hashlib.sha256()
    for p in paths:
        h.update(open(p, 'rb').read())
    return h.hexdigest()


# ---- 1. reproducibility: regenerate and compare
outs = [CSV, os.path.join(DIR, 'evidence', 'counts.json')] + [os.path.join(DIR, d) for d in DOCS]
before = digest(outs)
for s in ('build_directory.py', 'make_docs.py'):
    subprocess.run([sys.executable, os.path.join(HERE, s)], check=True, stdout=subprocess.DEVNULL)
if digest(outs) != before:
    bad('Regenerating changed the committed outputs: run build_directory.py and make_docs.py and re-check.')

# ---- 2. CSV structure
rows = list(csv.reader(open(CSV, encoding='utf-8')))
head, body = rows[0], rows[1:]
if head != [h for _, h in COLUMNS]:
    bad('CSV header does not match common.COLUMNS')
missing = [c for c in REQUIRED if c not in head]
if missing:
    bad(f'missing required columns: {missing}')
R = [dict(zip(head, r)) for r in body]
for i, r in enumerate(body):
    if len(r) != len(head):
        bad(f'row {i + 2} has {len(r)} cells')
ids = [r['Dataset ID'] for r in R]
if len(set(ids)) != len(ids):
    bad('duplicate IDs')
if ids != [f'TOCR-{n:03d}' for n in range(1, len(ids) + 1)]:
    bad('IDs are not a gap-free TOCR-001.. sequence')
idset = set(ids)
for r in R:
    rid = r['Dataset ID']
    for c in head:
        if c != 'Additional notes' and not r[c].strip():
            bad(f'{rid}: empty {c}')
    if r['Verification status'] not in STATUSES:
        bad(f'{rid}: bad status')
    if r['Resource category'] not in CATEGORIES:
        bad(f'{rid}: bad category')
    if (r['Verification status'] == 'REJECTED') != (r['Resource category'] == 'Rejected'):
        bad(f'{rid}: REJECTED status and Rejected category disagree')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r['Last verified date']):
        bad(f'{rid}: bad date')
    for ref in re.findall(r'TOCR-\d{3}', ' '.join(r.values())):
        if ref not in idset:
            bad(f'{rid}: refers to missing {ref}')
    if r['Parent dataset'] not in ('NONE',) and r['Parent dataset'] not in idset:
        bad(f'{rid}: parent {r["Parent dataset"]} not an ID')
    cat = r['Resource category']
    if cat.startswith('OCR image-text'):
        if r['Modality'].lower().startswith('text'):
            bad(f'{rid}: text-only modality in image-text category')
        if r['Annotation availability'].lower().startswith(('no', 'not applicable')):
            bad(f'{rid}: image-text category but no annotations')
    if cat == 'Text-only corpus (OCR language modelling)' and 'image' in r['Modality'].lower():
        bad(f'{rid}: text-only category with image modality')
    if cat.startswith('Layout') and re.search(r'transcription', r['Annotation type'], re.I) and not re.search(r'no transcription|no cell text|not ', r['Annotation type'], re.I):
        bad(f'{rid}: layout row claims transcription')
    lic = r['Licence'].lower()
    if re.search(r'\bnc\b|by-nc|non-?commercial', lic) and r['Commercial-use permission'].lower().startswith('allowed') and 'conflict' not in lic:
        bad(f'{rid}: NC licence but commercial use "Allowed"')
    d = r['Direct download URL']
    if d.startswith('http') and not re.search(r'NOT VERIFIED|404|\{', d) and r['Verification status'] in ('UNVERIFIED',):
        bad(f'{rid}: unverified row has a bare download URL')

# ---- 3. counts in docs match the CSV
stats = json.load(open(os.path.join(DIR, 'evidence', 'counts.json')))
if stats['total_rows'] != len(R):
    bad('counts.json total_rows mismatch')
readme = open(os.path.join(DIR, 'README.md'), encoding='utf-8').read()
for label, val in [('All rows in the CSV', stats['total_rows']), ('Rejected candidates', stats['rejected']),
                   ('**Distinct datasets** (`Counts as distinct dataset` = Y)', f"**{stats['distinct_datasets']}**")]:
    if f'| {label} | {val} |' not in readme:
        bad(f'README count "{label}" != {val}')
dist = sum(r['Counts as distinct dataset'].startswith('Y') for r in R if r['Resource category'] not in ('Related resource (not a dataset)', 'Rejected'))
if dist != stats['distinct_datasets'] or sum(stats['by_status_distinct'].values()) != dist:
    bad('distinct totals do not reconcile with status breakdown')
root_readme = open(os.path.join(ROOT, 'README.md'), encoding='utf-8').read()
m = re.search(r'\((\d+) rows, (\d+) distinct', root_readme)
if not m or (int(m.group(1)), int(m.group(2))) != (len(R), dist):
    bad('root README pointer counts are stale')
for d in DOCS:
    t = open(os.path.join(DIR, d), encoding='utf-8').read()
    for ref in set(re.findall(r'TOCR-\d{3}', t)) - idset:
        bad(f'{d}: refers to missing {ref}')

# ---- 4. link check covers every URL now in the CSV
lc = os.path.join(DIR, 'evidence', 'link_check.csv')
checked = {l['URL'] for l in csv.DictReader(open(lc, encoding='utf-8'))}
sys.path.insert(0, HERE)
from link_check import FIELDS, first_url  # noqa: E402
unchecked = sorted({first_url(r[f]) for r in R for f in FIELDS if first_url(r[f])} - checked)
if unchecked:
    bad(f'{len(unchecked)} URLs not in link_check.csv (re-run link_check.py): {unchecked[:5]}')

# ---- 5. hygiene: no secrets, no big files, master catalogue untouched
pat = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE|sk-[A-Za-z0-9]{20,}|/home/[a-z]+/(Desktop|\.claude)|/tmp/claude')
for base, dirs, files in os.walk(DIR):
    dirs[:] = [d for d in dirs if d != '__pycache__']
    for f in files:
        p = os.path.join(base, f)
        if os.path.getsize(p) > 10 * 1024 * 1024:
            bad(f'large file {p}')
        if p != os.path.abspath(__file__) and pat.search(open(p, encoding='utf-8', errors='ignore').read()):
            bad(f'secret-like string or local path in {os.path.relpath(p, ROOT)}')
diff = subprocess.run(['git', '-C', ROOT, 'diff', '--name-only', 'HEAD', '--', 'MASTER_CATALOGUE.csv', 'MASTER_CATALOGUE.xlsx', 'audit', 'catalogues', 'ocr/acquisition'],
                      capture_output=True, text=True).stdout.strip()
if diff:
    bad(f'existing work modified: {diff}')

print(f'{len(R)} rows, {dist} distinct datasets, {len(checked)} links checked')
if problems:
    print(f'{len(problems)} PROBLEMS:')
    for p in problems:
        print(' -', p)
    sys.exit(1)
print('ALL CHECKS PASSED')
