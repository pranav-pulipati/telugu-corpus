---
license: cc-by-sa-4.0
language:
- te
- en
pretty_name: "Telugu Sampada Classics: Vemana, Sumathi Satakam and Telugu proverbs"
size_categories:
- 1K<n<10K
task_categories:
- text-generation
- translation
tags:
- telugu
- poetry
- proverbs
- public-domain
- literature
configs:
- config_name: proverbs
  data_files: proverbs.csv
- config_name: vemana
  data_files: vemana.csv
- config_name: sumathi
  data_files: sumathi.csv
---

# Telugu Sampada Classics: Vemana, Sumathi Satakam and Telugu proverbs

Public-domain Telugu texts as published on [Telugu Sampada](https://telugusampada.com),
a free site of Telugu literature and learning, in CSV and JSON Lines.
Each record links to its page on the site, where the text appears with
word-by-word meanings and notes for readers.

The newest version is always at https://telugusampada.com/open-data, where the
site builds these files from its own pages. Versions are also kept on
Hugging Face (https://huggingface.co/datasets/telugusampada/telugu-sampada-classics), where each collection loads as
its own subset; on Zenodo (https://doi.org/10.5281/zenodo.24036151); and on
Kaggle (https://www.kaggle.com/datasets/telugusampada/telugu-sampada-classics).

| File | Records | What it is |
|---|---:|---|
| `vemana.csv`, `vemana.jsonl` | 1293 | Vemana's poems (Vemana Satakam) |
| `sumathi.csv`, `sumathi.jsonl` | 101 | Sumathi Satakam (attributed to Baddena) |
| `proverbs.csv`, `proverbs.jsonl` | 1586 | Telugu proverbs (samethalu) with English renderings of 1868 |

## Fields

- **Poems:** `id` (the poem's number on the site), `first_line`, `text`
  (Telugu script, one line per line of the poem), `transliteration`
  (Roman letters, line by line), `url` (its page on Telugu Sampada),
  `source`.
- **Proverbs:** `number` (its number in the 1868 collection and on the
  site), `telugu`, `english_1868` (the collection's own English rendering
  and note, as printed in 1868), `url`, `source` (its Wikisource page).

## Sources

- Vemana: Telugu Wikisource, https://te.wikisource.org/wiki/వేమన_పద్యాలు
- Sumathi Satakam: Telugu Wikisource, https://te.wikisource.org/wiki/సుమతీ_శతకము (indexed to a 1930
  Rajahmundry print) and its second part
- Proverbs: M. W. Carr, *A Collection of Telugu Proverbs*
  (ఆంధ్రలోకోక్తిచంద్రిక), Madras, 1868, as transcribed on Telugu Wikisource,
  https://te.wikisource.org/wiki/ఆంధ్రలోకోక్తిచంద్రిక/Contents

The texts are as the site shows them, including its readings where the
transcriptions were corrected against printed editions. A few poems and
proverbs that the site does not publish are left out.

## Licence

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (`LICENSE`),
as the Wikisource transcriptions it rests on are. Attribution: "Telugu
Sampada (https://telugusampada.com), from Telugu Wikisource transcriptions". The
underlying works are in the public domain.

## Citation

See `CITATION.cff`. Corrections are welcome in the Community tab, or at https://telugusampada.com/corrections.

Exported 2026-11-07.
