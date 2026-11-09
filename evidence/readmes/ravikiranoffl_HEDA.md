---
language:
- en
- te
license: mit
tags:
- osint
- news
- archives
- real-time
- india
- global
pretty_name: Huggingface Electronic Data Archive (HEDA)
size_categories:
- 10K<n<100K
---

# HEDA: Huggingface Electronic Data Archive

## The Ultimate Autonomous OSINT Matrix
HEDA is the deep-storage vault for **Project VEDA**. 

While VEDA handles the lightweight routing, temporal sorting, and frontend UI via GitHub, HEDA operates as a massive, passive data warehouse. It permanently stores the 1000+ word raw text extractions from over 30 global and regional news syndicates.

### Architecture
- **Command Engine:** VEDA (Python 3.12 / GitHub Actions)
- **Deep Extraction:** Trafilatura (Asynchronous NLP Scrape)
- **Warehouse Storage:** Hugging Face Datasets (JSON via Git LFS)
- **Sweep Frequency:** Every 2 Hours (Autonomous)

### Data Structure
The deep intel is stored in the `data/` directory using the `YYYY-MM-DD-deep.json` naming convention. 

The schema is a lightweight dictionary mapping MD5 hashes (generated from the clean URL) directly to the raw extracted text:

```json
{
  "md5_article_hash_id": "Raw 1000+ word text extracted directly from the DOM, stripped of ads, tracking, and bloat..."
}