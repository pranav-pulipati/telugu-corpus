#!/usr/bin/env python3
"""Second-pass Telugu content check for HF datasets the first pass could not confirm.

Improvements over hf_telugu_check.py:
  * picks the (config, split) pair whose config OR split name is Telugu (e.g. sangraha verified/tel)
  * if the viewer cannot serve rows, reads the first ~512 KB of a Telugu-named text-like file directly
    (txt/tsv/csv/json/jsonl, also .gz/.bz2/.xz/.zip/.tar.* — decompressed as a stream) and counts Telugu script.
Parquet files are not byte-sampled (column data is compressed in pages).

Writes evidence/hf_telugu_recheck.jsonl (same record format, plus "method").
Usage: hf_telugu_recheck.py id1 id2 ...   or   --from-master (all master HF records not CONFIRMED in pass 1)
"""
import bz2, csv, io, json, lzma, os, re, sys, tarfile, time, zipfile, zlib, urllib.request, urllib.parse, urllib.error

sys.path.insert(0, os.path.dirname(__file__))
import hf_telugu_check as H  # reuse get(), strings(), regexes

OUT = "evidence/hf_telugu_recheck.jsonl"
# Telugu files located with the HF tree API when the repo file list is too large / unnamed (see earlier size measurements)
EXPLICIT = {
    "allenai/MADLAD-400": ["data-v1p5/te/clean_docs_v2-00002-of-05000.jsonl.gz"],
    "espnet/yodas2": ["data/te000/text/00000000.json"],
    "parambharat/telugu_asr_corpus": ["data/train.jsonl"],
    "ai4bharat/IndicSentiment": ["data/test/te.json"],
}
TEXTY = re.compile(r"\.(txt|tsv|csv|json|jsonl|xml|conllu|conll|tar|zip|gz|bz2|xz)$", re.I)


def range_get(url, n=524288):
    req = urllib.request.Request(url, headers={**H.UA, "Range": f"bytes=0-{n-1}"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read(n)


def decode_prefix(name, data):
    """Best-effort decompression of a file prefix."""
    low = name.lower()
    try:
        if low.endswith(".zip"):
            # local file header: try raw deflate stream after the header
            if data[:4] == b"PK\x03\x04":
                fn_len = int.from_bytes(data[26:28], "little"); ex_len = int.from_bytes(data[28:30], "little")
                start = 30 + fn_len + ex_len
                return zlib.decompressobj(-15).decompress(data[start:])
        if low.endswith(".gz") or low.endswith(".tgz"):
            return zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(data)
        if low.endswith(".bz2"):
            return bz2.BZ2Decompressor().decompress(data)
        if low.endswith(".xz"):
            return lzma.LZMADecompressor().decompress(data)
    except Exception:
        return b""
    return data


def check(ds):
    q = urllib.parse.quote
    rec = {"hf_id": ds, "checked": time.strftime("%Y-%m-%d"), "method": "recheck"}
    st, info = H.get(f"https://huggingface.co/api/datasets/{ds}")
    if st != 200:
        rec.update(verdict="NOT_FOUND" if st == 404 else "ERROR", detail=f"api HTTP {st}")
        return rec
    gated = info.get("gated")
    rec["gated"] = gated
    files = [s["rfilename"] for s in info.get("siblings", [])]
    tel_files = [f for f in files if H.TEL_NAME.search(f.replace("/", " ").replace(".", " ").replace("_", " ")) or "telugu" in f.lower()]
    rec["telugu_files_sample"] = tel_files[:5]
    rec["n_telugu_files"] = len(tel_files)
    # 1) viewer rows from a Telugu-named config OR split
    st, sp = H.get(f"https://datasets-server.huggingface.co/splits?dataset={q(ds)}")
    splits = sp.get("splits", []) if st == 200 else []
    cand = [s for s in splits if H.TEL_NAME.search(s["config"]) or H.TEL_NAME.search(s["split"])
            or "telugu" in (s["config"] + s["split"]).lower()]
    cand.sort(key=lambda s: bool(H.ROMAN.search(s["config"] + s["split"])))
    rec["telugu_configs"] = [f'{s["config"]}/{s["split"]}' for s in cand][:10]
    for s in cand[:2]:
        st, fr = H.get(f"https://datasets-server.huggingface.co/first-rows?dataset={q(ds)}&config={q(s['config'])}&split={q(s['split'])}")
        if st == 200:
            rows = fr.get("rows", [])
            text = "".join(x for r in rows for x in H.strings(r.get("row", {})) if not x.startswith("http"))
            n = len(H.TEL.findall(text))
            rec["sample"] = {"config": f'{s["config"]}/{s["split"]}', "split": s["split"], "rows": len(rows),
                             "chars": len(text), "telugu_chars": n, "source": "viewer first-rows"}
            if n >= 20:
                rec["verdict"] = "CONFIRMED_TELUGU_TEXT"
                return rec
    # 2) direct byte sample of a Telugu-named text-like file (not possible for gated repos without a token)
    if not gated or ds in EXPLICIT:
        for f in (EXPLICIT.get(ds) or [f for f in tel_files if TEXTY.search(f)][:3]):
            url = f"https://huggingface.co/datasets/{ds}/resolve/main/{q(f)}"
            try:
                raw = range_get(url)
            except Exception as e:
                rec["file_error"] = str(e)[:100]
                continue
            text = decode_prefix(f, raw).decode("utf-8", "ignore")
            # JSON files often escape non-ASCII: count \u0c00-\u0c7f escapes as Telugu characters too
            n = len(H.TEL.findall(text)) + len(re.findall(r"\\u0[cC][0-7][0-9a-fA-F]", text))
            rec["sample"] = {"config": f, "split": "-", "rows": 0, "chars": len(text), "telugu_chars": n,
                             "source": f"first {len(raw):,} bytes of file"}
            if n >= 20:
                rec["verdict"] = "CONFIRMED_TELUGU_TEXT"
                return rec
    if tel_files or cand:
        rec["verdict"] = "ROMANISED_TELUGU_CLAIMED" if all(H.ROMAN.search(x) for x in (tel_files or rec["telugu_configs"])) else "TELUGU_STRUCTURE_ONLY"
    else:
        rec["verdict"] = "NOT_CHECKABLE"
    rec.setdefault("sample", {"error": "gated (login required)" if gated else "no Telugu-named split/file could be sampled"})
    return rec


def main():
    if sys.argv[1:] == ["--from-master"]:
        first = {}
        for l in open("evidence/hf_telugu_check.jsonl"):
            d = json.loads(l)
            first[d["hf_id"]] = d["verdict"]
        ids = []
        for r in csv.DictReader(open("MASTER_CATALOGUE.csv", encoding="utf-8")):
            m = re.match(r"https://huggingface\.co/datasets/([^/\s?#]+/[^/\s?#]+)", r["collection_url"])
            if m and first.get(m.group(1)) != "CONFIRMED_TELUGU_TEXT" and m.group(1) not in ids:
                ids.append(m.group(1))
    else:
        ids = sys.argv[1:]
    with open(OUT, "a") as fh:
        for ds in ids:
            try:
                rec = check(ds)
            except Exception as e:
                rec = {"hf_id": ds, "verdict": "ERROR", "detail": str(e)[:150], "method": "recheck"}
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            s = rec.get("sample", {})
            print(f"{ds:55s} {rec['verdict']:26s} {s.get('telugu_chars','')} {s.get('source', s.get('error',''))}", flush=True)


if __name__ == "__main__":
    main()
