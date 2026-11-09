#!/usr/bin/env python3
"""Script profile of sampled rows for HF datasets whose first-pass check found no Telugu script.

For each dataset: re-fetch the same sampled rows and count characters per writing system, words that look like
romanised Telugu, and how much of the text is file paths/ids. Used by build.py to decide Rejected vs Unconfirmed
conservatively (reject only when the text is demonstrably another language).
Writes evidence/hf_script_profile.jsonl.   Usage: hf_script_profile.py ids.txt
"""
import json, os, re, sys, urllib.parse

sys.path.insert(0, os.path.dirname(__file__))
import hf_telugu_check as H

SCRIPTS = {"Telugu": (0x0C00, 0x0C7F), "Devanagari": (0x0900, 0x097F), "Bengali": (0x0980, 0x09FF),
           "Gurmukhi": (0x0A00, 0x0A7F), "Gujarati": (0x0A80, 0x0AFF), "Oriya": (0x0B00, 0x0B7F), "Tamil": (0x0B80, 0x0BFF),
           "Kannada": (0x0C80, 0x0CFF), "Malayalam": (0x0D00, 0x0D7F), "Arabic": (0x0600, 0x06FF), "CJK": (0x4E00, 0x9FFF)}
# frequent romanised-Telugu function/content words (chosen to be rare in English)
ROMAN_TE = set("""nenu meeru miru nuvvu ledu ledhu undi undhi unnadi unnaru emi enti endi chala chaala kuda kooda naku naaku
miku meeku cheppu cheppandi cheyyi cheyandi vachindi vachhindi avunu kaadu kadu bagundi baagundi vaadu vadu aame idhi adhi
ela elaa enduku endhuku garu gaaru nijamga inka emaina evaru ekkada ippudu appudu manam mana memu vallu valla tho lo ki ni
anna akka amma nanna bayya babu sir garu ra ga kada kadha matram""".split())
PATHLIKE = re.compile(r"^[\w./\\:-]+\.(wav|mp3|flac|png|jpg|jpeg|json|txt|parquet|ogg|m4a)$|^[0-9a-f-]{16,}$", re.I)


def profile(ds, config, split):
    q = urllib.parse.quote
    st, fr = H.get(f"https://datasets-server.huggingface.co/first-rows?dataset={q(ds)}&config={q(config)}&split={q(split)}")
    if st != 200:
        return {"error": f"first-rows HTTP {st}"}
    strs = [s for r in fr.get("rows", []) for s in H.strings(r.get("row", {})) if not s.startswith("http")]
    pathlike = sum(len(s) for s in strs if PATHLIKE.match(s.strip()))
    text = " ".join(s for s in strs if not PATHLIKE.match(s.strip()))
    counts = {k: sum(lo <= ord(ch) <= hi for ch in text) for k, (lo, hi) in SCRIPTS.items()}
    counts["Latin letters"] = sum(ch.isascii() and ch.isalpha() for ch in text)
    words = re.findall(r"[a-z]+", text.lower())
    roman_hits = sum(w in ROMAN_TE for w in words)
    feats = []
    for f in fr.get("features", [])[:12]:
        t = f.get("type")
        feats.append(f'{f.get("name")}:{(t.get("_type") or t.get("dtype")) if isinstance(t, dict) else type(t).__name__}')
    return {"config": config, "split": split, "rows": len(fr.get("rows", [])), "text_chars": len(text), "pathlike_chars": pathlike,
            "scripts": {k: v for k, v in counts.items() if v}, "roman_telugu_word_hits": roman_hits, "n_words": len(words),
            "features": feats}


def main():
    first = {}
    for f in sorted(__import__("glob").glob("evidence/hf_telugu_check*.jsonl")):
        for l in open(f):
            d = json.loads(l)
            first[d["hf_id"]] = d
    ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    if os.path.exists("evidence/hf_script_profile.jsonl"):
        done = {json.loads(l)["hf_id"] for l in open("evidence/hf_script_profile.jsonl") if l.strip()}
        ids = [i for i in ids if i not in done]
    with open("evidence/hf_script_profile.jsonl", "a") as fh:
        for ds in ids:
            s = (first.get(ds) or {}).get("sample") or {}
            if "config" not in s or "split" not in s:
                continue
            p = profile(ds, s["config"], s["split"])
            p["hf_id"] = ds
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")
            fh.flush()
            print(f"{ds[:50]:50s} text={p.get('text_chars')} path={p.get('pathlike_chars')} roman={p.get('roman_telugu_word_hits')} {p.get('scripts')}", flush=True)


if __name__ == "__main__":
    main()
