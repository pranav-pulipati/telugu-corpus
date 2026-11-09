---
license: cc-by-4.0
pretty_name: indic-align
language:
- as
- bn
- gu
- en
- hi
- kn
- ml
- mr
- ne
- or
- pa
- sa
- ta
- te
- ur
task_categories:
- text-generation
dataset_info:
- config_name: Indic_ShareLlama
- config_name: Dolly_T
- config_name: OpenAssistant_T
- config_name: WikiHow
- config_name: IndoWordNet
- config_name: Anudesh
- config_name: Wiki_Conv
- config_name: Wiki_Chat
- config_name: IndicAlign-Toxic
- config_name: HHRLHF_T
- config_name: Toxic_Matrix
configs:
- config_name: Indic_ShareLlama
  data_files: indicalign-instruct/indicsharellama/*
- config_name: Dolly_T
  data_files: indicalign-instruct/dolly/*
- config_name: OpenAssistant_T
  data_files: indicalign-instruct/oasst/*
- config_name: WikiHow
  data_files: indicalign-instruct/wikihow/*
- config_name: IndoWordNet
  data_files: indicalign-instruct/indowordnet/*
- config_name: Anudesh
  data_files: indicalign-instruct/anudesh/*
- config_name: Wiki_Conv
  data_files: indicalign-instruct/wiki_conv/*
- config_name: Wiki_Chat
  data_files: indicalign-instruct/wiki_chat/*
- config_name: HHRLHF_T
  data_files: indicalign-toxic/hhrlhf/*
- config_name: Toxic_Matrix
  data_files: indicalign-toxic/toxicmatrix/*
size_categories:
- 100M<n<1B
---

# IndicAlign

A diverse collection of Instruction and Toxic alignment datasets for 14 Indic Languages. The collection comprises of:
- **IndicAlign - Instruct**
  - Indic-ShareLlama
  - Dolly-T
  - OpenAssistant-T
  - WikiHow
  - IndoWordNet
  - Anudesh
  - Wiki-Conv
  - Wiki-Chat
- **IndicAlign - Toxic**
  - HHRLHF-T
  - Toxic-Matrix
 
We use IndicTrans2 ([Gala et al., 2023](https://openreview.net/forum?id=vfT4YuzAYA)) for the translation of the datasets. 
We recommend the readers to check out our paper [on Arxiv](https://arxiv.org/abs/2403.06350) for detailed information on the curation process of these collections.

## Dataset Summaries

**IndicShareLlama**- Collection of first user prompts from [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) along with responses from [Llama2-70B-Chat](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) model.

**Dolly-T**- Translated and Romanised version of [Dolly-15K](https://huggingface.co/datasets/databricks/databricks-dolly-15k)

**OpenAssistant-T**- Translated and Romanised version of [OpenAssistant v1](https://huggingface.co/datasets/OpenAssistant/oasst1)

**WikiHow** - Translated and Romanised version of [WikiHow](https://huggingface.co/datasets/ai4bharat/indic-instruct-data-v0.1)

**IndoWordNet**- Novel dataset created by converting the entried of [IndoWordNet](https://pypi.org/project/pyiwn/) to Instruction-Response pairs in 18 Indic languages.

**Anudesh**- A crowd-sourced collection of prompts accompanied by responses generated from the Llama2-70B-Chat model.

**Wiki-Conv**- Collection of short, to-the-point conversations on Wikipedia passages and Wiki-Infoboxes created using Llama2-70B-Chat model.

**Wiki-Chat**- Collection of long, open conversations on Wikipedia passages, created by simulating conversations between a User and an Assistant models.

**HHRLHF-T**- Collection of "toxic" prompts from [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf) with refusals from Llama2-70B-Chat model.

**Toxic-Matrix**- A novel "synthetic" dataset with toxic prompts generated using [Mistral-7B Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) and non-toxic responses/refusals using Llama2-70B-Chat model.


## Dataset Statistics

| Component         | #Examples | Avg. Turns | Avg. Inst. Len | Avg. Out. Len |
|-------------------|-----------|------------|----------------|---------------|
| Indic ShareLlama  | 21.1k     | 1          | 60.45          | 267.98        |
| Dolly-T           | 15.0k     | 1          | 12.34          | 59.38         |
| OpenAssistant-T   | 19.9k     | 2.98       | 25.72          | 136.37        |
| WikiHow           | 20.3k     | 1          | 43.85          | 327.95        |
| IndoWordNet       | 74,272.2k | 1          | 19.74          | 14.84         |
| Anudesh           | 36.8k     | 1.58       | 12.4           | 149.28        |
| Wiki-Conv         | 144k      | 9.14       | 7.09           | 11.22         |
| Wiki-Chat         | 202k      | 2.8        | 23             | 227.75        |
| HH-RLHF-T         | 32.6k     | 1          | 14.11          | 64.88         |
| Toxic Matrix      | 90.3k     | 1          | 33.68          | 89.64         |



## Citation

```bibtex
@article{khan2024indicllmsuite,
  title   = {IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages},
  author  = {Mohammed Safi Ur Rahman Khan and Priyam Mehta and Ananth Sankar and Umashankar Kumaravelan and Sumanth Doddapaneni and Suriyaprasaad G and Varun Balan G and Sparsh Jain and Anoop Kunchukuttan and Pratyush Kumar and Raj Dabre and Mitesh M. Khapra},
  year    = {2024},
  journal = {arXiv preprint arXiv: 2403.06350}
}
```