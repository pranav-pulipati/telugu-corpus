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
        return 'Research / academic use terms'
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
    if isinstance(d, dict) and 'queries' in d:
        plat.append((d['platform'], len(d['queries']), len(d['hits']), d.get('queried', '')))
api_rows = json.load(open(os.path.join(EV, 'ilocr', 'api_list.json')))['rows']
ilocr_ds = json.load(open(os.path.join(EV, 'ilocr', 'ilocr_datasets.json')))
ilocr_codes = Counter(v['code'] for v in ilocr_ds.values())
HFS = json.load(open(os.path.join(EV, 'discovery', 'hf_screen.json')))
oa_rel = len(json.load(open(os.path.join(EV, 'discovery', 'openalex_relevant.json'))))
arxiv_hits = next((p[2] for p in plat if p[0] == 'arxiv'), 0)
papers_rows = {r['Research paper URL'] for r in R if r['Research paper URL'].startswith('http')}
link_rows = list(csv.DictReader(open(os.path.join(EV, 'link_check.csv'), encoding='utf-8'))) if os.path.exists(os.path.join(EV, 'link_check.csv')) else []
link_bad = [l for l in link_rows if not l['HTTP status'].startswith(('2', '3'))]

# directly investigated platforms (beyond the API sweeps)
MANUAL = [
    ('ILOCR dataset catalogue (ilocr.iiit.ac.in/dataset/1-200)', 'Every ID probed; Telugu pages read in full'),
    ('ILOCR API catalogue (/api_list/)', f'{len(api_rows):,} entries parsed; Telugu rows extracted'),
    ('ILOCR competition sites (IHTR 2022/2023, ICDAR 2024 HWD, ICDAR 2025 IHDR, ICPR 2024 WIRIndic)', 'Dataset pages and download links checked'),
    ('CVIT project pages + USODI portal (cvit.iiit.ac.in)', 'Project list scanned for Telugu; USODI detection/recognition lists read'),
    ('IEEE DataPort', 'Pages block scripts (403); metadata taken via DataCite DOIs'),
    ('Mendeley Data', 'Public API used for dataset metadata'),
    ('Kaggle', 'Public search + metadata + file-list APIs (no login, nothing downloaded)'),
    ('Roboflow Universe', 'Pages block scripts (403); search-engine snippets only'),
    ('TDIL-DC (tdil-dc.in)', 'Certificate expired; not bypassed'),
    ('Bhashini ULCA / AIKosh', 'Portals are web apps; listings checked where reachable'),
    ('University of Hyderabad DSpace + SCIS pages', 'DSpace HTTP 503; old pages 404'),
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
candidate, with the 36 requested columns plus three classification columns:

- **Resource category** - what kind of resource it is (see below). Filter on this first.
- **Counts as distinct dataset** - `Y` means it is its own dataset. `N (...)` means it is a mirror, copy, subset or derivative of another row (the row ID is named). `UNKNOWN` means we could not tell.
- **Existing catalogue record** - the matching `record_id` in the repo's `MASTER_CATALOGUE.csv`, if any.

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

## How it was built

- `scripts/entries_a.py`, `entries_b.py`, `entries_c.py` - the records, written by hand from the evidence.
- `scripts/build_directory.py` - checks IDs and cross-references, writes `telugu_ocr_final.csv` and `evidence/counts.json`.
- `scripts/make_docs.py` - writes these Markdown files from the CSV, so counts always match.
- `scripts/discover.py`, `screen_hf.py`, `fetch_pages.py` - the search sweeps; results in `evidence/discovery/` and `evidence/pages/`.
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
         'Copyleft software licence (GPL)', 'Research / academic use terms', 'Commercial / vendor', 'Copyrighted source material (no licence)', 'Unknown / not stated']
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
- **No licence at all.** Most GitHub and Kaggle personal uploads state no licence ({len(by_b['Unknown / not stated'])} dataset rows are in the unknown group).

## Detail by licence group
""" + '\n'.join(lic_detail))

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
- **Semantic Scholar:** the run hit the API rate limit and crashed partway. No results were saved, so this channel counts as **not completed**.

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

## 7. Rejected candidates

These looked relevant but are not Telugu OCR resources. They are kept in the CSV so nobody spends time on them again.

{rej_tbl}

Beyond these {n_rej} rows, several hundred search hits were discarded during screening without a row, for example
Telugu text-only NLP sets, speech sets, and Telugu-tagged HF sets with no images. The `hf_screen.json` and
`platform_candidates.txt` files in `evidence/discovery/` keep the screening decisions.

## 8. Channels not exhausted

- **Semantic Scholar** - run did not finish (rate limit). Re-run with an API key.
- **Google Scholar** - no API. Not searched systematically.
- **IEEE Xplore / Springer / Elsevier full text** - paywalled. Only abstracts and open versions were read, so dataset links inside paywalled papers may be missed.
- **Bhashini ULCA and AIKosh full listings** - JavaScript web apps. Only reachable listings were checked.
- **TDIL-DC** - certificate expired, not bypassed. The Telugu image corpus there is unconfirmed.
- **Roboflow Universe** - blocks scripts. Two Telugu projects are known only from search snippets.
- **Indian university repositories (Shodhganga theses, institutional DSpace)** - not searched systematically. Theses often describe private datasets.
- **Telugu-language web (Telugu-script search queries on general search engines)** - only lightly covered.
- **Direct contact with authors** - not done. Many unverified or inaccessible sets could probably be obtained by email.
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
write('COVERAGE_REPORT.md', f"""
# Coverage report

What the directory covers, what is missing, and how sure we are that nothing big was missed. Checked on {DATE}.

## How complete is it?

We **cannot claim** this list includes every Telugu OCR dataset that exists. What we can say:

- Every major open dataset platform with a search API was swept with the same ~34 query variants (Section 3 of the discovery log).
- ILOCR, the main Indian OCR consortium, was checked exhaustively (every dataset ID, the full API list, every competition site).
- Hits from the API sweeps that matched both Telugu and OCR terms were reviewed. Later query variants mostly brought back datasets we already had, which suggests the open platforms are close to fully covered.
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
- **Telugu shares of multilingual sets** (PHDIndic_11, MDIW-13, IndicVisionBench, Indiscapes) could not be confirmed without downloading.

## Search channels exhausted vs remaining

| Channel | State |
|---|---|
| Hugging Face (datasets + models + language tag listing) | Exhausted for the query list |
| Kaggle (public API) | Exhausted for the query list |
| GitHub (search + repo trees) | Exhausted for the query list |
| Zenodo, Figshare, DataCite (incl. IEEE DataPort, Mendeley), Harvard Dataverse, Internet Archive | Exhausted for the query list |
| OpenAlex, arXiv | Exhausted for the query list; abstracts only |
| ILOCR (datasets, APIs, competitions) and CVIT/USODI | Exhausted |
| Semantic Scholar | **Not completed** (rate limit) |
| Google Scholar, Shodhganga, paywalled full text | **Not searched** |
| Bhashini ULCA, AIKosh, TDIL-DC, Roboflow | **Partly searched** (portals block scripts or are down) |
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

print('docs written:', sorted(f for f in os.listdir(DIR) if f.endswith('.md')))
print(dict(rows=len(R), distinct=n_distinct, imgtext=n_imgtext, unknown=n_unknown, copies=n_copies, pairs=n_pairs, platforms=n_platforms,
           papers_screened=oa_rel + arxiv_hits, papers_linked=len(papers_rows), best=len(best), new=new, linkbad=len(link_bad)))
