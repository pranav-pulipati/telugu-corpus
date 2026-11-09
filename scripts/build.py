#!/usr/bin/env python3
"""Build every catalogue output from data/records/*.yaml.

Outputs: MASTER_CATALOGUE.csv/.xlsx, catalogues/<category>.csv, VERIFICATION_LOG.csv,
catalogues/hf_telugu_inventory.csv, and the generated sections of the Markdown reports.

Run:  .venv/bin/python scripts/build.py
"""
import csv, glob, json, os, re, sys, collections, datetime
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
schema = yaml.safe_load(open("data/schema.yaml"))
FIELDS = list(schema["fields"])
CATS = schema["categories"]
ENUMS = schema["enums"]
ENUM_FIELDS = {"record_type": "record_type", "org_type": "org_type", "telugu_scope": "telugu_scope",
               "modality": "modality", "digitization": "digitization", "bulk_download": "bulk_download",
               "registration": "registration", "authentication": "authentication", "license_scope": "license_scope",
               "redistribution": "redistribution", "commercial_use": "commercial_use",
               "size_confidence": "size_confidence", "verification_status": "verification_status",
               "corpus_value": "corpus_value", "quality_rating": "quality_rating", "content_role": "content_role",
               "dedup_role": "dedup_role", "count_in_totals": "count_in_totals", "audit_status": "audit_status"}
SEP = {"evidence_urls": " | ", "duplicates_mirrors": " | "}


def flat(field, v):
    if v is None:
        return ""
    if isinstance(v, list):
        return SEP.get(field, "; ").join(str(x) for x in v)
    return str(v).strip()


def load_records(pattern="data/records/*.yaml", known_extra=()):
    recs, errors = [], []
    for path in sorted(glob.glob(pattern)):
        doc = yaml.safe_load(open(path)) or {}
        defaults = doc.get("defaults", {})
        for raw in doc.get("records", []):
            r = dict(defaults)
            r.update(raw)
            r["_file"] = os.path.basename(path)
            recs.append(r)
    ids = collections.Counter(r.get("record_id") for r in recs)
    for i, n in ids.items():
        if n > 1:
            errors.append(f"duplicate record_id {i}")
    out = []
    for r in recs:
        rid = r.get("record_id", "?")
        row = {}
        for f in FIELDS:
            row[f] = flat(f, r.get(f))
        for f, (req, _) in schema["fields"].items():
            if req and not row[f]:
                errors.append(f"{rid} ({r['_file']}): missing required field {f}")
        for f, e in ENUM_FIELDS.items():
            if row[f] and row[f] not in ENUMS[e]:
                errors.append(f"{rid}: {f}={row[f]!r} not in {ENUMS[e]}")
        cats = [row["primary_category"]] + [c for c in row["secondary_categories"].split("; ") if c]
        for c in cats:
            if c not in CATS:
                errors.append(f"{rid}: unknown category {c}")
        if not re.fullmatch(r"TEL-[A-Z]+-\d{3}", rid):
            errors.append(f"{rid}: bad id format")
        elif rid.split("-")[1] not in CATS:
            errors.append(f"{rid}: id prefix not a category")
        row["_evidence"] = r.get("evidence", [])
        out.append(row)
    known = {r["record_id"] for r in out} | set(known_extra)
    for r in out:
        if r["parent_id"] and r["parent_id"] not in known:
            errors.append(f"{r['record_id']}: parent_id {r['parent_id']} unknown")
        for d in r["duplicates_mirrors"].split(" | "):
            if d.startswith("TEL-") and d.split()[0] not in known:
                errors.append(f"{r['record_id']}: duplicates_mirrors ref {d} unknown")
    out.sort(key=lambda r: (list(CATS).index(r["record_id"].split("-")[1]), r["record_id"]))
    return out, errors


def write_csv(path, rows, fields):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def verification_log(rows):
    """One row per evidence check. Explicit `evidence:` entries first, then automated link checks."""
    log = []
    linkchk = {}
    if os.path.exists("evidence/link_check.json"):
        linkchk = json.load(open("evidence/link_check.json"))
    for r in rows:
        for e in r["_evidence"]:
            log.append({"record_id": r["record_id"], "check_date": e.get("date", r["last_verified"]),
                        "check_type": e.get("type", "Manual inspection"), "url": e["url"],
                        "claim_checked": e.get("claim", ""), "result": e.get("result", ""),
                        "status_after_check": r["verification_status"]})
        for u in [u.strip() for u in r["evidence_urls"].split(" | ") if u.strip()]:
            if not any(e["url"] == u for e in r["_evidence"]):
                log.append({"record_id": r["record_id"], "check_date": r["last_verified"],
                            "check_type": "Evidence URL (supports record claims)", "url": u,
                            "claim_checked": r["verification_method"],
                            "result": f"Size: {r['size_telugu'] or 'unknown'} ({r['size_confidence']}); licence: {r['license']}",
                            "status_after_check": r["verification_status"]})
        tc = r.get("telugu_content_check", "")
        if tc and not tc.startswith("Not applicable"):
            log.append({"record_id": r["record_id"], "check_date": r["last_verified"], "check_type": "Sampled-content Telugu check (audit)",
                        "url": r["collection_url"], "claim_checked": "Dataset actually contains Telugu text (not just a tag)",
                        "result": tc, "status_after_check": r["verification_status"]})
        if r.get("audit_notes"):
            log.append({"record_id": r["record_id"], "check_date": r["last_verified"], "check_type": "Audit correction",
                        "url": r["license_evidence_url"] or r["collection_url"], "claim_checked": "Record re-examined in 2026-11 audit",
                        "result": r["audit_notes"][:900], "status_after_check": r["verification_status"]})
        for u in {r["collection_url"], r["license_evidence_url"]} - {""}:
            c = linkchk.get(u)
            if c:
                log.append({"record_id": r["record_id"], "check_date": c["date"], "check_type": "Automated HTTP check",
                            "url": u, "claim_checked": "URL reachable",
                            "result": f"HTTP {c['status']}" + (f" -> {c['final_url']}" if c.get("final_url") and c["final_url"] != u else "") + (f" ({c['error']})" if c.get("error") else ""),
                            "status_after_check": r["verification_status"]})
    for i, l in enumerate(log, 1):
        l["log_id"] = f"VL-{i:05d}"
    return log


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


HF_CHECKS = None


HF_PROFILES = {}
if os.path.exists("evidence/hf_script_profile.jsonl"):
    for _l in open("evidence/hf_script_profile.jsonl", encoding="utf-8"):
        if _l.strip():
            _d = json.loads(_l)
            HF_PROFILES[_d["hf_id"]] = _d


def hf_decision(hid, n_langs, found_via=""):
    """Inventory decision from the sampled-row Telugu check (see scripts/hf_telugu_check.py)."""
    global HF_CHECKS
    if HF_CHECKS is None:
        HF_CHECKS = load_hf_checks()
    d = HF_CHECKS.get(hid)
    if not d:
        return {"telugu_content_verdict": "NOT_YET_CHECKED", "sample_rows": "", "sample_telugu_chars": "",
                "telugu_configs_or_files": "", "inventory_decision": "Unconfirmed", "decision_reason": "Not checked in audit run"}
    s = d.get("sample") or {}
    v = d.get("verdict")
    if v == "NO_TELUGU_IN_SAMPLE":
        if re.search(r"roman|latn|translit", hid, re.I):
            v = "ROMANISED_TELUGU_CLAIMED"
        elif s.get("chars", 0) < 200:
            v = "NOT_CHECKABLE"
    telugu_specific = n_langs <= 3 or "telugu" in hid.lower()
    prof = HF_PROFILES.get(hid) if v == "NO_TELUGU_IN_SAMPLE" else None
    if prof and "error" not in prof:
        sc = prof.get("scripts", {})
        other = {k: n for k, n in sc.items() if k not in ("Telugu", "Latin letters")}
        name_part = hid.split("/", 1)[1].lower().replace("telugu-llm-labs", "")  # publisher name is not a language claim
        other_lang = re.search(r"(marathi|assamese|konkani|sindhi|urdu|nepali|bengali|bangla|tamil|hindi|kannada|malayalam|gujarati|punjabi|odia|oriya)", name_part)
        nw = max(prof.get("n_words", 0), 1)
        ev = (f"profile of {prof.get('rows')} sampled rows: scripts {sc or 'none'}; romanised-Telugu word hits "
              f"{prof.get('roman_telugu_word_hits')}/{nw}")
        base = {"telugu_content_verdict": v, "sample_rows": prof.get("rows", ""), "sample_telugu_chars": 0,
                "telugu_configs_or_files": ""}
        if other_lang and "telu" not in name_part:
            return {**base, "inventory_decision": "Rejected",
                    "decision_reason": f"Dataset is for {other_lang.group(1).title()}, matched only via the publisher name; no Telugu in sample ({ev})"}
        if "telu" not in hid.lower() and found_via == "name search":
            return {**base, "inventory_decision": "Rejected",
                    "decision_reason": f"Spurious name-search match (no 'telugu' in id) and no Telugu in sample ({ev})"}
        if prof.get("text_chars", 0) < 200:
            return {**base, "telugu_content_verdict": "NOT_CHECKABLE", "inventory_decision": "Unconfirmed",
                    "decision_reason": f"Sampled rows hold almost no text (audio/image/paths) ({ev})"}
        if prof.get("roman_telugu_word_hits", 0) >= 10 and prof["roman_telugu_word_hits"] / nw >= 0.02:
            return {**base, "telugu_content_verdict": "ROMANISED_TELUGU_LIKELY", "inventory_decision": "Unconfirmed",
                    "decision_reason": f"Latin-script text with frequent romanised-Telugu words — likely romanised Telugu ({ev})"}
        if sum(other.values()) >= 200 and n_langs <= 1:  # only single-language claims; multilingual samples may just miss Telugu
            top = max(other, key=other.get)
            return {**base, "inventory_decision": "Rejected",
                    "decision_reason": f"Claims Telugu but sampled text is in {top} script, no Telugu ({ev})"}
        return {**base, "inventory_decision": "Unconfirmed",
                "decision_reason": f"No Telugu script in sampled rows; text may be an English side, romanised, or Telugu appears later ({ev})"}
    if v == "CONFIRMED_TELUGU_TEXT":
        dec, why = "Retained", "Telugu script found in sampled rows"
    elif v == "ROMANISED_TELUGU_CLAIMED":
        dec, why = "Retained", "Romanised-Telugu configs/files; script test not applicable"
    elif v == "TELUGU_STRUCTURE_ONLY":
        dec, why = "Retained", "Telugu-named config/files exist; rows not sampled (gated / no viewer / non-text)"
    elif v == "NOT_FOUND":
        dec, why = "Rejected", "Dataset no longer exists on Hugging Face (404)"
    elif v == "NO_TELUGU_IN_SAMPLE" and telugu_specific:
        dec, why = "Rejected", "Claims Telugu but no Telugu script in sampled rows and no Telugu-named config/file"
    elif v == "NO_TELUGU_IN_SAMPLE":
        dec, why = "Unconfirmed", "Multilingual dataset; Telugu not present in the sampled rows and no Telugu-named config"
    else:
        dec, why = "Unconfirmed", f"Could not sample content ({v})"
    return {"telugu_content_verdict": v, "sample_rows": s.get("rows", ""), "sample_telugu_chars": s.get("telugu_chars", ""),
            "telugu_configs_or_files": "; ".join((d.get("telugu_configs") or []) + (d.get("telugu_files_sample") or [])[:2]),
            "inventory_decision": dec, "decision_reason": why}


def hf_inventory(rows):
    snaps = ["evidence/api_snapshots/hf_datasets_language_te_full.json"] + sorted(glob.glob("evidence/api_snapshots/hf_search_*.json"))
    seen, inv = set(), []
    in_master = collections.defaultdict(list)
    for r in rows:
        for u in (r["collection_url"] + " | " + r["evidence_urls"] + " | " + r["duplicates_mirrors"]).split(" | "):
            m = re.match(r"https://huggingface\.co/datasets/([^/\s?#]+/[^/\s?#]+)", u.strip())
            if m:
                in_master[m.group(1).lower()].append(r["record_id"])
    for s in snaps:
        if not os.path.exists(s):
            continue
        for d in json.load(open(s)):
            if d["id"] in seen:
                continue
            seen.add(d["id"])
            tags = d.get("tags", [])
            tg = lambda p: [t.split(":", 1)[1] for t in tags if t.startswith(p + ":")]
            langs = tg("language")
            inv.append({"hf_id": d["id"], "url": f"https://huggingface.co/datasets/{d['id']}",
                        "found_via": "language:te tag" if "language:te" in tags else "name search",
                        "n_languages_tagged": len(langs), "telugu_specific": "yes" if 0 < len(langs) <= 3 or (not langs and "telugu" in d["id"].lower()) else "no",
                        "license_tag": ";".join(tg("license")) or "none declared", "gated": str(d.get("gated", "")),
                        "size_category": ";".join(tg("size_categories")), "task_categories": ";".join(tg("task_categories")),
                        "modalities": ";".join(tg("modality")), "downloads_30d": d.get("downloads", ""), "likes": d.get("likes", ""),
                        "last_modified": d.get("lastModified", "")[:10], "in_master_catalogue": ";".join(sorted(set(in_master.get(d["id"].lower(), [])))),
                        **hf_decision(d["id"], len(langs), "language:te tag" if "language:te" in tags else "name search")})
    inv.sort(key=lambda x: -(x["downloads_30d"] or 0))
    return inv


def write_xlsx(rows, log, inv, rej=()):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    wb = Workbook()
    head = Font(bold=True, color="FFFFFF")
    fill = PatternFill("solid", fgColor="1F4E78")
    status_fill = {"Verified": "C6EFCE", "Partially Verified": "FFEB9C", "Unverified": "F4CCCC", "Inaccessible": "D9D9D9"}

    def sheet(ws, data, fields, widths=None):
        ws.append(fields)
        for c in ws[1]:
            c.font, c.fill = head, fill
        for d in data:
            ws.append([d.get(f, "") for f in fields])
        ws.freeze_panes = "C2"
        ws.auto_filter.ref = ws.dimensions
        for i, f in enumerate(fields, 1):
            ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(f, 22)
        if "verification_status" in fields:
            col = fields.index("verification_status") + 1
            for row in ws.iter_rows(min_row=2, min_col=col, max_col=col):
                for c in row:
                    if c.value in status_fill:
                        c.fill = PatternFill("solid", fgColor=status_fill[c.value])
    ws = wb.active
    ws.title = "Master Catalogue"
    sheet(ws, rows, FIELDS, {"description": 60, "acquisition_method": 50, "evidence_urls": 50, "collection_url": 40,
                             "license": 30, "size_telugu": 30, "unresolved_issues": 40, "collection_name": 34})
    ws2 = wb.create_sheet("Summary")
    ws2.append(["Metric", "Value"])
    for c in ws2[1]:
        c.font, c.fill = head, fill
    for k, v in summary(rows).items():
        ws2.append([k, v])
    ws2.column_dimensions["A"].width = 60
    ws2.column_dimensions["B"].width = 20
    ws3 = wb.create_sheet("Taxonomy")
    sheet(ws3, [{"code": k, "name": v["name"], "csv": "catalogues/" + v["csv"], "definition": v["desc"],
                 "records (primary)": sum(r["primary_category"] == k for r in rows)} for k, v in CATS.items()],
          ["code", "name", "csv", "definition", "records (primary)"], {"definition": 90, "name": 45})
    ws4 = wb.create_sheet("Field Dictionary")
    sheet(ws4, [{"field": f, "required": "yes" if q else "no", "definition": d,
                 "allowed values": "; ".join(ENUMS[ENUM_FIELDS[f]]) if f in ENUM_FIELDS else ""}
                for f, (q, d) in schema["fields"].items()], ["field", "required", "definition", "allowed values"],
          {"definition": 80, "allowed values": 80})
    ws5 = wb.create_sheet("Verification Log")
    sheet(ws5, log, LOG_FIELDS, {"url": 60, "claim_checked": 50, "result": 50})
    ws6 = wb.create_sheet("HF Telugu Inventory")
    sheet(ws6, inv, list(inv[0].keys()) if inv else ["hf_id"], {"hf_id": 50, "url": 60})
    ws7 = wb.create_sheet("Rejected (archive)")
    sheet(ws7, list(rej), FIELDS, {"description": 60, "rejection_reason": 60})
    wb.save("MASTER_CATALOGUE.xlsx")


LOG_FIELDS = ["log_id", "record_id", "check_date", "check_type", "url", "claim_checked", "result", "status_after_check"]


def summary(rows):
    s = collections.OrderedDict()
    s["Total catalogue records"] = len(rows)
    for st in ENUMS["verification_status"]:
        s[f"Status: {st}"] = sum(r["verification_status"] == st for r in rows)
    for k, v in CATS.items():
        s[f"Primary category {k} ({v['name']})"] = sum(r["primary_category"] == k for r in rows)
    for k in ENUMS["record_type"]:
        s[f"Record type: {k}"] = sum(r["record_type"] == k for r in rows)
    for k in ENUMS["commercial_use"]:
        s[f"Commercial use: {k}"] = sum(r["commercial_use"] == k for r in rows)
    for k in ENUMS["quality_rating"]:
        s[f"Quality: {k}"] = sum(r["quality_rating"] == k for r in rows)
    s["Records counted in totals (count_in_totals=Yes)"] = sum(r["count_in_totals"] == "Yes" for r in rows)
    s["Build date"] = datetime.date.today().isoformat()
    return s


def md_table(rows, cols, headers=None):
    headers = headers or cols
    esc = lambda x: str(x).replace("|", "\\|").replace("\n", " ")
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        out.append("| " + " | ".join(esc(r.get(c, "")) for c in cols) + " |")
    return "\n".join(out)


def inject(path, text):
    """Replace the block between GENERATED markers in a Markdown file."""
    if not os.path.exists(path):
        return
    s = open(path, encoding="utf-8").read()
    a, b = "<!-- BEGIN GENERATED -->", "<!-- END GENERATED -->"
    if a not in s:
        return
    pre, rest = s.split(a, 1)
    post = rest.split(b, 1)[1]
    open(path, "w", encoding="utf-8").write(pre + a + "\n" + text.strip() + "\n" + b + post)


def link(r):
    return f"[{r['collection_name']}]({r['collection_url']})"


def gen_docs(rows, inv):
    by = collections.defaultdict(list)
    for r in rows:
        by[r["primary_category"]].append(r)
    # README: category overview
    inject("README.md", md_table([{"code": k, "name": v["name"], "n": len(by[k]),
                                   "csv": f"[catalogues/{v['csv']}](catalogues/{v['csv']})"} for k, v in CATS.items()],
                                 ["code", "name", "n", "csv"], ["Code", "Category", "Records", "File"])
           + "\n\n" + md_table([{"k": k, "v": v} for k, v in summary(rows).items()], ["k", "v"], ["Metric", "Value"]))
    # DATASET_INVENTORY
    parts = []
    for k, v in CATS.items():
        if not by[k]:
            continue
        parts.append(f"### {k} — {v['name']} ({len(by[k])})\n")
        for r in by[k]:
            parts.append(f"#### {r['record_id']} · {r['collection_name']}\n"
                         f"- **Source:** {r['source_name']} ({r['organization']}) — {r['collection_url']}\n"
                         f"- **What:** {r['description']}\n"
                         f"- **Telugu size:** {r['size_telugu'] or 'unknown'} *(confidence: {r['size_confidence']})*"
                         + (f"; whole resource: {r['size_total']}" if r['size_total'] else "") + "\n"
                         f"- **Formats / content:** {r['formats'] or '—'} / {r['content_types'] or '—'}; modality {r['modality']}; {r['digitization']}\n"
                         + (f"- **Annotations / metadata:** {r['annotations'] or '—'} / {r['metadata_fields'] or '—'}\n")
                         + f"- **License:** {r['license']} · redistribution: {r['redistribution']} · commercial: {r['commercial_use']}\n"
                         f"- **Status:** {r['verification_status']} ({r['last_verified']})"
                         + (f" · open issues: {r['unresolved_issues']}" if r['unresolved_issues'] else "") + "\n")
    inject("DATASET_INVENTORY.md", "\n".join(parts))
    # LICENSING_REPORT
    lic_groups = collections.OrderedDict([
        ("Commercial use allowed", lambda r: r["commercial_use"] == "Allowed"),
        ("Non-commercial only", lambda r: r["commercial_use"] == "Not allowed"),
        ("Varies by item/subset", lambda r: r["commercial_use"] == "Varies"),
        ("Unclear / not stated", lambda r: r["commercial_use"] == "Unclear")])
    parts = []
    lc = collections.Counter(r["license"] for r in rows)
    parts.append("### License strings observed (records per license)\n\n" + md_table(
        [{"l": l, "n": n} for l, n in lc.most_common()], ["l", "n"], ["License (as stated by source)", "Records"]))
    for name, fn in lic_groups.items():
        sel = [r for r in rows if fn(r)]
        parts.append(f"\n### {name} ({len(sel)})\n\n" + md_table(
            [dict(r, link=link(r)) for r in sel], ["record_id", "link", "license", "license_scope", "redistribution", "copyright_notes"],
            ["ID", "Collection", "License", "Scope", "Redistribution", "Copyright notes"]))
    inject("LICENSING_REPORT.md", "\n".join(parts))
    # ACQUISITION_GUIDE
    parts = []
    for k, v in CATS.items():
        if by[k]:
            parts.append(f"\n### {k} — {v['name']}\n\n" + md_table(
                [dict(r, link=link(r)) for r in by[k]],
                ["record_id", "link", "bulk_download", "authentication", "api_endpoint", "acquisition_method", "processing_needs"],
                ["ID", "Collection", "Bulk", "Access gate", "API", "How to acquire", "Processing needed"]))
    inject("ACQUISITION_GUIDE.md", "\n".join(parts))
    # COVERAGE_ANALYSIS
    parts = ["### Records by primary category and verification status\n"]
    tbl = []
    for k, v in CATS.items():
        d = {"cat": f"{k} {v['name']}", "n": len(by[k])}
        for st in ENUMS["verification_status"]:
            d[st] = sum(r["verification_status"] == st for r in by[k])
        d["high"] = sum(r["corpus_value"] == "High" for r in by[k])
        d["sec"] = sum(k in r["secondary_categories"].split("; ") for r in rows)
        tbl.append(d)
    parts.append(md_table(tbl, ["cat", "n", "sec"] + ENUMS["verification_status"] + ["high"],
                          ["Category", "Primary", "Also tagged (secondary)"] + ENUMS["verification_status"] + ["High value"]))
    for fld, title in [("modality", "Modality"), ("telugu_scope", "Telugu scope"), ("digitization", "Digitization type"),
                       ("org_type", "Organisation type"), ("commercial_use", "Commercial use"), ("bulk_download", "Bulk download"),
                       ("authentication", "Access gate"), ("size_confidence", "Size confidence")]:
        c = collections.Counter(r[fld] for r in rows)
        parts.append(f"\n### {title}\n\n" + md_table([{"k": k, "n": n} for k, n in c.most_common()], ["k", "n"], [title, "Records"]))
    if inv:
        parts.append(f"\n### Hugging Face long tail\n\n{len(inv)} Hugging Face datasets were found by the language:te tag or a name search "
                     f"({sum(i['found_via']=='language:te tag' for i in inv)} tagged, {sum(i['found_via']=='name search' for i in inv)} name-only). "
                     f"{sum(1 for i in inv if i['in_master_catalogue'])} are covered by master-catalogue records; all are listed in "
                     f"[catalogues/hf_telugu_inventory.csv](catalogues/hf_telugu_inventory.csv) with API metadata only.\n")
        lc = collections.Counter(i["license_tag"] for i in inv)
        parts.append(md_table([{"k": k, "n": n} for k, n in lc.most_common(15)], ["k", "n"], ["HF license tag", "Datasets"]))
    inject("COVERAGE_ANALYSIS.md", "\n".join(parts))
    # RESEARCH_GAPS: unresolved issues list
    sel = [r for r in rows if r["unresolved_issues"] or r["verification_status"] in ("Unverified", "Inaccessible")]
    inject("RESEARCH_GAPS.md", md_table([dict(r, link=link(r)) for r in sel],
                                        ["record_id", "link", "verification_status", "unresolved_issues"],
                                        ["ID", "Collection", "Status", "Open questions"]))


def main():
    import yaml as _y
    active_ids = [x["record_id"] for f in glob.glob("data/records/*.yaml") for x in (_y.safe_load(open(f)) or {}).get("records", [])]
    rej, rej_err = load_records("data/rejected/*.yaml", known_extra=active_ids)
    rows, errors = load_records(known_extra=[r["record_id"] for r in rej])
    errors += rej_err
    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print("  -", e)
        if "--force" not in sys.argv:
            sys.exit(1)
    write_csv("MASTER_CATALOGUE.csv", rows, FIELDS)
    for k, v in CATS.items():
        write_csv(f"catalogues/{v['csv']}", [r for r in rows if r["primary_category"] == k or k in r["secondary_categories"].split("; ")], FIELDS)
    log = verification_log(rows)
    write_csv("VERIFICATION_LOG.csv", log, LOG_FIELDS)
    inv = hf_inventory(rows)
    if inv:
        write_csv("catalogues/hf_telugu_inventory.csv", inv, list(inv[0].keys()))
    write_xlsx(rows, log, inv, rej)
    # audit-folder copies (deliverables requested in the audit brief)
    import shutil
    os.makedirs("audit/catalogues", exist_ok=True)
    allrows = sorted(rows + rej, key=lambda r: r["record_id"])
    write_csv("audit/CORRECTED_CATALOGUE.csv", allrows, FIELDS)
    for f in ("MASTER_CATALOGUE.csv", "MASTER_CATALOGUE.xlsx"):
        shutil.copy(f, "audit/" + f)
    for f in glob.glob("catalogues/*.csv"):
        shutil.copy(f, "audit/catalogues/")
    gen_docs(rows, inv)
    s = summary(rows)
    print(f"built {len(rows)} records, {len(log)} log rows, {len(inv)} HF inventory rows")
    for k, v in s.items():
        if v:
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
