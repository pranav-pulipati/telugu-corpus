---
language:
  - as
  - bn
  - en
  - gu
  - hi
  - kn
  - ml
  - mr
  - ne
  - or
  - pa
  - ta
  - te
  - ur
language_details: >-
  asm_Beng, ben_Beng, eng_Latn, guj_Gujr,
  hin_Deva, kan_Knda, mal_Mlym, mar_Deva,
  npi_Deva, ory_Orya, pan_Guru, tam_Taml, 
  tel_Telu, urd_Arab
license: other
license_name: microsoft-research-license
license_link: https://huggingface.co/datasets/microsoft/Updesh_beta/blob/main/LICENSE.md
task_categories:
  - question-answering
size_categories:
  - 1M<n<10M
tags:
  - Updesh
  - synthetic data
  - microsoft
  - multilingual
dataset_info:
  features:
    - name: id
      dtype: string
    - name: messages
      dtype: string
configs:
- config_name: analytical_reasoning
  data_files:
  - split: asm_Beng
    path: analytical_reasoning/asm_Beng-*.parquet
  - split: ben_Beng
    path: analytical_reasoning/ben_Beng-*.parquet
  - split: guj_Gujr
    path: analytical_reasoning/guj_Gujr-*.parquet
  - split: hin_Deva
    path: analytical_reasoning/hin_Deva-*.parquet
  - split: kan_Knda
    path: analytical_reasoning/kan_Knda-*.parquet
  - split: mal_Mlym
    path: analytical_reasoning/mal_Mlym-*.parquet
  - split: mar_Deva
    path: analytical_reasoning/mar_Deva-*.parquet
  - split: npi_Deva
    path: analytical_reasoning/npi_Deva-*.parquet
  - split: ory_Orya
    path: analytical_reasoning/ory_Orya-*.parquet
  - split: pan_Guru
    path: analytical_reasoning/pan_Guru-*.parquet
  - split: tam_Taml
    path: analytical_reasoning/tam_Taml-*.parquet
  - split: tel_Telu
    path: analytical_reasoning/tel_Telu-*.parquet
  - split: urd_Arab
    path: analytical_reasoning/urd_Arab-*.parquet
- config_name: brain_teaser
  data_files:
  - split: asm_Beng
    path: brain_teaser/asm_Beng-*.parquet
  - split: ben_Beng
    path: brain_teaser/ben_Beng-*.parquet
  - split: guj_Gujr
    path: brain_teaser/guj_Gujr-*.parquet
  - split: hin_Deva
    path: brain_teaser/hin_Deva-*.parquet
  - split: kan_Knda
    path: brain_teaser/kan_Knda-*.parquet
  - split: mal_Mlym
    path: brain_teaser/mal_Mlym-*.parquet
  - split: mar_Deva
    path: brain_teaser/mar_Deva-*.parquet
  - split: npi_Deva
    path: brain_teaser/npi_Deva-*.parquet
  - split: ory_Orya
    path: brain_teaser/ory_Orya-*.parquet
  - split: pan_Guru
    path: brain_teaser/pan_Guru-*.parquet
  - split: tam_Taml
    path: brain_teaser/tam_Taml-*.parquet
  - split: tel_Telu
    path: brain_teaser/tel_Telu-*.parquet
  - split: urd_Arab
    path: brain_teaser/urd_Arab-*.parquet
- config_name: causal_reasoning
  data_files:
  - split: asm_Beng
    path: causal_reasoning/asm_Beng-*.parquet
  - split: ben_Beng
    path: causal_reasoning/ben_Beng-*.parquet
  - split: eng_Latn
    path: causal_reasoning/eng_Latn-*.parquet
  - split: guj_Gujr
    path: causal_reasoning/guj_Gujr-*.parquet
  - split: hin_Deva
    path: causal_reasoning/hin_Deva-*.parquet
  - split: kan_Knda
    path: causal_reasoning/kan_Knda-*.parquet
  - split: mal_Mlym
    path: causal_reasoning/mal_Mlym-*.parquet
  - split: mar_Deva
    path: causal_reasoning/mar_Deva-*.parquet
  - split: npi_Deva
    path: causal_reasoning/npi_Deva-*.parquet
  - split: ory_Orya
    path: causal_reasoning/ory_Orya-*.parquet
  - split: pan_Guru
    path: causal_reasoning/pan_Guru-*.parquet
  - split: tam_Taml
    path: causal_reasoning/tam_Taml-*.parquet
  - split: tel_Telu
    path: causal_reasoning/tel_Telu-*.parquet
  - split: urd_Arab
    path: causal_reasoning/urd_Arab-*.parquet
- config_name: creative_writing
  data_files:
  - split: asm_Beng
    path: creative_writing/asm_Beng-*.parquet
  - split: ben_Beng
    path: creative_writing/ben_Beng-*.parquet
  - split: eng_Latn
    path: creative_writing/eng_Latn-*.parquet
  - split: guj_Gujr
    path: creative_writing/guj_Gujr-*.parquet
  - split: hin_Deva
    path: creative_writing/hin_Deva-*.parquet
  - split: kan_Knda
    path: creative_writing/kan_Knda-*.parquet
  - split: mal_Mlym
    path: creative_writing/mal_Mlym-*.parquet
  - split: mar_Deva
    path: creative_writing/mar_Deva-*.parquet
  - split: npi_Deva
    path: creative_writing/npi_Deva-*.parquet
  - split: ory_Orya
    path: creative_writing/ory_Orya-*.parquet
  - split: pan_Guru
    path: creative_writing/pan_Guru-*.parquet
  - split: tam_Taml
    path: creative_writing/tam_Taml-*.parquet
  - split: tel_Telu
    path: creative_writing/tel_Telu-*.parquet
  - split: urd_Arab
    path: creative_writing/urd_Arab-*.parquet
- config_name: cultural_multihop_reasoning
  data_files:
  - split: asm_Beng
    path: cultural_multihop_reasoning/asm_Beng-*.parquet
  - split: ben_Beng
    path: cultural_multihop_reasoning/ben_Beng-*.parquet
  - split: eng_Latn
    path: cultural_multihop_reasoning/eng_Latn-*.parquet
  - split: guj_Gujr
    path: cultural_multihop_reasoning/guj_Gujr-*.parquet
  - split: hin_Deva
    path: cultural_multihop_reasoning/hin_Deva-*.parquet
  - split: kan_Knda
    path: cultural_multihop_reasoning/kan_Knda-*.parquet
  - split: mal_Mlym
    path: cultural_multihop_reasoning/mal_Mlym-*.parquet
  - split: mar_Deva
    path: cultural_multihop_reasoning/mar_Deva-*.parquet
  - split: npi_Deva
    path: cultural_multihop_reasoning/npi_Deva-*.parquet
  - split: ory_Orya
    path: cultural_multihop_reasoning/ory_Orya-*.parquet
  - split: pan_Guru
    path: cultural_multihop_reasoning/pan_Guru-*.parquet
  - split: tam_Taml
    path: cultural_multihop_reasoning/tam_Taml-*.parquet
  - split: tel_Telu
    path: cultural_multihop_reasoning/tel_Telu-*.parquet
  - split: urd_Arab
    path: cultural_multihop_reasoning/urd_Arab-*.parquet
- config_name: dialog_gen
  data_files:
  - split: asm_Beng
    path: dialog_gen/asm_Beng-*.parquet
  - split: ben_Beng
    path: dialog_gen/ben_Beng-*.parquet
  - split: eng_Latn
    path: dialog_gen/eng_Latn-*.parquet
  - split: guj_Gujr
    path: dialog_gen/guj_Gujr-*.parquet
  - split: hin_Deva
    path: dialog_gen/hin_Deva-*.parquet
  - split: kan_Knda
    path: dialog_gen/kan_Knda-*.parquet
  - split: mal_Mlym
    path: dialog_gen/mal_Mlym-*.parquet
  - split: mar_Deva
    path: dialog_gen/mar_Deva-*.parquet
  - split: npi_Deva
    path: dialog_gen/npi_Deva-*.parquet
  - split: ory_Orya
    path: dialog_gen/ory_Orya-*.parquet
  - split: pan_Guru
    path: dialog_gen/pan_Guru-*.parquet
  - split: tam_Taml
    path: dialog_gen/tam_Taml-*.parquet
  - split: tel_Telu
    path: dialog_gen/tel_Telu-*.parquet
  - split: urd_Arab
    path: dialog_gen/urd_Arab-*.parquet
- config_name: fermi
  data_files:
  - split: asm_Beng
    path: fermi/asm_Beng-*.parquet
  - split: ben_Beng
    path: fermi/ben_Beng-*.parquet
  - split: guj_Gujr
    path: fermi/guj_Gujr-*.parquet
  - split: hin_Deva
    path: fermi/hin_Deva-*.parquet
  - split: kan_Knda
    path: fermi/kan_Knda-*.parquet
  - split: mal_Mlym
    path: fermi/mal_Mlym-*.parquet
  - split: mar_Deva
    path: fermi/mar_Deva-*.parquet
  - split: npi_Deva
    path: fermi/npi_Deva-*.parquet
  - split: ory_Orya
    path: fermi/ory_Orya-*.parquet
  - split: pan_Guru
    path: fermi/pan_Guru-*.parquet
  - split: tam_Taml
    path: fermi/tam_Taml-*.parquet
  - split: tel_Telu
    path: fermi/tel_Telu-*.parquet
  - split: urd_Arab
    path: fermi/urd_Arab-*.parquet
- config_name: fs_cot_flow
  data_files:
  - split: asm_Beng
    path: fs_cot_flow/asm_Beng-*.parquet
  - split: ben_Beng
    path: fs_cot_flow/ben_Beng-*.parquet
  - split: guj_Gujr
    path: fs_cot_flow/guj_Gujr-*.parquet
  - split: hin_Deva
    path: fs_cot_flow/hin_Deva-*.parquet
  - split: kan_Knda
    path: fs_cot_flow/kan_Knda-*.parquet
  - split: mal_Mlym
    path: fs_cot_flow/mal_Mlym-*.parquet
  - split: mar_Deva
    path: fs_cot_flow/mar_Deva-*.parquet
  - split: npi_Deva
    path: fs_cot_flow/npi_Deva-*.parquet
  - split: ory_Orya
    path: fs_cot_flow/ory_Orya-*.parquet
  - split: pan_Guru
    path: fs_cot_flow/pan_Guru-*.parquet
  - split: tam_Taml
    path: fs_cot_flow/tam_Taml-*.parquet
  - split: tel_Telu
    path: fs_cot_flow/tel_Telu-*.parquet
  - split: urd_Arab
    path: fs_cot_flow/urd_Arab-*.parquet
- config_name: logical_reasoning
  data_files:
  - split: asm_Beng
    path: logical_reasoning/asm_Beng-*.parquet
  - split: ben_Beng
    path: logical_reasoning/ben_Beng-*.parquet
  - split: eng_Latn
    path: logical_reasoning/eng_Latn-*.parquet
  - split: guj_Gujr
    path: logical_reasoning/guj_Gujr-*.parquet
  - split: hin_Deva
    path: logical_reasoning/hin_Deva-*.parquet
  - split: kan_Knda
    path: logical_reasoning/kan_Knda-*.parquet
  - split: mal_Mlym
    path: logical_reasoning/mal_Mlym-*.parquet
  - split: mar_Deva
    path: logical_reasoning/mar_Deva-*.parquet
  - split: npi_Deva
    path: logical_reasoning/npi_Deva-*.parquet
  - split: ory_Orya
    path: logical_reasoning/ory_Orya-*.parquet
  - split: pan_Guru
    path: logical_reasoning/pan_Guru-*.parquet
  - split: tam_Taml
    path: logical_reasoning/tam_Taml-*.parquet
  - split: tel_Telu
    path: logical_reasoning/tel_Telu-*.parquet
  - split: urd_Arab
    path: logical_reasoning/urd_Arab-*.parquet
- config_name: math
  data_files:
  - split: asm_Beng
    path: math/asm_Beng-*.parquet
  - split: ben_Beng
    path: math/ben_Beng-*.parquet
  - split: guj_Gujr
    path: math/guj_Gujr-*.parquet
  - split: hin_Deva
    path: math/hin_Deva-*.parquet
  - split: kan_Knda
    path: math/kan_Knda-*.parquet
  - split: mal_Mlym
    path: math/mal_Mlym-*.parquet
  - split: mar_Deva
    path: math/mar_Deva-*.parquet
  - split: npi_Deva
    path: math/npi_Deva-*.parquet
  - split: ory_Orya
    path: math/ory_Orya-*.parquet
  - split: pan_Guru
    path: math/pan_Guru-*.parquet
  - split: tam_Taml
    path: math/tam_Taml-*.parquet
  - split: tel_Telu
    path: math/tel_Telu-*.parquet
  - split: urd_Arab
    path: math/urd_Arab-*.parquet
- config_name: mcq
  data_files:
  - split: asm_Beng
    path: mcq/asm_Beng-*.parquet
  - split: ben_Beng
    path: mcq/ben_Beng-*.parquet
  - split: guj_Gujr
    path: mcq/guj_Gujr-*.parquet
  - split: hin_Deva
    path: mcq/hin_Deva-*.parquet
  - split: kan_Knda
    path: mcq/kan_Knda-*.parquet
  - split: mal_Mlym
    path: mcq/mal_Mlym-*.parquet
  - split: mar_Deva
    path: mcq/mar_Deva-*.parquet
  - split: npi_Deva
    path: mcq/npi_Deva-*.parquet
  - split: ory_Orya
    path: mcq/ory_Orya-*.parquet
  - split: pan_Guru
    path: mcq/pan_Guru-*.parquet
  - split: tam_Taml
    path: mcq/tam_Taml-*.parquet
  - split: tel_Telu
    path: mcq/tel_Telu-*.parquet
  - split: urd_Arab
    path: mcq/urd_Arab-*.parquet
- config_name: multihop_reasoning
  data_files:
  - split: asm_Beng
    path: multihop_reasoning/asm_Beng-*.parquet
  - split: ben_Beng
    path: multihop_reasoning/ben_Beng-*.parquet
  - split: eng_Latn
    path: multihop_reasoning/eng_Latn-*.parquet
  - split: guj_Gujr
    path: multihop_reasoning/guj_Gujr-*.parquet
  - split: hin_Deva
    path: multihop_reasoning/hin_Deva-*.parquet
  - split: kan_Knda
    path: multihop_reasoning/kan_Knda-*.parquet
  - split: mal_Mlym
    path: multihop_reasoning/mal_Mlym-*.parquet
  - split: mar_Deva
    path: multihop_reasoning/mar_Deva-*.parquet
  - split: npi_Deva
    path: multihop_reasoning/npi_Deva-*.parquet
  - split: ory_Orya
    path: multihop_reasoning/ory_Orya-*.parquet
  - split: pan_Guru
    path: multihop_reasoning/pan_Guru-*.parquet
  - split: tam_Taml
    path: multihop_reasoning/tam_Taml-*.parquet
  - split: tel_Telu
    path: multihop_reasoning/tel_Telu-*.parquet
  - split: urd_Arab
    path: multihop_reasoning/urd_Arab-*.parquet
- config_name: rc
  data_files:
  - split: asm_Beng
    path: rc/asm_Beng-*.parquet
  - split: ben_Beng
    path: rc/ben_Beng-*.parquet
  - split: guj_Gujr
    path: rc/guj_Gujr-*.parquet
  - split: hin_Deva
    path: rc/hin_Deva-*.parquet
  - split: kan_Knda
    path: rc/kan_Knda-*.parquet
  - split: mal_Mlym
    path: rc/mal_Mlym-*.parquet
  - split: mar_Deva
    path: rc/mar_Deva-*.parquet
  - split: npi_Deva
    path: rc/npi_Deva-*.parquet
  - split: ory_Orya
    path: rc/ory_Orya-*.parquet
  - split: pan_Guru
    path: rc/pan_Guru-*.parquet
  - split: tam_Taml
    path: rc/tam_Taml-*.parquet
  - split: tel_Telu
    path: rc/tel_Telu-*.parquet
  - split: urd_Arab
    path: rc/urd_Arab-*.parquet
- config_name: summarization
  data_files:
  - split: asm_Beng
    path: summarization/asm_Beng-*.parquet
  - split: ben_Beng
    path: summarization/ben_Beng-*.parquet
  - split: eng_Latn
    path: summarization/eng_Latn-*.parquet
  - split: guj_Gujr
    path: summarization/guj_Gujr-*.parquet
  - split: hin_Deva
    path: summarization/hin_Deva-*.parquet
  - split: kan_Knda
    path: summarization/kan_Knda-*.parquet
  - split: mal_Mlym
    path: summarization/mal_Mlym-*.parquet
  - split: mar_Deva
    path: summarization/mar_Deva-*.parquet
  - split: npi_Deva
    path: summarization/npi_Deva-*.parquet
  - split: ory_Orya
    path: summarization/ory_Orya-*.parquet
  - split: pan_Guru
    path: summarization/pan_Guru-*.parquet
  - split: tam_Taml
    path: summarization/tam_Taml-*.parquet
  - split: tel_Telu
    path: summarization/tel_Telu-*.parquet
  - split: urd_Arab
    path: summarization/urd_Arab-*.parquet
- config_name: text_classification
  data_files:
  - split: asm_Beng
    path: text_classification/asm_Beng-*.parquet
  - split: ben_Beng
    path: text_classification/ben_Beng-*.parquet
  - split: guj_Gujr
    path: text_classification/guj_Gujr-*.parquet
  - split: hin_Deva
    path: text_classification/hin_Deva-*.parquet
  - split: kan_Knda
    path: text_classification/kan_Knda-*.parquet
  - split: mal_Mlym
    path: text_classification/mal_Mlym-*.parquet
  - split: mar_Deva
    path: text_classification/mar_Deva-*.parquet
  - split: npi_Deva
    path: text_classification/npi_Deva-*.parquet
  - split: ory_Orya
    path: text_classification/ory_Orya-*.parquet
  - split: pan_Guru
    path: text_classification/pan_Guru-*.parquet
  - split: tam_Taml
    path: text_classification/tam_Taml-*.parquet
  - split: tel_Telu
    path: text_classification/tel_Telu-*.parquet
  - split: urd_Arab
    path: text_classification/urd_Arab-*.parquet
- config_name: translation_enxx
  data_files:
  - split: asm_Beng
    path: translation_enxx/asm_Beng-*.parquet
  - split: ben_Beng
    path: translation_enxx/ben_Beng-*.parquet
  - split: guj_Gujr
    path: translation_enxx/guj_Gujr-*.parquet
  - split: hin_Deva
    path: translation_enxx/hin_Deva-*.parquet
  - split: kan_Knda
    path: translation_enxx/kan_Knda-*.parquet
  - split: mal_Mlym
    path: translation_enxx/mal_Mlym-*.parquet
  - split: mar_Deva
    path: translation_enxx/mar_Deva-*.parquet
  - split: npi_Deva
    path: translation_enxx/npi_Deva-*.parquet
  - split: ory_Orya
    path: translation_enxx/ory_Orya-*.parquet
  - split: pan_Guru
    path: translation_enxx/pan_Guru-*.parquet
  - split: tam_Taml
    path: translation_enxx/tam_Taml-*.parquet
  - split: tel_Telu
    path: translation_enxx/tel_Telu-*.parquet
  - split: urd_Arab
    path: translation_enxx/urd_Arab-*.parquet
- config_name: translation_xxen
  data_files:
  - split: asm_Beng
    path: translation_xxen/asm_Beng-*.parquet
  - split: ben_Beng
    path: translation_xxen/ben_Beng-*.parquet
  - split: guj_Gujr
    path: translation_xxen/guj_Gujr-*.parquet
  - split: hin_Deva
    path: translation_xxen/hin_Deva-*.parquet
  - split: kan_Knda
    path: translation_xxen/kan_Knda-*.parquet
  - split: mal_Mlym
    path: translation_xxen/mal_Mlym-*.parquet
  - split: mar_Deva
    path: translation_xxen/mar_Deva-*.parquet
  - split: npi_Deva
    path: translation_xxen/npi_Deva-*.parquet
  - split: ory_Orya
    path: translation_xxen/ory_Orya-*.parquet
  - split: pan_Guru
    path: translation_xxen/pan_Guru-*.parquet
  - split: tam_Taml
    path: translation_xxen/tam_Taml-*.parquet
  - split: tel_Telu
    path: translation_xxen/tel_Telu-*.parquet
  - split: urd_Arab
    path: translation_xxen/urd_Arab-*.parquet    
---

# 📢 Updesh: Synthetic Multilingual Instruction Tuning Dataset for 13 Indic Languages

![Version](https://img.shields.io/badge/version-1.0-blue) ![License](https://img.shields.io/badge/license-Microsoft--Research--License-green) ![Language Count](https://img.shields.io/badge/languages-13-yellow) [![HuggingFace](https://img.shields.io/badge/view_on-HuggingFace-orange)](https://huggingface.co/microsoft/Updesh_beta)

*NOTE: This is an initial $\beta$-release. We plan to release subsequent versions of Updesh with expanded coverage and enhanced quality control. Future iterations will include larger datasets, improved filtering pipelines.*

- **Updesh** is a large-scale synthetic dataset designed to advance post-training of LLMs for Indic languages. It integrates translated reasoning data and synthesized open-domain generative content to support culturally-grounded multilingual adaptation of LLMs.

- Despite the rapid progress in instruction-tuned LLMs, most existing datasets focus on English, creating a gap in high-quality, culturally grounded resources for Indic languages—resources that are essential for enabling Small Language Models (SLMs) to serve India’s diverse linguistic landscape. Updesh aims to fill this gap by providing rich, multilingual instruction-tuning data grounded in Indian languages and contexts.

- Unlike previous English centric translated datasets, Updesh employs a dual approach of culturally-grounded data generation and careful, selective translation, ensuring linguistic nuance and relevance for each language. 

- By releasing Updesh as open data, researchers and communities working on Indian languages as well as other low-resource languages gain unprecedented access to high-quality, culturally-nuanced data. 

---

## 📚 Overview

- **Languages:** _Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Odia, Punjabi, Tamil, Telugu, Urdu_  
- **Data Composition:**  
  - **Reasoning Data:** ~6.8M translated tuples  
  - **Generative Data:** ~2.1M synthesized tuples  
- **Structure:** System instruction → User prompt ⇄ Assistant response (single/multi-turn)  
- **Sources:**  
  - [Orca-AgentInstruct](https://huggingface.co/datasets/microsoft/orca-agentinstruct-1M-v1)  
  - [OrcaMath](https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k)  
  - [Wikipedia-20250301](https://huggingface.co/datasets/NeuML/wikipedia-20250123) 
- **Timeframe:** January–July 2025  

*For full methodology and evaluation, please refer to our [paper](https://arxiv.org/abs/2509.21294).*

---

## 📦 Dataset Construction

Our synthetic data creation methodology is grounded in two main innovations: 
- The use of language-specific, culturally-relevant seed data to create new synthetic data and 
- The use of selective translation to carefully translate relevant parts of already existing data. 

This dual approach enables us to effectively utilize data created by native speakers for each language, along with high-quality datasets created in English.  Updesh dataset consists of two subsets, open-domain generative data and reasoning data.

### Updesh-R Reasoning Data 🤔 (Translated)
- **Sources:** 8 specialized subsets from `Orca-AgentInstruct` and `OrcaMath`:
  - `Analytical Reasoning`: MCQ-style logical inference and deductive analysis
  - `Reading Comprehension`: GRE-level passages for nuanced understanding and inference
  - `Multiple-Choice Questions`: General cognitive problem-solving across domains
  - `Fermi (Guesstimation)` : Open-ended estimation and numerical reasoning
  - `Few-Shot Chain-of-Thought` : In-context multi-example reasoning
  - `Brain Teasers` : Lateral thinking and creative problem-solving
  - `Text Classification` : Semantic categorization and linguistic pattern recognition
  - `Math` : Arithmetic, algebraic, and geometric word problems.

- **Translation:**  
  - Model: [Llama-3.1-405B-Instruct 🦙](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct) 
  - Languages: All 13 target Indic languages  


### Updesh-G Generative Data 📝 (Synthesized)
- **Model:** [Qwen3-235B-A22B](Qwen/Qwen3-235B-A22B) (selected for superior generative and reasoning performance)
- **Methodology:** Instruction backtranslation using Wikipedia as a knowledge base  
- **Categories:**  
  - `Logical Reasoning`: Inference and deduction from implicit information in text.
  - `Multi-Hop QA`: Answering questions by synthesizing information across multiple sections of the passage.
  - `Creative Writing`: Generating colloquial engaging narratives grounded in factual content.
  - `Multi-turn Dialogue/Role-Playing/Conversational Advice Seeking` : Producing coherent, context-aware multi-turn conversations.
  - `Summarization`: (in-language and cross-lingual): Condensing content within or across languages while preserving meaning.
  - `Machine Translation`: Selectively Translating text between languages with semantic fidelity.
  - `Causal Reasoning`: Identifying and explaining cause-effect relationships in context.
  - `Culturally-grounded Multi-Hop QA`: X-lingual Multi-step question answering grounded in cultural or regional context.


- **Data Volume per Language and Subset of Updesh:** 
  - Only the English Split of the Generative Subsets are mentioned below. Since, Updesh-R (marked with ♠) is _selectively translated_ from  [Orca-AgentInstruct](https://huggingface.co/datasets/microsoft/orca-agentinstruct-1M-v1) and [OrcaMath](https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k), we do not re-release them in Updesh, and hence the sparsity in that column. We **strongly** recommend including these English subsets in Updesh during SFT. 

|subset                     |asm_Beng|ben_Beng|eng_Latn|guj_Gujr|hin_Deva|kan_Knda|mal_Mlym|mar_Deva|npi_Deva|ory_Orya|pan_Guru|tam_Taml|tel_Telu|urd_Arab|
|---------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|`analytical_reasoning`<sup>♠</sup>       |24.99   |25.0    |-     |25.0    |24.97   |25.0    |25.0    |25.0    |24.99   |24.98   |25.0    |25.0    |25.0    |24.93   |
|`brain_teaser`<sup>♠</sup>               |49.98   |49.99   |-     |49.99   |49.94   |49.99   |49.99   |49.99   |49.97   |49.94   |49.99   |49.99   |49.99   |49.99   |
|`causal_reasoning`           |16.15   |16.38   |16.38   |16.38   |16.38   |16.38   |16.38   |16.38   |15.68   |16.38   |16.38   |16.38   |16.38   |16.36   |
|`creative_writing`           |16.14   |16.38   |16.38   |16.38   |16.37   |16.38   |16.38   |16.38   |15.72   |16.38   |16.15   |16.38   |16.38   |16.37   |
|`cultural_multihop_reasoning`|26.74   |26.6    |26.78   |26.77   |26.73   |26.71   |26.75   |26.77   |26.76   |26.72   |26.12   |26.74   |26.67   |26.71   |
|`dialog_gen`                 |16.12   |16.37   |16.38   |16.38   |16.37   |16.38   |16.37   |16.38   |15.66   |16.37   |16.38   |16.38   |16.38   |16.36   |
|`fermi`<sup>♠</sup>                      |24.99   |25.0    |-     |25.0    |24.99   |25.0    |25.0    |25.0    |25.0    |24.99   |25.0    |25.0    |25.0    |24.99   |
|`fs_cot_flow`<sup>♠</sup>                |23.5    |24.65   |-     |24.37   |22.74   |24.21   |24.63   |24.23   |23.98   |23.99   |24.52   |24.48   |24.59   |22.85   |
|`logical_reasoning`          |16.14   |16.38   |16.36   |16.38   |16.38   |16.38   |16.38   |16.38   |15.68   |16.38   |16.38   |16.38   |16.38   |16.38   |
|`math`<sup>♠</sup>                       |199.99  |200.02  |-     |200.03  |199.3   |200.03  |200.03  |200.02  |200.0   |200.02  |200.03  |200.03  |200.03  |199.98  |
|`mcq`<sup>♠</sup>                        |99.88   |99.92   |-     |99.92   |99.41   |99.94   |99.96   |99.9    |99.78   |99.93   |99.93   |99.95   |99.95   |99.59   |
|`multihop_reasoning`         |16.14   |16.38   |16.38   |16.38   |16.37   |16.38   |16.38   |16.38   |15.68   |16.38   |16.38   |16.38   |16.38   |16.38   |
|`rc`<sup>♠</sup>                         |49.66   |49.92   |-    |49.93   |49.58   |49.91   |49.96   |49.81   |49.63   |49.8    |49.94   |49.92   |49.94   |49.52   |
|`summarization`              |16.13   |16.37   |16.37   |16.37   |16.36   |16.36   |16.35   |16.37   |15.72   |16.37   |16.37   |16.37   |16.37   |16.37   |
|`text_classification`<sup>♠</sup>        |48.56   |49.79   |-     |49.82   |47.86   |49.8    |49.94   |49.45   |49.15   |47.82   |49.93   |49.81   |49.92   |45.93   |
|`translation_enxx`           |16.28   |16.31   |-     |16.34   |16.25   |16.23   |16.26   |16.27   |16.27   |16.19   |16.25   |16.26   |16.24   |16.31   |
|`translation_xxen`           |13.59   |16.36   |-     |16.37   |16.24   |16.34   |16.34   |16.29   |14.56   |15.09   |16.3    |16.33   |16.3    |16.34   |
|**TOTAL**                    |675.0   |681.84  |125.04  |681.8   |676.26  |681.42  |682.12  |681.01  |674.23  |677.73  |681.06  |681.79  |681.92  |675.39  |

---

## ✅ Quality Assurance and Validation

Given the scale of Updesh (~8.9M data points across 13 languages), we implemented robust automatic multi-stage quality checks inspired by recent large-scale multilingual dataset practices.

- **Language Identification (LID):**  
  Each sample is validated using [NLLB LID](https://huggingface.co/facebook/fasttext-language-identification) and [IndicLID](https://github.com/AI4Bharat/IndicLID) to ensure correct classification into the intended target language. This helps detect and filter out mistranslations.


- **Word Repetition Ratio:**  
  For every sample, we compute the word repetition ratio, flagging and filtering out instances with excessive repetition to mitigate low-quality outputs and hallucinations.


- **Translation Quality Assessment:**  
  - For reasoning subsets, we adopted a backtranslation approach: generated outputs in target languages were translated back into English (using Llama 3.3 70B for efficiency), then compared with the original English source.
  - We randomly sampled 4,096 instances per subset per language for evaluation.
  - Translation fidelity was measured using SPBLEU and ChrF metrics (via the [SacreBLEU](https://github.com/mjpost/sacrebleu) library using the `FLORES-200 SPM` tokenizer).
  - Results consistently demonstrated high backtranslation scores across all languages and subsets, indicating robust translation quality even with a conservative evaluation setup.

- **Additional Filtering:**  
  - Automated deduplication to remove redundant samples.
  - Manual spot checks for select samples and categories.

We are in the process of implementing additional quality checks. The data and technical report will be updated accordingly in due course.

---

## 🎯 Intended Use
- **Primary:**  
  - Research in multilingual reasoning adaptation and Instruction-tuning LLMs for Indic languages.

- **Not Recommended For:**  
  - Non-Indic languages or high-risk domains  
  - Commercial deployment without further validation 
  - Use in educational, health, or legal systems without rigorous downstream testing.

---

## 🚀 Getting Started
You can access the Updesh dataset from HuggingFace as follows:-
```python
from datasets import load_dataset

# to load the Hindi split of Creative Writing subset:
subset = "creative_writing"
split = "hin_Deva"

dataset = load_dataset("microsoft/Updesh_beta", subset, split=split)
```


### Data Instances 

A typical data entry in the dataset consists of a conversation i.e. sequence of question and its corresponding answer. Below is an example from the dataset: 
```json
{ 
  "messages": [ 
    { 
      "role": "system", 
      "content": "" 
    }, 
    { 
      "role": "user", 
      "content": "Argue the importance of having a strong understanding of physics and mechanics in the design of electron beam systems for semiconductor equipment." 
    }, 
    { 
      "role": "assistant", 
      "content": "Having a strong understanding of physics and mechanics is crucial in the design of electron beam systems for semiconductor equipment. This is because electron beam systems rely heavily on the principles of physics and mechanics to function effectively and efficiently.\n\nFirstly, a strong understanding of physics is necessary to design the electron gun, which is the heart of the electron beam system. The electron gun generates and accelerates the electrons that are used to create the beam. The design of the electron gun must take into account the properties of electrons, such as their charge, mass, and velocity, as well as the principles of electromagnetism and quantum mechanics. Without a thorough understanding of these principles, it would be impossible to design an electron gun that can generate and accelerate electrons with the required energy and precision.\n\nSecondly, a strong understanding of mechanics is essential in the design of the electron beam system's optics. The optics are responsible for shaping and focusing the electron beam, which is critical for achieving high-resolution imaging and precise material processing. The design of the optics must take into account the principles of optics, such as refraction, reflection, and diffraction, as well as the mechanical properties of the components, such as their stiffness, thermal expansion, and vibration resistance. Without a thorough understanding of these principles, it would be impossible to design optics that can shape and focus the electron beam with the required precision and stability.\n\nIn conclusion, a strong understanding of physics and mechanics is essential in the design of electron beam systems for semiconductor equipment. Without this understanding, it would be impossible to design electron guns and optics that can generate and shape the electron beam with the required precision and stability. Therefore, designers of electron beam systems must have a solid foundation in physics and mechanics to ensure that their designs are effective and efficient." 
    }, 
    { 
      "role": "user", 
      "content": "Could you perhaps rephrase your entire explanation using only haiku poetry? It would certainly give your answer a more artistic touch, don't you think?" 
    }, 
    { 
      "role": "assistant", 
      "content": "Electron streams flow,\nPhysics guides their path and speed,\nSemiconduct's soul.\n\nElectron gun's heart,\nQuantum dance, charged particles,\nPrecision's fine art.\n\nOptics shape the beam,\nMechanics' firm hand guides light,\nFocused like a dream.\n\nIn the silicon dance,\nPhysics, mechanics embrace,\nAdvance our expanse.\n\nDesign's core must know,\nNature's laws to harness force,\nFor tech to grow, glow." 
    }, 
    { 
      "role": "user", 
      "content": "Just to make sure I've got it right, your haikus suggest that the electron gun and optics are like artists, requiring precision and a deep understanding of natural laws to create their masterpiece?" 
    }, 
    { 
      "role": "assistant", 
      "content": "Indeed, that's a poetic interpretation. The haikus suggest that the electron gun (the creator of the electron beam) and the optics (which shape and focus the beam) require a precise understanding of physics and mechanics, much like artists need a deep understanding of their tools and materials to create a masterpiece. The natural laws are the guidelines within which they must work to achieve the desired outcome in semiconductor equipment design." 
    }, 
    { 
      "role": "user", 
      "content": "I'd like to understand more about the 'precision's fine art' you mentioned. Can you explain how precision is achieved in the design of the electron gun and optics?" 
    }, 
    { 
      "role": "assistant", 
      "content": "Certainly! Achieving precision in the design of the electron gun and optics in electron beam systems involves several key factors:\n\n1. **Electron Gun Design:**\n   - **Vacuum Environment:** The electron gun operates in a high vacuum to prevent electron scattering by air molecules, ensuring a precise and concentrated beam.\n   - **Cathode Material:** The choice of cathode material affects the emission efficiency and stability of the electron beam. Materials like tungsten or lanthanum hexaboride are often used for their high melting points and low work functions.\n   - **Anode Configuration:** The anode accelerates the electrons and its design, including the shape and voltage applied, determines the beam's energy and focus.\n   - **Electromagnetic Lenses:** These lenses control the focus of the electron beam, and their design must account for spherical and chromatic aberrations to maintain precision.\n\n2. **Optics Design:**\n   - **Electromagnetic Lenses:** Just like in the electron gun, these lenses in the optical column are used to focus and deflect the electron beam with high precision. The design and alignment of these lenses are critical for achieving the desired spot size and shape on the target.\n   - **Stigmators:** These are used to correct for astigmatism in the electron beam, ensuring that the beam remains symmetrical and focused over a range of operating conditions.\n   - **Apertures:** Placed at strategic points in the optical column, apertures help to shape the beam and eliminate electrons that stray from the desired path, improving resolution and reducing aberrations.\n   - **Thermal Stability:** Precision in electron beam systems also depends on maintaining thermal stability to prevent drift or deformation of the optical components.\n\n3. **Control Systems:**\n   - **Feedback Loops:** Precision is maintained through feedback systems that monitor the beam's characteristics and make real-time adjustments to the electron gun and optics to correct any deviations.\n   - **Vibration Isolation:** The entire system must be isolated from external vibrations that could disturb the beam's path, often using pneumatic or magnetic isolation systems.\n\n4. **Material Science:**\n   - **Material Properties:** The materials used in the construction of the electron gun and optics must be chosen for their stability under the operating conditions, including resistance to thermal expansion and electromagnetic interference.\n\n5. **Computational Modeling:**\n   - **Simulation Software:** Advanced software is used to model the electron beam's behavior and interactions with the system's components, allowing for the optimization of the design before physical construction.\n\nIn summary, 'precision's fine art' in the context of electron beam systems refers to the meticulous design and engineering of the electron gun and optics, which are achieved through a deep understanding of physics and materials science, as well as the implementation of sophisticated control and feedback mechanisms." 
    } 
  ], 
} 
```
### Data Fields 

The dataset comprises the following fields: 

- `messages`: String representing a conversation in standard format.
- `id`: A numerical identifier.
```json
[
{"role": "system",  "content": "...."}, 
{"role": "user",  "content": "...."},
{"role": "assistant",  "content": "...."},
{"role": "user",  "content": "...."},
{"role": "assistant",  "content": "...."}, 
.... 
] 
```
To read the conversation use `json.loads()` 


---

## ⚠️ Limitations
- **Translation Quality:** Potential minor errors in automated translation with LLMs.
- **Coverage:** Limited to Orca / Wikipedia-derived content, which is general-purpose and not domain-specific. Our data curation methodology is extensible to other domains.  
- **Bias:** Not systematically audited for sociocultural/demographic biases  
- **Scope:** 13 Indic languages only  
- **Synthetic Nature**: As this data is fully synthetic, it may not fully reflect real-world distributions or generalize to all real-world cases.

---
## 💾 Dataset Structure
```
Updesh_beta
├── analytical_reasoning
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── brain_teaser
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── causal_reasoning
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── eng_Latn.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── creative_writing
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── eng_Latn.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── cultural_multihop_reasoning
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── eng_Latn.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── dialog_gen
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── eng_Latn.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── fermi
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── fs_cot_flow
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── logical_reasoning
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── eng_Latn.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── math
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── mcq
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── multihop_reasoning
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── eng_Latn.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── rc
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── summarization
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── eng_Latn.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── text_classification
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
├── translation_enxx
│   ├── asm_Beng.parquet
│   ├── ben_Beng.parquet
│   ├── guj_Gujr.parquet
│   ├── ...
└── translation_xxen
    ├── asm_Beng.parquet
    ├── ben_Beng.parquet
    ├── guj_Gujr.parquet
    ├── ...

17 directories, 228 files
```

## 📜 Transparency Note
### Audience  
Researchers, model developers, and the multilingual NLP community working on instruction-tuned models, particularly in Indic languages.

### Limitations  
- **Translation Artifacts**: Updesh contains translated data that may include translation errors not caught by automated quality checks.  
- **Source Limitations**: Updesh draws from Orca-Agent and Wikipedia, meaning it inherits their limitations in topic coverage and style.  
- **Language Coverage**: It only includes 13 Indic languages, excluding others spoken in the region.  
- **Bias & Representativeness**: Updesh has not been systematically evaluated for sociocultural, economic, or linguistic biases.  
- **Safety & Reliability**: Updesh is not suited for use in high-stakes applications (e.g., legal, healthcare, finance).  
- **Commercial Use**: Updesh is released for research purposes only and is not intended for commercial deployment without further validation.  
- **Web Links**: Updesh is not believed to contain external links, but any such links, if present, are outside the control of the authors.  
- **Safety Evaluations**: No adversarial safety testing (e.g., harmful content checks) has been conducted.

### Best Practices for Use  
- Validate models trained on Updesh with downstream evaluation and human review before real-world use.  
- Consider additional Responsible AI checks, especially when adapting for underrepresented groups.  
- Be cautious of potential biases introduced during translation and generation.  
- Ensure compliance with local data regulations and ethical guidelines when using this dataset.  
- Use in combination with other multilingual benchmarks for broader generalization.

### Future Updates  
We welcome community feedback and plan to iteratively improve the dataset. Please contact the authors if you observe any problematic data or have suggestions.

### Out of Scope Uses  
- Training LLMs in non-Indic languages not included in the dataset.  
- Deployment in commercial or production systems without rigorous evaluation.  
- Use in high-risk or regulated domains (e.g., healthcare, legal, financial decision-making).

---

##  📜 License
- We release this data under the [Microsoft Research License](https://huggingface.co/datasets/microsoft/Updesh_beta/blob/main/LICENSE.md). 
- **By using the materials, you accept the terms**. 

---

## 📬 Contact
- Authors: [Varun Gumma*](mailto:varun230999@gmail.com), [Sanchit Ahuja*](mailto:sanchitahuja205@gmail.com), [Pranjal A. Chitale*](mailto:pranjalchitale@gmail.com), [Deepthi Sudharsan](mailto:deepthi.sudharsan@gmail.com), [Prashant Kodali](mailto:kodali.prashant@gmail.com), [Manan Uppadhyay](mailto:mananuppadhyay@gmail.com)
- Corresponding Authors: [Kalika Bali](mailto:kalikab@microsoft.com), [Sunayana Sitaram](mailto:sunayana.sitaram@microsoft.com)
- HF Repository: [Tanuja Ganu](mailto:Tanuja.Ganu@microsoft.com)

---




##  📖  Citation
If you use this dataset, please cite our [paper](https://arxiv.org/abs/2509.21294):
```bibtex
@misc{chitale2026updeshsynthesizinggroundedinstruction,
      title={UPDESH: Synthesizing Grounded Instruction Tuning Data for 13 Indic}, 
      author={Pranjal A. Chitale and Varun Gumma and Sanchit Ahuja and Prashant Kodali and Manan Uppadhyay and Deepthi Sudharsan and Sunayana Sitaram},
      year={2026},
      eprint={2509.21294},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.21294}, 
}
```