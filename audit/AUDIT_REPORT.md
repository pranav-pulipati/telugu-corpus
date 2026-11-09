# Audit Report — Telugu Corpus Source Catalogue

Audit date: 2026-11-09. Scope: the 204 original catalogue records and the 1,563-entry Hugging Face (HF) inventory.
No new sources were added. The original research is preserved unchanged in `audit/original_snapshot/`.

## 1. Reconciled counts

Every original record falls in exactly one row of each table below.

**A. Record disposition** (sums to the original count)

| Disposition | Records |
|---|---|
| Original records | 204 |
| Active (kept in MASTER_CATALOGUE) | 200 |
| Rejected (moved to archive) | 4 |

**B. Active records by verification status** (sums to 200)

| Status | Records |
|---|---|
| Verified | 90 |
| Partially Verified | 89 |
| Unverified | 13 |
| Inaccessible | 8 |

**C. Active records by quality rating** (sums to 200; separate from status)

| Quality | Records |
|---|---|
| High | 84 |
| Medium | 44 |
| Low | 72 |

**D. Rejected records by reason** (sums to 4)

| Reason | Records | IDs |
|---|---|---|
| Out of scope | 1 | TEL-ACAD-002 |
| Not an identifiable collection | 1 | TEL-AV-004 |
| Not an independent source | 1 | TEL-DIAL-003 |
| Duplicate without independent value | 1 | TEL-TXT-024 |

Of these, *irrelevant* (out of scope) = 1; *duplicate without independent value* = 1.

**E. Audit outcome for active records** (sums to 200)

| Outcome | Records |
|---|---|
| Corrected (at least one claim or field changed, reason recorded) | 54 |
| Reviewed — no change to claims | 146 |

**F. Double counting** — 19 active records are mirrors, subsets, superseded versions or aggregates of other
records and are marked `count_in_totals = No`; 181 are counted. 58 active records carry a
duplicate/overlap relationship (`dedup_role`); all relationships are listed in `DUPLICATE_SOURCES.csv`.

**G. Licensing** — 95 active records have an unresolved licence, redistribution or commercial-use question
(`LICENSING_UNCERTAINTIES.csv`). Commercial use: Allowed 79, Unclear 60, Not allowed 34, Varies 27.

**H. Status changes made by the audit**

| Change | Records | IDs |
|---|---|---|
| Partially Verified → Verified | 5 | TEL-PAR-012, TEL-PAR-013, TEL-PAR-014, TEL-PAR-020, TEL-OCR-009 |
| Verified → Partially Verified | 4 | TEL-PAR-006, TEL-ANN-021, TEL-ANN-030, TEL-SPEECH-003 |
| Partially Verified → Inaccessible | 3 | TEL-LIT-010, TEL-TXT-003, TEL-PAR-016 |
| Unverified → Inaccessible | 2 | TEL-OCR-011, TEL-EDU-002 |
| Partially Verified → Unverified | 1 | TEL-PAR-015 |

## 2. What was wrong

1. **Licence claims stronger than the evidence (25 records corrected).** Examples:
   - Indian government material was treated as generally reusable. The Copyright Act s.52(1)(q) only covers Gazette
     matter (not Acts) and court judgments. Acts can be reproduced only with commentary, and Government Orders
     outside the Gazette are not covered (TEL-GOV-001/002/003/006).
   - "Public domain" and CC tags set by Internet Archive uploaders were taken as settled
     (TEL-MSS-001, TEL-PERIOD-004, TEL-GOV-004).
   - Licences recalled from memory: StoryWeaver, IndicSentiment, the Samanantar paper, GODL for PIB.
   - Paid LDC-IL licences were shown as "commercial allowed".

   Where primary licence files were read, licences were confirmed or filled in:
   - UD Telugu — CC BY-SA 4.0
   - LTRC treebank — CC BY-NC-SA 4.0
   - IndicCorp v2 — CC0
   - PMIndia, Anuvaad — CC BY 4.0
   - Joshua-IPC — CC BY-SA 3.0
   - Updesh — non-commercial research only
   - Nemotron — per-source terms

   IDs: TEL-DLIB-013, TEL-LIT-004, TEL-LIT-005, TEL-PERIOD-004, TEL-MSS-001, TEL-LEX-010, TEL-LEX-012, TEL-TXT-004, TEL-TXT-015, TEL-TXT-017, TEL-PAR-003, TEL-PAR-012, TEL-PAR-013, TEL-PAR-014, TEL-ANN-004, TEL-ANN-033, TEL-SPEECH-009, TEL-SPEECH-013, TEL-GOV-001, TEL-GOV-002, TEL-GOV-003, TEL-GOV-004, TEL-GOV-005, TEL-GOV-006, TEL-GOV-007.
2. **Verification statuses too generous or wrong (15 changed).**
   - Records were marked "Verified" although nobody had checked that Telugu text is really in the data.
   - Sites with invalid TLS certificates were counted as reachable.
   - Dead or unavailable sources were left as "Partially Verified" or "Unverified": IndicCorp v1 download (403), the
     CVIT-PIB homepage (404), the UoH DSpace record (503).
   - Gated datasets whose Telugu content cannot be sampled without a login were moved from "Verified" to
     "Partially Verified": Kathbath on HF, FLORES+, MILU.

   Five records were upgraded after their licences were confirmed. IDs: TEL-LIT-010, TEL-TXT-003, TEL-PAR-006, TEL-PAR-012, TEL-PAR-013, TEL-PAR-014, TEL-PAR-015, TEL-PAR-016, TEL-PAR-020, TEL-ANN-021, TEL-ANN-030, TEL-OCR-009, TEL-OCR-011, TEL-SPEECH-003, TEL-EDU-002.
3. **Telugu content was assumed from tags.** Sampling the actual rows or file bytes of the 84 active records whose
   collection is on HF gave: CONFIRMED_TELUGU_TEXT 60, TELUGU_STRUCTURE_ONLY 19, NOT_CHECKABLE 5. Records without
   confirmed Telugu text can no longer be "Verified". Gated datasets stay "Partially Verified" until someone logs in.
   This check also exposed:
   - the Braille corpus contains no Telugu script (TEL-PAR-018)
   - the code-switching set is romanised (TEL-ANN-029)
   - Telugu in Google SVQ is only a metadata tag (TEL-SPEECH-020)
   - the "Telugu clickbait" set is WX-romanised Telugu, not Telugu script (TEL-ANN-024)
   - "Telugu-book-text-images" has page images but no transcriptions, so it is not OCR ground truth (TEL-OCR-007)
4. **Numbers and descriptions (9 records).**
   - The OPUS en–te total was mis-summed: 55,280,752 instead of **55,907,602**.
   - Unverified claims were removed (share of bot-generated Wikipedia stubs; MASSIVE "51 locales" → 52 languages;
     purpose claims).
   - Figures from cards were added (IITB-IndicMonoDoc 767.18M Telugu tokens).
   - Synthetic content was confirmed from cards (Nemotron, StoryTOM).

   IDs: TEL-TXT-001, TEL-TXT-014, TEL-PAR-001, TEL-PAR-016, TEL-PAR-020, TEL-ANN-019, TEL-ANN-024, TEL-OCR-007, TEL-OCR-009.
5. **Misclassification (7 records).**
   - Bhashini and AIKosh were filed as speech datasets; they are multimodal portals (moved to DLIB).
   - Reference-only entries were typed as platforms.
   - Telugu scope was overstated (Braille).

   IDs: TEL-LIT-010, TEL-PAR-018, TEL-ANN-024, TEL-ANN-029, TEL-SPEECH-018, TEL-SPEECH-019, TEL-ACAD-003.
6. **Broken or wrong URLs (11 records changed in this audit).** Licence evidence was re-pointed to primary
   licence files. Earlier fixes (OPUS page URLs, Rashtriya e-Pustakalaya, the encyclopedia mirror) are kept. IDs: TEL-LEX-010, TEL-LEX-012, TEL-TXT-004, TEL-PAR-012, TEL-PAR-014, TEL-ANN-033, TEL-GOV-001, TEL-GOV-002, TEL-GOV-003, TEL-GOV-005, TEL-GOV-006.
7. **Duplicates and non-sources.**
   - 4 records rejected: an IndicCorp re-upload, a cross-reference stub, English-language research papers, and a
     generic YouTube entry.
   - Mirror and subset relationships were made explicit, so totals no longer double-count: CulturaX ⊃ OSCAR+mC4,
     OPUS ⊃ NLLB/Samanantar/PMIndia/Anuvaad/Joshua/Tatoeba, IA aggregate ⊃ its collections, the GOML portal ↔ its IA
     mirror, Sapthagiri ⊂ TTD, and others.

## 3. Hugging Face inventory (1563 datasets)

Every inventory entry now has a sampled-content verdict and a decision.

| Decision | Datasets |
|---|---|
| Retained | 1060 |
| Unconfirmed | 486 |
| Rejected | 17 |

| Content verdict | Datasets | Meaning |
|---|---|---|
| CONFIRMED_TELUGU_TEXT | 741 | ≥20 Telugu-script characters found in sampled rows/file bytes |
| TELUGU_STRUCTURE_ONLY | 313 | Telugu-named config/split/file exists; content not sampleable (gated, no viewer, audio) |
| ROMANISED_TELUGU_CLAIMED | 6 | Only romanised-Telugu parts; script test not applicable |
| ROMANISED_TELUGU_LIKELY | 10 | Latin text with frequent romanised-Telugu words |
| NO_TELUGU_IN_SAMPLE | 232 | Rows sampled, no Telugu script, no Telugu-named part |
| NOT_CHECKABLE | 261 | No viewer / gated / too little text, and no Telugu-named part |
| NOT_FOUND | 0 | Dataset deleted from Hugging Face |
| ERROR | 0 | Request failed |
| NOT_YET_CHECKED | 0 | Not reached in this audit run |

Rules (conservative): a dataset is **Rejected** only with positive evidence that it is not Telugu:
- it no longer exists on HF;
- it is a dataset for another language that matched only through the publisher name (e.g. Telugu-LLM-Labs'
  Marathi/Urdu/Nepali sets and their mirrors);
- it was a spurious name-search hit (no "telugu" in its id) with no Telugu in the sample; or
- it claims a single language, and the sampled text is in another script.

Everything else that lacks Telugu evidence is **Unconfirmed**. That covers multilingual samples that simply missed
Telugu, audio or image rows with no text, likely romanised Telugu (frequent words such as *nenu, ledu, undi, chala*),
and Latin text that may be an English side. A first-pass "no Telugu" result was re-profiled by script before any
rejection (`evidence/hf_script_profile.jsonl`).

Sampling method: up to 100 rows of a Telugu-named config or split, otherwise the first split, otherwise the first
512 KB of a Telugu-named file (including `\u0c..` JSON escapes). It proves Telugu is present; it does not measure
how much. Rejected entries stay in the inventory CSV with `decision_reason`.

## 4. Unresolved

- **Licensing:** 95 records (see `LICENSING_UNCERTAINTIES.csv`). The largest open questions:
  - uploader-applied licences on Internet Archive
  - reuse status of AP Assembly debates, Government Orders and statute translations
  - the licence for Leipzig, StoryWeaver, IndoWordNet, IndicTTS and MSR speech
  - per-source terms inside Nemotron and Aya
- **Access:** gated HF datasets (IndicVoices, Kathbath on HF, Vaani, MILU, BPCC, FLORES+, CulturaX, OSCAR) need a
  logged-in check. Government and academic sites with invalid TLS certificates or timeouts need checking from an
  Indian network: TDIL-DC, Sahitya Akademi, SCERT Telangana, Gyan Bharatam, IITM IndicTTS, Shodhganga.
- **Content:** 13 active records remain Unverified. They are kept with Low quality and listed in `AUDIT_RESULTS.csv`.

## 5. Limitations of this audit

- Content checks sample a small part of each dataset; they prove presence of Telugu, not its share or quality.
- Legal readings of the Copyright Act come from a secondary legal source (lawgist.in). The official DPIIT page could
  not be read because its TLS certificate is invalid. Not legal advice.
- JavaScript-only portals (NDLI, Bhashini, AIKosh, LDC-IL, Gyan Bharatam) and bot-protected sites (HathiTrust, EAP,
  Leipzig) were not enumerated.
- Counts are as of 2026-11-09. A re-run on that date reproduced every Internet Archive figure exactly or within one
  newly uploaded item (`evidence/api_snapshots/ia_recheck_2026-11-09.csv`). Wikimedia, Common Voice and StoryWeaver
  also reproduced (`other_recheck_2026-11-09.csv`). The OPUS recheck exposed the summation error corrected above.

## 6. Deliverables

| File | Content |
|---|---|
| `audit/AUDIT_REPORT.md` | This report |
| `audit/AUDIT_RESULTS.csv` | One row per original record: before/after status, quality, fields changed, content check, notes |
| `audit/CHANGELOG.md` | Every field-level change with old → new values and the reason |
| `audit/INVALID_SOURCES.csv` | Rejected records, inaccessible records, rejected HF-inventory datasets |
| `audit/DUPLICATE_SOURCES.csv` | Mirror/subset/overlap relationships and how each is counted |
| `audit/LICENSING_UNCERTAINTIES.csv` | Records with unsettled licence / redistribution / commercial-use status |
| `audit/CORRECTED_CATALOGUE.csv` | All 204 records after correction, rejected ones included and flagged |
| `audit/MASTER_CATALOGUE.xlsx`, `.csv`, `audit/catalogues/` | Updated catalogue (active records) — same as repository root |
| `audit/VALIDATION_REPORT.csv` | Output of the automated quality checks |
| `audit/AUDIT_SUMMARY.json` | Machine-readable counts behind this report |
| `audit/original_snapshot/` | Untouched original records and outputs |

Reproduce: `scripts/apply_audit.py` → `scripts/build.py` → `scripts/validate.py` → `scripts/audit_outputs.py`.
