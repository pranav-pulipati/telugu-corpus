---
license: cc-by-4.0
task_categories:
  - automatic-speech-recognition
  - audio-classification
language:
  - hi
  - te
  - or
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: benchmark.parquet
---

# Agri STT Benchmarking Dataset

10,808 farmer voice queries in Hindi, Telugu and Odia, with reference transcripts, for benchmarking automatic speech recognition in agricultural contexts. The audio is included in this repository.

Every recording is a smallholder farmer speaking a question to [Farmer.Chat](https://farmerchat.digitalgreen.org/), an AI advisory service run by [Digital Green](https://www.digitalgreen.org/). Reference transcripts were produced by human annotators. Nothing here is read from a script or recorded in a studio, so the audio carries the noise, overlap and dialect of real field conditions.

## Contents

- `audio/` - 10,808 OGG files, numbered `00001.ogg` upward and split across subdirectories of 1,000 (`audio/000/`, `audio/001/`, and so on). Use the `Filename` column rather than assembling the path yourself.
- `benchmark.parquet` - all three languages in one table
- `Agri_Benchmark_Hindi.csv` - Hindi only, 4,576 rows
- `Agri_Benchmark_Telugu.csv` - Telugu only, 4,027 rows
- `Agri_Benchmark_Oriya.csv` - Odia only, 2,205 rows

| Column | Description |
|--------|-------------|
| `Filename` | Path to the audio file within this repository |
| `Language` | BCP-47 language code of the utterance |
| `reference` | Human reference transcript |

## Splits

| Language | Code | Utterances |
|---|---|---:|
| Hindi | `hi` | 4,576 |
| Telugu | `te` | 4,027 |
| Odia | `or` | 2,205 |
| **Total** | | **10,808** |

## Usage

```python
from datasets import load_dataset
from huggingface_hub import snapshot_download

ds = load_dataset("DigiGreen/Agri_STT_Benchmarking_Dataset", split="train")
root = snapshot_download("DigiGreen/Agri_STT_Benchmarking_Dataset", repo_type="dataset")

row = ds[0]
audio_path = f'{root}/{row["Filename"]}'
print(row["Language"], row["reference"])
```

## Privacy

Earlier versions of this dataset delivered the audio as links to a cloud storage bucket, and the filename in each link carried an internal message identifier. Both are gone. The audio now ships from this repository under sequential filenames that carry no information about the speaker, the conversation, or the original record. The `Filename` column keeps its name and now holds a path inside this repository.

Every reference transcript was screened for personal information by two language models independently, the second reviewing everything the first flagged plus a blind sample of what it cleared. 56 recordings were removed because the speech contained personal information: a person's name, a village or landmark specific enough to narrow down a household, a phone or ID number, money tied to a named person, a medical detail, or a private domestic matter.

| Reason for removal | Recordings |
|---|---:|
| place name | 31 |
| person name | 16 |
| health | 9 |
| household | 6 |
| money | 1 |
| phone | 1 |

Two limits are worth stating rather than leaving implied. The screening read the transcripts, not the audio, and a recording holds everything its transcript holds plus whatever the annotator left out. And a voice is biometric whatever the words are: these are real people, identifiable to anyone who knows them, which is the nature of a speech corpus rather than a defect in this one. Treat the recordings as personal data. If you find something that should not be here, please open a discussion and it will be removed.

Some recordings also capture speech that is not the farmer's question, such as a second person in the room or a field agent explaining the app. Where that speech carried nothing identifying it was left in, because it is part of the real acoustic conditions this benchmark is meant to measure. Expect it when scoring against the references.

## Changelog

**July 2026.** Audio moved into the repository as `audio/00001.ogg` upward; the `Filename` column now holds that path instead of a storage URL. Added `benchmark.parquet` covering all three languages. Screened every transcript for personal information and removed 56 recordings.

## Citation

The accompanying paper, *Benchmarking Automatic Speech Recognition for Indian Languages in Agricultural Contexts*, is included in this repository ([arXiv:2602.03868](https://arxiv.org/abs/2602.03868)).

```bibtex
@dataset{digigreen_agri_stt_2026,
  title={Agri STT Benchmarking Dataset},
  author={Digital Green},
  year={2026},
  url={https://huggingface.co/datasets/DigiGreen/Agri_STT_Benchmarking_Dataset},
  license={CC-BY-4.0}
}
```

## License

Released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the data for any purpose, provided you give appropriate credit to Digital Green.
