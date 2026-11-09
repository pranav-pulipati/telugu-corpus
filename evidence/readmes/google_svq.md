---
license: cc-by-4.0
task_categories:
- question-answering
- automatic-speech-recognition
- text-retrieval
- text-ranking
- audio-classification
- feature-extraction
language:
- ar
- bn
- en
- fi
- gu
- hi
- id
- ja
- kn
- ko
- ml
- mr
- ru
- sw
- ta
- te
- ur
pretty_name: Simple Voice Questions
size_categories:
- 100K<n<1M
configs:
- config_name: audio
  features:
  - name: utt_id
    dtype: string
  - name: waveform
    dtype:
      audio:
        sampling_rate: 16000
        decode: false
  - name: locale
    dtype: string
  - name: speaker_id
    dtype: string
  - name: speaker_age
    dtype: int32
  - name: speaker_gender
    dtype: string
  - name: environment
    dtype: string
  - name: text
    dtype: string
  - name: candidate_salient_terms
    sequence:
      dtype: string
  - name: candidate_salient_terms_timestamps
    sequence:
      sequence:
        dtype: float64
  - name: candidates
    sequence:
      dtype: string
  - name: "classifications/speaker_gender"
    dtype: bool
  - name: "clusterings/speaker_age"
    dtype: bool
  - name: "clusterings/speaker_gender"
    dtype: bool
  - name: "clusterings/speaker_id"
    dtype: bool
  - name: page_id_cross_lang
    dtype: string
  - name: page_id_in_lang
    dtype: string
  - name: page_title_cross_lang
    dtype: string
  - name: page_title_in_lang
    dtype: string
  - name: passage_id_cross_lang
    dtype: string
  - name: passage_id_in_lang
    dtype: string
  - name: passage_text_cross_lang
    dtype: string
  - name: passage_text_in_lang
    dtype: string
  - name: "reasonings/span_cross_lang"
    dtype: bool
  - name: "reasonings/span_in_lang"
    dtype: bool
  - name: "rerankings/query"
    dtype: bool
  - name: "rerankings/salient_term"
    dtype: bool
  - name: "retrievals/document_cross_lang"
    dtype: bool
  - name: "retrievals/document_in_lang"
    dtype: bool
  - name: "retrievals/passage_cross_lang"
    dtype: bool
  - name: "retrievals/passage_in_lang"
    dtype: bool
  - name: "segmentation_selections/salient_term"
    dtype: bool
  - name: "segmentations/salient_term"
    dtype: bool
  - name: span_context_id_cross_lang
    dtype: string
  - name: span_context_id_in_lang
    dtype: string
  - name: span_context_text_cross_lang
    dtype: string
  - name: span_context_text_in_lang
    dtype: string
  - name: span_context_title_cross_lang
    dtype: string
  - name: span_context_title_in_lang
    dtype: string
  - name: span_cross_lang
    dtype: string
  - name: span_in_lang
    dtype: string
  - name: spans_cross_lang
    sequence:
      dtype: string
  - name: spans_in_lang
    sequence:
      dtype: string
  - name: "stabilities/speech"
    dtype: bool
  - name: topk_salient_terms
    sequence:
      dtype: string
  - name: topk_salient_terms_timestamps
    sequence:
      sequence:
        dtype: float64
  - name: transcript_truth
    dtype: string
  - name: "transcriptions/speech"
    dtype: bool
  data_files:
  - split: test
    path: 2.0.0/utts_*.parquet
- config_name: audio_en_us_clean
  features:
  - name: utt_id
    dtype: string
  - name: waveform
    dtype:
      audio:
        sampling_rate: 16000
        decode: false
  - name: locale
    dtype: string
  - name: speaker_id
    dtype: string
  - name: speaker_age
    dtype: int32
  - name: speaker_gender
    dtype: string
  - name: environment
    dtype: string
  - name: text
    dtype: string
  - name: candidate_salient_terms
    sequence:
      dtype: string
  - name: candidate_salient_terms_timestamps
    sequence:
      sequence:
        dtype: float64
  - name: candidates
    sequence:
      dtype: string
  - name: "classifications/speaker_gender"
    dtype: bool
  - name: "clusterings/speaker_age"
    dtype: bool
  - name: "clusterings/speaker_gender"
    dtype: bool
  - name: "clusterings/speaker_id"
    dtype: bool
  - name: page_id_cross_lang
    dtype: string
  - name: page_id_in_lang
    dtype: string
  - name: page_title_cross_lang
    dtype: string
  - name: page_title_in_lang
    dtype: string
  - name: passage_id_cross_lang
    dtype: string
  - name: passage_id_in_lang
    dtype: string
  - name: passage_text_cross_lang
    dtype: string
  - name: passage_text_in_lang
    dtype: string
  - name: "reasonings/span_cross_lang"
    dtype: bool
  - name: "reasonings/span_in_lang"
    dtype: bool
  - name: "rerankings/query"
    dtype: bool
  - name: "rerankings/salient_term"
    dtype: bool
  - name: "retrievals/document_cross_lang"
    dtype: bool
  - name: "retrievals/document_in_lang"
    dtype: bool
  - name: "retrievals/passage_cross_lang"
    dtype: bool
  - name: "retrievals/passage_in_lang"
    dtype: bool
  - name: "segmentation_selections/salient_term"
    dtype: bool
  - name: "segmentations/salient_term"
    dtype: bool
  - name: span_context_id_cross_lang
    dtype: string
  - name: span_context_id_in_lang
    dtype: string
  - name: span_context_text_cross_lang
    dtype: string
  - name: span_context_text_in_lang
    dtype: string
  - name: span_context_title_cross_lang
    dtype: string
  - name: span_context_title_in_lang
    dtype: string
  - name: span_cross_lang
    dtype: string
  - name: span_in_lang
    dtype: string
  - name: spans_cross_lang
    sequence:
      dtype: string
  - name: spans_in_lang
    sequence:
      dtype: string
  - name: "stabilities/speech"
    dtype: bool
  - name: topk_salient_terms
    sequence:
      dtype: string
  - name: topk_salient_terms_timestamps
    sequence:
      sequence:
        dtype: float64
  - name: transcript_truth
    dtype: string
  - name: "transcriptions/speech"
    dtype: bool
  data_files:
  - split: test
    path: 2.0.0/utts_en_us_clean.parquet
- config_name: document_retrieval_cross_lang_small_index
  data_files:
  - split: test
    path: 2.0.0/document_retrieval_cross_lang_small_index.parquet
- config_name: document_retrieval_in_lang_small_index
  data_files:
  - split: test
    path: 2.0.0/document_retrieval_in_lang_small_index.parquet
- config_name: passage_retrieval_cross_lang_index
  data_files:
  - split: test
    path: 2.0.0/passage_retrieval_cross_lang_index.parquet
- config_name: passage_retrieval_in_lang_index
  data_files:
  - split: test
    path: 2.0.0/passage_retrieval_in_lang_index.parquet
- config_name: span_retrieval_cross_lang_index
  data_files:
  - split: test
    path: 2.0.0/span_retrieval_cross_lang_index.parquet
- config_name: span_retrieval_in_lang_index
  data_files:
  - split: test
    path: 2.0.0/span_retrieval_in_lang_index.parquet
---
# Simple Voice Questions

Simple Voice Questions (SVQ) is a set of short audio questions recorded in 26 locales across 17 languages under multiple audio conditions. It serves as a core evaluation componenet for **Massive Sound Embedding Benchmark (MSEB)**.

## Technical Specifications

| Feature | Details |
| :--- | :--- |
| **Locales** | 26 |
| **Languages** | 17 |
| **Total Speakers** | ~700 (Capped at 250 recordings per speaker) |
| **Audio Conditions** | Clean, Background Speech, Media, Traffic Noise |
| **Gender Classes** | Female, Male, Non-binary, No answer |

---

## Data Collection

Speakers were presented with recording instructions specifying the recording environment and text query to be recorded.
They recorded using their own phones or tablets under four conditions:
- clean: Record in quiet environment
- background speech noise: Record while audio from sources like podcasts, talk radio, or YouTube plays on a separate device (e.g., TV, tablet, computer, or another phone) at a normal listening volume, ensuring it is audible in the recording
- traffic noise: Record while speaker is a passenger within a moving vehicle. This includes various forms of transport like buses, trains, and cars (where someone else is driving)
- media noise: Record while background media (music, TV, movies, etc.) is playing on a separate device (TV, tablet, computer, or phone). The playback volume should be a normal listening level,sufficient to be audible in the recording.

In all conditions, speakers were instructed to minimize other background noise (like fans or conversations), hold their phone naturally, avoid extra sounds (like clicks or taps), use wired headphones if applicable, and speak naturally and expressively with emotion.

The query’s text comes from validation and test sets of the XTREME-UP’s retrieval and question answering benchmark datasets. The XTREME-UP dataset is a collection of TYDI QA datasets which are question answering datasets covering 11 typologically diverse languages and the professional translation of the cross-lingual open-retrieval question answering (XOR QA) dataset into 23 Indic languages.

The audio queries were approximately uniformly recorded across the four environmental conditions. To ensure speaker diversity, we attempted to cap the number of recordings per speaker at 250. This resulted in a total of 700unique speakers. We collected speaker gender information in four classes: female, male, non_binary, and no_answer. In addition, speakers were askedto report their age.

## Splits

The audio data in this release is presented as a single, comprehensive collection, rather than being pre-divided into training, validation, or testing subsets.
This decision stems directly from the design of the data acquisition process.
Specifically, text prompts and recording environments were randomly allocated across the speaker cohort.
While this approach promotes a rich variety of conditions, it introduces a complexity for traditional data splitting:
creating partitions that ensure no overlap of speakers and no overlap of text material between splits (a common best practice)
would lead to a substantial data reduction, estimated at around 40% of the total recordings.

The primary goal guiding this release strategy is to maximize the utility and volume of the data available to users.
Therefore, to avoid this significant data loss and provide the fullest possible dataset, the data is released in its entirety
as an undivided evaluation set. Users intending to train models with this data will need to devise and implement their own
splitting strategies, keeping in mind the inherent trade-offs between data volume and strict speaker/text disjointness
if they attempt to replicate such conditions.

## Citation

If you use this dataset, please cite the MSEB paper:

```bibtex
@inproceedings{heigoldmassive,
title={Massive Sound Embedding Benchmark(MSEB)},
author={Heigold, Georg and Variani, Ehsan and Bagby, Tom and Allauzen, Cyril and Ma, Ji and Kumar, Shankar and Riley, Michael},
booktitle={The Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
}
```
