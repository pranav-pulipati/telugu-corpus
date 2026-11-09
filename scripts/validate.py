#!/usr/bin/env python3
"""Automated quality checks on the built catalogue. Exit code 1 if any ERROR is found.

Checks: mandatory fields, enum values, malformed URLs, duplicate IDs / collection URLs / HF dataset ids,
unsupported licensing claims, inconsistent verification statuses, quality-rating rules, internal references,
double counting across mirrors, CSV <-> XLSX consistency, HF inventory decisions vs master records.

Writes audit/VALIDATION_REPORT.csv.  Run after build.py:  .venv/bin/python scripts/validate.py
"""
import csv, json, os, re, sys, collections
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
schema = yaml.safe_load(open("data/schema.yaml"))
FIELDS, ENUMS, CATS = list(schema["fields"]), schema["enums"], schema["categories"]
ENUM_FIELDS = ["record_type", "org_type", "telugu_scope", "modality", "digitization", "bulk_download", "registration",
               "authentication", "license_scope", "redistribution", "commercial_use", "size_confidence",
               "verification_status", "corpus_value", "quality_rating", "content_role", "dedup_role",
               "count_in_totals", "audit_status"]
URL_RE = re.compile(r"^https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(:\d+)?(/[^\s]*)?$")
issues = []


def add(level, rid, check, msg):
    issues.append({"level": level, "record_id": rid, "check": check, "message": msg})


def read_csv(p):
    return list(csv.DictReader(open(p, encoding="utf-8")))


master = read_csv("MASTER_CATALOGUE.csv")
corrected = read_csv("audit/CORRECTED_CATALOGUE.csv")
ids_all = {r["record_id"]: r for r in corrected}
active = {r["record_id"]: r for r in master}
# master rows take precedence; rejected rows come from the corrected (all-records) file
allrows = master + [r for r in corrected if r["record_id"] not in active]
link = json.load(open("evidence/link_check.json")) if os.path.exists("evidence/link_check.json") else {}

# 1. mandatory fields + enums + categories
for r in allrows:
    rid = r["record_id"]
    for f, (req, _) in schema["fields"].items():
        if req and not r.get(f, "").strip():
            add("ERROR", rid, "mandatory field", f"missing {f}")
    for f in ENUM_FIELDS:
        if r.get(f) and r[f] not in ENUMS[f]:
            add("ERROR", rid, "enum value", f"{f}={r[f]!r} not allowed")
    for c in [r["primary_category"]] + [c for c in r["secondary_categories"].split("; ") if c]:
        if c not in CATS:
            add("ERROR", rid, "category", f"unknown category {c}")

# 2. malformed URLs
for r in allrows:
    for f in ("official_url", "collection_url", "license_evidence_url"):
        u = r.get(f, "").strip()
        if u and not URL_RE.match(u.replace(" ", "%20")):
            add("ERROR", r["record_id"], "malformed URL", f"{f}: {u}")
        if " " in u:
            add("WARN", r["record_id"], "malformed URL", f"{f} contains a space: {u}")
    for u in [x.strip() for x in r["evidence_urls"].split(" | ") if x.strip()]:
        if not URL_RE.match(u.replace(" ", "%20")):
            add("ERROR", r["record_id"], "malformed URL", f"evidence_urls: {u}")

# 3. duplicates: ids, collection URLs, HF dataset ids
cnt = collections.Counter(r["record_id"] for r in master)
for r in corrected:
    if r["record_id"] not in active and r["quality_rating"] != "Rejected":
        add("ERROR", r["record_id"], "missing record", "record in CORRECTED_CATALOGUE is neither active nor rejected")
for i, n in cnt.items():
    if n > 1:
        add("ERROR", i, "duplicate id", f"{n} records share this id")
by_url = collections.defaultdict(list)
for r in master:
    by_url[r["collection_url"].rstrip("/").lower()].append(r["record_id"])
for u, rs in by_url.items():
    if len(rs) > 1:
        declared = all(any(o in (ids_all[x]["duplicates_mirrors"] + ids_all[x]["canonical_record"]) for o in rs if o != x) for x in rs)
        add("WARN" if declared else "ERROR", ";".join(rs), "duplicate collection_url",
            f"{u} used by {len(rs)} records ({'declared' if declared else 'NOT declared'} as related)")
hf_of = lambda u: (re.match(r"https://huggingface\.co/datasets/([^/\s?#]+/[^/\s?#]+)", u) or [None, None])[1]
hfids = collections.defaultdict(list)
for r in master:
    h = hf_of(r["collection_url"])
    if h:
        hfids[h.lower()].append(r["record_id"])
for h, rs in hfids.items():
    if len(rs) > 1:
        add("ERROR", ";".join(rs), "duplicate dataset id", f"HF dataset {h} is the collection of {len(rs)} records")

# 4. unsupported licensing claims
for r in master:
    rid, lic = r["record_id"], r["license"]
    weak = re.search(r"not confirmed|unknown|none declared|not read|no licence|no license|not stated", lic, re.I)
    if r["commercial_use"] == "Allowed" and weak:
        add("ERROR", rid, "unsupported licence", f"commercial_use=Allowed but licence is '{lic[:80]}'")
    if r["commercial_use"] == "Allowed" and not r["license_evidence_url"]:
        add("ERROR", rid, "unsupported licence", "commercial_use=Allowed without license_evidence_url")
    if r["redistribution"] == "Allowed" and r["license_scope"] == "Unknown":
        add("ERROR", rid, "unsupported licence", "redistribution=Allowed with license_scope=Unknown")
    if r["license_scope"] == "Uniform (single license)" and re.search(r"varies|mixed", lic, re.I):
        add("WARN", rid, "licence scope", "scope Uniform but licence text says varies/mixed")

# 5. verification status consistency
for r in master:
    rid, st = r["record_id"], r["verification_status"]
    lc = link.get(r["collection_url"])
    if st == "Verified":
        if not r["license_evidence_url"]:
            add("ERROR", rid, "status consistency", "Verified without license_evidence_url")
        if lc and not (200 <= lc["status"] < 400):
            add("ERROR", rid, "status consistency", f"Verified but collection URL check = {lc['status']}")
        if r["telugu_content_check"].startswith(("NO_TELUGU", "NOT_FOUND", "NOT_CHECKABLE", "TELUGU_STRUCTURE")):
            add("ERROR", rid, "status consistency", f"Verified but Telugu content not confirmed: {r['telugu_content_check'][:60]}")
    if st == "Unverified" and r["size_confidence"] == "Confirmed":
        add("ERROR", rid, "status consistency", "Unverified record claims a Confirmed size")
    if st == "Inaccessible" and lc and 200 <= lc["status"] < 400 and "certificate" not in r["verification_method"].lower() \
            and "403" not in r["verification_method"] and "404" not in r["verification_method"]:
        add("WARN", rid, "status consistency", "Inaccessible but collection URL responded 2xx/3xx — re-check")
    if r["telugu_content_check"] == "Not yet checked":
        add("WARN", rid, "telugu content", "HF dataset not yet content-checked")

# 6. quality rating rules (separate from status, but bounded by it)
for r in allrows:
    q, st, rid = r["quality_rating"], r["verification_status"], r["record_id"]
    if q == "High" and st != "Verified":
        add("ERROR", rid, "quality rule", "High quality requires Verified status")
    if q == "Rejected" and not r["rejection_reason"]:
        add("ERROR", rid, "quality rule", "Rejected without rejection_reason")
    if q != "Rejected" and r["rejection_reason"]:
        add("ERROR", rid, "quality rule", "rejection_reason set on non-rejected record")
    if q == "Rejected" and rid in active:
        add("ERROR", rid, "rejected leak", "Rejected record present in MASTER_CATALOGUE")

# 7. internal references (must exist; must not point at rejected records)
for r in master:
    rid = r["record_id"]
    refs = [("parent_id", r["parent_id"]), ("canonical_record", r["canonical_record"])] + \
           [("duplicates_mirrors", d.split()[0]) for d in r["duplicates_mirrors"].split(" | ") if d.startswith("TEL-")]
    for f, ref in refs:
        if not ref:
            continue
        if ref not in ids_all:
            add("ERROR", rid, "broken reference", f"{f} -> {ref} does not exist")
        elif ref not in active:
            add("WARN", rid, "reference to rejected", f"{f} -> {ref} is rejected")

# 8. double counting across mirrors
for r in master:
    rid, role, can, cnt_ = r["record_id"], r["dedup_role"], r["canonical_record"], r["count_in_totals"]
    if role in ("Mirror of", "Subset of", "Included in", "Superseded by", "Same corpus as", "Derived from", "Probable duplicate of", "Partial overlap", "Same platform as") and not can:
        add("ERROR", rid, "dedup", f"dedup_role '{role}' without canonical_record")
    if role in ("Subset of", "Superseded by", "Same corpus as", "Probable duplicate of", "Aggregate (contains other records)") and cnt_ == "Yes":
        add("ERROR", rid, "double counting", f"'{role}' record must have count_in_totals=No")
    if role == "Mirror of" and cnt_ == "Yes" and can in active and active[can]["count_in_totals"] == "Yes":
        add("ERROR", rid, "double counting", f"mirror and its original {can} are both counted")
    if role == "Included in" and cnt_ == "Yes" and can in active and active[can]["count_in_totals"] == "Yes":
        add("ERROR", rid, "double counting", f"record and its container {can} are both counted")

# 9. CSV <-> XLSX consistency
try:
    import openpyxl
    wb = openpyxl.load_workbook("MASTER_CATALOGUE.xlsx", read_only=True)
    ws = wb["Master Catalogue"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = list(rows[0])
    if hdr != FIELDS:
        add("ERROR", "-", "csv/xlsx", "XLSX header differs from schema field order")
    x = {row[0]: ["" if v is None else str(v) for v in row] for row in rows[1:]}
    if set(x) != set(active):
        add("ERROR", "-", "csv/xlsx", f"record sets differ: xlsx-only {set(x)-set(active)}, csv-only {set(active)-set(x)}")
    for rid, r in active.items():
        if rid in x and [r[f] for f in FIELDS] != x[rid]:
            add("ERROR", rid, "csv/xlsx", "row values differ between CSV and XLSX")
    rej = list(wb["Rejected (archive)"].iter_rows(values_only=True))[1:]
    if {row[0] for row in rej} != {r["record_id"] for r in corrected if r["quality_rating"] == "Rejected"}:
        add("ERROR", "-", "csv/xlsx", "Rejected sheet does not match rejected records")
except Exception as e:
    add("ERROR", "-", "csv/xlsx", f"could not compare: {e}")

# 10. per-category CSVs contain exactly the right records
for code, c in CATS.items():
    p = "catalogues/" + c["csv"]
    want = {r["record_id"] for r in master if r["primary_category"] == code or code in r["secondary_categories"].split("; ")}
    got = {r["record_id"] for r in read_csv(p)} if os.path.exists(p) else set()
    if want != got:
        add("ERROR", "-", "category csv", f"{p} mismatch: missing {want-got}, extra {got-want}")

# 11. HF inventory vs master
inv = {r["hf_id"]: r for r in read_csv("catalogues/hf_telugu_inventory.csv")}
for r in master:
    h = hf_of(r["collection_url"])
    if h and h in inv and inv[h]["inventory_decision"] == "Rejected":
        add("ERROR", r["record_id"], "hf inventory", f"master record's dataset {h} is Rejected in inventory: {inv[h]['decision_reason']}")

os.makedirs("audit", exist_ok=True)
with open("audit/VALIDATION_REPORT.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["level", "record_id", "check", "message"])
    w.writeheader()
    w.writerows(issues)
c = collections.Counter(i["level"] for i in issues)
print(f"validation: {c.get('ERROR',0)} errors, {c.get('WARN',0)} warnings (audit/VALIDATION_REPORT.csv)")
for i in issues:
    if i["level"] == "ERROR":
        print("  ERROR", i["record_id"], i["check"], "-", i["message"][:140])
sys.exit(1 if c.get("ERROR") else 0)
