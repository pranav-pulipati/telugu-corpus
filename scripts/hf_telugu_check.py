#!/usr/bin/env python3
"""Check whether Hugging Face datasets really contain Telugu, using sampled rows — not tags.

For each dataset id:
  1. /api/datasets/{id}            -> exists? gated? file names (siblings), language tags
  2. datasets-server /splits       -> config names
  3. datasets-server /first-rows   -> up to 100 sample rows from the Telugu config if one exists, else the first config
  4. Count Telugu-script characters (U+0C00-U+0C7F) in every string value of the sampled rows.

Verdicts:
  CONFIRMED_TELUGU_TEXT     sampled rows contain Telugu script (>= 20 Telugu chars)
  TELUGU_STRUCTURE_ONLY     Telugu-named config/file exists, but rows could not be sampled (gated / no viewer / audio-only)
  ROMANISED_TELUGU_CLAIMED  only romanised-Telugu configs/files (tel_Latn, romanized) — script test not applicable
  NO_TELUGU_IN_SAMPLE       rows sampled, no Telugu script, and no Telugu-named config/file
  NOT_CHECKABLE             gated or no dataset viewer, and no Telugu-named config/file
  NOT_FOUND                 dataset no longer exists (404)
  ERROR                     other failure (see detail)

Resumable: results appended to evidence/hf_telugu_check.jsonl; already-checked ids are skipped.
Usage: hf_telugu_check.py ids.txt
"""
import json, os, re, sys, time, urllib.request, urllib.parse, urllib.error

OUT = os.environ.get("HF_CHECK_OUT", "evidence/hf_telugu_check.jsonl")
UA = {"User-Agent": "telugu-corpus-audit/1.0 (research; polite)"}
TEL = re.compile(r"[ఀ-౿]")
TEL_NAME = re.compile(r"(^|[^a-z])(te|tel|telugu|tel_telu|te_in|te-in|te-telu-in|te_telu)([^a-z]|$)", re.I)
ROMAN = re.compile(r"(tel_latn|te-latn|roman|translit)", re.I)
MIN_GAP = 0.8  # seconds between requests
_last = [0.0]


def get(url):
    for attempt in range(6):
        wait = MIN_GAP - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.status, json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(30 * (attempt + 1))
                continue
            try:
                body = json.load(e)
            except Exception:
                body = {}
            return e.code, body
        except Exception as e:
            if attempt < 2:
                time.sleep(5)
                continue
            return 0, {"error": str(e)[:120]}
    return 429, {"error": "rate limited"}


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


def check(ds):
    q = urllib.parse.quote
    rec = {"hf_id": ds, "checked": time.strftime("%Y-%m-%d")}
    st, info = get(f"https://huggingface.co/api/datasets/{ds}")
    if st == 404 or (st == 401 and "Repository not found" in json.dumps(info)):
        rec.update(verdict="NOT_FOUND", detail=f"HTTP {st}")
        return rec
    if st != 200:
        rec.update(verdict="ERROR", detail=f"api HTTP {st} {json.dumps(info)[:100]}")
        return rec
    rec["gated"] = info.get("gated")
    files = [s["rfilename"] for s in info.get("siblings", [])]
    rec["n_files"] = len(files)
    tel_files = [f for f in files if TEL_NAME.search(f.replace("/", " ").replace(".", " "))]
    st, sp = get(f"https://datasets-server.huggingface.co/splits?dataset={q(ds)}")
    splits = sp.get("splits", []) if st == 200 else []
    configs = sorted({s["config"] for s in splits})
    tel_cfgs = [c for c in configs if TEL_NAME.search(c) or "telugu" in c.lower()]
    rec["telugu_configs"] = tel_cfgs[:10]
    rec["telugu_files_sample"] = tel_files[:5]
    rec["n_telugu_files"] = len(tel_files)
    roman_only = (tel_cfgs or tel_files) and all(ROMAN.search(x) for x in (tel_cfgs or tel_files))
    structure = bool(tel_cfgs or tel_files)
    sample = None
    if splits:
        pick = next((s for s in splits if s["config"] in tel_cfgs and not ROMAN.search(s["config"])), None) \
            or next((s for s in splits if s["config"] in tel_cfgs), None) or splits[0]
        st, fr = get(f"https://datasets-server.huggingface.co/first-rows?dataset={q(ds)}&config={q(pick['config'])}&split={q(pick['split'])}")
        if st == 200:
            rows = fr.get("rows", [])
            text = "".join(s for r in rows for s in strings(r.get("row", {})) if not s.startswith("http"))
            n_tel = len(TEL.findall(text))
            sample = {"config": pick["config"], "split": pick["split"], "rows": len(rows),
                      "chars": len(text), "telugu_chars": n_tel}
        else:
            sample = {"config": pick["config"], "error": f"first-rows HTTP {st}"}
    else:
        sample = {"error": f"splits HTTP {st} {str(sp.get('error',''))[:80]}"}
    rec["sample"] = sample
    if sample and sample.get("telugu_chars", 0) >= 20:
        rec["verdict"] = "CONFIRMED_TELUGU_TEXT"
    elif roman_only:
        rec["verdict"] = "ROMANISED_TELUGU_CLAIMED"
    elif structure:
        rec["verdict"] = "TELUGU_STRUCTURE_ONLY"
    elif sample and "rows" in sample and sample["rows"] > 0:
        rec["verdict"] = "NO_TELUGU_IN_SAMPLE"
    else:
        rec["verdict"] = "NOT_CHECKABLE"
    return rec


def main():
    ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    import glob as _g
    done = set()
    for f in _g.glob("evidence/hf_telugu_check*.jsonl"):  # skip ids finished by any worker
        done |= {json.loads(l)["hf_id"] for l in open(f) if l.strip()}
    todo = [i for i in ids if i not in done]
    print(f"{len(ids)} ids, {len(done)} already done, {len(todo)} to check", flush=True)
    with open(OUT, "a") as fh:
        for n, ds in enumerate(todo, 1):
            try:
                rec = check(ds)
            except Exception as e:
                rec = {"hf_id": ds, "verdict": "ERROR", "detail": str(e)[:150]}
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            if n % 50 == 0:
                print(f"{n}/{len(todo)}", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
