"""Shared record helper for the Telugu OCR directory."""

COLUMNS = [
    ('id', 'Dataset ID'), ('name', 'Official dataset name'), ('aliases', 'Alternative names'), ('parent', 'Parent dataset'),
    ('version', 'Dataset version'), ('desc', 'Dataset description'), ('url', 'Official webpage URL'), ('download', 'Direct download URL'),
    ('hf', 'Hugging Face URL'), ('github', 'GitHub URL'), ('kaggle', 'Kaggle URL'), ('archive', 'Zenodo / Figshare / archive URL'),
    ('paper', 'Research paper URL'), ('doi', 'DOI'), ('inst', 'Institution'), ('authors', 'Authors'), ('lang', 'Language'), ('script', 'Script'),
    ('modality', 'Modality'), ('task', 'Task'), ('gran', 'Granularity'), ('rs', 'Real / synthetic'), ('count', 'Published sample count'),
    ('unit', 'Sample count unit'), ('ann', 'Annotation availability'), ('ann_type', 'Annotation type'), ('lic', 'Licence'),
    ('comm', 'Commercial-use permission'), ('redis', 'Redistribution permission'), ('access_req', 'Access requirements'),
    ('access', 'Access status'), ('ver', 'Verification status'), ('verified', 'Last verified date'), ('overlap', 'Duplicate / overlap notes'),
    ('quality', 'Dataset quality notes'), ('notes', 'Additional notes'),
    # classification columns (beyond the 36 required)
    ('cat', 'Resource category'), ('distinct', 'Counts as distinct dataset'), ('catalogue', 'Existing catalogue record'),
    ('round', 'Discovery round'), ('changed', 'Round 2 change'),
]

STATUSES = ['VERIFIED', 'PARTIALLY VERIFIED', 'UNVERIFIED', 'INACCESSIBLE', 'GATED', 'COMMERCIAL', 'DISCONTINUED', 'REJECTED']

CATEGORIES = [
    'OCR image-text: printed', 'OCR image-text: handwritten', 'OCR image-text: scene text', 'OCR image-text: synthetic',
    'Character / glyph classification', 'Layout / detection (no transcription)', 'Script identification',
    'Text-in-image benchmark (VQA / document understanding)', 'Image-only (no transcription)', 'Image-only (transcription NOT VERIFIED)',
    'Scanned archive (image-only)', 'Machine-labelled OCR (not human ground truth)', 'Text-only corpus (OCR language modelling)',
    'Related resource (not a dataset)', 'Rejected',
]

DEFAULTS = dict(aliases='NONE KNOWN', parent='NONE', version='UNKNOWN', download='NOT PROVIDED / see official page', hf='NONE', github='NONE',
                kaggle='NONE', archive='NONE', paper='NONE FOUND', doi='NONE', inst='UNKNOWN', authors='UNKNOWN', lang='Telugu', script='Telugu',
                count='UNKNOWN', unit='UNKNOWN', ann='UNKNOWN', ann_type='UNKNOWN', lic='UNKNOWN', comm='UNKNOWN', redis='UNKNOWN',
                access_req='UNKNOWN', access='UNKNOWN', verified='2026-11-11', overlap='None identified', quality='Not assessed',
                notes='', catalogue='NONE', round='Round 1 (2026-11-11)', changed='NONE')


def E(**kw):
    rec = dict(DEFAULTS)
    rec.update({k: v for k, v in kw.items() if v is not None})
    assert rec['ver'] in STATUSES, (rec['id'], rec['ver'])
    assert rec['cat'] in CATEGORIES, (rec['id'], rec['cat'])
    for k, _ in COLUMNS:
        rec.setdefault(k, 'UNKNOWN')
        if rec[k] in ('', None) and k != 'notes':
            rec[k] = 'UNKNOWN'
    return rec
