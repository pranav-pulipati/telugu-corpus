#!/usr/bin/env python3
"""Apply the 2026-11 audit to the ORIGINAL records and write the corrected records.

Reproducible by design:
    audit/original_snapshot/records/*.yaml  (untouched original research)
  + this file's decisions (each with a reason and evidence)
  + evidence/hf_telugu_check.jsonl (sampled-row Telugu check) and evidence/link_check.json
  = data/records/*.yaml (corrected, non-rejected) and data/rejected/rejected_records.yaml (archive)

Run: .venv/bin/python scripts/apply_audit.py && .venv/bin/python scripts/build.py && .venv/bin/python scripts/validate.py
"""
import glob, json, os, re, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
AUDIT_DATE = "2026-11-09"
LIC = "evidence/licences/"

# ---------------------------------------------------------------------------------------------------------
# 1. Rejections (record kept in data/rejected/ with its original content and the reason).
# ---------------------------------------------------------------------------------------------------------
REJECT = {
    "TEL-TXT-024": "Duplicate without independent value: a line-split re-upload of IndicCorp text (TEL-TXT-003/TEL-TXT-004) with no licence, provenance or added annotation.",
    "TEL-DIAL-003": "Not an independent source: cross-reference record that only points to TEL-LEX-001, TEL-SPEECH-001/010/012/013 (no data of its own). Its dialect-gap note is preserved in the audit report.",
    "TEL-ACAD-002": "Out of scope: English-language research papers about Telugu NLP (ACL Anthology/arXiv), not Telugu-language data. Used only as provenance evidence for other records.",
    "TEL-AV-004": "Not an identifiable collection: generic platform record (YouTube/podcast/audiobook apps) with no enumerable Telugu collection, no size and no reusable terms; the openly licensed YouTube subset is already catalogued as TEL-SPEECH-016 (YODAS).",
}

# ---------------------------------------------------------------------------------------------------------
# 2. Field corrections. Each entry: fields to set + a note (appended to audit_notes) explaining why.
# ---------------------------------------------------------------------------------------------------------
FIX = {}


def fix(rid, note, **fields):
    FIX.setdefault(rid, []).append((note, fields))


# --- Licensing: corrected only where a primary/authoritative text was read (evidence/licences/) ----------
fix("TEL-LEX-010", "Licence conflict resolved from the repository LICENSE.txt (CC BY-SA 4.0); README prose mentioning CC BY-NC-SA 3.0 is superseded.",
    license="CC BY-SA 4.0 (LICENSE.txt in repository)", license_scope="Uniform (single license)", commercial_use="Allowed",
    license_evidence_url="https://raw.githubusercontent.com/UniversalDependencies/UD_Telugu-MTG/HEAD/LICENSE.txt",
    unresolved_issues="", add_evidence=["https://raw.githubusercontent.com/UniversalDependencies/UD_Telugu-MTG/HEAD/LICENSE.txt"])
fix("TEL-LEX-012", "Licence read from repository LICENSE.txt: CC BY-NC-SA 4.0 (was 'NOASSERTION/unknown').",
    license="CC BY-NC-SA 4.0 (LICENSE.txt in repository)", license_scope="Uniform (single license)",
    redistribution="Allowed with conditions", commercial_use="Not allowed",
    license_evidence_url="https://raw.githubusercontent.com/ltrc/telugu_treebank/HEAD/LICENSE.txt", unresolved_issues="",
    add_evidence=["https://raw.githubusercontent.com/ltrc/telugu_treebank/HEAD/LICENSE.txt"])
fix("TEL-TXT-004", "Licence found in the IndicBERT repository README: 'All the datasets created as part of this work will be released under a CC-0 license' (IndicCorp v2 is that work's corpus). Compilation licence only; crawled content copyright not cleared.",
    license="CC0 1.0 (IndicBERT v2 repository README; HF card declares none)", license_scope="Uniform (single license)",
    redistribution="Allowed with conditions", commercial_use="Allowed",
    license_evidence_url="https://github.com/AI4Bharat/IndicBERT#license",
    unresolved_issues="HF card itself declares no licence; licence taken from the project README.",
    add_evidence=["https://raw.githubusercontent.com/AI4Bharat/IndicBERT/HEAD/README.md"])
fix("TEL-PAR-003", "Removed unsupported claim that the Samanantar paper uses CC0; the HF card's Licensing Information section states CC BY-NC 4.0.",
    license="CC BY-NC 4.0 (HF card, Licensing Information)",
    copyright_notes="Non-commercial licence stated on the dataset card.", unresolved_issues="")
fix("TEL-PAR-012", "Licence confirmed from data.statmt.org/pmindia/README: 'released under the CC-BY-4.0'. Count from OPUS API; download URL responds. Upgraded to Verified.",
    license="CC BY 4.0 (PMIndia README)", license_evidence_url="https://data.statmt.org/pmindia/README",
    verification_status="Verified", verification_method="OPUS API count; README licence read; download URL HTTP 200",
    unresolved_issues="", add_evidence=["https://data.statmt.org/pmindia/README"])
fix("TEL-PAR-013", "Licence confirmed from the project README (Creative Commons Attribution 4.0). Upgraded to Verified.",
    license="CC BY 4.0 (project README)", verification_status="Verified",
    verification_method="OPUS API count; GitHub README licence read; download URL HTTP 200", unresolved_issues="",
    add_evidence=["https://raw.githubusercontent.com/project-anuvaad/anuvaad-parallel-corpus/HEAD/README.md"])
fix("TEL-PAR-014", "Licence confirmed from repository LICENSE (CC BY-SA 3.0 Unported, commercial use permitted). Upgraded to Verified.",
    license="CC BY-SA 3.0 Unported (repository LICENSE)", license_evidence_url="https://raw.githubusercontent.com/joshua-decoder/indian-parallel-corpora/HEAD/LICENSE",
    verification_status="Verified", verification_method="OPUS API count; repository LICENSE read; download URL HTTP 200", unresolved_issues="",
    add_evidence=["https://raw.githubusercontent.com/joshua-decoder/indian-parallel-corpora/HEAD/LICENSE"])
fix("TEL-PAR-007", "Licence confirmed from the NTREX README (CC BY-SA 4.0).",
    add_evidence=["https://raw.githubusercontent.com/MicrosoftTranslator/NTREX/HEAD/README.md"])
fix("TEL-OCR-009", "tel.traineddata confirmed in tessdata_best (9,098,795 bytes, GitHub API); repository licence Apache-2.0 (GitHub API).",
    size_telugu="tessdata_best/tel.traineddata = 9,098,795 bytes; langdata files not counted", size_confidence="Confirmed",
    verification_status="Verified", verification_method="GitHub contents API (file size) and repository licence API",
    add_evidence=["https://api.github.com/repos/tesseract-ocr/tessdata_best/contents/tel.traineddata"])
fix("TEL-TXT-015", "Card read: tagged 'synthetic' and 'translation'; states 'ready for commercial or non-commercial uses. Use is subject to the applicable source-specific terms' (sources mainly CC BY 4.0).",
    license="NVIDIA card: commercial or non-commercial use permitted, subject to source-specific governing terms (mostly CC BY 4.0)",
    license_scope="Varies per subset", redistribution="Allowed with conditions", commercial_use="Varies",
    unresolved_issues="Exact governing terms per sub-source must be checked before use.",
    add_evidence=["https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Indic-Specialized-v1/raw/main/README.md"])
fix("TEL-ANN-033", "LICENSE.md read: Microsoft Research License — use 'solely for non-commercial, non-revenue generating, research purposes'.",
    license="Microsoft Research License (non-commercial research only)", license_scope="Uniform (single license)",
    redistribution="Unclear", commercial_use="Not allowed",
    license_evidence_url="https://huggingface.co/datasets/microsoft/Updesh_beta/blob/main/LICENSE.md",
    unresolved_issues="Telugu row count not measured.")
fix("TEL-PAR-020", "Card read: 'Paired English–Telugu Children's Stories', tagged machine-translated / TinyStories — synthetic Telugu side confirmed.",
    description="English–Telugu parallel children's stories built from TinyStories-style English text with machine-translated Telugu (card tags: tinystories, machine-translated, parallel-corpus).",
    verification_status="Verified", verification_method="Dataset card read; datasets-server row count", unresolved_issues="",
    processing_needs="Synthetic/machine-translated Telugu — keep separate from natural text.")

# Unsupported / over-broad licence claims removed or weakened
fix("TEL-ANN-004", "Removed unsupported claim (from memory) that IndicXTREME benchmarks are CC0.",
    license="None declared on HF card")
fix("TEL-LIT-004", "Licence claim 'mostly CC BY 4.0' was not read from StoryWeaver (terms page is JavaScript-rendered; API exposes only a publisher copyright notice). Marked unconfirmed.",
    license="Not confirmed — per-book licence not exposed by API; terms page not readable by our tools",
    license_scope="Varies per item", redistribution="Unclear", commercial_use="Unclear",
    unresolved_issues="Confirm per-book licence on the StoryWeaver website before reuse.")
fix("TEL-LIT-005", "Removed unread claim that platform terms prohibit scraping; no open licence observed, so default copyright applies.",
    license="No open licence found; authors' default copyright", copyright_notes="Terms of service not read.")
fix("TEL-GOV-001", "Over-broad legal claim corrected: Copyright Act s.52(1)(q)(i) covers only matter published in the Official Gazette (excluding Acts); Government Orders not published in the Gazette are not covered (text checked via secondary legal source lawgist.in).",
    license="No licence statement; government copyright. Statutory exception s.52(1)(q)(i) applies only to GOs published in the Official Gazette",
    redistribution="Unclear", commercial_use="Unclear", license_evidence_url="https://lawgist.in/copyright-act/52",
    copyright_notes="IA collection is a volunteer mirror, not the official source (goir.ap.gov.in).")
fix("TEL-GOV-002", "Same legal correction as TEL-GOV-001.",
    license="No licence statement; government copyright. s.52(1)(q)(i) applies only to Gazette-published matter",
    redistribution="Unclear", commercial_use="Unclear", license_evidence_url="https://lawgist.in/copyright-act/52")
fix("TEL-GOV-003", "s.52(1)(q)(i) permits reproduction/publication of Gazette matter EXCEPT Acts of a Legislature; gazettes also print Acts, so terms vary by item (secondary legal source).",
    license="Statutory exception s.52(1)(q)(i) for Gazette matter, excluding Acts (which need commentary under s.52(1)(q)(ii))",
    license_scope="Varies per item", redistribution="Allowed with conditions", commercial_use="Varies",
    license_evidence_url="https://lawgist.in/copyright-act/52")
fix("TEL-GOV-004", "PD statement on IA is the uploader's (Public Resource) assertion, not the AP Legislature's; commercial use downgraded to Unclear pending confirmation.",
    license="Public domain per IA licenseurl on all items (uploader assertion; not confirmed by the AP Legislature)",
    commercial_use="Unclear", redistribution="Allowed with conditions",
    unresolved_issues="Confirm status of legislative debates with AP Legislature / legal review.")
fix("TEL-GOV-005", "Statutory exception s.52(1)(q)(iv) permits reproduction/publication of judgments unless prohibited by the court (secondary legal source).",
    license="Statutory exception s.52(1)(q)(iv): judgments may be reproduced unless the court prohibits it",
    redistribution="Allowed with conditions", commercial_use="Allowed", license_evidence_url="https://lawgist.in/copyright-act/52")
fix("TEL-GOV-006", "Over-broad claim corrected: s.52(1)(q)(ii) allows reproducing an Act only together with commentary or other original matter; bare redistribution of statute text is not covered (secondary legal source).",
    license="Government copyright; s.52(1)(q)(ii) permits reproduction of Acts only with commentary/original matter",
    redistribution="Not allowed", commercial_use="Unclear", license_evidence_url="https://lawgist.in/copyright-act/52")
fix("TEL-GOV-007", "Removed unsupported claim that GODL-India applies to PIB releases.",
    license="No licence statement verified", license_scope="Unknown", redistribution="Unclear", commercial_use="Unclear")
fix("TEL-MSS-001", "PD Mark is the IA uploader's assertion and conflicts with the source portal's 'all rights reserved' line; commercial use downgraded to Unclear.",
    commercial_use="Unclear", redistribution="Allowed with conditions")
fix("TEL-PERIOD-004", "CC BY-SA was applied by the IA uploader; whether the uploader holds the rights is unconfirmed — commercial use downgraded to Unclear.",
    commercial_use="Unclear")
fix("TEL-DLIB-013", "EAP terms page could not be read (guessed URLs 404); licence restrictions were not confirmed, so commercial/redistribution set to Unclear.",
    redistribution="Unclear", commercial_use="Unclear")
fix("TEL-SPEECH-009", "Licence text (Microsoft Research data licence linked from OpenSLR 103) was not read; restrictions marked Unclear instead of asserted.",
    license="Microsoft Research data licence (linked from OpenSLR 103; text not read)", redistribution="Unclear", commercial_use="Unclear")
fix("TEL-TXT-017", "'Allowed' was misleading: commercial use requires a paid LDC-IL licence.", commercial_use="Varies")
fix("TEL-SPEECH-013", "'Allowed' was misleading: commercial use requires a paid LDC-IL licence.", commercial_use="Varies")

# --- Unsupported numerical / descriptive claims ----------------------------------------------------------
fix("TEL-TXT-001", "Removed unsupported provenance claim about the share of bot-generated village stubs (not measured).",
    provenance="Volunteer-written Telugu Wikipedia.",
    processing_needs="Wiki-markup stripping; check for template-generated short articles; dedup against web crawls that include Wikipedia.")
fix("TEL-TXT-014", "Added Telugu token count from the dataset card (767.18M tokens); removed unsupported 'long-context' purpose claim.",
    size_telugu="16.63 GB (te/shard-*.txt); 767.18M tokens (dataset card table)",
    description="Document-level monolingual corpus for 22 scheduled Indian languages + English (IIT Bombay CFILT).",
    add_evidence=["https://huggingface.co/datasets/cfilt/IITB-IndicMonoDoc/raw/main/README.md"])
fix("TEL-ANN-019", "Corrected language count: MASSIVE README states >1M utterances across 52 languages (record said 51 locales).",
    description="Spoken-language-understanding dataset of virtual-assistant utterances (intent + slots), localised by professional translators; >1M utterances across 52 languages incl. Telugu (te-IN).")
fix("TEL-ANN-030", "Pair count (20,329) came from a search-index extract of the README, not from our fetched copy; downgraded to Partially Verified.",
    verification_status="Partially Verified", verification_method="README licence read; pair count via search extract (not re-counted)",
    unresolved_issues="Count lines in TeSum_data/ to confirm 20,329.")
fix("TEL-MSS-008", "Description already softened (copper-plate count unverified); no figures retained.")

# --- Content findings from sampled rows / files -----------------------------------------------------------
fix("TEL-PAR-018", "Content check: the 'Telugu' side is Bharati Braille cells (data.tebb), so no Telugu script is expected; Telugu text itself is not present.",
    telugu_scope="Telugu-related", unresolved_issues="Telugu side is Braille transcription only; provenance of underlying Telugu text undocumented.")
fix("TEL-ANN-029", "Content check: CodeSwitching-TE-EN sample is romanised Telugu-English social-media text (e.g. 'geniune review bayya'), no Telugu script.",
    scripts=["Latn", "Telu"])
fix("TEL-ANN-024", "Content check: the Telugu_Clickbait repo's text is Telugu in WX romanisation (e.g. 'kApI vivAxaMlo xeviSrI prasAx'), not Telugu script; needs WX→Telugu conversion.",
    scripts=["Telu", "Latn"],
    description="One corpus of 35,142 Telugu sentences annotated for four tasks (sentiment, emotion, hate speech, sarcasm), published as four HF repos; plus a separate 112,657-row clickbait dataset whose text is WX-romanised Telugu (Latin letters).")
fix("TEL-OCR-007", "Content check: Telugu-book-text-images has only image, file_name and page_number columns — no transcription, so it is not OCR ground truth; the family is a mix of labelled and unlabelled sets.",
    description="Family of Telugu document-image datasets by one uploader: telugu-wikisource-text-images (659,924 rows, CC BY-SA 4.0), telugu-line-ocr-bench (1,044, CC BY-SA 4.0) and synthetic line images (MIT) carry text; Telugu-book-text-images (232,500, MIT) holds page images WITHOUT transcriptions (columns image, file_name, page_number).",
    annotations=["line transcriptions (some subsets only)"],
    unresolved_issues="Book source and copyright for Telugu-book-text-images undocumented; MIT tag on book scans questionable; it has no text labels.")
fix("TEL-SPEECH-020", "Content check: Telugu appears only in the card's language tags; no Telugu locale or rows found in sampled data — relevance unconfirmed.",
    unresolved_issues="Confirm that SVQ actually contains Telugu (te) utterances; only the metadata tag mentions Telugu.")
fix("TEL-SPEECH-022", "Content check: config 'Telugu' exists but rows hold audio + metadata only (no text to test).")

# --- Arithmetic error found on recheck -------------------------------------------------------------------
fix("TEL-PAR-001", "Corrected total: the original sum (55,280,752) stopped at a corpus with an empty count (Ubuntu) and omitted later corpora. Recomputed over all numeric alignment_pairs from the OPUS API: 55,907,602 (NLLB 46,376,267 = 83%).",
    size_telugu="55,907,602 en-te sentence pairs across 21 corpora (sum of numeric alignment_pairs, OPUS API 2026-11-09; NLLB-mined = 83%)",
    add_evidence=["https://opus.nlpl.eu/opusapi/?source=en&target=te&preprocessing=moses&version=latest"])

# --- Verification status corrections from access checks ---------------------------------------------------
fix("TEL-LIT-010", "Status corrected: site presents an invalid TLS certificate and no catalogue content was inspected — Inaccessible, not Partially Verified.",
    verification_status="Inaccessible", verification_method="HTTPS certificate verification fails (2026-11-09); no content inspected")
fix("TEL-EDU-002", "Status corrected: site presents an invalid TLS certificate; nothing inspected.",
    verification_status="Inaccessible", verification_method="HTTPS certificate verification fails (2026-11-09); no content inspected")
fix("TEL-PAR-015", "Status corrected: TDIL-DC fails certificate verification and the Telugu ILCI data was never seen; existence rests on a 2012 presentation and LREC 2010 paper.",
    verification_status="Unverified", verification_method="Secondary documents only; tdil-dc.in fails HTTPS certificate verification (2026-11-09)")
fix("TEL-OCR-011", "Status corrected: repository returned HTTP 503 in both link checks.",
    verification_status="Inaccessible", verification_method="DSpace item returned HTTP 503 (2026-11-09)")
fix("TEL-TXT-003", "Status corrected: the documented download URL returns HTTP 403; data cannot be obtained from the stated source.",
    verification_status="Inaccessible", bulk_download="Unknown")
fix("TEL-PAR-016", "Status corrected: project homepage returns 404 and the HF loader points to the same dead server; only the 5,049-pair Mann Ki Baat test set survives (in TEL-ANN-002).",
    verification_status="Inaccessible", size_telugu="Accessible part: cvit-mkb-clsr.en-te 5,049 pairs (inside IndicGLUE, TEL-ANN-002); PIB v1.3 en-te not obtainable",
    size_confidence="Confirmed")

# --- Reclassification ---------------------------------------------------------------------------------
fix("TEL-SPEECH-018", "Reclassified: Bhashini/ULCA is a multimodal national data portal, not a speech dataset (ID kept permanent).",
    primary_category="DLIB", secondary_categories=["SPEECH", "PAR", "OCR", "TXT"])
fix("TEL-SPEECH-019", "Reclassified: AIKosh is a multimodal dataset platform, not a speech dataset (ID kept permanent).",
    primary_category="DLIB", secondary_categories=["SPEECH", "OCR", "TXT", "PAR"])
fix("TEL-ACAD-003", "Content role clarified: no digital collection found — reference/contact record only.",
    record_type="Portal/Index")
fix("TEL-LIT-010", "Content role clarified: catalogue/award metadata only.", record_type="Portal/Index")

# ---------------------------------------------------------------------------------------------------------
# 3. Content role and de-duplication (prevents double counting). count_in_totals = No for any record whose
#    data is fully contained in, mirrored by, or superseded by another record.
# ---------------------------------------------------------------------------------------------------------
ROLE = {  # rid: (content_role, dedup_role, canonical_record, count_in_totals)
    "TEL-DLIB-001": ("Aggregator/platform", "Aggregate (contains other records)", "", "No"),
    "TEL-DLIB-003": ("Mirror/re-packaging", "Partial overlap", "TEL-DLIB-002", "Yes"),
    "TEL-DLIB-007": ("Aggregator/platform", "Aggregate (contains other records)", "", "No"),
    "TEL-DLIB-008": ("Aggregator/platform", "Partial overlap", "TEL-LIT-001", "Yes"),
    "TEL-DLIB-009": ("Index/reference only", "Aggregate (contains other records)", "", "No"),
    "TEL-DLIB-010": ("Aggregator/platform", "Canonical", "", "Yes"),
    "TEL-DLIB-011": ("Aggregator/platform", "Canonical", "", "Yes"),
    "TEL-DLIB-012": ("Aggregator/platform", "Canonical", "", "Yes"),
    "TEL-DLIB-013": ("Original data", "Partial overlap", "TEL-DLIB-004", "Yes"),
    "TEL-SPEECH-018": ("Index/reference only", "Aggregate (contains other records)", "", "No"),
    "TEL-SPEECH-019": ("Index/reference only", "Aggregate (contains other records)", "", "No"),
    "TEL-PERIOD-002": ("Original data (sub-collection)", "Partial overlap", "TEL-DLIB-005", "Yes"),
    "TEL-PERIOD-006": ("Original data", "Canonical", "", "Yes"),
    "TEL-PERIOD-008": ("Original data (sub-collection)", "Subset of", "TEL-REL-001", "No"),
    "TEL-MSS-001": ("Mirror/re-packaging", "Mirror of", "TEL-MSS-002", "Yes"),
    "TEL-MSS-002": ("Original data", "Canonical", "", "No"),
    "TEL-MSS-004": ("Index/reference only", "Canonical", "", "Yes"),
    "TEL-MSS-008": ("Original data", "Partial overlap", "TEL-REL-001", "Yes"),
    "TEL-LIT-002": ("Original data", "Same platform as", "TEL-LEX-001", "Yes"),
    "TEL-LIT-006": ("Original data", "Canonical", "", "Yes"),
    "TEL-LIT-010": ("Index/reference only", "Canonical", "", "Yes"),
    "TEL-LEX-009": ("Original data", "Partial overlap", "TEL-LEX-001", "Yes"),
    "TEL-TXT-002": ("Derived (cleaned re-packaging)", "Mirror of", "TEL-TXT-001", "No"),
    "TEL-TXT-003": ("Original data", "Superseded by", "TEL-TXT-004", "No"),
    "TEL-TXT-005": ("Derived (compiled from other sources)", "Partial overlap", "TEL-TXT-004", "Yes"),
    "TEL-TXT-006": ("Derived (compiled from other sources)", "Canonical", "", "Yes"),
    "TEL-TXT-007": ("Derived (compiled from other sources)", "Partial overlap", "TEL-TXT-025", "Yes"),
    "TEL-TXT-008": ("Derived (compiled from other sources)", "Partial overlap", "TEL-TXT-025", "Yes"),
    "TEL-TXT-009": ("Derived (compiled from other sources)", "Partial overlap", "TEL-TXT-025", "Yes"),
    "TEL-TXT-010": ("Derived (compiled from other sources)", "Partial overlap", "TEL-TXT-025", "Yes"),
    "TEL-TXT-011": ("Derived (compiled from other sources)", "Included in", "TEL-TXT-006", "No"),
    "TEL-TXT-012": ("Derived (compiled from other sources)", "Partial overlap", "TEL-TXT-025", "Yes"),
    "TEL-TXT-013": ("Derived (compiled from other sources)", "Included in", "TEL-TXT-006", "No"),
    "TEL-TXT-019": ("Derived (compiled from other sources)", "Partial overlap", "TEL-TXT-025", "Yes"),
    "TEL-TXT-020": ("Derived (compiled from other sources)", "Partial overlap", "TEL-TXT-026", "Yes"),
    "TEL-TXT-025": ("Original data", "Aggregate (contains other records)", "", "No"),
    "TEL-TXT-026": ("Derived (compiled from other sources)", "Canonical", "", "Yes"),
    "TEL-PAR-001": ("Aggregator/platform", "Aggregate (contains other records)", "", "No"),
    "TEL-PAR-002": ("Original data", "Included in", "TEL-PAR-001", "Yes"),
    "TEL-PAR-003": ("Derived (compiled from other sources)", "Included in", "TEL-PAR-001", "Yes"),
    "TEL-PAR-004": ("Derived (compiled from other sources)", "Partial overlap", "TEL-PAR-003", "Yes"),
    "TEL-PAR-008": ("Derived (compiled from other sources)", "Subset of", "TEL-PAR-001", "No"),
    "TEL-PAR-009": ("Derived (compiled from other sources)", "Partial overlap", "TEL-GOV-007", "Yes"),
    "TEL-PAR-012": ("Original data", "Included in", "TEL-PAR-001", "Yes"),
    "TEL-PAR-013": ("Original data", "Included in", "TEL-PAR-001", "Yes"),
    "TEL-PAR-014": ("Original data", "Included in", "TEL-PAR-001", "Yes"),
    "TEL-PAR-016": ("Original data", "Partial overlap", "TEL-ANN-002", "No"),
    "TEL-PAR-017": ("Original data", "Included in", "TEL-PAR-001", "Yes"),
    "TEL-PAR-021": ("Mirror/re-packaging", "Probable duplicate of", "TEL-PAR-003", "No"),
    "TEL-PAR-023": ("Derived (cleaned re-packaging)", "Derived from", "TEL-GOV-008", "Yes"),
    "TEL-ANN-013": ("Derived (compiled from other sources)", "Derived from", "TEL-ANN-012", "Yes"),
    "TEL-ANN-016": ("Aggregator/platform", "Aggregate (contains other records)", "", "No"),
    "TEL-ANN-017": ("Original data", "Included in", "TEL-ANN-016", "Yes"),
    "TEL-ANN-020": ("Derived (compiled from other sources)", "Canonical", "", "Yes"),
    "TEL-ANN-026": ("Derived (compiled from other sources)", "Partial overlap", "TEL-ANN-020", "Yes"),
    "TEL-ANN-028": ("Derived (compiled from other sources)", "Canonical", "", "Yes"),
    "TEL-OCR-005": ("Derived (cleaned re-packaging)", "Derived from", "TEL-LIT-001", "Yes"),
    "TEL-OCR-007": ("Derived (cleaned re-packaging)", "Partial overlap", "TEL-OCR-005", "Yes"),
    "TEL-SPEECH-002": ("Derived (cleaned re-packaging)", "Derived from", "TEL-SPEECH-001", "Yes"),
    "TEL-SPEECH-004": ("Derived (compiled from other sources)", "Derived from", "TEL-AV-001", "Yes"),
    "TEL-SPEECH-017": ("Derived (compiled from other sources)", "Partial overlap", "TEL-SPEECH-007", "Yes"),
    "TEL-SPEECH-022": ("Derived (synthetic)", "Derived from", "TEL-SPEECH-003", "Yes"),
    "TEL-EDU-004": ("Derived (compiled from other sources)", "Partial overlap", "TEL-EDU-001", "Yes"),
    "TEL-EDU-005": ("Derived (compiled from other sources)", "Same corpus as", "TEL-EDU-004", "No"),
    "TEL-GOV-003": ("Mirror/re-packaging", "Partial overlap", "TEL-DLIB-007", "Yes"),
    "TEL-GOV-001": ("Mirror/re-packaging", "Mirror of external source", "", "Yes"),
    "TEL-GOV-002": ("Mirror/re-packaging", "Mirror of external source", "", "Yes"),
    "TEL-GOV-008": ("Mirror/re-packaging", "Mirror of", "TEL-GOV-005", "Yes"),
    "TEL-GOV-005": ("Original data", "Canonical", "", "No"),
    "TEL-GOV-007": ("Original data", "Canonical", "", "Yes"),
    "TEL-REL-001": ("Original data", "Canonical", "", "Yes"),
    "TEL-REL-002": ("Original data", "Partial overlap", "TEL-PAR-001", "Yes"),
    "TEL-REL-003": ("Original data", "Partial overlap", "TEL-LIT-001", "Yes"),
    "TEL-DIAL-002": ("Derived (compiled from other sources)", "Canonical", "", "Yes"),
    "TEL-ACAD-003": ("Index/reference only", "Canonical", "", "Yes"),
    "TEL-ACAD-001": ("Aggregator/platform", "Canonical", "", "Yes"),
    "TEL-AV-001": ("Original data", "Canonical", "", "Yes"),
    "TEL-AV-003": ("Original data (sub-collection)", "Canonical", "", "Yes"),
}
ROLE_NOTES = {
    "TEL-GOV-001": "Volunteer mirror of the official GO register goir.ap.gov.in (not separately catalogued).",
    "TEL-GOV-002": "Volunteer mirror of the official Telangana GO register (not separately catalogued).",
    "TEL-MSS-002": "Counted via its accessible IA mirror TEL-MSS-001 to avoid double counting.",
    "TEL-GOV-005": "Supreme Court portion counted via TEL-GOV-008 (bulk mirror); AP HC Telugu judgments (811) not separately downloadable.",
    "TEL-PAR-021": "Provenance undocumented; likely re-packaged Samanantar/OPUS — excluded from totals pending evidence.",
    "TEL-PAR-016": "Accessible part already inside TEL-ANN-002.",
}


def default_role(r):
    t = r.get("record_type")
    if t == "Platform":
        return ("Aggregator/platform", "Canonical", "", "Yes")
    if t == "Portal/Index":
        return ("Index/reference only", "Canonical", "", "Yes")
    if t == "Tool/Resource":
        return ("Tool/model (not a corpus)", "Canonical", "", "Yes")
    if r.get("parent_id"):
        return ("Original data (sub-collection)", "Canonical", "", "Yes")
    return ("Original data", "Canonical", "", "Yes")


# ---------------------------------------------------------------------------------------------------------
# 4. Sampled-row Telugu check (evidence/hf_telugu_check.jsonl) — applied to records whose collection is on HF.
# ---------------------------------------------------------------------------------------------------------
def load_hf_checks():
    out = {}
    # pass 1 (all datasets) then pass 2 recheck (targeted); a later CONFIRMED or more specific result wins
    for p in sorted(glob.glob("evidence/hf_telugu_check*.jsonl")) + ["evidence/hf_telugu_recheck.jsonl"]:
        if os.path.exists(p):
            for line in open(p, encoding="utf-8"):
                if line.strip():
                    d = json.loads(line)
                    prev = out.get(d["hf_id"])
                    rank = {"CONFIRMED_TELUGU_TEXT": 4, "TELUGU_STRUCTURE_ONLY": 3, "ROMANISED_TELUGU_CLAIMED": 3,
                            "NO_TELUGU_IN_SAMPLE": 2, "NOT_FOUND": 2, "NOT_CHECKABLE": 1, "ERROR": 0}
                    # a later result replaces an earlier one only if it carries at least as much evidence
                    if prev is None or rank.get(d.get("verdict"), 0) >= rank.get(prev.get("verdict"), 0):
                        out[d["hf_id"]] = d
    return out


def final_verdict(d, name=""):
    """Post-process raw verdicts: too little text sampled => not checkable; romanised names => romanised."""
    v = d.get("verdict")
    s = d.get("sample") or {}
    if v == "NO_TELUGU_IN_SAMPLE":
        if re.search(r"roman|latn|translit", d["hf_id"], re.I):
            return "ROMANISED_TELUGU_CLAIMED"
        if s.get("chars", 0) < 200:
            return "NOT_CHECKABLE"
    return v


def hf_id_of(url):
    m = re.match(r"https://huggingface\.co/datasets/([^/\s?#]+/[^/\s?#]+)", url or "")
    return m.group(1) if m else None


def describe_check(d):
    v = final_verdict(d)
    s = d.get("sample") or {}
    if "telugu_chars" in s:
        return f"{v}: {s['telugu_chars']:,} Telugu-script chars in {s['rows']} sampled rows (config {s['config']}) on {d.get('checked')}"
    return f"{v}: {s.get('error') or d.get('detail','')} (Telugu configs: {', '.join(d.get('telugu_configs') or []) or 'none'}) on {d.get('checked')}"


# ---------------------------------------------------------------------------------------------------------
# 5. Quality rating (kept separate from verification status).
# ---------------------------------------------------------------------------------------------------------
def quality(r):
    st, sc = r.get("verification_status"), r.get("size_confidence")
    lic = str(r.get("license", ""))
    lic_known = r.get("license_scope") not in ("Unknown",) and not re.search(r"not confirmed|unknown|none declared|not read", lic, re.I)
    if st == "Verified":
        if sc in ("Confirmed", "Reported by source") and lic_known:
            return "High", "Directly verified; size measured or documented by source; licence stated by source."
        why = []
        if sc not in ("Confirmed", "Reported by source"):
            why.append("size not established")
        if not lic_known:
            why.append("licence not established")
        return "Medium", "Verified, but " + " and ".join(why) + "."
    if st == "Partially Verified":
        if sc in ("Confirmed", "Reported by source"):
            return "Medium", "Relevant and partially verified; limitations listed in unresolved_issues."
        return "Low", "Partially verified with no established Telugu size; weak or incomplete metadata."
    if st == "Inaccessible":
        return "Low", "Source not accessible on the check date; claims rest on secondary evidence."
    return "Low", "Unverified: not inspected at source; relevance or details uncertain."


# ---------------------------------------------------------------------------------------------------------
def load_original():
    recs = []
    for path in sorted(glob.glob("audit/original_snapshot/records/*.yaml")):
        doc = yaml.safe_load(open(path, encoding="utf-8")) or {}
        defaults = doc.get("defaults", {})
        for raw in doc.get("records", []):
            r = dict(defaults)
            r.update(raw)
            recs.append((os.path.basename(path), r))
    return recs


def as_list(v):
    if v in (None, ""):
        return []
    return list(v) if isinstance(v, list) else [x.strip() for x in str(v).split(" | ") if x.strip()]


def main():
    hf = load_hf_checks()
    link = json.load(open("evidence/link_check.json")) if os.path.exists("evidence/link_check.json") else {}
    by_file, rejected = {}, []
    for fname, r in load_original():
        rid = r["record_id"]
        notes = []
        # field fixes
        for note, fields in FIX.get(rid, []):
            notes.append(note)
            for k, v in fields.items():
                if k == "add_evidence":
                    ev = as_list(r.get("evidence_urls"))
                    r["evidence_urls"] = ev + [u for u in v if u not in ev]
                else:
                    r[k] = v
        # role / dedup
        role = ROLE.get(rid, default_role(r))
        r["content_role"], r["dedup_role"], r["canonical_record"], r["count_in_totals"] = role
        if rid in ROLE_NOTES:
            notes.append(ROLE_NOTES[rid])
        # HF sampled-row check
        hid = hf_id_of(r.get("collection_url"))
        if hid and hid in hf:
            d = hf[hid]
            v = final_verdict(d)
            r["telugu_content_check"] = describe_check(d)
            if v == "CONFIRMED_TELUGU_TEXT":
                pass
            elif r.get("verification_status") == "Verified":
                r["verification_status"] = "Partially Verified"
                notes.append(f"Downgraded from Verified: Telugu text was not observed in sampled rows ({v}).")
            if v == "NOT_FOUND":
                r["verification_status"] = "Inaccessible"
                notes.append("Hugging Face repository no longer exists (404).")
        elif hid:
            r["telugu_content_check"] = "Not yet checked"
        else:
            r["telugu_content_check"] = "Not applicable (not a Hugging Face dataset); see verification_method"
        # link status sanity: a Verified record whose collection URL is dead cannot stay Verified
        lc = link.get(r.get("collection_url"))
        if lc and not (200 <= lc.get("status", 0) < 400) and r.get("verification_status") == "Verified":
            r["verification_status"] = "Partially Verified"
            notes.append(f"Downgraded from Verified: collection URL returned {lc.get('status')} {lc.get('error','')} in the automated check.")
        r["last_verified"] = AUDIT_DATE
        if rid in REJECT:
            r["quality_rating"], r["quality_rationale"] = "Rejected", REJECT[rid]
            r["rejection_reason"] = REJECT[rid]
            r["audit_status"] = "Rejected"
            r["count_in_totals"] = "No"
            r["audit_notes"] = " ".join(notes) if notes else ""
            rejected.append(r)
            continue
        r["quality_rating"], r["quality_rationale"] = quality(r)
        r["rejection_reason"] = ""
        r["audit_status"] = "Corrected" if notes else "Reviewed - no change to claims"
        r["audit_notes"] = " ".join(notes)
        by_file.setdefault(fname, []).append(r)
    os.makedirs("data/records", exist_ok=True)
    for f in glob.glob("data/records/*.yaml"):
        os.remove(f)
    hdr = "# Corrected records (generated by scripts/apply_audit.py from audit/original_snapshot/records). Edit apply_audit.py, not this file.\n"
    for fname, recs in by_file.items():
        with open(f"data/records/{fname}", "w", encoding="utf-8") as fh:
            fh.write(hdr)
            yaml.safe_dump({"records": recs}, fh, allow_unicode=True, sort_keys=False, width=10000)
    os.makedirs("data/rejected", exist_ok=True)
    with open("data/rejected/rejected_records.yaml", "w", encoding="utf-8") as fh:
        fh.write("# Rejected records — original content preserved with rejection_reason. Excluded from MASTER_CATALOGUE.\n")
        yaml.safe_dump({"records": rejected}, fh, allow_unicode=True, sort_keys=False, width=10000)
    n = sum(len(v) for v in by_file.values())
    print(f"wrote {n} active records, {len(rejected)} rejected; HF checks available for {len(hf)} datasets")


if __name__ == "__main__":
    main()
