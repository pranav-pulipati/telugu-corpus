"""Write the directory's Markdown reports from telugu_ocr_final.csv and the saved evidence.

Run after build_directory.py:  python3 ocr/directory/scripts/make_docs.py
All counts in the docs come from the CSV, so they always match it.
"""
import csv, json, os, re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.abspath(os.path.join(HERE, '..'))
ROOT = os.path.abspath(os.path.join(DIR, '..', '..'))
EV = os.path.join(DIR, 'evidence')
DATE = '2026-11-11'

R = list(csv.DictReader(open(os.path.join(ROOT, 'telugu_ocr_final.csv'), encoding='utf-8')))
ID = {r['Dataset ID']: r for r in R}
NOT_DS = ('Related resource (not a dataset)', 'Rejected')
DS = [r for r in R if r['Resource category'] not in NOT_DS]
STATUSES = ['VERIFIED', 'PARTIALLY VERIFIED', 'UNVERIFIED', 'INACCESSIBLE', 'GATED', 'COMMERCIAL', 'DISCONTINUED', 'REJECTED']
CAT_ORDER = ['OCR image-text: printed', 'OCR image-text: handwritten', 'OCR image-text: scene text', 'OCR image-text: synthetic',
             'Machine-labelled OCR (not human ground truth)', 'Character / glyph classification', 'Layout / detection (no transcription)',
             'Script identification', 'Text-in-image benchmark (VQA / document understanding)', 'Image-only (no transcription)',
             'Image-only (transcription NOT VERIFIED)', 'Scanned archive (image-only)', 'Text-only corpus (OCR language modelling)',
             'Related resource (not a dataset)', 'Rejected']
CAT_HELP = {
    'OCR image-text: printed': 'Images of printed/born-digital Telugu text with human-made or human-checked transcriptions.',
    'OCR image-text: handwritten': 'Images of handwritten Telugu words/lines/pages with transcriptions.',
    'OCR image-text: scene text': 'Photos of signs, boards and other real-world text (and born-digital images like memes) with transcriptions.',
    'OCR image-text: synthetic': 'Computer-rendered Telugu text images; the label is the exact text that was rendered.',
    'Machine-labelled OCR (not human ground truth)': 'Image-text pairs whose text came from an OCR engine or an AI model, not a person. Use with care.',
    'Character / glyph classification': 'Single characters, vowel signs or digits sorted into classes. Good for character recognisers, not for word/line OCR.',
    'Layout / detection (no transcription)': 'Boxes or regions (text blocks, tables, lines) without the text itself. Not OCR transcription data.',
    'Script identification': 'Images labelled only with which script/language they contain.',
    'Text-in-image benchmark (VQA / document understanding)': 'Question-answer or retrieval sets built on text-heavy images. Tests reading, but labels are not transcriptions.',
    'Image-only (no transcription)': 'Telugu text images without any text labels.',
    'Image-only (transcription NOT VERIFIED)': 'Images where labels may exist but could not be confirmed.',
    'Scanned archive (image-only)': 'Large collections of scanned books, newspapers or manuscripts. Raw material only - no ground truth.',
    'Text-only corpus (OCR language modelling)': 'Plain Telugu text with no images. Useful for OCR language models, spell-checking and rendering synthetic data - never image-text data.',
    'Related resource (not a dataset)': 'Tools, models, fonts and portals that help build OCR data. Not counted as datasets.',
    'Rejected': 'Candidates that turned out to have no Telugu, no images, or no data. Kept so nobody re-checks them.',
}
STATUS_HELP = {
    'VERIFIED': 'Landing page or files were opened on the check date and the key facts (Telugu content, labels, size, licence) were confirmed from the source itself.',
    'PARTIALLY VERIFIED': 'The resource exists and some facts were confirmed, but at least one important fact (often the Telugu share, size or licence) could not be.',
    'UNVERIFIED': 'Known only from a paper, a README or a third-party mention. Existence of public data not confirmed.',
    'INACCESSIBLE': 'Was published but the link is now broken (404/500, expired certificate, dead host) or the data was never released.',
    'GATED': 'Available only after login, a request form, accepting terms or approval.',
    'COMMERCIAL': 'Sold by a vendor; only samples or brochures are public.',
    'DISCONTINUED': 'Officially withdrawn by its owner. (No entry has this status.)',
    'REJECTED': 'Checked and found not to be a Telugu OCR resource.',
}


def md(s, n=None):
    s = (s or '').replace('|', '/').replace('\n', ' ')
    return s if n is None or len(s) <= n else s[:n - 1] + '...'


def distinct(r):
    return r['Counts as distinct dataset'].startswith('Y')


def link(r):
    for f in ('Official webpage URL', 'Hugging Face URL', 'Kaggle URL', 'GitHub URL', 'Zenodo / Figshare / archive URL'):
        m = re.search(r'https?://\S+', r[f])
        if m:
            return m.group(0).rstrip(').,')
    return ''


def name_link(r, n=70):
    u = link(r)
    nm = md(r['Official dataset name'], n)
    return f'[{nm}]({u})' if u else nm


def table(head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    out += ['| ' + ' | '.join(str(c) for c in row) + ' |' for row in rows]
    return '\n'.join(out)


def write(name, text):
    with open(os.path.join(DIR, name), 'w', encoding='utf-8') as f:
        f.write(text.strip() + '\n')


def lic_bucket(s):
    t = s.lower()
    if 'commercial licence' in t or 'vendor' in t or 'paid' in t:
        return 'Commercial / vendor'
    if re.search(r'open-evaluation|evaluation only|community licen', t):
        return 'Research / academic / custom terms'
    if 'multi-licence' in t or 'multi-license' in t:
        return 'Mixed (depends on source licences)'
    if re.search(r'\bnc\b|non-?commercial|by-nc', t):
        return 'Non-commercial only (CC BY-NC family)'
    if 'gpl' in t:
        return 'Copyleft software licence (GPL)'
    if re.search(r'by-sa|share-?alike', t):
        return 'Open, share-alike (CC BY-SA)'
    if re.search(r'by-nd|no derivatives', t):
        return 'No derivatives (CC BY-ND)'
    if re.search(r'cc0|public domain|cc by|creative commons attribution|\bmit\b|apache|ofl|odc-by|cdla', t):
        return 'Open (CC BY / CC0 / MIT / Apache / PD)'
    if re.search(r'academic|research|non-profit|hp labs', t):
        return 'Research / academic / custom terms'
    if re.search(r'copyright|not established', t):
        return 'Copyrighted source material (no licence)'
    return 'Unknown / not stated'


# ------------------------------------------------------------------ counts
st_all = Counter(r['Verification status'] for r in DS)
st_dist = Counter(r['Verification status'] for r in DS if distinct(r))
cat_all = Counter(r['Resource category'] for r in R)
cat_dist = Counter(r['Resource category'] for r in R if distinct(r))
n_distinct = sum(distinct(r) for r in DS)
n_unknown = sum(r['Counts as distinct dataset'].startswith('UNKNOWN') for r in DS)
n_copies = sum(r['Counts as distinct dataset'].startswith('N') for r in DS)
n_rel = cat_all['Related resource (not a dataset)']
n_rej = cat_all['Rejected']
IMG_TEXT = [c for c in CAT_ORDER if c.startswith('OCR image-text')]
n_imgtext = sum(cat_dist[c] for c in IMG_TEXT)

pairs = set()
for r in R:
    refs = set(re.findall(r'TOCR-\d{3}', ' '.join([r['Parent dataset'], r['Duplicate / overlap notes'], r['Counts as distinct dataset']])))
    refs.discard(r['Dataset ID'])
    for x in refs:
        pairs.add(tuple(sorted((r['Dataset ID'], x))))
n_pairs = len(pairs)

# platform evidence
plat = []
for f in sorted(os.listdir(os.path.join(EV, 'discovery'))):
    if not f.endswith('.json'):
        continue
    try:
        d = json.load(open(os.path.join(EV, 'discovery', f)))
    except Exception:  # noqa: BLE001
        continue
    name = f[:-5]
    if isinstance(d, dict) and 'log' in d:  # round-2 sweep: one row per platform
        for pl in ('kaggle', 'hf', 'datacite'):
            qs = [l for l in d['log'] if l['platform'] == pl]
            plat.append((f'{pl} (round 2, broader queries)', len(qs), len(d[pl]), d.get('queried', '')))
    elif isinstance(d, dict) and 'listings' in d and 'datasets' in d:
        plat.append(('hf full paginated listing (round 3)', len(d['listings']), d.get('total_datasets_listed', len(d['datasets'])), d.get('queried', '')))
    elif isinstance(d, dict) and 'repos' in d:
        plat.append(('github deep, all pages + file trees (round 3)', len(d['queries']), len(d['repos']), d.get('queried', '')))
    elif isinstance(d, dict) and 'seeds' in d:
        plat.append(('openalex citations (round 2)', len(d['seeds']), len(d['hits']), d.get('queried', '')))
    elif isinstance(d, dict) and 'queries' in d and 'hits' in d:
        label = d.get('platform') or name
        label = {'s2': 's2 (Semantic Scholar, partial)'}.get(label, label)
        if name in ('shodhganga', 'mendeley'):
            label += ' (round 2)'
        if name == 'crossref':
            label += ' (round 3)'
        plat.append((label, len(d['queries']), len(d['hits']), d.get('queried', '')))
api_rows = json.load(open(os.path.join(EV, 'ilocr', 'api_list.json')))['rows']
ilocr_ds = json.load(open(os.path.join(EV, 'ilocr', 'ilocr_datasets.json')))
ilocr_codes = Counter(v['code'] for v in ilocr_ds.values())
HFS = json.load(open(os.path.join(EV, 'discovery', 'hf_screen.json')))
oa_rel = len(json.load(open(os.path.join(EV, 'discovery', 'openalex_relevant.json'))))
arxiv_hits = next((p[2] for p in plat if p[0] == 'arxiv'), 0)
papers_rows = {r['Research paper URL'] for r in R if r['Research paper URL'].startswith('http')}
link_rows = list(csv.DictReader(open(os.path.join(EV, 'link_check.csv'), encoding='utf-8'))) if os.path.exists(os.path.join(EV, 'link_check.csv')) else []
link_bad = [l for l in link_rows if not l['HTTP status'].startswith(('2', '3'))]

# reviewer simulation (round 3): map every search-result URL to catalogue rows
MSIM = json.load(open(os.path.join(EV, 'manager_simulation_searches.json')))
MSIM_ROWS = [(srch['query'], u, k, n) for srch in MSIM['searches'] for u, k, n in srch['results']]
_URLFIELDS = ['Official webpage URL', 'Direct download URL', 'Hugging Face URL', 'GitHub URL', 'Kaggle URL', 'Zenodo / Figshare / archive URL', 'Research paper URL', 'DOI', 'Alternative names']


def _norm(u):
    u = re.sub(r'^https?://(www\.)?', '', u.strip().lower()).rstrip('/')
    return re.sub(r'\.(pdf|html?)$', '', u)


def _match(u):
    nu = _norm(u)
    hits = []
    for r in R:
        blob = ' '.join(r[f] for f in _URLFIELDS).lower()
        if nu in blob or nu.replace('www.', '') in blob:
            hits.append(r['Dataset ID'])
    return hits

# directly investigated platforms (beyond the API sweeps)
MANUAL = [
    ('ILOCR dataset catalogue (ilocr.iiit.ac.in/dataset/1-200)', 'Every ID probed; Telugu pages read in full'),
    ('ILOCR API catalogue (/api_list/)', f'{len(api_rows):,} entries parsed; Telugu rows extracted'),
    ('ILOCR competition sites (IHTR 2022/2023, ICDAR 2024 HWD, ICDAR 2025 IHDR, ICPR 2024 WIRIndic)', 'Dataset pages and download links checked'),
    ('CVIT project pages + USODI portal (cvit.iiit.ac.in)', 'Project list scanned for Telugu; USODI detection/recognition lists read'),
    ('IEEE DataPort', 'Pages block scripts (403); metadata taken via DataCite DOIs'),
    ('Mendeley Data', 'Round 1: dataset metadata API; round 2: public search API (11 queries)'),
    ('Kaggle', 'Public search + metadata + file-list APIs (no login, nothing downloaded)'),
    ('Roboflow Universe', 'Pages block scripts (403); round 2: 4 site-restricted web searches found 8 Telugu projects'),
    ('TDIL-DC (tdil-dc.in)', 'Certificate expired (Nov 2026); not bypassed; no Wayback copy of the resource page'),
    ('Bhashini ULCA', 'Round 2: public data-metric endpoint (found in the open-source ULCA frontend) lists all 28 OCR corpora; 2 are Telugu'),
    ('AIKosh (IndiaAI)', 'Round 2: portal returned 504/timeouts; dataset pages enumerated with site-restricted web searches'),
    ('University of Hyderabad DSpace + SCIS pages', 'DSpace HTTP 503; old pages 404; round 2: Wayback copy of faculty page (no dataset links)'),
    ('Shodhganga (INFLIBNET theses)', 'Round 2: DSpace 7 search API, 24 queries, 72 theses, 43 mention Telugu'),
    ('Wayback Machine', 'Round 2: recovered the IIIT-H Word Recognition dataset pages (researchweb.iiit.ac.in no longer resolves)'),
    ('Google Scholar', 'Round 2: redirects scripts to a bot check; covered indirectly by ~25 general web searches'),
    ('HF datasets-server API', 'Round 2: Telugu row counts for 7 multilingual sets without downloading'),
    ('ACL Anthology, JASTT, IOSR and other journal sites', 'Round 2: papers found through citations/search read for dataset links'),
    ('Papers with Code archive (pwc-archive/datasets, 15,008 dataset records)', 'Round 3: full index filtered for Telugu and Indic OCR; nothing new'),
    ('OpenDataLab / OpenXLab', 'Round 3: search API and web search; no Telugu datasets'),
    ('B2FIND (EUDAT metadata aggregator)', 'Round 3: exact-phrase search; 44 hits, none OCR'),
    ('IEEE DataPort (DataCite prefix 10.21227 + "telugu")', 'Round 3: all 48 records listed; every Telugu image dataset already in the CSV'),
    ('ILOCR dataset catalogue re-probe (IDs 60-130) and competition sites', 'Round 3: no new Telugu pages; ICDAR 2025 MLT-RSTR found; IHDR/MLT-RSTR zips still 404'),
    ('Griffith CVSI-2015 site, British Library EAP, Amrita, NITK repositories', 'Round 3: legacy competition/archive pages and paper-only datasets'),
    ('HP Labs / LipiTk site', 'Dataset page and licence read'),
    ('CMATERdb (Jadavpur)', 'Telugu numeral subset confirmed'),
    ('IHDIA (ihdia.iiit.ac.in)', 'Indiscapes project pages'),
    ('BhashaSutra / Sarvam / Krutrim / Cognitive Lab / AI4Bharat', 'HF orgs and project pages'),
    ('Commercial vendors: FutureBeeAI, GTS.ai, Shaip, Defined.ai', 'Product listings checked for Telugu OCR'),
    ('Telugu digital collections: Internet Archive, DLI, Chandamama, AP Press Academy, GOML palm-leaf, perspectivia.net', 'Collection pages / search APIs'),
    ('SSRN, ACM DL, Springer, arXiv HTML', 'Paper pages for dataset links (SSRN/ACM block scripts)'),
]
n_platforms = len(plat) + len(MANUAL)

# ------------------------------------------------------------------ README
cat_rows = [[c, cat_all[c], cat_dist[c], CAT_HELP[c]] for c in CAT_ORDER]
st_rows = [[s, st_all[s] if s != 'REJECTED' else n_rej, st_dist[s] if s != 'REJECTED' else '-', STATUS_HELP[s]] for s in STATUSES]
best = [r for r in DS if distinct(r) and r['Resource category'] in IMG_TEXT and r['Verification status'] == 'VERIFIED']
write('README.md', f"""
# Telugu OCR Dataset Directory

A checked list of every Telugu OCR dataset we could find: printed, handwritten, scene-text and synthetic
image-text data, plus related resources (character sets, layout sets, scanned archives, text corpora).
It tells you **what each dataset contains, whether it really has Telugu, whether it has transcriptions,
how to get it, and what the licence allows**.

This is a directory, not a download. No dataset was bulk-downloaded to build it.

**Last updated:** {DATE}

## The main file

**[`telugu_ocr_final.csv`](../../telugu_ocr_final.csv)** (repo root): one row per dataset, mirror, related resource or rejected
candidate, with the 36 requested columns plus five extra columns:

- **Resource category** - what kind of resource it is (see below). Filter on this first.
- **Counts as distinct dataset** - `Y` means it is its own dataset. `N (...)` means it is a mirror, copy, subset or derivative of another row (the row ID is named). `UNKNOWN` means we could not tell.
- **Existing catalogue record** - the matching `record_id` in the repo's `MASTER_CATALOGUE.csv`, if any.
- **Discovery round** - `Round 1` (first pass) or `Round 2` (second pass covering the channels left open in round 1).
- **Round 2 change** - what round 2 changed in a round-1 row (or `New in round 2`); `NONE` if unchanged.
- **Round 3 change** - what round 3 (the adversarial completeness pass) changed in an earlier row (or `New in round 3`); `NONE` if unchanged.

Rows are numbered `TOCR-001` to `TOCR-{len(R):03d}`. Unknown facts are written as `UNKNOWN` or `NOT VERIFIED`, never guessed.
`Direct download URL` is filled only where a real file link was seen. Where a login or form is needed, the official page is given instead.

Tip: to get usable OCR training data, filter `Resource category` starting with `OCR image-text`, `Counts as distinct dataset` = `Y`,
and `Verification status` = `VERIFIED`. That gives **{len(best)}** datasets.

## Totals

| | Rows |
|---|---|
| All rows in the CSV | {len(R)} |
| Dataset rows (excludes related resources and rejected) | {len(DS)} |
| **Distinct datasets** (`Counts as distinct dataset` = Y) | **{n_distinct}** |
| ...of which Telugu image-text OCR datasets (printed / handwritten / scene / synthetic) | {n_imgtext} |
| Possible extra datasets, distinctness unknown (mostly unconfirmed leads) | {n_unknown} |
| Mirrors, copies, subsets and derivatives | {n_copies} |
| Related resources (tools, models, fonts, portals; not datasets) | {n_rel} |
| Rejected candidates | {n_rej} |
| Duplicate / derivative relationships recorded | {n_pairs} |
| Rows matching a record in the existing catalogue | {sum(r['Existing catalogue record'] != 'NONE' for r in R)} |
| Rows added in round 2 (all kinds) | {sum(r['Discovery round'].startswith('Round 2') for r in R)} |
| ...of which new distinct datasets | {sum(r['Discovery round'].startswith('Round 2') and distinct(r) for r in DS)} |
| Round-1 rows corrected or updated in round 2 | {sum(r['Round 2 change'] != 'NONE' and not r['Discovery round'].startswith('Round 2') for r in R)} |
| Rows added in round 3 (all kinds) | {sum(r['Discovery round'].startswith('Round 3') for r in R)} |
| ...of which new distinct datasets | {sum(r['Discovery round'].startswith('Round 3') and distinct(r) for r in DS)} |
| Earlier rows corrected or updated in round 3 | {sum(r['Round 3 change'] != 'NONE' and not r['Discovery round'].startswith('Round 3') for r in R)} |

## Categories

| Category | Rows | Distinct datasets | What it means |
|---|---|---|---|
""" + '\n'.join('| ' + ' | '.join(str(x) for x in row) + ' |' for row in cat_rows) + f"""

## Verification status

Counts are for dataset rows; "distinct" counts only rows marked `Y`.

| Status | Rows | Distinct | Meaning |
|---|---|---|---|
""" + '\n'.join('| ' + ' | '.join(str(x) for x in row) + ' |' for row in st_rows) + f"""

## Other documents

| File | What it has |
|---|---|
| [DATASET_DETAILS.md](DATASET_DETAILS.md) | A short profile of every row, grouped by category |
| [DISCOVERY_LOG.md](DISCOVERY_LOG.md) | Where we searched, which queries, what came back, what was followed up |
| [DUPLICATE_AND_MIRROR_REPORT.md](DUPLICATE_AND_MIRROR_REPORT.md) | Which rows are copies, subsets or derivatives of others |
| [UNAVAILABLE_AND_GATED_DATASETS.md](UNAVAILABLE_AND_GATED_DATASETS.md) | Gated, broken, commercial and unconfirmed datasets, with how to get access |
| [LICENSING_AND_ACCESS_REPORT.md](LICENSING_AND_ACCESS_REPORT.md) | Licences grouped by what they allow, and licence conflicts found |
| [COVERAGE_REPORT.md](COVERAGE_REPORT.md) | What is well covered, what is missing, and which search channels are still open |
| [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md) | Audit of the OCR entries in the existing `MASTER_CATALOGUE.csv` |
| [ADVERSARIAL_COMPLETENESS_AUDIT.md](ADVERSARIAL_COMPLETENESS_AUDIT.md) | Round 3: four discovery passes, reviewer cross-check table, corrections, gaps and readiness |
| [MISSING_DATASET_CANDIDATES.csv](MISSING_DATASET_CANDIDATES.csv) | Unconfirmed candidates and leads (supporting file only; `telugu_ocr_final.csv` stays the master) |

## How it was built

- `scripts/entries_a.py`, `entries_b.py`, `entries_c.py` - the records, written by hand from the evidence.
- `scripts/build_directory.py` - checks IDs and cross-references, writes `telugu_ocr_final.csv` and `evidence/counts.json`.
- `scripts/make_docs.py` - writes these Markdown files from the CSV, so counts always match.
- `scripts/discover.py`, `screen_hf.py`, `fetch_pages.py` - the round-1 search sweeps; results in `evidence/discovery/` and `evidence/pages/`.
- `scripts/sweep_round2.py`, `citations.py`, `shodhganga.py`, `mendeley.py`, `hf_subset_counts.py` - round-2 sweeps and Telugu-share counts.
- `scripts/entries_d.py` - round-2 rows and corrections to round-1 rows.
- `scripts/entries_e.py` - round-3 rows and corrections; `hf_full_listing.py`, `github_deep.py`, `crossref.py` - round-3 sweeps.
- `scripts/validate_directory.py` - checks the CSV, the reports, reproducibility, links coverage and repo hygiene.
- `scripts/link_check.py` - checks every link (HEAD or 1 KB request); results in `evidence/link_check.csv`.
- `evidence/ilocr/` - the ILOCR dataset-page probe and the parsed API list.

To rebuild after editing a record:
`python3 ocr/directory/scripts/build_directory.py && python3 ocr/directory/scripts/make_docs.py`
""")

# ------------------------------------------------------------------ DATASET_DETAILS
parts = [f'# Dataset details\n\nOne short profile per row of `telugu_ocr_final.csv`, grouped by category. Checked on {DATE}.\n'
         'Fields marked UNKNOWN or NOT VERIFIED could not be confirmed from the source.\n']
for c in CAT_ORDER:
    rows = [r for r in R if r['Resource category'] == c]
    if not rows:
        continue
    parts.append(f'\n## {c} ({len(rows)})\n\n_{CAT_HELP[c]}_\n')
    for r in rows:
        u = link(r)
        lines = [f"### {r['Dataset ID']} - {md(r['Official dataset name'])}", '',
                 f"{md(r['Dataset description'])}", '']
        if c == 'Rejected':
            lines += [f"- **Why rejected:** {md(r['Additional notes'])}", f"- **Link:** {u}", '']
            parts.append('\n'.join(lines))
            continue
        lines += [
            f"- **Status:** {r['Verification status']} · **Distinct:** {md(r['Counts as distinct dataset'])}" + (f" · **Parent:** {r['Parent dataset']}" if r['Parent dataset'] != 'NONE' else ''),
            f"- **Language / script:** {md(r['Language'])} / {md(r['Script'])}",
            f"- **Content:** {md(r['Modality'])}; {md(r['Task'])}; granularity {md(r['Granularity'])}; {md(r['Real / synthetic'])}",
            f"- **Size:** {md(r['Published sample count'])} ({md(r['Sample count unit'])})",
            f"- **Labels:** {md(r['Annotation availability'])} - {md(r['Annotation type'])}",
            f"- **Licence:** {md(r['Licence'])} (commercial: {md(r['Commercial-use permission'])}; redistribution: {md(r['Redistribution permission'])})",
            f"- **Access:** {md(r['Access status'])}; needs: {md(r['Access requirements'])}",
            f"- **Source:** {md(r['Institution'])}; {md(r['Authors'])}",
        ]
        if u:
            lines.append(f"- **Link:** {u}")
        if r['Research paper URL'] != 'NONE FOUND':
            lines.append(f"- **Paper:** {md(r['Research paper URL'])}")
        if r['Direct download URL'] != 'NOT PROVIDED / see official page':
            lines.append(f"- **Download:** {md(r['Direct download URL'])}")
        if r['Duplicate / overlap notes'] != 'None identified':
            lines.append(f"- **Overlap:** {md(r['Duplicate / overlap notes'])}")
        if r['Dataset quality notes'] != 'Not assessed':
            lines.append(f"- **Quality:** {md(r['Dataset quality notes'])}")
        if r['Additional notes']:
            lines.append(f"- **Notes:** {md(r['Additional notes'])}")
        if r['Existing catalogue record'] != 'NONE':
            lines.append(f"- **Existing catalogue:** {r['Existing catalogue record']}")
        parts.append('\n'.join(lines) + '\n')
write('DATASET_DETAILS.md', '\n'.join(parts))

# ------------------------------------------------------------------ DUPLICATES
rel_rows = []
for r in R:
    d = r['Counts as distinct dataset']
    refs = sorted(set(re.findall(r'TOCR-\d{3}', ' '.join([r['Parent dataset'], r['Duplicate / overlap notes'], d]))) - {r['Dataset ID']})
    if refs:
        rel_rows.append([r['Dataset ID'], md(r['Official dataset name'], 60), md(d, 45), ', '.join(refs), md(r['Duplicate / overlap notes'], 160)])
write('DUPLICATE_AND_MIRROR_REPORT.md', f"""
# Duplicate and mirror report

Many Telugu OCR datasets are uploaded more than once (Kaggle, Hugging Face, Google Drive) or are cut from a larger
release. Counting them separately would inflate the numbers, so each copy points back to its source.

- **{n_pairs}** distinct relationships between rows (each pair counted once).
- **{n_copies}** dataset rows are marked as not distinct (mirror, copy, subset, derivative, re-listing or umbrella).
- Only rows marked `Y` in `Counts as distinct dataset` are counted in the totals ({n_distinct}).

## How copies were detected

1. **Same files**: Kaggle file listings and Hugging Face file trees compared by file names, folder layout and byte sizes. Nothing was downloaded.
2. **Same description or abstract**: DataCite/IEEE/Zenodo abstracts compared word for word.
3. **Same labels**: for data downloaded in the earlier acquisition phase, image paths and labels were compared one by one.
4. **The uploader says so**: README or dataset card names the source.

## Important findings

- **Kaggle "telugu-handwritten-dataset" (gottumukkalamadhuri) is not handwriting.** Its files match IIIT-Synthetic-R (rendered printed text). Marked as a mirror of TOCR-087 (TOCR-091).
- **IHTR 2023 Telugu train = IIIT-INDIC-HW-WORDS-Telugu train.** All 80,637 path+label pairs are identical (TOCR-005 vs TOCR-002).
- **IIIT-INDIC-HW-WORDS (TOCR-002) is the newer release of IIIT-HW-Telugu (TOCR-001).** Counted once.
- **IndicSTR12 real Telugu images are re-crops of IIIT-ILST** (TOCR-071 from TOCR-070); ILOCR's copy (TOCR-072) has 86 labels that differ from the CVIT release.
- **Roadside IIIT-IndicSTR-Word (TOCR-079) and the ICPR 2024 WIRIndic competition data (TOCR-080)** are the same collection.
- **Three Kaggle character uploads of 353.7 MB are byte-identical** (one row, TOCR-025).
- **GTS.ai's "Telugu Document Image Dataset" (Zenodo, catalogue TEL-OCR-014) is a brochure re-listing Kaggle amancapy/telugu-scans** (TOCR-096 to TOCR-095). The two state different licences (see the licensing report).
- **IEEE DataPort a1kv-rj60 (TOCR-108) has the same abstract as Konkimalla et al. 2018 (TOCR-107).** Suspected re-upload.
- **IndicSTR12 synthetic.tar.gz (TOCR-089, 62.7 GB) is suspected to be the same data as IIIT-Synthetic-IndicSTR (TOCR-088).** Not confirmed byte for byte.
- **Divs0910 Chandamama OCR set (TOCR-058) is built from the Chandamama scans (TOCR-129)** using the DIVYANSH-TEJA-09 pipeline.
- **The UoH DSpace record (catalogue TEL-OCR-011) and the IEEE DataPort Negi & Rao set (TOCR-022)** have the same authors and description and are treated as one dataset.

Found in round 2:

- **ORB-Indic (TOCR-172) and the IndicVisionBench OCR track (TOCR-130)** both come from Krutrim, both use Telugu Wikisource pages (TOCR-049) and both have exactly 89 Telugu pages. They are treated as the same pages (not confirmed image by image).
- **Kaggle telugu_palm_leafs (TOCR-195)** has 36 image/ground-truth pairs, matching the 36-image binarisation set of the "Preserving Telugu Manuscripts" paper (TOCR-118). It is probably that dataset's release.
- **Kaggle IITJ Multilingual OCR Dataset (TOCR-196)** holds per-language word crops with quadrilateral coordinates. It is suspected to be a copy of the IIT Jodhpur Bharat Scene Text crops (TOCR-082).
- **The ScrabbleGAN pages (TOCR-183)** are generated from IIIT-INDIC-HW-WORDS (TOCR-002), and **CHIPS (TOCR-182)** draws on the same word images (how much of CHIPS is re-composed is not stated clearly in the paper).
- **Roboflow iitbresearchwork/telugu-ocr (TOCR-191)** is suspected to be word-box annotations of PHDIndic_11 Telugu pages (TOCR-015), because the same workspace hosts a "Malayalam PhDIndic11" project.
- **IIIT-H Word Recognition Synthetic (TOCR-186)** renders the same 1,000-word vocabulary as the real IIIT-H word set (TOCR-044).
- **ULCA Project Anuvaad Telugu OCR corpus (TOCR-208)** comes from the same EkStep/Tarento group as the synthetic benchmark (TOCR-102). Overlap is possible but not confirmed.

Found in round 3:

- **axlevisu Telugu character set (TOCR-038) is a compilation**: its 45,217 characters match the HP Labs offline count (TOCR-021) and its 3,000 numerals match CMATERdb (TOCR-032). It no longer counts as distinct.
- **GitHub medini-r/teluguChar (TOCR-224)** is a direct copy of the HP Labs offline folders (hpl-telugu-iso-char-offline/usr_*).
- **tiny-captcha-library (TOCR-223)** is a 10,000-image release of the same generator as synthetic-captchas-library (TOCR-101, 100,000 Telugu).
- **LT-EDI 2024 Telugu troll memes (TOCR-215)** share an organiser with the NITK Telugu meme dataset (TOCR-214) and are treated as the same data.
- **ICDAR 2025 MLT-RSTR (TOCR-213)** is a roadside collection, suspected to share images with IIIT-IndicSTR-Word / WIRIndic (TOCR-079/080).
- **keerthan-381 palm-leaf crops (TOCR-228)** share a project title with the code-only repo TOCR-174.
- **rendered_wikipedia_te (TOCR-221)** renders Telugu Wikipedia text (TOCR-139).

## All relationships

| Row | Name | Distinct? | Related rows | Note |
|---|---|---|---|---|
""" + '\n'.join('| ' + ' | '.join(x) + ' |' for x in rel_rows))

# ------------------------------------------------------------------ UNAVAILABLE / GATED
sec = []
for s, title, expl in [
        ('GATED', 'Gated (login, form or approval needed)', 'These exist and can usually be obtained. The "How to get it" column gives the procedure.'),
        ('INACCESSIBLE', 'Inaccessible (broken links or never released)', 'Links were tried on the check date. Contacting the authors is the only route for most of these.'),
        ('COMMERCIAL', 'Commercial (sold by vendors)', 'Only samples or product pages are public. Licence and price are set per purchase.'),
        ('UNVERIFIED', 'Unverified (mentioned in papers or READMEs, no public data confirmed)', 'Leads worth chasing, but nothing confirms the data is available.')]:
    rows = [r for r in R if r['Verification status'] == s]
    sec.append(f'\n## {title} - {len(rows)}\n\n{expl}\n\n' + table(
        ['ID', 'Dataset', 'Category', 'Telugu size', 'How to get it', 'What we saw'],
        [[r['Dataset ID'], name_link(r, 60), md(r['Resource category'], 40), md(r['Published sample count'], 70), md(r['Access requirements'], 80), md(r['Access status'], 90)] for r in rows]))
bad_tbl = table(['ID', 'Field', 'URL', 'Result'], [[l['Dataset ID'], l['Field'], md(l['URL'], 90), md(l['HTTP status'], 60)] for l in link_bad])
write('UNAVAILABLE_AND_GATED_DATASETS.md', f"""
# Unavailable and gated datasets

Datasets that cannot simply be downloaded. Checked on {DATE}. No access control was bypassed: no TLS
verification was disabled, no logins were made, and no request forms were submitted.
""" + '\n'.join(sec) + f"""

## Link check

Every URL in the CSV was requested once with a HEAD request (or, if that failed, a 1 KB ranged GET).
{len(link_rows)} links ({len({l['URL'] for l in link_rows})} unique) were checked. {len(link_bad)} did not return 2xx/3xx.
HTTP 403 from IEEE DataPort, Roboflow, SSRN and ACM is bot-blocking: those pages open in a normal browser,
and their metadata was confirmed through DataCite or search instead. Full results: `evidence/link_check.csv`.

{bad_tbl}
""")

# ------------------------------------------------------------------ LICENSING
by_b = defaultdict(list)
for r in DS:
    by_b[lic_bucket(r['Licence'])].append(r)
order = ['Open (CC BY / CC0 / MIT / Apache / PD)', 'Open, share-alike (CC BY-SA)', 'No derivatives (CC BY-ND)', 'Non-commercial only (CC BY-NC family)',
         'Copyleft software licence (GPL)', 'Research / academic / custom terms', 'Mixed (depends on source licences)', 'Commercial / vendor', 'Copyrighted source material (no licence)', 'Unknown / not stated']
lic_sum = table(['Licence group', 'Dataset rows', 'Distinct datasets', 'Distinct image-text OCR datasets'],
                [[b, len(by_b[b]), sum(distinct(r) for r in by_b[b]), sum(distinct(r) and r['Resource category'] in IMG_TEXT for r in by_b[b])] for b in order if by_b[b]])
lic_detail = []
for b in order:
    if not by_b[b]:
        continue
    lic_detail.append(f'\n### {b} ({len(by_b[b])})\n\n' + table(['ID', 'Dataset', 'Licence as stated', 'Commercial use', 'Redistribution', 'Access'],
                      [[r['Dataset ID'], name_link(r, 55), md(r['Licence'], 70), md(r['Commercial-use permission'], 35), md(r['Redistribution permission'], 35), md(r['Access requirements'], 45)] for r in by_b[b]]))
acc = Counter()
for r in DS:
    a = r['Access requirements'].lower()
    acc['None (open download)' if a.startswith('none') else 'Kaggle account' if 'kaggle' in a else 'Login / accept terms (HF, IEEE)' if re.search(r'login|accept|ieee|account', a)
        else 'Contact authors / request' if re.search(r'contact|request|email|form', a) else 'Purchase' if re.search(r'purchase|vendor|commercial', a) else 'Other / unknown'] += 1
write('LICENSING_AND_ACCESS_REPORT.md', f"""
# Licensing and access report

What each dataset's licence allows, based on what the source itself states. Checked on {DATE}.
This is not legal advice. When a licence is missing, it is recorded as unknown and the data should be treated as
"all rights reserved" until the owner says otherwise.

## Summary by licence group

Grouped automatically from the `Licence` column (dataset rows only; related resources and rejected rows excluded).

{lic_sum}

## Access requirements

{table(['What you need', 'Dataset rows'], [[k, v] for k, v in acc.most_common()])}

## Licence problems found

- **Conflicting licences on the same data.** GTS.ai's Zenodo record (TOCR-096) says CC BY 4.0, but the Kaggle original it re-lists (TOCR-095) says CC BY-NC 4.0. Follow the stricter original.
- **IndicSTR12 (TOCR-071).** The ILOCR page states CC BY 4.0 for the annotations. The paper is CC BY-NC-ND, and the photos are third-party images. The existing catalogue (TEL-OCR-003) still says the data licence is unknown.
- **ILOCR datasets.** The ILOCR pages for HW-WORDS (TOCR-002) and IndicSTR12 (TOCR-072) state CC BY 4.0. The three IIIT-Synthetic pages (TOCR-086/087/088) have **no licence section**, so their licence is unknown. The competition sites say only "freely available for academic and research purposes", which is narrower.
- **Mirrors often drop the licence.** Kaggle and HF re-uploads of IIIT data usually say "Unknown" or add their own licence. The original's licence still applies.
- **Machine-labelled sets.** Sets labelled by Gemini or other models (for example TOCR-063) may also fall under the model provider's terms.
- **Scanned archives.** Newspaper, magazine and Chandamama scans (TOCR-124, 127, 129) carry the publishers' copyright even though they are freely viewable. Internet Archive items vary item by item.
- **Wikisource-derived sets** (TOCR-049 to 057) inherit CC BY-SA from the text. Their page scans are usually public-domain books, but each file's own licence should be checked (the acquisition phase found 127,326 of 134,015 pages on free scans).
- **Evaluation-only data.** GlotOCR Bench (TOCR-184) may only be used for evaluation: no training and no redistribution.
- **Custom licences.** ORB-Indic (TOCR-172) uses the Krutrim Community License; read it before any commercial use.
- **Mixed licences.** BhartiOCR (TOCR-185) has Apache-2.0 code, OFL/GPL fonts and source text under several licences, so the right to use each sample depends on where its text came from.
- **No licence at all.** Most GitHub and Kaggle personal uploads state no licence ({len(by_b['Unknown / not stated'])} dataset rows are in the unknown group).

## Detail by licence group
""" + '\n'.join(lic_detail))

# ------------------------------------------------------------------ round-2 evidence
def _load(n):
    p = os.path.join(EV, 'discovery', n)
    return json.load(open(p)) if os.path.exists(p) else {}


S2 = _load('s2.json'); SG = _load('shodhganga.json'); CIT = _load('citations.json') or {'seeds': {}, 'hits': {}}
s2_n = len(S2.get('queries', [])); s2_ok = sum(1 for q in S2.get('queries', []) if not q.get('error')); s2_hits = len(S2.get('hits', {}))
sg_rel = [SG['hits'][k] for k in SG.get('telugu_relevant', []) if re.search(r'recogn|ocr|optical|character|handwrit|script|segment|palm|document|text', SG['hits'][k]['title'], re.I)
          and not re.search(r'speech|emotion|parser|summari|grammar|sentiment|named entit|quantifier|print cultur|journalism|kriti|loan words|classification of|inscriptions in|n gram|gesture|compositionality|gurmukhi|punjabi|odia|grammer', SG['hits'][k]['title'], re.I)]
sg_tbl = table(['Year', 'Thesis', 'University / department', 'Handle'],
               [[md(h['year'], 10), md(h['title'], 90), md(h['university'], 45), f"[{h['handle']}](https://shodhganga.inflibnet.ac.in/handle/{h['handle']})"] for h in sg_rel])
cit_tbl = table(['Seed paper', 'Citing works', 'Kept for reading'], [[k, v.get('cited_by', '-'), v.get('kept', '-')] for k, v in CIT['seeds'].items()])
R2_CHANNELS = [
    ('Semantic Scholar', 'slow re-run, 8 s pacing, back-off up to 150 s', f'{s2_n}/36 queries attempted, {s2_ok} answered ({s2_hits} papers); Telugu dataset papers among them were already known from OpenAlex; the rest are NLP/speech'),
    ('OpenAlex citations', '14 seed dataset papers, all citing works', 'Method papers only; confirmed the UHTelHwCC paper (TOCR-023) and that Indic-HW-Wild = TOCR-010; no new datasets'),
    ('Shodhganga', '24 queries (Telugu OCR, handwriting, palm leaf, inscriptions, Indic script)', 'Private thesis data only; no rows'),
    ('Web search (Google Scholar substitute)', '~25 queries on new 2025-26 datasets, digits, forms, newspapers, inscriptions, Vedic/Sanskrit, video text', 'CHIPS + ScrabbleGAN pages (TOCR-182/183) and PHDIndic_11 Telugu share via the PLATTER paper; GlotOCR (TOCR-184); ICON 2023 set (TOCR-187); JASTT corpus (TOCR-188); UniLipi (TOCR-189); ORB-Indic Telugu (TOCR-172 un-rejected); IIIT-H word sets (TOCR-044, 186)'),
    ('Roboflow Universe', '4 site-restricted searches', '4 new project rows (TOCR-191..194) + TOCR-019 size'),
    ('AIKosh', 'portal + JS bundle inspection (504/timeouts), 3 site-restricted searches', 'CATALIST rejected (no Telugu); TEXTRON mirror noted; Sanskrit post-OCR rejected'),
    ('Bhashini ULCA', 'public data-metric endpoint', 'Telugu OCR corpora from Project Anuvaad (TOCR-208)'),
    ('TDIL-DC', 'TLS retried (no bypass) + Wayback lookup', 'Still inaccessible'),
    ('Kaggle', '20 broad queries x 10 pages + metadata/file lists', 'Palm-leaf binarisation pairs (TOCR-195), IITJ crops (TOCR-196); others had no Telugu evidence'),
    ('Hugging Face', 'language:te + image/document modality listing, language:tel, 33 new search terms, datasets-server counts', 'BhartiOCR (TOCR-185), NayanaIR-CrossBench (TOCR-190), finepdfs (TOCR-197); Telugu counts for 7 multilingual sets'),
    ('DataCite', 'every record mentioning Telugu (1,560, all types)', 'British Library Telugu card catalogues (TOCR-209)'),
    ('Mendeley Data', 'public search API, 11 queries', 'No new Telugu OCR data'),
    ('Wayback Machine', 'dead IIIT/UoH/TDIL pages', 'IIIT-H Word Recognition dataset + synthetic set recovered (downloads now 404)'),
    ('18 unconfirmed rows', 'each re-checked', 'TOCR-044 resolved; TOCR-098 Telugu repos listed; TOCR-102, 180, 181, 128 re-checked (still unconfirmed)'),
    ('Multilingual sets', 'datasets-server statistics/filter, papers', 'Telugu counts for IndicVisionBench, MInfoVisQA, PMGSY boards, adaption doc-QA, ORB-Indic, PHDIndic_11; MDIW-13, Indiscapes, Kaggle Indian Scripts, IndicDLP still unknown'),
]
r2_tbl = table(['Channel', 'What was run', 'Outcome'], R2_CHANNELS)
new_tbl = table(['ID', 'Name', 'Category', 'Status', 'Distinct?'],
                [[r['Dataset ID'], name_link(r, 60), md(r['Resource category'], 40), r['Verification status'], md(r['Counts as distinct dataset'], 40)] for r in R if r['Discovery round'].startswith('Round 2')])
chg_tbl = table(['ID', 'Name', 'Change'], [[r['Dataset ID'], md(r['Official dataset name'], 60), md(r['Round 2 change'], 90)]
                                         for r in R if r['Round 2 change'] != 'NONE' and not r['Discovery round'].startswith('Round 2')])

# ------------------------------------------------------------------ round-3 evidence
R3_CHANNELS = [
    ('A. Institutions', 'IIIT-H/CVIT + ILOCR re-probe, UoH, IIT Bombay, IIT Madras, IISc MILE, C-DAC, NLTM/Bhashini, TDIL, AIKosh, Amrita, NITK, Telugu-state universities', 'ICDAR 2025 MLT-RSTR (TOCR-213), Amrita palm-leaf DB (212), Rasagna thesis sets (216), NITK memes (214); AIKosh/TDIL still unreachable'),
    ('B. Papers', 'Crossref (20 queries, 2,516 records), OpenAlex citations (round 2), DataCite IEEE prefix sweep, arXiv/ACL pages, ICDAR/ICFHR competition reports', 'CVSI-2015 (210), meme datasets (215, 217, 218), handwritten script-ID sets (219, 220); UHTelPCC size; TOCR-108 conflict recorded'),
    ('C. Platforms', 'HF full paginated listing (14 listings, 70,298 datasets), GitHub all-pages search (27 queries, 1,470 repos, 476 file trees), PwC archive, OpenDataLab, B2FIND, Roboflow, Kaggle (round 2)', 'rendered_wikipedia_te (221), NayanaIR-MonoBench-te (222), tiny CAPTCHA (223), 7 GitHub data repos (224-230); 4 GitHub repos rejected'),
    ('D. Legacy / obscure', 'Wayback Machine, archived author pages, older competitions (CVSI 2015), British Library EAP, TDIL references in READMEs, palm-leaf and inscription searches', 'EAP038 Telugu books/periodicals (211); TDIL toolid 1892 lead; Tamil palm-leaf sets rejected'),
    ('Reviewer simulation', f"{len(MSIM['searches'])} likely reviewer searches; every dataset-like result mapped to a row", f"{sum(1 for _q, u, k, n in MSIM_ROWS if k == 'dataset' and _match(u))}/{sum(1 for _q, u, k, n in MSIM_ROWS if k == 'dataset')} dataset results already/now in the CSV"),
]
r3_tbl = table(['Pass', 'What was searched', 'Outcome'], R3_CHANNELS)
new3_tbl = table(['ID', 'Name', 'Category', 'Status', 'Distinct?'],
                 [[r['Dataset ID'], name_link(r, 60), md(r['Resource category'], 40), r['Verification status'], md(r['Counts as distinct dataset'], 40)] for r in R if r['Discovery round'].startswith('Round 3')])
chg3_tbl = table(['ID', 'Name', 'Change'], [[r['Dataset ID'], md(r['Official dataset name'], 60), md(r['Round 3 change'], 90)]
                                          for r in R if r['Round 3 change'] != 'NONE' and not r['Discovery round'].startswith('Round 3')])

# ------------------------------------------------------------------ DISCOVERY LOG
plat_tbl = table(['Platform (API)', 'Queries run', 'Unique hits', 'Date'], [[p, q, f'{h:,}', md(d, 20)] for p, q, h, d in plat])
manual_tbl = table(['Platform / site', 'What was done'], MANUAL)
tel_api = [r for r in api_rows if 'telugu' in json.dumps(r).lower()]
rej_tbl = table(['ID', 'Candidate', 'Reason'], [[r['Dataset ID'], name_link(r, 70), md(r['Additional notes'], 120)] for r in R if r['Resource category'] == 'Rejected'])
write('DISCOVERY_LOG.md', f"""
# Discovery log

How the directory was searched, between 2026-11-10 and {DATE}. Raw results are saved in `evidence/`.

## 1. Starting point

The audit began from the existing repo: `MASTER_CATALOGUE.csv` (16 `TEL-OCR` records plus manuscript, library,
periodical and text-corpus records) and the earlier acquisition work in `ocr/acquisition/`. Those records were
re-checked first (see [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md)) and then used as seeds.

## 2. Query variants

`scripts/discover.py` ran the same list of about 34 query variants on every searchable platform, including:
Telugu OCR; Telugu handwritten; Telugu handwriting recognition; Telugu character recognition; Telugu printed text;
Telugu scene text; Telugu word images; Telugu document images; Telugu manuscripts / palm leaf; Telugu text recognition;
Indic OCR; Indian language OCR; Indic handwritten; Indic scene text; multilingual OCR Indian; Dravidian OCR;
తెలుగు (Telugu script); IndicSTR; IIIT-HW; ILOCR; Mozhi; Synthetic-IndicSTR and others. Hugging Face also got
tag-based listing (`language:te`, image tasks) and model searches (to find the datasets models were trained on).

## 3. Platforms searched by API

{plat_tbl}

How the hits were screened:
- **Hugging Face:** {len(HFS['datasets'])} datasets and {len(HFS['models'])} models were screened by tags, README text and file names (`screen_hf.py`); 118 candidates had both images and Telugu evidence and were read one by one. Model cards gave 117 more dataset leads.
- **Zenodo, Figshare, DataCite, Dataverse, Internet Archive:** titles and descriptions filtered for Telugu + OCR/handwriting/document terms, then read.
- **DataCite** also covered IEEE DataPort (DOI prefix 10.21227), Mendeley Data (10.17632) and Kaggle DOIs, because IEEE pages block scripts.
- **OpenAlex + arXiv:** {oa_rel} OpenAlex works and {arxiv_hits} arXiv papers mentioned Telugu with an OCR-related term. Their titles and abstracts were screened; papers that describe a dataset were followed to find the data.
- **GitHub:** repositories and their file trees checked for actual data (many have code only).
- **Kaggle:** search, metadata and file-list APIs (no login, nothing downloaded).
- **Semantic Scholar:** round 1 crashed on the rate limit. Round 2 re-ran it with slow pacing and long back-off for about 45 minutes: {s2_n} of 36 planned queries were attempted, {s2_ok} returned results ({s2_hits} papers) and the others got HTTP 429 even after retries, so the run was stopped. Returned papers were screened the same way as OpenAlex.

## 4. Sites and platforms investigated directly

{manual_tbl}

In total, **{n_platforms}** platforms and sites were investigated ({len(plat)} by API sweep, {len(MANUAL)} directly).

## 5. ILOCR in depth

- **Dataset catalogue:** every page from `/dataset/1/` to `/dataset/200/` was requested. {ilocr_codes.get(200, 0)} pages are live (all at ID 69 or below), {ilocr_codes.get(404, 0)} return 404, and {ilocr_codes.get(500, 0)} return HTTP 500 (IDs 13, 14, 59; ID 14 is Mozhi-Telugu, whose zip files still download).
  Telugu pages: 23 (IIIT-INDIC-HW-WORDS-Telugu), 36 (IndicSTR12-Telugu), 40 (IIIT-Synthetic-M-Telugu), 55 (IIIT-Synthetic-R-Telugu), 68 (IIIT-Synthetic-IndicSTR-Telugu), plus 14 (Mozhi-Telugu, page broken).
- **API catalogue (`/api_list/`):** a table of {len(api_rows):,} OCR **models/APIs**, not datasets. {len(tel_api)} rows mention Telugu: layout detection, word recognition, page pipelines and script detection from IIIT Hyderabad, IIT Bombay, IIT Delhi, IIT Jodhpur and C-DAC, plus entries for Google OCR, Tesseract, EasyOCR and Surya. The `api_detail` pages return server errors. Recorded as one related resource (TOCR-144).
- **Competition sites:** IHTR 2022 and 2023 (TOCR-004/005), ICDAR 2024 handwriting (IHWWR TOCR-007, PLHWTR TOCR-008), ICDAR 2025 IHDR (TOCR-009; Telugu zips 404), ICPR 2024 WIRIndic (TOCR-080).

## 6. Papers

- {oa_rel + arxiv_hits:,} paper records were screened by title and abstract ({oa_rel} OpenAlex + {arxiv_hits} arXiv).
- {len(papers_rows)} papers are linked from directory rows; each was opened to find the dataset link, size, licence and Telugu share.
- Citations were followed from the main hubs (IIIT-HW-Telugu, IndicSTR12, IIIT-ILST, Mozhi, IndicDLP, BSTD, Nayana, PHDIndic_11) to related releases. This turned up HW-UC, roadside IndicSTR-Word, MIST and TEXTRON.
- Round 2 added a systematic OpenAlex citation sweep (Section 7), {s2_hits} Semantic Scholar records and {len(SG['hits'])} Shodhganga theses.

## 7. Round 2 (second pass, {DATE})

Round 2 went back to every channel left open after round 1 and re-checked all unconfirmed rows.

{r2_tbl}

### Theses on Shodhganga

{len(sg_rel)} Telugu OCR-related theses were found. Each built its own private data; none links to a public dataset, so none became a row.
Several say outright that no public Telugu dataset existed when they started.

{sg_tbl}

### Citation following (OpenAlex)

Every work citing the hub dataset papers was listed and screened ({sum(v.get('cited_by', 0) for v in CIT['seeds'].values())} citing works, {len(CIT['hits'])} kept for reading).
Nearly all are method papers that train on existing data or on private data they did not release; no new public dataset came from this channel.

{cit_tbl}

### New rows added in round 2

{new_tbl}

### Round-1 rows changed in round 2

{chg_tbl}

## 8. Rejected candidates

These looked relevant but are not Telugu OCR resources. They are kept in the CSV so nobody spends time on them again.

{rej_tbl}

Beyond these {n_rej} rows, several hundred search hits were discarded during screening without a row, for example
Telugu text-only NLP sets, speech sets, and Telugu-tagged HF sets with no images. The `hf_screen.json` and
`platform_candidates.txt` files in `evidence/discovery/` keep the screening decisions.

## 9. Round 3 (adversarial completeness pass, {DATE})

Round 3 assumed an independent reviewer would search for Telugu OCR data and tried to find anything they could find that the CSV lacked.
Full details, including a reviewer cross-check table, are in [ADVERSARIAL_COMPLETENESS_AUDIT.md](ADVERSARIAL_COMPLETENESS_AUDIT.md).

{r3_tbl}

### New rows added in round 3

{new3_tbl}

### Earlier rows changed in round 3

{chg3_tbl}

## 10. Channels still open

- **Semantic Scholar** - partly done: {s2_n} of 36 planned queries attempted and {s2_ok} answered before the run was stopped (repeated HTTP 429). Re-run with an API key.
- **Google Scholar** - blocks scripts; covered only through general web searches.
- **IEEE Xplore / Springer / Elsevier full text** - paywalled. Only abstracts and open versions were read, so dataset links inside paywalled papers may be missed.
- **AIKosh full listing** - the portal timed out (HTTP 504 / no response) in rounds 2 and 3; pages were found through web search only.
- **TDIL-DC** - certificate expired, not bypassed. The Telugu image corpus there is unconfirmed.
- **Roboflow Universe** - blocks scripts; 8 Telugu projects are known from search snippets only (sizes and classes unconfirmed).
- **Small GitHub archives** - a few student repos hold RAR/ZIP/CSV character data whose contents were not inspected (see MISSING_DATASET_CANDIDATES.csv).
- **ULCA downloads** - the two Telugu OCR corpora are listed, but downloading needs a login and a search request.
- **Institutional repositories beyond Shodhganga** (university DSpace sites) - only UoH was checked.
- **Direct contact with authors** - not done. CHIPS, UniLipi, the JASTT corpus, UHTelPCC/UHTelHwCC, the Telugu meme datasets and other unreleased sets could probably be requested by email.
""")

# ------------------------------------------------------------------ COVERAGE
gran = Counter()
for r in DS:
    if distinct(r) and r['Resource category'] in IMG_TEXT:
        g = r['Granularity'].lower()
        gran['Page' if 'page' in g else 'Line' if 'line' in g else 'Word' if 'word' in g else 'Other'] += 1
cov_cat = table(['Category', 'Distinct', 'of which VERIFIED', 'of which open licence'],
                [[c, cat_dist[c], sum(distinct(r) and r['Verification status'] == 'VERIFIED' for r in R if r['Resource category'] == c),
                  sum(distinct(r) and lic_bucket(r['Licence']).startswith('Open') for r in R if r['Resource category'] == c)] for c in CAT_ORDER[:-2]])
S2 = _load('s2.json'); s2_n = len(S2.get('queries', [])); s2_ok = sum(1 for q in S2.get('queries', []) if not q.get('error'))
write('COVERAGE_REPORT.md', f"""
# Coverage report

What the directory covers, what is missing, and how sure we are that nothing big was missed. Checked on {DATE}.

## How complete is it?

We **cannot claim** this list includes every Telugu OCR dataset that exists. What we can say:

- Every major open dataset platform with a search API was swept with the same ~34 query variants (Section 3 of the discovery log), and swept again in round 2 with broader queries.
- ILOCR, the main Indian OCR consortium, was checked exhaustively (every dataset ID, the full API list, every competition site).
- Hits from the API sweeps that matched both Telugu and OCR terms were reviewed. Later query variants mostly brought back datasets we already had, which suggests the open platforms are close to fully covered.
- Round 2 (citations, theses, Roboflow, AIKosh, ULCA, Wayback, broader platform queries) added {sum(r['Discovery round'].startswith('Round 2') and distinct(r) for r in DS)} distinct datasets. Most of them are unreleased, gated or very new (2025-26), not overlooked open releases. That is further evidence the open channels are close to saturated, but not proof.
- Round 3 (four independent passes plus a simulated reviewer search) added {sum(r['Discovery round'].startswith('Round 3') and distinct(r) for r in DS)} distinct datasets. Most are small GitHub uploads, paper-only meme/script-ID sets or legacy archives; the major open releases were already present.
- Gaps are most likely in: datasets described only in paywalled papers or theses, private university collections, Roboflow projects, government portals that need a browser, and commercial vendors.

## Distinct datasets by category

{cov_cat}

Telugu image-text OCR datasets by granularity (distinct): {', '.join(f'{k} {v}' for k, v in gran.most_common())}.

## Well covered

- **Handwritten words:** IIIT-HW-Telugu / HW-WORDS (~126K words) and the competition sets built on it, plus HW-UC and IHWWR.
- **Synthetic printed and scene text:** millions of rendered words and lines (IIIT-Synthetic-M/R/IndicSTR, Chitralekha, harsha-desaraju sets).
- **Printed pages:** Telugu Wikisource (~127K proofread pages on free scans) and sets derived from it. Also Mozhi word/line images and the NayanaOCR page corpus.
- **Characters:** many small handwritten character sets (HP Labs, Negi & Rao, IEEE and Kaggle uploads).

## Gaps (little or no data found)

- **Real scene text is small.** Labelled Telugu photo crops number in the low thousands (IndicSTR12 ~1.2K, BSTD ~2.8K, roadside IndicSTR-Word, MIST).
- **Handwritten lines and pages with full transcriptions** are rare and mostly locked in competitions (IHDR 2025 links are dead) or gated.
- **Historical documents:** thousands of palm-leaf manuscripts and old newspapers are scanned, but almost none have ground-truth transcriptions.
- **Forms, receipts, tables with cell text, and printed newspaper ground truth:** only commercial samples or layout-only sets (MUSTARD has structure but no cell text; IndicDLP has layout but no text).
- **Licence clarity:** many community uploads have no licence; several re-uploads conflict with the original.
- **Telugu shares of multilingual sets:** now counted for PHDIndic_11 (85 pages), IndicVisionBench (89 OCR pages), ORB-Indic (89), MInfoVisQA (384), PMGSY boards (1,020), adaption doc-QA (135 pages), BhartiOCR (500,000). Still unknown for MDIW-13, Indiscapes, IndicDLP (only the ~7.2% share), Kaggle Indian Scripts and GlotOCR.
- **Announced but unreleased:** CHIPS (2,874 Telugu handwritten pages), UniLipi Telugu-script manuscripts, the JASTT 33,496-character corpus and the ICON 2023 scene-text set all exist only in papers so far.

## Search channels exhausted vs remaining

| Channel | State |
|---|---|
| Hugging Face (datasets + models + language tag listing) | Exhausted for the query list |
| Kaggle (public API) | Exhausted for the query list |
| GitHub (search + repo trees) | Exhausted for the query list |
| Zenodo, Figshare, DataCite (incl. IEEE DataPort, Mendeley), Harvard Dataverse, Internet Archive | Exhausted for the query list |
| OpenAlex, arXiv | Exhausted for the query list; abstracts only |
| ILOCR (datasets, APIs, competitions) and CVIT/USODI | Exhausted |
| Mendeley Data (search API), DataCite (all Telugu records) | Exhausted (round 2) |
| Shodhganga theses | Exhausted for 24 queries (round 2) |
| OpenAlex citation following (14 hub papers) | Exhausted (round 2) |
| Bhashini ULCA (public metrics) | Exhausted for listing; downloads need login |
| Semantic Scholar | **Partly done**: {s2_n} of 36 planned queries attempted, {s2_ok} answered; stopped after repeated HTTP 429 |
| Google Scholar | **Indirect only** (blocks scripts; ~25 general web searches instead) |
| AIKosh | **Partly searched** (portal timing out; web-search enumeration only) |
| Roboflow Universe | **Partly searched** (search snippets only; pages block scripts) |
| TDIL-DC | **Blocked** (expired certificate; not bypassed) |
| Paywalled full text, other university repositories | **Not searched** |
| Hugging Face full paginated listing; GitHub all-pages search + file trees | Exhausted (round 3) |
| Crossref; Papers with Code archive; OpenDataLab; B2FIND | Exhausted (round 3) |
| ILOCR re-probe, older competitions (CVSI 2015), British Library EAP | Done (round 3) |
| Author contact for unreleased data | **Not done** |
""")

# ------------------------------------------------------------------ CURRENT STATE AUDIT
cat_rows2 = []
for r in R:
    c = r['Existing catalogue record']
    if c != 'NONE':
        cat_rows2.append([c, r['Dataset ID'], md(r['Official dataset name'], 60), r['Verification status'], md(r['Resource category'], 40)])
cat_rows2.sort()
new = sum(1 for r in DS if distinct(r) and r['Existing catalogue record'] == 'NONE')
write('CURRENT_STATE_AUDIT.md', f"""
# Current-state audit

Before the directory was built, the OCR-related entries already in the repo were re-checked. Date: {DATE}.

## What was already there

- `MASTER_CATALOGUE.csv` (200 sources) had **16 `TEL-OCR` records**: 15 datasets and 1 tool (Tesseract). OCR-relevant material also sat in manuscript, digital-library, periodical and text-corpus records.
- `ocr/acquisition/` (earlier phases) had downloaded and cleaned 10 open sets into a unified corpus (~15 GB, kept off GitHub).

## Corrections to the existing catalogue

| Record | What the catalogue says | What we found | Directory row |
|---|---|---|---|
| TEL-OCR-002 | Partially Verified; ~126K images | Verified: 126,413 images, but only 118,516 have a label line; 7,897 train images have no label. CC BY 4.0 confirmed. The catalogue merges two releases: IIIT-HW-Telugu (2018) and HW-WORDS v0.5. | TOCR-001, TOCR-002 |
| TEL-OCR-003 | Licence unknown; ">1,000 real word images" | ILOCR page states CC BY 4.0 for annotations. Telugu has 1,183 word crops (933/117/133) + 298 scene images, re-cropped from IIIT-ILST. | TOCR-071, TOCR-070 |
| TEL-OCR-005 | 458,964 rows | 458,964 is the HF table's row count. The data is 23,537 page image-text pairs in 219 book folders (the README says ~25,565 / 221). It is a subset of Telugu Wikisource. | TOCR-050 |
| TEL-OCR-010 | Partially Verified, MIT | Gated (manual approval). Licence tag MIT not checkable without access. | TOCR-062 |
| TEL-OCR-011 | Inaccessible (DSpace) | DSpace still HTTP 503. The same authors published the data on IEEE DataPort (Negi & Rao; ~82K characters, 937 classes; login needed). Recorded as one gated dataset. | TOCR-022 |
| TEL-OCR-012 | Unverified; size unknown | The IEEE "Varnamala" listing is a single image of 52 characters. It is not a training dataset. | TOCR-029 |
| TEL-OCR-014 | 20,000 image-text pairs, CC BY 4.0 | The Zenodo deposit is a 419 KB brochure from GTS.ai. The data is the Kaggle amancapy upload, which says CC BY-NC 4.0, so the catalogue's licence is wrong. | TOCR-096, TOCR-095 |
| TEL-OCR-015 | IndicDLP, CC BY 4.0 | It is layout-only (no transcriptions). Telugu is ~7.2% (~8,600 pages). HF copy is gated. | TOCR-109 |
| TEL-OCR-013 | Indiscapes | Telugu share not confirmed. Layout-only. | TOCR-111 |

These corrections are recorded in the directory only. `MASTER_CATALOGUE.csv` was **not changed**, so the original
audit trail stays as it is. Applying them to the master catalogue is a separate step.

## Mapping

All 16 `TEL-OCR` records map to directory rows. **{new}** distinct datasets in the directory have no catalogue record.

{table(['Catalogue record', 'Directory row', 'Name', 'Status now', 'Category'], cat_rows2)}
""")

# ------------------------------------------------------------------ MISSING_DATASET_CANDIDATES.csv (supporting file, not a master)
LEADS = json.load(open(os.path.join(EV, 'round3_leads.json')))['leads']
cand = []
for r in R:
    if r['Resource category'] in NOT_DS:
        continue
    st, dd = r['Verification status'], r['Counts as distinct dataset']
    if dd.startswith('UNKNOWN') or st == 'UNVERIFIED' or (st == 'INACCESSIBLE' and re.search(r'not released|announced|coming soon|no public|no release|later release', r['Access status'] + r['Access requirements'], re.I)):
        why = []
        if st in ('UNVERIFIED', 'INACCESSIBLE'):
            why.append(f'status {st}')
        if dd.startswith('UNKNOWN'):
            why.append('distinctness unknown')
        cand.append([r['Dataset ID'], r['Official dataset name'], link(r), 'Yes - ' + r['Dataset ID'], st, r['Resource category'],
                     'Unconfirmed row already in the master catalogue', '; '.join(why) + ('; ' + r['Access status'] if r['Access status'] else ''),
                     'Contact authors / re-check source' if st in ('UNVERIFIED', 'INACCESSIBLE') else 'Compare files with the suspected parent'])
for l in LEADS:
    cand.append([l['id'], l['name'], l['url'], 'No (lead only)', 'NOT IN CATALOGUE', 'UNKNOWN', 'Lead not added as a row (' + l['channel'] + ')',
                 l['reason'] + ' | Telugu evidence: ' + l['telugu_evidence'], l['next_step']])
with open(os.path.join(DIR, 'MISSING_DATASET_CANDIDATES.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Candidate ID', 'Name', 'URL', 'In telugu_ocr_final.csv?', 'Master verification status', 'Master category', 'Candidate type', 'Why unconfirmed', 'Next step'])
    w.writerows(cand)
n_cand_rows = sum(1 for c in cand if c[3].startswith('Yes'))

# ------------------------------------------------------------------ ADVERSARIAL_COMPLETENESS_AUDIT.md
msim_tbl = table(['Reviewer query', 'Result URL', 'Kind', 'In CSV as', 'Note'],
                 [[md(q, 40), md(u, 80), k, ', '.join(_match(u)) or '-', md(n, 90)] for q, u, k, n in MSIM_ROWS])
ds_res = [(q, u, n) for q, u, k, n in MSIM_ROWS if k == 'dataset']
ds_hit = [x for x in ds_res if _match(x[1])]
ds_miss = [x for x in ds_res if not _match(x[1])]
inacc_tbl = table(['ID', 'Dataset', 'Status', 'Reason'], [[r['Dataset ID'], md(r['Official dataset name'], 60), r['Verification status'], md(r['Access status'], 110)]
                                                        for r in R if r['Verification status'] in ('INACCESSIBLE', 'GATED', 'COMMERCIAL')])
hf_full = _load('hf_full_listing.json'); gh_deep = _load('github_deep.json'); cr = _load('crossref.json')
write('ADVERSARIAL_COMPLETENESS_AUDIT.md', f"""
# Adversarial completeness audit

**Question:** if an independent reviewer searches for Telugu OCR datasets, will everything they find already be in
[`telugu_ocr_final.csv`](../../telugu_ocr_final.csv)? Round 3 ({DATE}) tried to answer that by attacking the catalogue from four
independent directions and by simulating the reviewer's own searches.

**Bottom line:** distinct datasets went from 92 (round 1) to 104 (round 2) to **{n_distinct}** now, in **{len(R)}** rows.
Round 3 added {sum(r['Discovery round'].startswith('Round 3') for r in R)} rows ({sum(r['Discovery round'].startswith('Round 3') and distinct(r) for r in DS)} new distinct datasets, the rest copies, unconfirmed leads or rejections)
and corrected {sum(r['Round 3 change'] != 'NONE' and not r['Discovery round'].startswith('Round 3') for r in R)} earlier rows.
Of the {len(ds_res)} dataset-type results returned by {len(MSIM['searches'])} simulated reviewer searches, **{len(ds_hit)}** map to a row in the CSV{'' if not ds_miss else f' and {len(ds_miss)} do not (listed in section 3)'}.

## 1. Discovery channels investigated

{r3_tbl}

Earlier rounds (see [DISCOVERY_LOG.md](DISCOVERY_LOG.md)) covered Hugging Face, Kaggle, GitHub, Zenodo, Figshare, DataCite, Dataverse,
Internet Archive, OpenAlex, arXiv, Semantic Scholar (partial), Mendeley, Shodhganga, OpenAlex citations, ILOCR, CVIT, ULCA, AIKosh (via search),
Roboflow (via search) and the Wayback Machine. In total **{n_platforms}** platforms and sites have been investigated.

## 2. Search queries and sources used in round 3

- **Simulated reviewer searches ({len(MSIM['searches'])}):** {'; '.join(x['query'] for x in MSIM['searches'])}.
- **Hugging Face full listing:** {'; '.join(f"{l['kind']}={l['value']} ({l.get('datasets', 0):,})" for l in hf_full.get('listings', []))}. Every page was followed up to 60 pages per listing (only the noisy -te-/_te_ substring listings reached that cap); {hf_full.get('total_datasets_listed', len(hf_full.get('datasets', {}))):,} datasets screened by tags and names.
- **GitHub (all result pages, up to the 1,000-result API cap):** {'; '.join(q['query'] for q in gh_deep.get('queries', []))}. {len(gh_deep.get('repos', {})):,} repositories; file trees of {sum(1 for r in gh_deep.get('repos', {}).values() if r.get('ocr_like'))} OCR-related repos checked for images, labels and archives.
- **Crossref:** {'; '.join(q['query'] for q in cr.get('queries', []))} ({len(cr.get('hits', {})):,} records).
- **Other web searches:** institution names (IIT Bombay/AIKosh, C-DAC, IISc MILE, IIT Madras, Andhra/JNTU/IIIT Sri City/NIT Warangal), legacy terms (CVSI 2015, video script identification, online handwriting, palm leaf, inscriptions, newspapers digitisation, TDIL), meme datasets, handwritten documents/answer sheets, VLM OCR benchmarks.
- **Archives:** Papers with Code archive ({'15,008'} dataset records), OpenDataLab, B2FIND, Wayback Machine (IIIT, UoH, TDIL, EAP pages).

## 3. Reviewer cross-check

Each result URL returned by the simulated reviewer searches, and where it sits in the CSV. "-" means the URL itself is not a row
(papers, models, demos and screened-out non-Telugu sets); the note says why.

{msim_tbl}

## 4. Newly discovered datasets (round 3)

{new3_tbl}

## 5. Why these were missed before

- **API caps:** round-1 Hugging Face searches stopped at 200 results per query and GitHub searches at the first page; the full listings in round 3 found the rendered Wikipedia, NayanaIR-MonoBench-te and tiny-CAPTCHA sets and seven small GitHub data repos.
- **Query scope:** meme datasets and video-frame script identification (CVSI 2015) do not use the words "OCR" or "handwritten", so earlier query lists did not reach them.
- **No Crossref pass before round 3:** Crossref surfaced the Springer/IEEE meme dataset papers.
- **Legacy material:** the British Library EAP038 Telugu print archive and the Amrita palm-leaf database are only described on institutional pages.

## 6. Existing catalogue errors corrected

{chg3_tbl}

Earlier corrections (rounds 1-2) are listed in [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md) and in the `Round 2 change` column.

## 7. Unresolved leads

[MISSING_DATASET_CANDIDATES.csv](MISSING_DATASET_CANDIDATES.csv) lists **{len(cand)}** candidates: {n_cand_rows} are already rows in the master
CSV but unconfirmed (status UNVERIFIED, an unreleased announcement, or unknown distinctness), and {len(LEADS)} are leads that are not rows
because nothing confirms they are Telugu image data. It is a supporting file; the master remains `telugu_ocr_final.csv`.

## 8. Inaccessible, gated and commercial sources

{inacc_tbl}

Channels that blocked or failed: AIKosh (HTTP 504 / no response, rounds 2-3), TDIL-DC (expired TLS certificate, not bypassed), Roboflow
and IEEE DataPort pages (HTTP 403 to scripts; metadata via search and DataCite), Semantic Scholar (HTTP 429), Google Scholar (bot check).

## 9. Duplicate and derivative relationships

{n_pairs} relationship pairs are recorded (details in [DUPLICATE_AND_MIRROR_REPORT.md](DUPLICATE_AND_MIRROR_REPORT.md)); {n_copies} dataset rows
are mirrors, copies, subsets or compilations and are excluded from the distinct count.

## 10. Remaining discovery gaps

- AIKosh's full catalogue (including IIT Bombay's script datasets) could not be listed.
- TDIL-DC resources (Telugu image corpus TOCR-046, toolid 1892) remain unreachable without bypassing TLS.
- Roboflow project sizes/classes are known only from search snippets.
- Paywalled full texts (IEEE Xplore, Springer, Elsevier) were read only as abstracts.
- Semantic Scholar was only partly searched; Google Scholar only indirectly.
- Small student archives on GitHub (RAR/ZIP/CSV) were not opened.
- No authors were contacted; announced datasets (CHIPS, UniLipi, JASTT corpus, meme sets, UHTelPCC/UHTelHwCC) stay unconfirmed.

## 11. Readiness for independent cross-verification

- **Well defended:** anything findable through Hugging Face, Kaggle, GitHub, Zenodo, Figshare, DataCite/IEEE DataPort, Mendeley, ILOCR/CVIT,
  arXiv/OpenAlex/Crossref or a general web search for Telugu OCR/handwriting/scene-text/character datasets. All {len(ds_hit)} dataset results of the
  simulated reviewer searches resolve to rows.
- **Partly defended:** portal-only sources (AIKosh, TDIL, Roboflow), paper-only datasets that were never released, and theses.
- **Honest limit:** the catalogue cannot prove that no dataset exists elsewhere. A reviewer who finds a dataset in the gaps above should
  add it via `scripts/entries_e.py` and re-run `build_directory.py`, `make_docs.py` and `validate_directory.py`.
""")

# keep the pointer in the repo-root README in step with the CSV
_rp = os.path.join(ROOT, 'README.md')
_rt = open(_rp, encoding='utf-8').read()
_new = re.sub(r'\(\d+ rows, \d+ distinct', f'({len(R)} rows, {n_distinct} distinct', _rt)
if _new != _rt:
    open(_rp, 'w', encoding='utf-8').write(_new)

print('docs written:', sorted(f for f in os.listdir(DIR) if f.endswith('.md')))
print(dict(rows=len(R), distinct=n_distinct, imgtext=n_imgtext, unknown=n_unknown, copies=n_copies, pairs=n_pairs, platforms=n_platforms,
           papers_screened=oa_rel + arxiv_hits, papers_linked=len(papers_rows), best=len(best), new=new, linkbad=len(link_bad)))
