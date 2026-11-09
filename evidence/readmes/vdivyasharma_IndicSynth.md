---
license: cc-by-nc-4.0
configs:
- config_name: Bengali
  data_files:
  - split: train
    path: Bengali/train-*
- config_name: Gujarati
  data_files:
  - split: train
    path: Gujarati/train-*
- config_name: Hindi
  data_files:
  - split: train
    path: Hindi/train-*
- config_name: Kannada
  data_files:
  - split: train
    path: Kannada/train-*
- config_name: Malayalam
  data_files:
  - split: train
    path: Malayalam/train-*
- config_name: Marathi
  data_files:
  - split: train
    path: Marathi/train-*
- config_name: Odia
  data_files:
  - split: train
    path: Odia/train-*
- config_name: Punjabi
  data_files:
  - split: train
    path: Punjabi/train-*
- config_name: Sanskrit
  data_files:
  - split: train
    path: Sanskrit/train-*
- config_name: Tamil
  data_files:
  - split: train
    path: Tamil/train-*
- config_name: Telugu
  data_files:
  - split: train
    path: Telugu/train-*
- config_name: Urdu
  data_files:
  - split: train
    path: Urdu/train-*
dataset_info:
- config_name: Bengali
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 26636977797.52
    num_examples: 83448
  download_size: 33644253977
  dataset_size: 26636977797.52
- config_name: Gujarati
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 35729511328.708
    num_examples: 118778
  download_size: 50811268801
  dataset_size: 35729511328.708
- config_name: Hindi
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 53003219701.92
    num_examples: 205938
  download_size: 56012925652
  dataset_size: 53003219701.92
- config_name: Kannada
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 45376904249.101
    num_examples: 115023
  download_size: 68372746210
  dataset_size: 45376904249.101
- config_name: Malayalam
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 15637888779.776
    num_examples: 34128
  download_size: 24407793288
  dataset_size: 15637888779.776
- config_name: Marathi
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 71754219535.2
    num_examples: 130150
  download_size: 42561790240
  dataset_size: 71754219535.2
- config_name: Odia
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: string
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 16945788457.908
    num_examples: 52236
  download_size: 23671968893
  dataset_size: 16945788457.908
- config_name: Punjabi
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 66672910244.46
    num_examples: 248354
  download_size: 100577772676
  dataset_size: 66672910244.46
- config_name: Sanskrit
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 197955155096.904
    num_examples: 377504
  download_size: 167171842242
  dataset_size: 197955155096.904
- config_name: Tamil
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 85162574185.912
    num_examples: 282312
  download_size: 148502748897
  dataset_size: 85162574185.912
- config_name: Telugu
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 64247424400.08
    num_examples: 169896
  download_size: 91708786871
  dataset_size: 64247424400.08
- config_name: Urdu
  features:
  - name: audio
    dtype: audio
  - name: Generative Model
    dtype: string
  - name: Source Speaker_ID
    dtype: float64
  - name: Target Speaker ID
    dtype: int64
  - name: Gender
    dtype: string
  - name: Source Reference Audio
    dtype: string
  - name: Target Reference Audio
    dtype: string
  - name: TTS Transcript
    dtype: string
  splits:
  - name: train
    num_bytes: 23993474813.016
    num_examples: 94898
  download_size: 37773964000
  dataset_size: 23993474813.016
tags:
- indian speech
- indian languages
- synthetic speech
- deepfake
- audio deepfake detection
- indian deepfake detection
- anti-spoofing
- text-to-speech
- tts
- voice cloning
- voice conversion
- vc
- add
- fake
- speech
- low-resource languages
- multilingual
- asv
- sv
- speaker verification
- linguistic bias
- gender
- bias
- generalizable
language:
- bn
- gu
- hi
- kn
- ml
- mr
- or
- pa
- sa
- ta
- te
- ur
task_categories:
- audio-classification
- text-to-speech
- automatic-speech-recognition
pretty_name: IndicSynth
---

# IndicSynth: Indian Multilingual Audio Deepfake Detection & Anti-Spoofing Dataset

*A Large-Scale Multilingual Synthetic Speech Dataset for Low-Resource Indian Languages to facilitate audio deepfake detection and anti-spoofing research*

**🏆 Outstanding Paper Award, ACL 2025**

---

## 🧠 Overview

**IndicSynth** is a novel multilingual synthetic speech dataset designed to advance multilingual **audio deepfake detection (ADD)** and **anti-spoofing** research. It covers **12 low-resource Indian languages** and provides both **mimicry** and **diversity** subsets.

- 4,000+ hours of synthetic audio  
- 12 languages: Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Sanskrit, Tamil, Telugu, Urdu  
- Useful for:
  
   1. Multilingual audio deepfake detection (ADD) research or mitigating linguistic biases in audio deepfake detection systems
   2. Enhancing the robustness of speaker verification (SV) systems against spoofing (impersonation) attacks and developing anti-spoofing solutions
   3. Cross-lingual or gender bias studies in speech synthesis and recognition systems

---
## 📂 Dataset Structure

Each language folder contains:

<pre>  
IndicSynth/
├── Bengali/
│ ├── audio/ # All .wav files (synthetic clips)
│ └── metadata.csv # Metadata for all synthetic clips
├── Gujarati/
│ ├── audio/
│ └── metadata.csv
</pre>
Each 'metadata.csv' includes:
- Generative Model (xtts_v2 / vits / freevc24)
- Speaker IDs
- Gender
- Transcript (if applicable)
- File path to synthetic audio

**Bona fide audios**: The bona fide source and target speech samples referenced in IndicSynth metadata are drawn from the IndicSUPERB dataset. Please refer to the official repository for details: https://github.com/AI4Bharat/indicSUPERB.


📝 **Note on Transcripts in Metadata:**
The transcripts included in the metadata.csv files represent the intended text prompts used during synthetic speech generation via TTS models. We provide these transcripts to enable future explorations, but do not guarantee perfect alignment with the generated audio. If you intend to use IndicSynth for speech-to-text or similar tasks, we strongly recommend conducting careful human evaluation with proficient native speakers of the respective languages.

---
## ⚙️ IndicSynth Generation?
Synthetic data was generated using:

| Model      | Type      | Transcript | Fine-Tuned |
|------------|-----------|------------|-------------|
| xtts_v2  | TTS       | Yes        | Yes (for 10 languages) |
| vits     | TTS       | Yes        | No          |
| freevc24 | VC        | No         | No          |

- **Mimicry subset**: For anti-spoofing research
- **Diversity subset**: Contains diverse set of realistic synthetic voices for multilingual audio deepfake detection research
  
For more details, please see the Table 1 and Section 3 of our paper: https://aclanthology.org/2025.acl-long.1070.pdf

---

## 📦 Access the Dataset

You can load data in a specific target language using the following code:

```python

import os
import soundfile as sf
from datasets import load_dataset
from tqdm import tqdm
import pandas as pd

language = "Hindi" # Specify the target language here

# Load Dataset
dataset = load_dataset("vdivyasharma/IndicSynth", name=language, split="train") 

# Create target directory structure
output_dir = language
audio_dir = os.path.join(output_dir, "audio")
os.makedirs(audio_dir, exist_ok=True)

# Store metadata rows here
metadata_rows = []

# Loop through dataset and save each clip
for example in tqdm(dataset):
    audio_array = example["audio"]["array"]
    sampling_rate = example["audio"]["sampling_rate"]
    
    # Get filename
    original_name = example.get("file") or example.get("path") or example["audio"]["path"].split("/")[-1]
    
    # Save audio to audio/ subfolder
    audio_path = os.path.join("audio", original_name)  # relative path for metadata
    sf.write(os.path.join(output_dir, audio_path), audio_array, sampling_rate)
    
    # Store metadata row
    row = {k: v for k, v in example.items() if k != "audio"}
    row["file_name"] = audio_path
    metadata_rows.append(row)

# Save metadata to CSV
df = pd.DataFrame(metadata_rows)
df.to_csv(os.path.join(output_dir, "metadata.csv"), index=False)


```

---

## License
IndicSynth is released under the **CC BY-NC 4.0 License**.  
It is intended for **non-commercial, academic research only**.

## Citation
If you use IndicSynth, please cite the following papers:
<pre>@inproceedings{sharma-etal-2025-indicsynth,
    title = "{I}ndic{S}ynth: A Large-Scale Multilingual Synthetic Speech Dataset for Low-Resource {I}ndian Languages",
    author = "Sharma, Divya V  and
      Ekbote, Vijval  and
      Gupta, Anubha",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.1070/",
    pages = "22037--22060",
    ISBN = "979-8-89176-251-0"
}
</pre>
<pre>@article{IndicSuperb,
author = {Javed, Tahir and Bhogale, Kaushal and Raman, Abhigyan and Kumar, Pratyush and Kunchukuttan, Anoop and Khapra, Mitesh},
year = {2023},
month = {06},
pages = {12942-12950},
title = {IndicSUPERB: A Speech Processing Universal Performance Benchmark for Indian Languages},
volume = {37},
journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
doi = {10.1609/aaai.v37i11.26521}
}
</pre>
---

## 💬 Contact
For questions or feedback, please feel free to reach out at divyas@iiitd.ac.in.

## 🙏 Acknowledgments
- 🌍 ACL Diversity & Inclusion Subsidy for enabling in-person presentation at ACL 2025
- 🤝 HuggingFace for dataset hosting support
- 🎓SBILab and Infosys Centre for Artificial Intelligence (CAI) at IIIT-Delhi for their support