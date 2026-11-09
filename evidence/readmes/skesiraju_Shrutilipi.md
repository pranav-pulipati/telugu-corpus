---
license: cc-by-4.0
task_categories:
- automatic-speech-recognition
language:
- bn
- hi
- kn
- ml
- mr
- or
- ta
- te
size_categories:
- 1M<n<10M
---

# Dataset Card for Shrutilipi (Full Version)

<!-- Provide a quick summary of the dataset. -->

> ⚠️ Some of the audio samples in the original Shrutilipi were empty and they are present in this version. A new version without the empty audio samples will be updated soon.

This is a **full** and **unfiltered version** of the Shrutilipi dataset for languages: Bengali, Hindi, Kannada, Malayalam, Marathi, Odia, Tamil and Telugu - originally described in the paper: [Effectiveness of Mining Audio and Text Pairs from Public Data for Improving ASR Systems for Low-Resource Languages](https://arxiv.org/abs/2208.12666).
The data for Gujarati, Punjabi and Sanskrit will be uploaded later.

## Dataset Details

Since the dataset was automatically curated from broadcast audio, not all transcriptions are perfectly accurate. Each utterance includes an alignment quality score (see Section 3.3 of the paper) to help users filter data based on their quality requirements.

### Why This Version?

The previously available version [ai4bharat/Shrutilipi](https://huggingface.co/datasets/ai4bharat/Shrutilipi) on HuggingFace contains only a filtered subset of the original corpus. However, **the complete unfiltered dataset provides significant value for research and development**:

1. **Flexibility in Quality vs. Quantity Trade-offs**: Researchers can experiment with different alignment score thresholds (e.g., ≥80, ≥85, ≥90) to find optimal balances for their specific use cases. Lower thresholds provide more training data, while higher thresholds ensure better quality.

2. **Low-Resource Language Research**: For extremely low-resource languages, even lower-quality data can improve model performance. Having access to the full dataset enables researchers to explore weakly-supervised and semi-supervised learning approaches.

3. **Reproducibility**: This full version has been used in multiple published research works, making it essential for reproducibility:
   - [BUT Systems for IWSLT 2023 Marathi-Hindi Low Resource Speech Translation Task](https://aclanthology.org/2023.iwslt-1.19/) - Demonstrates use in speech translation systems
   - [End-to-End Speech Translation for Low-Resource Languages Using Weakly Labeled Data](https://www.isca-archive.org/interspeech_2025/pothula25_interspeech.html) - Shows effectiveness of weakly labeled data for speech translation

4. **Data Augmentation**: The lower-scored utterances can be used for data augmentation, semi-supervised learning, or as additional unlabeled data for self-supervised pre-training approaches.

By providing the full dataset with alignment scores, researchers can make informed decisions about data selection rather than being limited to a pre-filtered subset.


### Dataset Description

- **Curated by:** [AI4Bharat](https://ai4bharat.iitm.ac.in/)
- **Funded by:** Ministry of Electronics and Information Technology (MeitY), Government of India and Centre for Development of Advanced Computing (CDAC)
- **Language(s):** Bengali, Hindi, Kannada, Malayalam, Marathi, Odia, Tamil, Telugu (Gujarati, Punjabi, Sanskrit will be uploaded later.)
- **License:** CC-BY-4.0

### Dataset Sources

- **Paper:** [Effectiveness of Mining Audio and Text Pairs from Public Data for Improving ASR Systems for Low-Resource Languages](https://arxiv.org/pdf/2208.12666)
- **Original subset:** [ai4bharat/Shrutilipi](https://huggingface.co/datasets/ai4bharat/Shrutilipi) (this is the full version)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

The dataset is suitable for:
- Training and fine-tuning ASR models for Indian languages
- Low-resource speech recognition research
- Multilingual ASR model development
- Speech-to-text translation systems

Users can filter utterances by alignment score to control data quality vs. quantity trade-off.

### Out-of-Scope Use

- The dataset is sourced from radio broadcast news, so models trained on it may not generalize well to conversational speech, read speech, or other domains
- Since transcriptions are automatically generated with alignment scores, they may contain errors - not suitable for applications requiring 100% accuracy without manual verification
- Not suitable for speaker identification or verification tasks

## Dataset Structure

The dataset is organized as a DatasetDict with separate datasets for each language:

```python
DatasetDict({
    'bengali': Dataset({...}),
    'hindi': Dataset({...}),
    'kannada': Dataset({...}),
    'malayalam': Dataset({...}),
    'marathi': Dataset({...}),
    'odia': Dataset({...}),
    'tamil': Dataset({...}),
    'telugu': Dataset({...})
})
```

### Fields

- **utterance_id** (string): Unique identifier in format `{language}_{subdirectory}_{sent_index}`
- **audio** (Audio): Audio data at 16kHz sampling rate
- **text** (string): Transcription text in native script
- **score** (int32): Alignment quality score (0-100) - higher is better
- **language** (string): Language code (bn, hi, kn, ml, mr, or, ta, te)

All utterances belong to the `train` split (no dev/test splits provided).

### Usage

For loading and using the dataset:

```python
from datasets import load_dataset

# Load the dataset from hub - Telugu 
dataset = load_dataset("skesiraju/Shrutilipi", "telugu", streaming=True)

# If the datasets is already downloaded to disk - use the following
# from datasets import load_from_disk
# dataset = load_dataset("/path/to/Shrutilipi/telugu", keep_in_memory=False)

# Filter by alignment score (recommended: ≥85)
scores = dataset['score']  # Just the score column

# Find indices where score >= 85
high_quality_indices = [i for i, s in enumerate(scores) if s >= 85]

# Now select only those samples
high_quality = dataset.select(high_quality_indices)

# Access audio and text
sample = high_quality[0]
audio_array = sample['audio']['array']  # numpy array
sampling_rate = sample['audio']['sampling_rate']  # 16000 Hz
text = sample['text']
```

See the [original paper](https://arxiv.org/abs/2208.12666) for details on the mining and alignment methodology.

## Dataset Creation

### Curation Rationale

To create large-scale ASR training data for low-resource Indian languages by automatically mining and aligning audio-text pairs from publicly available broadcast content.

### Source Data

Radio broadcast news from All India Radio (AIR) stations across India, covering 11 Indian languages.

#### Data Collection and Processing

Audio and text pairs were automatically mined from public broadcast data using alignment techniques. Each utterance has an alignment quality score (0-100) computed as described in Section 3.3 of the paper. Audio is resampled to 16kHz mono format.

#### Who are the source data producers?

All India Radio (AIR) - Prasar Bharati (India's public service broadcaster)

### Annotations [optional]

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

Transcriptions were automatically generated using alignment techniques (not manually annotated). See the paper for details on the automatic mining and alignment process.

#### Who are the annotators?

N/A - Transcriptions are automatically generated, not manually annotated.

#### Personal and Sensitive Information

The dataset contains radio broadcast news which is public domain content. No personal or sensitive information is expected, though news content may reference public figures and events.

## Bias, Risks, and Limitations

- **Automatic transcriptions**: Since transcriptions are automatically generated, they may contain errors. The alignment score helps identify quality but doesn't guarantee accuracy
- **Domain bias**: Dataset is limited to broadcast news domain, which may not represent conversational or informal speech
- **Regional variations**: May not adequately represent all dialects and regional variations within each language
- **Quality variation**: Alignment scores vary (0-100), so users should filter based on their quality requirements

### Recommendations

- **Filter by score**: Users should experiment with different alignment score thresholds (e.g., ≥85 or ≥90) to balance data quality vs. quantity
- **Domain adaptation**: Consider fine-tuning on domain-specific data if deploying for non-news applications
- **Manual verification**: For high-stakes applications, manually verify a sample of transcriptions
- **Combine with other datasets**: Use alongside other ASR datasets for better coverage of speaking styles and domains

## Citation

**BibTeX:**

```bibtex
@inproceedings{bhogale2022effectiveness,
 author={Bhogale, Kaushal and Raman, Abhigyan and Javed, Tahir and Doddapaneni, Sumanth and Kunchukuttan, Anoop and Kumar, Pratyush and Khapra, Mitesh M.},
  booktitle={IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}, 
  title={Effectiveness of Mining Audio and Text Pairs from Public Data for Improving ASR Systems for Low-Resource Languages}, 
  year={2023},
  volume={},
  number={},
  pages={1-5},
  keywords={Training;Bridges;Atmospheric modeling;Optical character recognition;Speech recognition;Signal processing;Benchmark testing;Alignment;Low-Resource Languages},
  doi={10.1109/ICASSP49357.2023.10096933}}
```

**APA:**

Bhogale, K. S., et al. (2022). Effectiveness of Mining Audio and Text Pairs from Public Data for Improving ASR Systems for Low-Resource Languages. arXiv preprint arXiv:2208.12666.

## Dataset Card Authors

Santosh Kesiraju (kesiraju@fit.vutbr.cz)

## Dataset Card Contact

For questions or issues regarding this dataset, please contact:
- Santosh Kesiraju (kesiraju@fit.vutbr.cz)
- AI4Bharat team: https://ai4bharat.iitm.ac.in/