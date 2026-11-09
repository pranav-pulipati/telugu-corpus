---
license: mit
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6841289965
    num_examples: 1352251
  - name: test
    num_bytes: 263979906
    num_examples: 48607
  download_size: 2661318672
  dataset_size: 7105269871
task_categories:
- text-generation
language:
- te
---