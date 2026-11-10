#!/usr/bin/env bash
# Resumable bulk downloads for the Telugu OCR corpus (phase 2).
# Each archive goes into its own data/<dataset>/zips/ folder; originals are never modified.
# Usage: bash ocr/acquisition/scripts/download_sources.sh [group ...]   (groups: hwuc hwwords synr synstr)
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data"
C=https://cdn.iiit.ac.in/cdn/ilocr.iiit.ac.in

fetch() {  # fetch <dest> <url>
  local dest="$1" url="$2"
  mkdir -p "$(dirname "$dest")"
  for i in 1 2 3 4 5 6 7 8; do
    curl -sSL -C - --retry 5 --retry-delay 10 -A "Mozilla/5.0" -o "$dest" "$url" && break
    echo "retry $i $url" >&2; sleep 20
  done
  local want; want=$(curl -sIL -A "Mozilla/5.0" "$url" | grep -i '^content-length' | tail -1 | tr -dc '0-9')
  local got; got=$(stat -c %s "$dest" 2>/dev/null || echo 0)
  echo "$(date -Is) $dest bytes=$got expected=$want $([ "$got" = "$want" ] && echo OK || echo SIZE_MISMATCH)"
}

group() {
  case "$1" in
    # cvit.iiit.ac.in limits each connection to ~0.1-0.3 MB/s, so use 16 parallel ranges
    hwuc)    mkdir -p "$DATA/cvit_hw_uc_telugu/zips"; python3 -I "$ROOT/scripts/segmented_download.py" https://cvit.iiit.ac.in/images/datasets/indic_handwritten/telugu.zip "$DATA/cvit_hw_uc_telugu/zips/telugu.zip" --workers 16 ;;
    hwwords) for s in train val test; do fetch "$DATA/ilocr_hw_words_telugu/zips/$s.zip" "$C/public/handwritten/phase-0/v0.5/telugu/IIIT-INDIC-HW-WORDS-Telugu/$s.zip"; done ;;
    synr)    for s in val test train; do fetch "$DATA/ilocr_synthetic_r_telugu/zips/$s.zip" "$C/public/printed/phase-0/v0.5/telugu/IIIT-Synthetic-R-Telugu/$s.zip"; done ;;
    synstr)  for s in val test train; do fetch "$DATA/ilocr_synthetic_indicstr_telugu/zips/$s.zip" "$C/public/scenetext/phase-0/v0.5/telugu/IIIT-Synthetic-Telugu/$s.zip"; done ;;
  esac
}

groups=("$@"); [ ${#groups[@]} -eq 0 ] && groups=(hwuc hwwords synr synstr); [ "${1:-}" = "mozhi" ] && groups=()
for g in "${groups[@]}"; do group "$g" & done
wait

# phase 2b: official Mozhi train/val (filenames carry book-page IDs needed for leakage-safe splits)
if [ "${1:-}" = "mozhi" ]; then
  for s in train val; do fetch "$DATA/ilocr_mozhi_telugu_official/zips/$s.zip" "$C/public/printed/phase-0/v0.5/telugu/akshara/$s.zip"; done
fi
