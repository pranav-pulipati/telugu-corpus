---
license: other
task_categories:
  - text-generation
tags:
  - text
  - pre-training
  - synthetic
  - translation
  - multilingual
  - indic
language:
  - as
  - bn
  - brx
  - doi
  - gu
  - hi
  - kn
  - gom
  - ks
  - mai
  - ml
  - mni
  - mr
  - ne
  - or
  - pa
  - sa
  - sat
  - sd
  - ta
  - te
  - ur
size_categories:
  - 100M<n<1B
modality:
  - text
source:
  - synthetic
track_downloads: true
configs:
  - config_name: bn-Beng-IN
    data_files:
      - split: train
        path: data/bn-Beng-IN/train-*
  - config_name: bn-Latn-IN
    data_files:
      - split: train
        path: data/bn-Latn-IN/train-*
  - config_name: gu-Gujr-IN
    data_files:
      - split: train
        path: data/gu-Gujr-IN/train-*
  - config_name: gu-Latn-IN
    data_files:
      - split: train
        path: data/gu-Latn-IN/train-*
  - config_name: hi-Deva-IN
    data_files:
      - split: train
        path: data/hi-Deva-IN/train-*
  - config_name: hi-Latn-IN
    data_files:
      - split: train
        path: data/hi-Latn-IN/train-*
  - config_name: kn-Knda-IN
    data_files:
      - split: train
        path: data/kn-Knda-IN/train-*
  - config_name: kn-Latn-IN
    data_files:
      - split: train
        path: data/kn-Latn-IN/train-*
  - config_name: ml-Mlym-IN
    data_files:
      - split: train
        path: data/ml-Mlym-IN/train-*
  - config_name: ml-Latn-IN
    data_files:
      - split: train
        path: data/ml-Latn-IN/train-*
  - config_name: mr-Deva-IN
    data_files:
      - split: train
        path: data/mr-Deva-IN/train-*
  - config_name: mr-Latn-IN
    data_files:
      - split: train
        path: data/mr-Latn-IN/train-*
  - config_name: ne-Deva-IN
    data_files:
      - split: train
        path: data/ne-Deva-IN/train-*
  - config_name: ne-Latn-IN
    data_files:
      - split: train
        path: data/ne-Latn-IN/train-*
  - config_name: or-Orya-IN
    data_files:
      - split: train
        path: data/or-Orya-IN/train-*
  - config_name: or-Latn-IN
    data_files:
      - split: train
        path: data/or-Latn-IN/train-*
  - config_name: pa-Guru-IN
    data_files:
      - split: train
        path: data/pa-Guru-IN/train-*
  - config_name: pa-Latn-IN
    data_files:
      - split: train
        path: data/pa-Latn-IN/train-*
  - config_name: ta-Taml-IN
    data_files:
      - split: train
        path: data/ta-Taml-IN/train-*
  - config_name: ta-Latn-IN
    data_files:
      - split: train
        path: data/ta-Latn-IN/train-*
  - config_name: te-Telu-IN
    data_files:
      - split: train
        path: data/te-Telu-IN/train-*
  - config_name: te-Latn-IN
    data_files:
      - split: train
        path: data/te-Latn-IN/train-*
  - config_name: ur-Arab-IN
    data_files:
      - split: train
        path: data/ur-Arab-IN/train-*
  - config_name: ur-Latn-IN
    data_files:
      - split: train
        path: data/ur-Latn-IN/train-*
  - config_name: as-Beng-IN
    data_files:
      - split: train
        path: data/as-Beng-IN/train-*
  - config_name: brx-Deva-IN
    data_files:
      - split: train
        path: data/brx-Deva-IN/train-*
  - config_name: doi-Deva-IN
    data_files:
      - split: train
        path: data/doi-Deva-IN/train-*
  - config_name: gom-Deva-IN
    data_files:
      - split: train
        path: data/gom-Deva-IN/train-*
  - config_name: ks-Arab-IN
    data_files:
      - split: train
        path: data/ks-Arab-IN/train-*
  - config_name: mai-Deva-IN
    data_files:
      - split: train
        path: data/mai-Deva-IN/train-*
  - config_name: mni-Mtei-IN
    data_files:
      - split: train
        path: data/mni-Mtei-IN/train-*
  - config_name: sa-Deva-IN
    data_files:
      - split: train
        path: data/sa-Deva-IN/train-*
  - config_name: sat-Olck-IN
    data_files:
      - split: train
        path: data/sat-Olck-IN/train-*
  - config_name: sd-Deva-IN
    data_files:
      - split: train
        path: data/sd-Deva-IN/train-*
---

# Nemotron-Pretraining-Indic-Specialized-v1

## Dataset Description:

Nemotron-Pretraining-Indic-Specialized-v1 is the Specialized portion of the Nemotron-Pretraining-Indic corpus. It keeps only the records whose `_source_repo` is `nvidia/Nemotron-Pretraining-Specialized-v1` or `nvidia/Nemotron-Pretraining-Specialized-v1.1`; the other source datasets are released separately as Nemotron-Pretraining-Indic-CC-v1. The two datasets do not overlap and together make up the full corpus. The schema, field values and file layout are identical in both.

The Nemotron-Pretraining-Indic corpus is a large-scale synthetic Indic pretraining corpus designed to strengthen language-model capabilities across 22 Indian languages. It combines native-script and Latin-script/romanized data for twelve priority languages with native-script data for ten additional lower-resource languages.

The Nemotron-Pretraining-Indic corpus covers general-domain, STEM and mathematics, instruction-style, specialized, and educational content, split between Nemotron-Pretraining-Indic-CC-v1 and this dataset; this dataset contains only the Specialized-v1 and Specialized-v1.1 portions. The corpus was created by translating selected English source data and automatically evaluating candidate translations for faithfulness, fluency, terminology, and formatting preservation. The twelve-language pipeline uses quality-guided rewriting and re-evaluation. The lower-resource extension uses Bodhan-MT translation, Gemma-based quality assessment, and language-specific processing and filtering, without the twelve-language rewrite stage.

The dataset has 34 language-script configurations with record-level source provenance: 24 configurations for the twelve priority languages and ten native-script configurations for the lower-resource extension.

This dataset is ready for commercial or non-commercial uses.

Use is subject to the applicable source-specific terms below.

## Dataset Details:

### Languages

The following twelve priority languages have both native-script and Latin-script/romanized data:

| Language | Language code | Native script |
| --- | --- | --- |
| Bengali | `bn` | Bengali–Assamese |
| Gujarati | `gu` | Gujarati |
| Hindi | `hi` | Devanagari |
| Kannada | `kn` | Kannada |
| Malayalam | `ml` | Malayalam |
| Marathi | `mr` | Devanagari |
| Nepali | `ne` | Devanagari |
| Odia | `or` | Odia |
| Punjabi | `pa` | Gurmukhi |
| Tamil | `ta` | Tamil |
| Telugu | `te` | Telugu |
| Urdu | `ur` | Perso-Arabic |

The additional ten languages have native-script data only; no romanized configurations were generated for this group:

| Language | Configuration | Script |
| --- | --- | --- |
| Assamese | `as-Beng-IN` | Bengali–Assamese |
| Bodo | `brx-Deva-IN` | Devanagari |
| Dogri | `doi-Deva-IN` | Devanagari |
| Konkani | `gom-Deva-IN` | Devanagari |
| Kashmiri | `ks-Arab-IN` | Perso-Arabic |
| Maithili | `mai-Deva-IN` | Devanagari |
| Manipuri | `mni-Mtei-IN` | Meitei Mayek, obtained via Bengali-script Manipuri |
| Sanskrit | `sa-Deva-IN` | Devanagari |
| Santali | `sat-Olck-IN` | Ol Chiki |
| Sindhi | `sd-Deva-IN` | Devanagari |

Sindhi is provided in Devanagari script. Configuration and directory names follow BCP-47 `language-Script-Region` tags with the shortest ISO 639 language subtag. The `language_code` field inside the rows of four configurations uses the three-letter ISO 639-3 form instead: `as-Beng-IN` rows carry `asm-Beng-IN`, `ks-Arab-IN` rows carry `kas-Arab-IN`, `sa-Deva-IN` rows carry `san-Deva-IN`, and `sd-Deva-IN` rows carry `snd-Deva-IN`.

Each of the 34 configurations is a single language in a single script, named `<language>-<script>-IN` (e.g. `hi-Deva-IN`, `hi-Latn-IN`). Configuration names use the two-letter language code where one exists (the twelve priority languages, plus Assamese, Kashmiri, Sanskrit, and Sindhi) and a three-letter code otherwise (Bodo, Dogri, Konkani, Maithili, Manipuri, and Santali). Within the twelve-language group, native and romanized configurations for the same language are not necessarily derived from the same source samples and may contain different numbers of records.

### Configurations and source datasets

The 34 configurations are organized by language and script, not by source dataset.

The two sources are listed below. Source membership and proportions vary by configuration; the source of each record is preserved in `_source_repo` and `_source_config`.

| English-language seed dataset |
| --- |
| [`nvidia/Nemotron-Pretraining-Specialized-v1`](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1) |
| [`nvidia/Nemotron-Pretraining-Specialized-v1.1`](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1.1) |

The twelve-language group uses a common translation, automated evaluation, rewriting, and filtering workflow across its sources. The additional ten languages use the separate lower-resource routes described below; the common rewrite policy does not apply to them.

No specific revision or snapshot is pinned for each source.

### Creation pipeline

The logic for the translation is provided as a plugin in [`NVIDIA-NeMo/DataDesignerPlugins`](https://github.com/NVIDIA-NeMo/DataDesignerPlugins/tree/main/plugins/data-designer-nemotron-indic-translation) (`plugins/data-designer-nemotron-indic-translation`).

#### Twelve priority languages: translation, assessment, and repair

The same maker-checker-remaker workflow was applied to every source in the twelve-language group:

1. **Translation:** Selected English records were translated into the target Indic language.
2. **Automated evaluation:** Candidate translations were scored for source faithfulness, target-language fluency, terminology, and formatting preservation.
3. **Rewrite:** Candidates scoring below 75 were rewritten and evaluated again.
4. **Final filtering:** Rewritten candidates that still scored below 75 were dropped.
5. **Romanization:** Latin-script/romanized variants were generated for all 12 languages using separate romanization prompts.

The twelve-language maker-checker-remaker and romanization pipeline used the following Gemma checkpoints:

- [`google/gemma-4-31B-it`](https://huggingface.co/google/gemma-4-31B-it) was used for the initial small-scale generation runs, including the original approximately 10B-token run.
- [`RedHatAI/gemma-4-31B-it-FP8-block`](https://huggingface.co/RedHatAI/gemma-4-31B-it-FP8-block) was used for the vast majority of generation after the pipeline was optimized.
- [`google/gemma-4-31B-it-assistant`](https://huggingface.co/google/gemma-4-31B-it-assistant) was also used in the generation and automated evaluation workflow.

#### Ten additional languages: lower-resource translation routes

The lower-resource extension was developed with Bodhan-MT, supplied by Bodhan, because the twelve-language generation recipe did not transfer reliably to these languages. Candidate systems were compared using document-length translation tests, reference-based chrF scores, structure-preservation checks, and Gemma-based quality assessments. The automated judge has not been calibrated against human judgments for this group, so its scores are not evidence of human-validated quality.

| Languages | Production route |
| --- | --- |
| Assamese, Bodo, Dogri, Kashmiri, Konkani, Maithili, Sanskrit, Sindhi | Bodhan-MT translates whole documents; Gemma-4-31B evaluates the translations using the primary group's quality-assessment prompt. |
| Santali | Bodhan-MT translates documents up to 2,048 tokens whole. Longer documents are translated in overlapping 2,048-token windows; Gemma selects and lightly corrects translated sections to assemble the document. |
| Manipuri | Bodhan-MT produces Bengali-script Manipuri, which is mapped to Meitei Mayek using a fixed, deterministic graphemic mapping. Gemma provides the automated quality assessment. |

There is no document-level rewrite-and-rejudge stage for these ten languages, and no romanized data was generated for them. A final-output score threshold of 75 was applied, with lower-scoring outputs excluded rather than rewritten.

The Bodhan-MT production checkpoint and the immutable revisions of the pipeline models are not pinned. Santali window-tokenizer details and the Manipuri mapping version are not documented here.

### Data fields

All 34 configurations share a common 21-field schema. Intermediate-stage fields are used for the twelve romanized configurations and for Manipuri (`mni-Mtei-IN`); they are null in the other native-script configurations. Manipuri retains its Bengali-script intermediate and that intermediate's evaluation, separately from the final Meitei Mayek text and evaluation.

In the sampled lower-resource shards, unused intermediate columns have Arrow `null` type, whereas Manipuri's intermediate columns have `string`, nested `struct`, and `int64` types. Readers combining configurations should therefore normalize nullable intermediate-column types rather than assume identical physical schemas.

- **`uuid`**: A new unique identifier for each released row.
- **`text`**: The final native-script or romanized target text.
- **`language_code`**: The `<language>-<script>-IN` tag for the row's configuration (e.g. `hi-Deva-IN`). In the four configurations noted in the Languages section it uses the three-letter form (e.g. `asm-Beng-IN`).
- **`source_text`**: The original English source text.
- **`intermediate_text`**: The native-script translation used to produce a romanized row, or the Bengali-script Manipuri translation used to produce a `mni-Mtei-IN` row. Null elsewhere.
- **`evaluation_result`**: Automated quality evaluation (analysis, error analysis, justification, overall score) of `text`.
- **`overall_score`**: The overall score from `evaluation_result`.
- **`intermediate_evaluation_result`**: The automated evaluation of `intermediate_text`, where present.
- **`intermediate_overall_score`**: The overall score from `intermediate_evaluation_result`, where present.
- **`metadata`**: Source-record metadata, serialized as a JSON string.
- **`_source_repo`**, **`_source_config`**, **`_subset_key`**, **`_tier`**, **`_source_file`**: Source-dataset provenance fields.
- **`license`**: The source record's license field as carried through the pipeline.
- **`token_count_source`**: Token count of the source text.
- **`tokenizer_model`**: The tokenizer used to compute `token_count_source`.
- **`source_language`**: The source language (English for all rows).
- **`language`**: The target Indic language.
- **`source_uuid`**: The original dataset UUID, retained for source traceability.

`token_count_source` and `tokenizer_model` describe source-text accounting; they do not establish the tokenizer or counts for generated target text.

## Dataset Owner(s):

NVIDIA Corporation

## Dataset Creation Date:

2026-09-03

## Version:

Version: `v1`

Previous versions: No previous version.

This collection consists of translated outputs produced from selected records in the source datasets listed above. It is not a replacement for those source datasets.

## License/Terms of Use:

The applicable terms vary by source-derived component. The source-specific terms are reproduced below, including their applicable hyperlinks.

### `nvidia/Nemotron-Pretraining-Specialized-v1`

**GOVERNING TERMS:** This dataset is governed by the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0), except for the Nemotron-Pretraining-Wiki-Rewrite and Nemotron-Pretraining-Scientific-Coding datasets, which are governed by [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) and the [GNU Free Documentation License Version 1.3 (GFDL)](https://www.gnu.org/licenses/fdl-1.3.html) as indicated in the Hugging Face dataset viewer.

### `nvidia/Nemotron-Pretraining-Specialized-v1.1`

**Governing Terms:** This dataset is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/deed.en) (CC BY 4.0).

The applicable terms are determined by the source-derived component of each record rather than by its language-script configuration. The `_source_repo`, `_source_config`, `_subset_key`, and carried-through `license` fields preserve that mapping.

## Intended Usage:

Nemotron-Pretraining-Indic-Specialized-v1 is intended to support:

- multilingual pretraining and continued pretraining;
- research on Indic-language modeling and data mixtures;
- development of models for Indian languages; and
- commercial model development where permitted by the applicable terms.

The dataset is not designed as a benchmark, a factual ground-truth source, or a substitute for native-speaker evaluation. Additional review is required before using it in high-impact or safety-critical applications.

## Dataset Characterization

**Data Collection Method**

- **Hybrid: Automated, Synthetic.** The seed datasets have heterogeneous collection and generation methods documented in their source cards. Both language groups use synthetic translation, automated quality assessment, and filtering. Quality-gated rewriting and Latin-script romanization apply to the twelve-language group; the ten-language extension instead uses the lower-resource routes described above.

**Labeling Method**

- **Not Applicable for traditional labels.** The release contains pretraining text rather than supervised labels. Automated quality scores (`evaluation_result`, `overall_score`, and their `intermediate_*` counterparts) are curation signals, not human-validated labels. No claim of exhaustive human validation is made.

## Dataset Format

- Modality: Text
- Format: Parquet
- Split: Train
- Configurations: 34 language-script configurations (24 priority-language and ten lower-resource configurations)
- Path layout: `data/<language>-<script>-IN/train-*.parquet`
- Parquet shards: 10,959 across the 34 configurations

## Dataset Quantification

This dataset contains 167,954,507 rows across 34 language-script configurations and approximately 295.8 billion output tokens. This includes native-script and romanized outputs for the twelve priority languages, plus native-script outputs for the ten additional languages. Input tokens are reported separately and are not added to the output-token corpus size.

Input tokens are the per-row `token_count_source` values, which count the English source text. Output tokens were counted on the `text` field with the [`google/gemma-4-31B-it`](https://huggingface.co/google/gemma-4-31B-it) tokenizer. Row counts and token counts were computed across every shard; stored Parquet bytes and shard counts are summed from the file inventory.

### Records and storage

| Group | Configurations | Rows | Parquet shards | Stored Parquet bytes |
| --- | ---: | ---: | ---: | ---: |
| Twelve priority languages | 24 | 165,979,826 | 10,858 | 1,231,281,762,715 |
| Ten additional lower-resource languages | 10 | 1,974,681 | 101 | 21,858,968,406 |
| Total | 34 | 167,954,507 | 10,959 | 1,253,140,731,121 (~1.14 TiB) |

The schema has 21 fields.

### Token distribution by language group and script

Token counts are in billions (B), computed from exact per-file totals and rounded to one decimal.

| Group / script | Rows | Input tokens (B) | Output tokens (B) |
| --- | ---: | ---: | ---: |
| Twelve priority languages — native script | 138,762,873 | 157.4 | 242.8 |
| Twelve priority languages — romanized | 27,216,953 | 30.3 | 43.8 |
| Ten additional languages — native script only | 1,974,681 | 4.2 | 9.2 |
| Total | 167,954,507 | 191.9 | 295.8 |

These totals count stored language-script representations, not deduplicated unique content or tokens consumed during model training.

### Twelve priority languages: configuration-level counts

| Configuration | Rows | Input tokens (B) | Output tokens (B) |
| --- | ---: | ---: | ---: |
| `bn-Beng-IN` | 11,685,514 | 13.4 | 16.5 |
| `bn-Latn-IN` | 2,279,084 | 2.6 | 3.7 |
| `gu-Gujr-IN` | 11,738,710 | 13.4 | 21.3 |
| `gu-Latn-IN` | 2,312,913 | 2.6 | 3.5 |
| `hi-Deva-IN` | 12,041,387 | 13.9 | 17.4 |
| `hi-Latn-IN` | 2,357,646 | 2.8 | 3.8 |
| `kn-Knda-IN` | 11,056,436 | 12.3 | 20.1 |
| `kn-Latn-IN` | 2,221,840 | 2.4 | 3.7 |
| `ml-Mlym-IN` | 10,699,964 | 11.9 | 18.7 |
| `ml-Latn-IN` | 2,228,851 | 2.4 | 3.7 |
| `mr-Deva-IN` | 11,778,571 | 13.3 | 17.4 |
| `mr-Latn-IN` | 2,204,349 | 2.4 | 3.4 |
| `ne-Deva-IN` | 12,031,171 | 13.9 | 18.9 |
| `ne-Latn-IN` | 2,307,544 | 2.6 | 3.8 |
| `or-Orya-IN` | 11,163,976 | 12.2 | 29.1 |
| `or-Latn-IN` | 2,229,257 | 2.4 | 3.4 |
| `pa-Guru-IN` | 10,808,208 | 11.9 | 24.2 |
| `pa-Latn-IN` | 2,272,343 | 2.5 | 3.4 |
| `ta-Taml-IN` | 11,735,355 | 13.5 | 18.5 |
| `ta-Latn-IN` | 2,139,697 | 2.3 | 3.9 |
| `te-Telu-IN` | 11,969,113 | 13.8 | 21.8 |
| `te-Latn-IN` | 2,286,686 | 2.6 | 3.6 |
| `ur-Arab-IN` | 12,054,468 | 13.9 | 19.0 |
| `ur-Latn-IN` | 2,376,743 | 2.8 | 3.8 |

### Ten additional languages: configuration-level counts

| Configuration | Rows | Input tokens (B) | Output tokens (B) | Stored Parquet bytes |
| --- | ---: | ---: | ---: | ---: |
| `as-Beng-IN` | 232,680 | 0.5 | 0.9 | 2,532,615,881 |
| `brx-Deva-IN` | 184,075 | 0.4 | 0.7 | 1,902,050,143 |
| `doi-Deva-IN` | 244,798 | 0.5 | 0.8 | 2,635,089,725 |
| `gom-Deva-IN` | 231,959 | 0.5 | 0.8 | 2,495,460,127 |
| `ks-Arab-IN` | 184,882 | 0.4 | 1.0 | 1,800,253,755 |
| `mai-Deva-IN` | 245,379 | 0.5 | 0.8 | 2,628,182,158 |
| `mni-Mtei-IN` | 156,477 | 0.3 | 1.8 | 2,489,564,760 |
| `sa-Deva-IN` | 226,968 | 0.5 | 0.8 | 2,541,760,577 |
| `sat-Olck-IN` | 122,616 | 0.3 | 1.0 | 1,239,722,094 |
| `sd-Deva-IN` | 144,847 | 0.3 | 0.6 | 1,594,269,186 |

## Quality, Risks, and Limitations:

- Automated translation can introduce omissions, additions, mistranslations, unnatural phrasing, or formatting errors.
- Quality may vary by language, script, domain, source dataset, text length, and technical terminology.
- The corpus may contain translationese and may underrepresent regional varieties, code-mixing, colloquial language, and culturally specific usage.
- An LLM-based evaluator or remaker can share blind spots with the translation model. Automated scoring, rewriting, and filtering are not equivalent to native-speaker review.
- Coverage is asymmetric: twelve languages have native-script and romanized data, while the additional ten have native-script data only. The 22 languages may be unevenly distributed; aggregate size alone does not establish language-level quality or coverage.
- The lower-resource group uses a different translator, language-specific processing, and no document-level rewrite stage. Its automated quality scores are not calibrated against native-speaker judgments and should not be treated as directly comparable quality guarantees across languages.
- Manipuri's deterministic Bengali-to-Meitei-Mayek mapping is many-to-one, and the pipeline can preserve proper nouns in Latin script. Native-speaker validation of the mapping is not documented. Windowing and section assembly for Santali can introduce additional document-boundary and structure errors.
- Risks, biases, inaccuracies, personal information, or license constraints present in the source datasets may propagate to translated outputs.
- Related source versions may overlap. No quantified cross-source overlap or deduplication analysis is provided.
- The data may be unsuitable for safety-critical, high-impact, or factual-grounding applications without additional domain-specific validation.

## Reference(s):

### Source datasets

- [`nvidia/Nemotron-Pretraining-Specialized-v1`](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1)
- [`nvidia/Nemotron-Pretraining-Specialized-v1.1`](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1.1)

### Pipeline models

- [`google/gemma-4-31B-it`](https://huggingface.co/google/gemma-4-31B-it)
- [`RedHatAI/gemma-4-31B-it-FP8-block`](https://huggingface.co/RedHatAI/gemma-4-31B-it-FP8-block)
- [`google/gemma-4-31B-it-assistant`](https://huggingface.co/google/gemma-4-31B-it-assistant)
- [`bodhan-ai/indic-translate`](https://huggingface.co/bodhan-ai/indic-translate)

### Code

- [`NVIDIA-NeMo/DataDesignerPlugins`](https://github.com/NVIDIA-NeMo/DataDesignerPlugins/tree/main/plugins/data-designer-nemotron-indic-translation) — translation plugin (`data-designer-nemotron-indic-translation`)

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).
