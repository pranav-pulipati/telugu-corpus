---
license: cc-by-4.0
task_categories:
- text-generation
language:
- as
- bn
- gu
- en
- hi
- kn
- ks
- ml
- mr
- ne
- or
- pa
- sa
- sd
- ta
- te
- ur
tags:
- language-modeling
- casual-lm
- llm
pretty_name: sangraha
dataset_info:
- config_name: verified
  features:
  - name: doc_id
    dtype: string
  - name: type
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: asm
  - name: ben
  - name: brx
  - name: doi
  - name: eng
  - name: gom
  - name: guj
  - name: hin
  - name: kan
  - name: kas
  - name: mai
  - name: mal
  - name: mar
  - name: mni
  - name: nep
  - name: ori
  - name: pan
  - name: san
  - name: sat
  - name: snd
  - name: tam
  - name: tel
  - name: urd
- config_name: unverified
  features:
  - name: doc_id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: asm
  - name: ben
  - name: guj
  - name: hin
  - name: kan
  - name: mal
  - name: mar
  - name: nep
  - name: ori
  - name: pan
  - name: san
  - name: tam
  - name: tel
  - name: urd
- config_name: synthetic
  features:
  - name: doc_id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: asm_Beng
  - name: asm_Latn
  - name: ben_Beng
  - name: ben_Latn
  - name: guj_Gujr
  - name: guj_Latn
  - name: hin_Deva
  - name: hin_Latn
  - name: kan_Knda
  - name: kan_Latn
  - name: mal_Mlym
  - name: mal_Latn
  - name: mar_Deva
  - name: mar_Latn
  - name: npi_Deva
  - name: npi_Latn
  - name: ory_Orya
  - name: ory_Latn
  - name: pan_Guru
  - name: pan_Latn
  - name: san_Deva
  - name: san_Latn
  - name: tam_Taml
  - name: tam_Latn
  - name: tel_Telu
  - name: tel_Latn
  - name: urd_Arab
  - name: urd_Latn

configs:
  - config_name: verified
    data_files:
      - split: asm
        path: verified/asm/*.parquet
      - split: ben
        path: verified/ben/*.parquet
      - split: brx
        path: verified/brx/*.parquet
      - split: doi
        path: verified/doi/*.parquet
      - split: eng
        path: verified/eng/*.parquet
      - split: gom
        path: verified/gom/*.parquet
      - split: guj
        path: verified/guj/*.parquet
      - split: hin
        path: verified/hin/*.parquet
      - split: kan
        path: verified/kan/*.parquet
      - split: kas
        path: verified/kas/*.parquet
      - split: mai
        path: verified/mai/*.parquet
      - split: mal
        path: verified/mal/*.parquet
      - split: mar
        path: verified/mar/*.parquet
      - split: mni
        path: verified/mni/*.parquet
      - split: nep
        path: verified/nep/*.parquet
      - split: ori
        path: verified/ori/*.parquet
      - split: pan
        path: verified/pan/*.parquet
      - split: san
        path: verified/san/*.parquet
      - split: sat
        path: verified/sat/*.parquet
      - split: snd
        path: verified/snd/*.parquet
      - split: tam
        path: verified/tam/*.parquet
      - split: tel
        path: verified/tel/*.parquet
      - split: urd
        path: verified/urd/*.parquet
  - config_name: unverified
    data_files:
      - split: asm
        path: unverified/asm/*.parquet
      - split: ben
        path: unverified/ben/*.parquet
      - split: guj
        path: unverified/guj/*.parquet
      - split: hin
        path: unverified/hin/*.parquet
      - split: kan
        path: unverified/kan/*.parquet
      - split: mal
        path: unverified/mal/*.parquet
      - split: mar
        path: unverified/mar/*.parquet
      - split: nep
        path: unverified/nep/*.parquet
      - split: ori
        path: unverified/ori/*.parquet
      - split: pan
        path: unverified/pan/*.parquet
      - split: san
        path: unverified/san/*.parquet
      - split: tam
        path: unverified/tam/*.parquet
      - split: tel
        path: unverified/tel/*.parquet
      - split: urd
        path: unverified/urd/*.parquet
  - config_name: synthetic
    data_files:
      - split: asm_Beng
        path: synthetic/asm_Beng/*.parquet
      - split: asm_Latn
        path: synthetic/asm_Latn/*.parquet
      - split: ben_Beng
        path: synthetic/ben_Beng/*.parquet
      - split: ben_Latn
        path: synthetic/ben_Latn/*.parquet
      - split: guj_Gujr
        path: synthetic/guj_Gujr/*.parquet
      - split: guj_Latn
        path: synthetic/guj_Latn/*.parquet
      - split: hin_Deva
        path: synthetic/hin_Deva/*.parquet
      - split: hin_Latn
        path: synthetic/hin_Latn/*.parquet
      - split: kan_Knda
        path: synthetic/kan_Knda/*.parquet
      - split: kan_Latn
        path: synthetic/kan_Latn/*.parquet
      - split: mal_Mlym
        path: synthetic/mal_Mlym/*.parquet
      - split: mal_Latn
        path: synthetic/mal_Latn/*.parquet
      - split: mar_Deva
        path: synthetic/mar_Deva/*.parquet
      - split: mar_Latn
        path: synthetic/mar_Latn/*.parquet
      - split: npi_Deva
        path: synthetic/npi_Deva/*.parquet
      - split: npi_Latn
        path: synthetic/npi_Latn/*.parquet
      - split: ory_Orya
        path: synthetic/ory_Orya/*.parquet
      - split: ory_Latn
        path: synthetic/ory_Latn/*.parquet
      - split: pan_Guru
        path: synthetic/pan_Guru/*.parquet
      - split: pan_Latn
        path: synthetic/pan_Latn/*.parquet
      - split: san_Deva
        path: synthetic/san_Deva/*.parquet
      - split: san_Latn
        path: synthetic/san_Latn/*.parquet
      - split: tam_Taml
        path: synthetic/tam_Taml/*.parquet
      - split: tam_Latn
        path: synthetic/tam_Latn/*.parquet
      - split: tel_Telu
        path: synthetic/tel_Telu/*.parquet
      - split: tel_Latn
        path: synthetic/tel_Latn/*.parquet
      - split: urd_Arab
        path: synthetic/urd_Arab/*.parquet
      - split: urd_Latn
        path: synthetic/urd_Latn/*.parquet

size_categories:
  - 100B<n<1T
---

# Sangraha

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/63ef3cd11e695b35aa48bebc/nDnyidcqIOLAP9dTw9GrK.png" />
</p>

Sangraha is the largest high-quality, cleaned Indic language pretraining data containing 251B tokens summed up over 22 languages, extracted from curated sources, existing multilingual corpora and large scale translations.


**More information**:

- For detailed information on the curation and cleaning process of Sangraha, please checkout our paper [on Arxiv](https://arxiv.org/abs/2403.06350);
- Check out the scraping and cleaning pipelines used to curate Sangraha [on GitHub](https://github.com/AI4Bharat/IndicLLMSuite);

## Getting Started

For downloading the entire Sangraha:

```python
from datasets import load_dataset

dataset = load_dataset("ai4bharat/sangraha")
```

For downloading a subset (Verified/Unverified) of Sangraha:

```python
from datasets import load_dataset

dataset = load_dataset("ai4bharat/sangraha", data_dir="<subset_name>")
# for example: dataset = load_dataset("ai4bharat/sangraha", data_dir="verified")
```

For downloading one language from a subset of Sangraha:

```python
from datasets import load_dataset

dataset = load_dataset("ai4bharat/sangraha", data_dir="<subset_name>/<lang_code>")
# for example: dataset = load_dataset("ai4bharat/sangraha", data_dir="verified/asm")
```

## Background

Sangraha contains three broad components:

- **Sangraha Verified**: Containing scraped data from "human-verified" Websites, OCR-extracted data from high quality Indic language PDFs, transcribed data from various Indic language videos, podcasts, movies, courses, etc.
- **Sangraha Unverfied**: High quality Indic language data extracted from existing multilingual corpora employing perplexity filtering using n-gram language models trained on Sangraha Verified.
- **Sangraha Synthetic**: WikiMedia English translated to 14 Indic languages and further "romanised" from 14 languages by transliteration to English.

## Data Statistics

| **Lang Code** | **Verified** | **Synthetic** | **Unverified** | **Total Tokens (in Millions)** |
| ------------- | ------------ | ------------- | -------------- | ------------------------------ |
| asm           | 292.1        | 11,696.4      | 17.5           | 12,006.0                       |
| ben           | 10,604.4     | 13,814.1      | 5,608.8        | 30,027.5                       |
| brx           | 1.5          | -             | -              | 1.5                            |
| doi           | 0.06         | -             | -              | 0.06                           |
| eng           | 12,759.9     | -             | -              | 12,759.9                       |
| gom           | 10.1         | -             | -              | 10.1                           |
| guj           | 3,647.9      | 12,934.5      | 597.0          | 17,179.4                       |
| hin           | 12,617.3     | 9,578.7       | 12,348.3       | 34,544.3                       |
| kan           | 1,778.3      | 12,087.4      | 388.8          | 14,254.5                       |
| kas           | 0.5          | -             | -              | 0.5                            |
| mai           | 14.6         | -             | -              | 14.6                           |
| mal           | 2,730.8      | 13,130.0      | 547.8          | 16,408.6                       |
| mar           | 2,827.0      | 10,816.7      | 652.1          | 14,295.8                       |
| mni           | 7.4          | -             | -              | 7.4                            |
| npi           | 1,822.5      | 10,588.7      | 485.5          | 12,896.7                       |
| ori           | 1,177.1      | 11,338.0      | 23.7           | 12,538.8                       |
| pan           | 1,075.3      | 9,969.6       | 136.9          | 11,181.8                       |
| san           | 1,329.0      | 13,553.5      | 9.8            | 14,892.3                       |
| sat           | 0.3          | -             | -              | 0.3                            |
| snd           | 258.2        | -             | -              | 258.2                          |
| tam           | 3,985.1      | 11,859.3      | 1,515.9        | 17,360.3                       |
| urd           | 3,658.1      | 9,415.8       | 1,328.2        | 14,402.1                       |
| tel           | 3,706.8      | 11,924.5      | 647.4          | 16,278.7                       |
| **Total**     | **64,306.1** | **162,707.9** | **24,307.7**   | **251,321.0**                  |

To cite Sangraha, please use:

```
@article{khan2024indicllmsuite,
  title   = {IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages},
  author  = {Mohammed Safi Ur Rahman Khan and Priyam Mehta and Ananth Sankar and Umashankar Kumaravelan and Sumanth Doddapaneni and Suriyaprasaad G and Varun Balan G and Sparsh Jain and Anoop Kunchukuttan and Pratyush Kumar and Raj Dabre and Mitesh M. Khapra},
  year    = {2024},
  journal = {arXiv preprint arXiv: 2403.06350}
}
```
