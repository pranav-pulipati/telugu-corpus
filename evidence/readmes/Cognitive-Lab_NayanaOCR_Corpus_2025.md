---
license: cc-by-nc-4.0
license_name: nayana-ocr-research-license
license_link: LICENSE.md
pretty_name: NayanaOCR Corpus 2025
language:
  - ar
  - bn
  - de
  - en
  - es
  - fr
  - gu
  - hi
  - it
  - ja
  - kn
  - ko
  - ml
  - mr
  - or
  - pa
  - ru
  - sa
  - ta
  - te
  - th
  - zh
multilinguality:
  - multilingual
language_creators:
  - machine-generated
annotations_creators:
  - machine-generated
task_categories:
  - image-to-text
  - visual-question-answering
  - image-text-to-text
task_ids:
  - multiple-choice-qa
  - closed-domain-qa
size_categories:
  - 1M<n<10M
source_datasets:
  - original
tags:
  - ocr
  - parallel-corpus
  - multilingual-parallel
  - cross-lingual
  - document-ai
  - document-understanding
  - document-analysis
  - multilingual
  - indic
  - indic-languages
  - low-resource-languages
  - vlm
  - vision-language-model
  - vqa
  - visual-question-answering
  - layout-analysis
  - bounding-box
  - synthetic-data
  - retrieval
  - nayana
paperswithcode_id: nayana-ocr
dataset_info:
- config_name: ar
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 32251897661.0
    num_examples: 45735
  download_size: 27973653719
  dataset_size: 32251897661.0
- config_name: bn
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 40197529965.0
    num_examples: 45735
  download_size: 37080372202
  dataset_size: 40197529965.0
- config_name: de
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 43560050637.0
    num_examples: 45735
  download_size: 40214753809
  dataset_size: 43560050637.0
- config_name: en
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        sequence: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 40341644513.0
    num_examples: 45735
  download_size: 37492877638
  dataset_size: 40341644513.0
- config_name: es
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 41298697550.0
    num_examples: 45735
  download_size: 37518697055
  dataset_size: 41298697550.0
- config_name: fr
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 42041691546.0
    num_examples: 45735
  download_size: 38585494503
  dataset_size: 42041691546.0
- config_name: gu
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 38668362592.0
    num_examples: 45735
  download_size: 35597322238
  dataset_size: 38668362592.0
- config_name: hi
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        sequence: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 40725011127.0
    num_examples: 45735
  download_size: 37592601136
  dataset_size: 40725011127.0
- config_name: it
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 41910804470.0
    num_examples: 45735
  download_size: 38451788872
  dataset_size: 41910804470.0
- config_name: ja
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 36080909756.0
    num_examples: 45735
  download_size: 32519562806
  dataset_size: 36080909756.0
- config_name: kn
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        sequence: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 42756469883.0
    num_examples: 45735
  download_size: 39726502251
  dataset_size: 42756469883.0
- config_name: ko
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 36386121775.0
    num_examples: 45735
  download_size: 33123200769
  dataset_size: 36386121775.0
- config_name: ml
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 44484045110.0
    num_examples: 45735
  download_size: 41486205192
  dataset_size: 44484045110.0
- config_name: mr
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 39057695885.0
    num_examples: 45735
  download_size: 35882976729
  dataset_size: 39057695885.0
- config_name: or
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 41357857942.0
    num_examples: 45735
  download_size: 38323671608
  dataset_size: 41357857942.0
- config_name: pa
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 39812643165.0
    num_examples: 45735
  download_size: 36707388972
  dataset_size: 39812643165.0
- config_name: ru
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 44510980243.0
    num_examples: 45735
  download_size: 40981126526
  dataset_size: 44510980243.0
- config_name: sa
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 40503563888.0
    num_examples: 45735
  download_size: 37345327352
  dataset_size: 40503563888.0
- config_name: ta
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 43202258433.0
    num_examples: 45735
  download_size: 40161750777
  dataset_size: 43202258433.0
- config_name: te
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 40875481317.0
    num_examples: 45735
  download_size: 37819541209
  dataset_size: 40875481317.0
- config_name: th
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 35696446028.0
    num_examples: 45735
  download_size: 32067484848
  dataset_size: 35696446028.0
- config_name: zh
  features:
  - name: jpg
    dtype: image
  - name: image_id.txt
    dtype: string
  - name: font_used.txt
    dtype: string
  - name: regions.json
    list:
    - name: bbox
      struct:
      - name: xmax
        dtype: int64
      - name: xmin
        dtype: int64
      - name: ymax
        dtype: int64
      - name: ymin
        dtype: int64
    - name: english_text
      dtype: string
    - name: layout_type
      dtype: string
    - name: region_id
      dtype: int64
    - name: translated_text
      dtype: string
  - name: vqa.json
    struct:
    - name: questions
      list:
      - name: answer
        dtype: string
      - name: options
        list: string
      - name: question
        dtype: string
      - name: type
        dtype: string
  - name: __key__
    dtype: string
  - name: __url__
    dtype: string
  splits:
  - name: train
    num_bytes: 40355796651.0
    num_examples: 45735
  download_size: 36972255157
  dataset_size: 40355796651.0
configs:
- config_name: ar
  data_files:
  - split: train
    path: ar/train-*
- config_name: bn
  data_files:
  - split: train
    path: bn/train-*
- config_name: de
  data_files:
  - split: train
    path: de/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
- config_name: gu
  data_files:
  - split: train
    path: gu/train-*
- config_name: hi
  data_files:
  - split: train
    path: hi/train-*
- config_name: it
  data_files:
  - split: train
    path: it/train-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
- config_name: kn
  data_files:
  - split: train
    path: kn/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: ml
  data_files:
  - split: train
    path: ml/train-*
- config_name: mr
  data_files:
  - split: train
    path: mr/train-*
- config_name: or
  data_files:
  - split: train
    path: or/train-*
- config_name: pa
  data_files:
  - split: train
    path: pa/train-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
- config_name: sa
  data_files:
  - split: train
    path: sa/train-*
- config_name: ta
  data_files:
  - split: train
    path: ta/train-*
- config_name: te
  data_files:
  - split: train
    path: te/train-*
- config_name: th
  data_files:
  - split: train
    path: th/train-*
- config_name: zh
  data_files:
  - split: train
    path: zh/train-*
---

# 🪷 NayanaOCR Corpus 2025

> **A 1M-page, 22-language fully-parallel synthetic OCR + VQA corpus for document-centric vision-language models — every page rendered in every language.**

NayanaOCR Corpus 2025 is **one of the largest open-source multilingual, multi-task document datasets** for training and evaluating **OCR**, **layout detection**, and **visual question answering (VQA)** in low-resource and underrepresented languages.

**The headline property: it's a true parallel corpus.** The same ~45,700 source pages are re-rendered into **all 22 languages** with consistent region IDs and bounding boxes, joined by a shared `image_id.txt`. That means every page exists in *all* 22 scripts — Latin, Devanagari, Dravidian, CJK, Arabic, Thai — giving you free cross-lingual pairs, script-invariant supervision, and clean cross-script ablations out of the box (see [§ Why a Parallel Corpus?](#-why-a-parallel-corpus-and-how-weve-used-it) below).

In total: **~1,006,170 richly annotated document page renderings across 22 languages**, with per-region bounding boxes, English ground-truth, in-language translations, and synthetic VQA pairs (descriptive + multiple-choice).

This dataset is part of the **Nayana initiative** — a **2025 recipient of the [Meta Llama Impact Grant](https://llama.meta.com/llama-impact-grants/)**. We're grateful to Meta and the Llama Impact Grant programme for supporting this work.

### 📦 Versions

- **NayanaOCR Corpus 2025** *(this release, public)* — the dataset documented on this page.
- **NayanaOCR 2026** *(private — request access)* — our next iteration: **~5× larger**, with higher rendering quality and improved annotations. To request access, email **contact@cognitivelab.in**.
- 🎯 **Companion eval set (from the 2026 line):** [v1v1d1/NayanaOCRBench_Synthetic_final](https://huggingface.co/datasets/v1v1d1/NayanaOCRBench_Synthetic_final) — use this for OCR/VQA evaluation

### 🆕 NayanaOCR 2026 at a glance

| Property | NayanaOCR Corpus 2025 (this dataset) | **NayanaOCR 2026** |
|---|---|---|
| Pages / language | ~45,700 | **~200,000** |
| Total rows | ~1,006,170 | **~4,412,985** |
| Total size | ~814 GB | **~1.5 TB** |
| Languages | 22 | 22 |
| Status | Public (this page) | **Private — by request** |

---

## ✨ TL;DR

| Property | Value |
|---|---|
| **Rows (total)** | ~1,006,170 |
| **Pages per language** | ~45,700 |
| **Languages** | 22 (10 Indic, 6 European, 3 East Asian, 1 Semitic, 1 SE-Asian, 1 classical) |
| **Per-language size** | ~28–42 GB (parquet) |
| **Total size** | ~814 GB |
| **Format** | Parquet (auto-converted from WebDataset) |
| **Modalities** | Image + Text (+ structured JSON) |
| **Tasks** | OCR · Layout Detection · Translation · VQA · MCQ |
| **Split** | `train` only (use the data as a pretraining / SFT corpus) |
| **License** | CC BY-NC 4.0 — research & academic use; commercial use requires commercial license (see below) |

---

## 🌍 Language Coverage

22 languages organised by script family:

| Family | Languages |
|---|---|
| **Indic** | Hindi (`hi`), Kannada (`kn`), Tamil (`ta`), Telugu (`te`), Marathi (`mr`), Punjabi (`pa`), Bengali (`bn`), Odia (`or`), Malayalam (`ml`), Gujarati (`gu`), Sanskrit (`sa`) |
| **European** | English (`en`), German (`de`), French (`fr`), Italian (`it`), Spanish (`es`), Russian (`ru`) |
| **East Asian** | Chinese (`zh`), Japanese (`ja`), Korean (`ko`) |
| **Semitic** | Arabic (`ar`) |
| **South-East Asian** | Thai (`th`) |

Each language is exposed as a top-level **config** (`ar`, `bn`, …, `zh`). All configs share the same schema and image stock — they are *parallel renderings* of the same underlying page corpus, so the same `image_id.txt` value appears across languages (use it as the join key to pull the same page in multiple scripts).

---

## 🧱 Dataset Schema

The dataset is published in **WebDataset** format (sharded TAR archives) and **auto-converted to Parquet** by the Hub for streaming-friendly access. Both views surface the same logical sample.

### Underlying WebDataset layout

Inside each TAR, one *sample* is a group of files that share the same numeric stem (`XXXXXXXX`):

```
00000000.jpg                 # the document image
00000000.image_id.txt        # unique image identifier
00000000.font_used.txt       # font used for this rendering
00000000.regions.json        # text-region annotations (bboxes + OCR + translation)
00000000.vqa.json            # visual question-answering annotations

00000001.jpg
00000001.image_id.txt
...
```

### Repository folder organisation

```
Cognitive-Lab/NayanaOCR_Corpus_2025/
├── ar/
│   ├── ar_00000.tar
│   ├── ar_00001.tar
│   └── ...
├── bn/
│   ├── bn_00000.tar
│   └── ...
├── kn/
│   └── ...
├── ...   # 22 language folders in total
└── README.md
```

Each language folder is ~28–42 GB, sharded into 5 GB TAR chunks. The Hub also exposes a `convert/parquet` branch with the same data in Parquet form (used by `load_dataset` and the SQL Console).

### Top-level columns (Parquet view)

When loaded via `datasets`, each row corresponds to a **single rendered document page**:

| Column | Type | Description |
|---|---|---|
| `jpg` | `Image` (PIL) | Rendered document page. Most pages are **3300 × 2550 px** (US Letter @ 300 DPI). Decoded lazily by the `Image` feature. |
| `image_id.txt` | `string` | Canonical page identifier, e.g. `document_10009_page_1`. **Stable across all 22 language configs** — use it as the cross-language join key. |
| `font_used.txt` | `string` | Font file used to render this language (e.g. `NotoSansKannada-Regular.ttf`, `ja_1.ttf`, `ar_1.ttf`). `None` for the source `en` config (no re-rendering required). |
| `regions.json` | `List[Region]` | Per-region layout + OCR + translation annotations (schema below). |
| `vqa.json` | `{questions: List[Question]}` | Synthetic VQA — mix of descriptive open answers and 4-option MCQ. |
| `__key__` | `string` | WebDataset shard-local key (e.g. `00000002`) — the numeric stem from the TAR. |
| `__url__` | `string` | Provenance — original WebDataset TAR path on the generation host. |

### `regions.json` — region-level annotations

A list of regions, one entry per detected layout element on the page.

```jsonc
[
  {
    "region_id": 1,                                      // 1-indexed within the page
    "bbox": {                                            // pixel coords on the rendered jpg
      "xmin": 146,
      "ymin": 1301,
      "xmax": 2387,
      "ymax": 1765
    },
    "layout_type": "text",                               // see vocabulary below
    "english_text": "type of community in which the open water is found…",
    "translated_text": "ತೆರೆದ ನೀರು ಕಂಡುಬರುವ ಸಮುದಾಯದ ಪ್ರಕಾರ…"
  },
  {
    "region_id": 2,
    "bbox": { "xmin": 148, "ymin": 279, "xmax": 1977, "ymax": 279 },
    "layout_type": "title",
    "english_text": "The Ecological Communities of Hillsborough County: Open Water",
    "translated_text": "ಹಿಲ್ಸ್‌ಬರೋ ಕೌಂಟಿಯ ಪರಿಸರ ಸಮುದಾಯಗಳು: ತೆರೆದ ನೀರು"
  }
]
```

**Field reference:**

| Field | Type | Notes |
|---|---|---|
| `region_id` | `int64` | Region index within the page. Not guaranteed contiguous after filtering. |
| `bbox.xmin` / `ymin` / `xmax` / `ymax` | `int64` | Absolute pixel coordinates on the rendered page. Origin is top-left. |
| `layout_type` | `string` | One of: `text`, `title`, `list`, `table`, `figure`, `caption`, `header`, `footer` (most pages only use `text` and `title`). |
| `english_text` | `string` | Source English text for the region. Present for **all** configs (so a non-English row carries both the original English and its localised counterpart). |
| `translated_text` | `string` | Localised text for the region. Present for **all non-English configs**; **omitted** in `en/train` (since the English IS the source). |

### `vqa.json` — page-level visual question answering

```jsonc
{
  "questions": [
    {
      "type": "descriptive",                          // open-ended Q
      "question": "What types of aquatic plants are commonly found in open water habitats?",
      "answer": "Aquatic plants commonly found in open water habitats include waterlilies, pondweeds, spikerushes, lemon bacopa, and bladderworts.",
      "options": null
    },
    {
      "type": "mcq",                                  // 4-option multiple choice
      "question": "Which of the following is a characteristic of the water scorpion?",
      "answer": "They have two long thin tubes that function as snorkels projecting from the rear of the abdomen.",
      "options": [
        "They have a stinger on their tail that they use for defense.",
        "They are primarily found in terrestrial habitats.",
        "They have two long thin tubes that function as snorkels projecting from the rear of the abdomen.",
        "They are known for their bright red coloration."
      ]
    }
  ]
}
```

**Field reference:**

| Field | Type | Notes |
|---|---|---|
| `type` | `string` | `descriptive` (open) or `mcq` (4-option multiple choice). |
| `question` | `string` | Question in the **target language** of the config. |
| `answer` | `string` | Reference answer in the **target language**. For `mcq`, this string exactly matches one of the `options`. |
| `options` | `List[string]` \| `null` | Four candidate answers for `mcq`; `null` for `descriptive`. |

Most pages carry **5 questions**: 4 descriptive + 1 MCQ.

### Loading: WebDataset vs Parquet

The Hub auto-converts to Parquet, so the simplest path is `datasets`:

```python
from datasets import load_dataset

ds = load_dataset("Cognitive-Lab/NayanaOCR_Corpus_2025", name="kn", split="train", streaming=True)
for row in ds.take(1):
    print(row["image_id.txt"])         # document_10009_page_1
    print(row["font_used.txt"])        # NotoSansKannada-Regular.ttf
    print(row["regions.json"][0])      # dict with bbox / layout_type / english_text / translated_text
    print(row["vqa.json"]["questions"][0]["question"])
```

If you want raw streaming over the underlying TARs (faster for large-scale training jobs), use the `webdataset` library against the source files. The per-sample keys are: `jpg`, `image_id.txt`, `font_used.txt`, `regions.json`, `vqa.json`.

```python
import io, json
import webdataset as wds
from PIL import Image

# Stream Kannada TARs directly from the Hub
url = "pipe:curl -s -L https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025/resolve/main/kn/kn_{00000..00085}.tar"
ds = wds.WebDataset(url)

for sample in ds:
    image    = Image.open(io.BytesIO(sample["jpg"]))
    image_id = sample["image_id.txt"].decode("utf-8")
    font     = sample["font_used.txt"].decode("utf-8")
    regions  = json.loads(sample["regions.json"].decode("utf-8"))
    vqa      = json.loads(sample["vqa.json"].decode("utf-8"))
    # … train loop
    break
```

### Performance tips

- **Stream first.** Each language config is 28–42 GB; pass `streaming=True` to `load_dataset` or iterate the WebDataset TARs directly. Materialise a config to disk only if you'll re-use it many times.
- **Use `webdataset` for max throughput.** For multi-GPU training the `webdataset` library handles sharded reads, decoding, and dataloader-side batching better than the `datasets` Parquet path.
- **Selective language loading.** Don't load all 22 configs upfront — pick the languages your run actually needs.
- **Image decode is the bottleneck.** Decode `jpg` lazily in your transform; don't decode unused fields.

---

## 🚀 Quickstart

### Python (`datasets`)

```python
from datasets import load_dataset

# Load one language
kn = load_dataset("Cognitive-Lab/NayanaOCR_Corpus_2025", name="kn", split="train")

row = kn[2]
print(row["image_id.txt"])   # document_10009_page_1
print(row["font_used.txt"])  # NotoSansKannada-Regular.ttf
print(row["regions.json"][0]["translated_text"])

# Stream to avoid downloading the whole config (each is 28–42 GB)
hi = load_dataset(
    "Cognitive-Lab/NayanaOCR_Corpus_2025",
    name="hi", split="train",
    streaming=True,
)
for row in hi.take(5):
    print(row["image_id.txt"])
```

### Iterate multiple languages

```python
LANGS = ["en", "hi", "kn", "ta", "te", "ar", "ja", "ko", "zh", "fr", "de"]
ds = {lang: load_dataset("Cognitive-Lab/NayanaOCR_Corpus_2025", name=lang, split="train", streaming=True)
      for lang in LANGS}
```

---

## 🛠️ How was this built?

NayanaOCR Corpus 2025 was generated by the **synthetic-data pipeline** described in our two papers. For the full method, ablations, and evaluation, please read:

- 📄 **[Nayana OCR: A Scalable Framework for Document OCR in Low-Resource Languages](https://aclanthology.org/2025.lm4uc-1.11/)** — Kolavi, Samarth & Jain, *LM4UC 2025*. Introduces the OCR-focused training framework and the Indic VLM adaptation method.
- 📄 **[Nayana: A Foundation for Document-Centric Vision-Language Models via Multi-Task, Multimodal, and Multilingual Data Synthesis](https://openaccess.thecvf.com/content/ICCV2025W/CV4DC/html/Kolavi_Nayana_A_Foundation_for_Document-Centric_Vision-Language_Models_via_Multi-Task_Multimodal_ICCVW_2025_paper.html)** — Kolavi & Jain, *ICCVW 2025 (CV4DC)*. Describes the broader multi-task, multilingual data-synthesis approach that this dataset is one component of.

A condensed view of the pipeline:

1. **Source ingestion.** English PDFs are parsed into page images and a structured layout tree (titles, paragraphs, lists, tables, figures, captions) using SOTA document-understanding models. The pipeline preserves hierarchical relationships, reading order, and per-region bounding boxes.
2. **Region-level text extraction.** OCR + structural cues are reconciled to produce the canonical `english_text` for every region, which becomes the ground truth.
3. **Contextual translation.** Each region's English text is translated into the 21 target languages using translation models tuned to preserve domain terminology, technical vocabulary, casing, and rough line-break behaviour. Translation operates region-by-region rather than page-by-page, so layout positions are preserved.
4. **Re-rendering.** The page is *re-rendered* using the localised text inside the original bounding boxes with script-appropriate fonts (e.g. Noto Sans family for Indic, dedicated TTFs for CJK and Arabic). The `font_used.txt` field captures which font was applied.
5. **Synthetic VQA generation.** A page-conditioned LLM generates 4 descriptive Q/A pairs and 1 multiple-choice question per page, grounded in the visible region text. Questions and answers are produced in the target language.
6. **Packaging.** Outputs are sharded into 5 GB WebDataset TARs per language, then auto-converted to Parquet for streaming-friendly access on the Hub.

The result is a **parallel multilingual rendering corpus**: the same source page exists in up to 22 scripts with consistent region IDs and bounding boxes, which is uniquely useful for OCR transfer, layout-preserving translation, and cross-lingual VQA studies.

---

## 🌐 Why a Parallel Corpus? (and how we've used it)

NayanaOCR Corpus 2025 is not "22 separate datasets" — it's **the same set of ~45.7K document pages, re-rendered into 22 scripts, with consistent region IDs and bounding boxes**. The `image_id.txt` field is the join key: `document_10009_page_1` in English, Kannada, Japanese, Arabic, etc. all refer to the *same* underlying page.

### What "parallel" buys you

| Property | What it enables |
|---|---|
| **Same content, 22 scripts** | Train a single multilingual model that is invariant to script. The semantic signal is shared; only the surface form changes. |
| **Aligned layouts** | Bounding boxes are preserved across renderings, so layout-grounded supervision (region classification, table structure, reading order) transfers across languages without re-annotation. |
| **Free cross-lingual pairs** | Every page yields *C(22, 2) = 231* cross-lingual document pairs at zero additional labelling cost. This is the foundation for cross-lingual retrieval and cross-lingual VQA training. |
| **Controlled ablations** | Hold layout / content fixed, vary only the script — clean way to study script-family transfer (e.g. Latin → Devanagari → CJK). |
| **In-batch negatives that mean something** | A batch of "same page in 8 languages" gives contrastive losses semantically meaningful positives without the usual cross-batch correlation problems. |

### 👀 See it: one page, many scripts

Here is a preview of a few languages — the **same source page** (`image_id = document_10009_page_1`) rendered across the corpus. Same layout, same regions, same bounding boxes — only the script changes.

<table>
<tr>
<td align="center" width="25%"><b>en</b> · English<br><sub>source · no font remap</sub><br><img src="assets/parallel_demo/en_document_10009_page_1.jpg" width="220" alt="English"/></td>
<td align="center" width="25%"><b>de</b> · German<br><sub>de_3.ttf</sub><br><img src="assets/parallel_demo/de_document_10009_page_1.jpg" width="220" alt="German"/></td>
<td align="center" width="25%"><b>fr</b> · French<br><sub>fr_3.ttf</sub><br><img src="assets/parallel_demo/fr_document_10009_page_1.jpg" width="220" alt="French"/></td>
<td align="center" width="25%"><b>es</b> · Spanish<br><sub>es_3.ttf</sub><br><img src="assets/parallel_demo/es_document_10009_page_1.jpg" width="220" alt="Spanish"/></td>
</tr>
<tr>
<td align="center" width="25%"><b>ru</b> · Russian<br><sub>ru_3.ttf</sub><br><img src="assets/parallel_demo/ru_document_10009_page_1.jpg" width="220" alt="Russian"/></td>
<td align="center" width="25%"><b>ar</b> · Arabic<br><sub>ar_2.ttf</sub><br><img src="assets/parallel_demo/ar_document_10009_page_1.jpg" width="220" alt="Arabic"/></td>
<td align="center" width="25%"><b>ja</b> · Japanese<br><sub>ja_3.ttf</sub><br><img src="assets/parallel_demo/ja_document_10009_page_1.jpg" width="220" alt="Japanese"/></td>
<td align="center" width="25%"><b>ko</b> · Korean<br><sub>ko_2.ttf</sub><br><img src="assets/parallel_demo/ko_document_10009_page_1.jpg" width="220" alt="Korean"/></td>
</tr>
<tr>
<td align="center" width="25%"><b>hi</b> · Hindi<br><sub>NotoSerifDevanagari</sub><br><img src="assets/parallel_demo/hi_document_10009_page_1.jpg" width="220" alt="Hindi"/></td>
<td align="center" width="25%"><b>mr</b> · Marathi<br><sub>NotoSansDevanagari</sub><br><img src="assets/parallel_demo/mr_document_10009_page_1.jpg" width="220" alt="Marathi"/></td>
<td align="center" width="25%"><b>sa</b> · Sanskrit<br><sub>JainiPurva-Regular</sub><br><img src="assets/parallel_demo/sa_document_10009_page_1.jpg" width="220" alt="Sanskrit"/></td>
<td align="center" width="25%"><b>bn</b> · Bengali<br><sub>AnekBangla-Regular</sub><br><img src="assets/parallel_demo/bn_document_10009_page_1.jpg" width="220" alt="Bengali"/></td>
</tr>
<tr>
<td align="center" width="25%"><b>gu</b> · Gujarati<br><sub>NotoSerifGujarati</sub><br><img src="assets/parallel_demo/gu_document_10009_page_1.jpg" width="220" alt="Gujarati"/></td>
<td align="center" width="25%"><b>pa</b> · Punjabi<br><sub>NotoSansGurmukhi</sub><br><img src="assets/parallel_demo/pa_document_10009_page_1.jpg" width="220" alt="Punjabi"/></td>
<td align="center" width="25%"><b>or</b> · Odia<br><sub>AnekOdia-Regular</sub><br><img src="assets/parallel_demo/or_document_10009_page_1.jpg" width="220" alt="Odia"/></td>
<td align="center" width="25%"><b>ta</b> · Tamil<br><sub>KarlaTamilInclined</sub><br><img src="assets/parallel_demo/ta_document_10009_page_1.jpg" width="220" alt="Tamil"/></td>
</tr>
<tr>
<td align="center" width="25%"><b>te</b> · Telugu<br><sub>NotoSerifTelugu</sub><br><img src="assets/parallel_demo/te_document_10009_page_1.jpg" width="220" alt="Telugu"/></td>
<td align="center" width="25%"><b>kn</b> · Kannada<br><sub>NotoSansKannada</sub><br><img src="assets/parallel_demo/kn_document_10009_page_1.jpg" width="220" alt="Kannada"/></td>
<td align="center" width="25%"><b>ml</b> · Malayalam<br><sub>NotoSerifMalayalam</sub><br><img src="assets/parallel_demo/ml_document_10009_page_1.jpg" width="220" alt="Malayalam"/></td>
<td align="center" width="25%"><b>th</b> · Thai<br><sub>th_3.ttf</sub><br><img src="assets/parallel_demo/th_document_10009_page_1.jpg" width="220" alt="Thai"/></td>
</tr>
</table>

> Every cell above is **the same page** with the same layout — only the text and the rendering font change. The English row is the source; all 19 others come from the same English content translated and re-rendered region-by-region. This is the parallel-corpus property in one screenshot.

### How we used it: **M3DR — Multilingual Multimodal Document Retrieval**

We've used the parallel structure of NayanaOCR to build **M3DR**, a multilingual multimodal document retrieval system:

📄 **[M3DR: Towards Universal Multilingual Multimodal Document Retrieval](https://arxiv.org/abs/2512.03514)** — Kolavi & Jain, 2025 (arXiv:2512.03514)

**Training data construction.** Starting from the parallel rendering corpus, we generate **5 query types per document** with Llama 3.1 90B Vision / Llama 4 Scout: factual (×2), long-answer (×1), short-answer / MCQ (×1), and cross-paragraph reasoning (×1). Combined with the 22-language parallel renderings, this yields **~1M page-image / query pairs across 22 languages** — all from the same source pages, so every query has a natural positive in every language.

**Why parallel mattered here.**

- The same query, translated, can retrieve the page in *any* of the 22 scripts → directly trainable cross-lingual retrieval signal.
- In-batch negatives become genuinely hard: each batch is many languages of the same content, so the model must learn semantics, not script shortcuts.
- Layout is preserved across renderings, so visual-token retrievers (ColBERT-style) get consistent spatial cues regardless of language.

**The Nayana-IR retrieval benchmark** *(also derived from this dataset)*:

- 23 datasets — 1 cross-lingual + 22 per-language monolingual.
- 27,870 document images, 5,400 queries.
- 5,870 parallel images × 1,000 queries on the cross-lingual split.
- BEIR-compatible format.

**Models released:**

- **NetraEmbed** (single-vector dense, Gemma 3 4B-IT backbone, 2560-dim with Matryoshka 768 / 1536 / 2560)
- **ColNetraEmbed** (ColBERT-style multi-vector, 256 visual tokens × 128 dim, MaxSim late interaction)

**Headline result.** NetraEmbed reaches **0.716 NDCG@5 on cross-lingual retrieval vs ColPali-v1.3's 0.284** — a **~152% relative improvement** — and ~80% relative improvement on monolingual retrieval. Per-language performance is consistent across Latin, Devanagari, CJK, Arabic, and Dravidian scripts.

### Other things the parallel structure unlocks (open invitations)

- **Cross-lingual layout-grounded VQA** — answer in one language, page rendered in another.
- **Script-invariant OCR pretraining** — same content, different glyphs, makes a strong contrastive signal for visual text encoders.
- **Translation-with-layout** — train a model that respects bounding-box constraints when translating, not just text-to-text.
- **Font-robustness ablations** — `font_used.txt` lets you study how much rendering choice affects downstream task accuracy.

If you build something on top of the parallel structure, please cite the dataset *and* the M3DR paper — and we'd love to hear about it: **contact@cognitivelab.in**.

---

## 🎯 Intended uses

✅ Suitable for:

- Training OCR / document-VLM models, especially for low-resource Indic and SE-Asian scripts.
- Layout detection (titles, text blocks, tables) with bounding-box supervision.
- Cross-lingual transfer: same page, 22 scripts.
- Synthetic-data ablations and scaling-law studies.
- Document VQA (descriptive + MCQ).

⚠️ Out-of-scope:

- **Not a benchmark.** This is synthetic training data; for evaluation use held-out, human-curated test sets.
- **Not a ground-truth translation corpus** — translations are model-generated and may contain errors, especially on technical jargon.
- **Not for identity-sensitive applications** — source PDFs are general-domain English documents and may reflect underlying corpus biases.

---

## ⚖️ Known limitations (2025 iteration)

> **This is our 2025 iteration of the dataset, and it is fully synthetic.** The 2026 release (in progress) addresses most of the issues below — please contact **contact@cognitivelab.in** for early access. The known issues in *this* release are:

### Rendering artefacts

- **Font-rendering glitches.** Certain glyphs (especially Indic conjuncts, CJK rare characters, Arabic ligatures) do not render correctly with the open fonts used in the pipeline. Sanskrit (`sa`) and Odia (`or`) have the most fallback-rendering issues.
- **Overlapping text.** Because the localised string can be longer (or wider) than the original English in the same bounding box, you'll occasionally see text **overflowing the bbox** or **overlapping a neighbouring region**. Most pronounced in German (`de`), Russian (`ru`), Tamil (`ta`), and Malayalam (`ml`).
- **Line-break drift.** Region-level translation doesn't always preserve the original line-break structure, so the rendered text may wrap differently from the source layout.
- **Font fallback gaps.** Some shards fall back to a generic font when the primary font can't render a glyph — visible as boxy or boxed characters.

### Annotation artefacts

- **Translation quality is uneven.** Translations are model-generated. Expect higher fidelity in `hi`, `kn`, `ja`, `de`, `fr`, `es` and more drift in lower-resource scripts and technical jargon.
- **VQA grounding errors.** Synthetic VQA pairs can contain factual mistakes, hallucinated entities, or answers that aren't strictly grounded in the visible page content.
- **Layout-type vocabulary skews.** Most pages use `text` / `title` heavily; `table` and `figure` annotations are present but sparser and noisier.

### Corpus-level limitations

- **Domain skew.** The English source corpus is weighted toward technical / instructional content (user guides, policy transcripts, ecology/watershed reports). Literary, legal, and medical genres are under-represented.
- **Synthetic ≠ real.** Pages are *renderings* of translated text into clean templates — they don't capture real-world scan noise, paper texture, handwriting, faded ink, multi-column newspaper layouts, etc. Pair with a real-document benchmark (e.g. the [NayanaOCRBench](https://huggingface.co/datasets/v1v1d1/NayanaOCRBench_Synthetic_final) eval set) when reporting OCR results.
- **Not for identity-sensitive applications** — source PDFs are general-domain English documents and may reflect underlying corpus biases.

---

## 📜 License & attribution

**License: CC BY-NC 4.0 with supplemental terms** — full text in [LICENSE.md](./LICENSE.md).

- ✅ **Free for non-commercial use** — research, education, students, open-source projects — with attribution and citation.
- ⚠️ **For commercial use, please email us at [contact@cognitivelab.in](mailto:contact@cognitivelab.in)** and we'll arrange a commercial licence. Same address for **NayanaOCR 2026** access requests.

### Attribution

If you use NayanaOCR Corpus 2025 in any work, please:

1. Cite the underlying papers (see [Citation](#-citation) below).
2. Link back to this dataset page.
3. Preserve the licence notice in any derivative dataset.

---

## 📚 Citation

If you use NayanaOCR Corpus 2025, please cite both papers:

```bibtex
@inproceedings{kolavi2025nayanaocr,
  title     = {Nayana {OCR}: A Scalable Framework for Document {OCR} in Low-Resource Languages},
  author    = {Kolavi, Adithya S. and Samarth, P. and Jain, Vyoman},
  booktitle = {Proceedings of the 1st Workshop on Language Models for Underserved Communities (LM4UC)},
  year      = {2025},
  pages     = {86--103},
  url       = {https://aclanthology.org/2025.lm4uc-1.11/}
}

@inproceedings{kolavi2025nayana,
  title     = {Nayana: A Foundation for Document-Centric Vision-Language Models via Multi-Task, Multimodal, and Multilingual Data Synthesis},
  author    = {Kolavi, Adithya S. and Samarth, P. and Jain, Vyoman},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops (ICCVW) -- CV4DC},
  year      = {2025},
  pages     = {1678--1687},
  url       = {https://openaccess.thecvf.com/content/ICCV2025W/CV4DC/html/Kolavi_Nayana_A_Foundation_for_Document-Centric_Vision-Language_Models_via_Multi-Task_Multimodal_ICCVW_2025_paper.html}
}

@misc{kolavi2025m3dr,
  title         = {{M3DR}: Towards Universal Multilingual Multimodal Document Retrieval},
  author        = {Kolavi, Adithya S. and Jain, Vyoman},
  year          = {2025},
  eprint        = {2512.03514},
  archivePrefix = {arXiv},
  primaryClass  = {cs.IR},
  url           = {https://arxiv.org/abs/2512.03514}
}
```

You can also cite the dataset directly:

```bibtex
@misc{nayanaocr2025dataset,
  title  = {{NayanaOCR Corpus 2025}: A 22-Language Multilingual Document {OCR} and {VQA} Dataset},
  author = {Kolavi, Adithya S. and {Cognitive Lab}},
  year   = {2025},
  howpublished = {\url{https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025}},
  note   = {Released under CC BY-NC 4.0}
}
```

---

## 🙏 Acknowledgements

- 🦙 **[Meta Llama Impact Grant](https://llama.meta.com/llama-impact-grants/)** — the Nayana initiative is a **2025 recipient** of the Llama Impact Grant. We thank Meta and the Llama programme for funding and supporting our work on multilingual document AI for underrepresented languages.
- The Indic NLP and document-AI community — for the open fonts, translation models, and corpora that made multilingual rendering tractable.
- The **Hugging Face** team — for hosting, parquet auto-conversion, and the dataset-viewer infrastructure that makes a corpus this size accessible.
- All authors and contributors at **Cognitive Lab** who built and validated the VIVID pipeline.

---

## 🔗 Links

- 📄 **Paper 1 (LM4UC 2025):** [Nayana OCR — Scalable Framework for Document OCR](https://aclanthology.org/2025.lm4uc-1.11/)
- 📄 **Paper 2 (ICCVW 2025, CV4DC):** [Nayana — Foundation for Document-Centric VLMs](https://openaccess.thecvf.com/content/ICCV2025W/CV4DC/html/Kolavi_Nayana_A_Foundation_for_Document-Centric_Vision-Language_Models_via_Multi-Task_Multimodal_ICCVW_2025_paper.html)
- 📄 **Paper 3 (arXiv 2025):** [M3DR — Multilingual Multimodal Document Retrieval](https://arxiv.org/abs/2512.03514)
- 🎯 **Evaluation benchmark:** [v1v1d1/NayanaOCRBench_Synthetic_final](https://huggingface.co/datasets/v1v1d1/NayanaOCRBench_Synthetic_final)
- 🦙 **Meta Llama Impact Grant:** [llama.meta.com/llama-impact-grants](https://llama.meta.com/llama-impact-grants/)
- 🆕 **NayanaOCR 2026 (request access):** contact@cognitivelab.in
- 🏢 **Cognitive Lab:** [https://www.cognitivelab.in](https://www.cognitivelab.in)

---

*Built with 🪷 by [Cognitive Lab](https://www.cognitivelab.in).*
