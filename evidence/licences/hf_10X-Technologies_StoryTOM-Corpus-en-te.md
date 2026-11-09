---
pretty_name: "StoryTOM Corpus: Paired English–Telugu Children's Stories"
license: cdla-sharing-1.0
language:
- en
- te
task_categories:
- text-generation
- translation
tags:
- storytom
- tom
- task-oriented-model
- tinystories
- children-stories
- parallel-corpus
- machine-translated
- telugu
size_categories:
- 1M<n<10M
configs:
- config_name: default
  data_files:
  - split: train
    path: "data/train-*.parquet"
  - split: validation
    path: "data/validation-*.parquet"
  - split: test
    path: "data/test-*.parquet"
---

# StoryTOM Corpus: Paired English–Telugu Children's Stories

The StoryTOM Corpus contains about 2.17 million children's stories, each in English and in Telugu machine translation. It is the training and evaluation data for **StoryTOM**, the first release of **TOM (Task-Oriented Models)**, and for the research paper *"Same Stories, Different Language: A Controlled Comparison of Tiny English and Telugu Language Models."*

**TOM = Task-Oriented Model:** a model trained from scratch for a single task. TOM is unrelated to Theory of Mind (ToM).

## Dataset summary

- **Content:** short, simple synthetic children's stories.
- **Languages:** English (original) and Telugu (machine translation of each English story).
- **Pairing:** every record holds the same story in both languages, so English and Telugu models can be trained and compared on exactly the same content.
- **Source:** the English stories come from TinyStories V2 (Eldan and Li, 2023).
- **Translation:** Telugu translations were generated with Gemma 4 E2B; 20 stories were translated with ChatGPT.

## Dataset structure

### Fields

| Field | Description |
|---|---|
| `id` | Unique story identifier |
| `en` | Original English story (TinyStories V2) |
| `te` | Telugu translation of the same story |
| `translator` | Which system produced the Telugu text: `gemma-4-e2b` or `chatgpt` |

### Splits

| Split | Story pairs | Source | Translator counts |
|---|---|---|---|
| `train` | 2,125,871 | TinyStories V2 training data | gemma-4-e2b: 2,125,851 · chatgpt: 20 |
| `validation` | 21,974 | TinyStories V2 validation file | gemma-4-e2b: 21,974 |
| `test` | 21,473 | 1% of the training pool, held out with a fixed random seed | gemma-4-e2b: 21,473 |

- The training pool contained 2,147,344 pairs; the test split was taken from it, and the rest forms the training split.
- No story appears in more than one split.
- In the paper, story pairs longer than the models' 544-token context in either language were excluded from scoring (179 validation and 178 test pairs). They are **included** in this dataset.

## How the dataset was made

1. **Source.** English stories were taken from TinyStories V2 (Hugging Face: `roneneldan/TinyStories`, revision `f54c09fd23315a6f9c86f9dc80f725de7d8f9c64`).
2. **Translation.** Each story was translated into Telugu with **Gemma 4 E2B** through Amazon Bedrock (model identifier `google.gemma-4-e2b`, temperature 0.2).
3. **Filtering.** An automatic script-based filter checked each translation; about **21%** of translations failed and were removed. Removed stories are not in either language of this dataset.
4. **ChatGPT subset.** For **20** stories whose Gemma translation failed the filter, a Telugu translation was produced manually in the ChatGPT interface, using the same instructions (model version not recorded). These 20 stories are in the training split and are marked `chatgpt` in the `translator` field.
5. **Splitting.** 1% of the training pool was held out as the test split with a fixed random seed. The validation split is the translated TinyStories V2 validation file.

The filter kept a translation only if the model finished its answer, it had at least 50 characters, at least 97% of its letters were Telugu script, it contained no Latin letters and no letters of any other script, its length was between half and twice the length of the English story, and it showed no repetition loops (repeated word sequences) beyond those in the English story. A translation identical to one already accepted was also removed.

## Known issues and limitations

- **Machine translation.** The Telugu text is machine-translated, not written by native speakers. It carries the translation model's errors and style and may differ from naturally written Telugu.
- **Gender agreement for named animals.** In an automatic audit of training samples, human characters received consistent gender agreement in Telugu, but **named male animals were translated inconsistently**, sometimes with masculine and sometimes with non-masculine verb forms (see the paper, Section 5.3).
- **Synthetic, simple content.** The stories are synthetic and written for young children. They cover a narrow range of vocabulary and topics.
- **Filtering bias.** Removing about 21% of translations may have removed some kinds of stories more than others.

## Intended use

- Research on language models, cross-language comparison, translation quality, and small-model training.
- Training and evaluating small story models such as StoryTOM.

This dataset is not intended as a reference for correct or natural Telugu.

## License

This dataset is released under the **Community Data License Agreement – Sharing, Version 1.0 (CDLA-Sharing-1.0)**. The full license text is in the `LICENSE` file.

- You may use, modify and share this data.
- **If you publish this data or a modified version of it, you must do so under CDLA-Sharing-1.0.**

**Credits:**
- English stories: **TinyStories** (Eldan and Li, 2023), released under CDLA-Sharing-1.0: https://huggingface.co/datasets/roneneldan/TinyStories
- Telugu translations: generated with **Gemma 4 E2B** (Google), released under the Apache 2.0 license. 20 stories were translated with **ChatGPT**.

## Related resources

- StoryTOM models and collections: https://huggingface.co/collections/10X-Technologies/same-stories-different-language-6ada28b2050b13239f31737f
- Paper: the arXiv link will be added here when the paper is published.

## Citation

If you use this dataset, please cite the TinyStories paper and our paper.

```bibtex
@article{eldan-li-2023-tinystories,
  title   = {{TinyStories}: How Small Can Language Models Be and Still Speak Coherent {English}?},
  author  = {Ronen Eldan and Yuanzhi Li},
  journal = {arXiv preprint arXiv:2305.07759},
  year    = {2023}
}
```

The BibTeX for our paper will be added here when the arXiv number is available.

## Contact

10X Technologies (Pikachu Global Technologies Pvt. Ltd.) · manibhavan@10xtechnologies.tech
