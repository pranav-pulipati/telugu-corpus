---
license: mit
task_categories:
- question-answering
- text-generation
language:
- hi
- te
- en
configs:
- config_name: Hindi
  data_files: "Hindi100k.json"
- config_name: Hinglish
  data_files: "Hinglish100k.json"
- config_name: Telugu
  data_files: "Telugu100k.json"
size_categories:
- 10K<n<100K
---
# Indic Vault — everyday Indian language QA pairs, tuned for chatbots & voice agents.
<img src="https://cdn-uploads.huggingface.co/production/uploads/64d36fa5df7be14f0a2e3b7b/2VpwFBjjeSEOIu1GZks6t.png" width="600"/>

---

## 🧾 Overview

Indic Vault is a high-quality, instruction-tuned dataset featuring question-answer pairs crafted in the contemporary, everyday language spoken across India in 2025. Unlike traditional datasets that lean heavily on formal or outdated linguistic styles, Indic Vault captures the authentic, colloquial expressions used in daily conversations, making it ideal for building AI assistants that feel genuinely relatable.

---

## 🧠 Key Features

* **Conversational Language**: Reflects the way people actually speak in 2025, moving beyond rigid textbook Hindi or English.
* **Diverse Topics**: Covers 20 essential categories, including Finance, Health, Technology, Relationships, Home & Living, Food & Cooking, Education, Career, Entertainment, Travel, Sports, Culture, Society, Environment, Science, Law & Government, Business, Agriculture, Beauty & Fashion, and Politics.
* **High-Quality QA Pairs**: Each entry is thoughtfully curated to provide meaningful and contextually relevant information.
* **Model Compatibility**: Optimized for fine-tuning on open-source models ranging from 4B to 27B parameters.

---

## 💬 Sample Entry

### Hindi

**Question**: "आजकल सोशल मीडिया का टीनएजर्स के मेंटल हेल्थ पर क्या असर होता है?"

**Answer**: "आजकल सोशल मीडिया टीनएजर्स (किशोरों) की ज़िंदगी का एक बहुत अहम हिस्सा बन गया है। इसका उनके मेंटल हेल्थ पर सकारात्मक और नकारात्मक दोनों तरह के प्रभाव पड़ सकते हैं। यह इस बात पर निर्भर करता है कि वे इसका इस्तेमाल कैसे करते हैं, कितना समय देते हैं और किस तरह की सामग्री से जुड़ते हैं। उदाहरण के लिए, ज़्यादा देर स्क्रीन टाइम या दूसरों से तुलना करने की आदत चिंता और आत्म-सम्मान पर असर डाल सकती है, जबकि सकारात्मक कंटेंट और सपोर्ट ग्रुप्स से मदद मिल सकती है।"

### Hinglish (Romanized Hindi + Telugu inserts)

**Question**: "Mujhe apna budget kitni baar check aur update karna chahiye?"

**Answer**: "Chal, suno yaar, yeh budget ko kitni baar check karna hai aur update karna hai na, yeh bahut important sawaal hai. Basically, har week ek quick check maaro, aur mahine mein ek baar deep dive karo. Telugu mein bolte hain kadaa — 'vaaram vaaramu parikshinchi sarididdandi', ante weekly review chesi correct cheyyandi. Life mein koi major change aaye toh budget turant update karo, simple!"

### Telugu

**Question**: "ఇండియాలో మార్జినలైజ్డ్ కమ్యూనిటీస్ కి హెల్థ్ కేర్ ఆక్సెస్ చేయడానికి ఎలాంటి బ్యారియర్స్ ఉన్నాయి?"

**Answer**: "ఇండియాలో మార్జినలైజ్డ్ కమ్యూనిటీస్ హెల్త్ కేర్ అందుకోవడానికి చాలా బ్యారియర్స్ ఉన్నాయి. ముఖ్యంగా డబ్బు లేకపోవడం, హాస్పిటల్ లకు దూరం ఉండటం, మరియు సామాజిక వివక్ష (social discrimination) ఇవన్నీ పెద్ద అవరోధాలు. చాలా మందికి హెల్త్ స్కీమ్స్ గురించి తెలియకపోవడం, లేదా హాస్పిటల్స్ లో సరైన సదుపాయాలు లేకపోవడం కూడా ప్రధాన సమస్యలు."

These examples demonstrate how the dataset handles:

* **Natural, colloquial tone** — responses are written the way people actually speak in casual, real conversations.
* **Code-mixed constructs with native script fidelity** — even when English words are used, they’re written in native script (e.g., फ़ोन, బ్యాటరీ), making it voice-friendly.
* **Blended cultural references** — Hinglish examples mix South/North Indian idioms, showing real-life cross-lingual fluency.
* **Context-rich responses** — not just short-form answers, but full, thoughtful breakdowns suited for actual deployments.
* **Multilingual coverage** — answers are crafted per language nuance, not just translated.

These qualities make Indic Vault ideal for training:

* Chatbots that sound culturally in-tune and emotionally aware
* Voice agents that can read responses naturally with Indic TTS
* Assistants that respond with empathy, depth, and real-world fluency
* Fine-tuned LLMs that don't require further alignment for tone or format how the dataset handles:
* **Natural, colloquial tone**
* **Code-mixed constructs with native script fidelity**
* **Real-life topics written to match 2025 Indian user expectations**

---

## 🌟 Real-World Use & Benefits

Indic Vault isn’t just a dataset — it’s how you make your chatbot or voice assistant actually *work* in India. Most datasets sound robotic, too formal, or disconnected from how users actually talk. Indic Vault fixes that.

You can fine-tune LLMs like **Gemma-12B**, **LLaMA 3**, or **Mistral** using Indic Vault to:

* Build **chatbots** that handle informal, context-heavy queries with the same ease as human agents
* Train **voice agents** that feel culturally grounded and natural when speaking
* Create **personal assistants** that can understand common queries like “budget kaise banayein?” or “EMI kaunsa best hai?”
* Power **creator tools** that generate content in native scripts, using tone and phrasing that actually resonates

Fine-tuning on Indic Vault gives your model a massive boost in user relatability, script fluency, and tone correctness — especially for mixed-language Indian audiences.

---

## 🛠️ Technical Details

* **Format**: JSON with fields: `question`, `response`
* **Languages**: Currently includes Hindi, Hinglish, and Telugu; with Tamil, Marathi, and Bengali planned.
* **Script**: Only native scripts used (e.g., Devanagari, Telugu, Tamil). English borrowings appear in transliterated form, never Latin.
* **Size**: Approx. **80,000 QA pairs per language**, actively growing with each update

---

## 📈 Performance Insights

While Indic Vault is designed to enable natural, conversational AI, we do not claim exact performance parity with Gemini 2.5 or GPT-4o. However, in internal evaluations, open-source models like **Gemma-12B**, **Mistral-7B**, and **LLaMA 3-8B** fine-tuned on Indic Vault were able to handle code-mixed, context-rich prompts with a level of naturalness and relatability that rivaled closed models in **tone and usability**.

The key distinction is not raw benchmark scores, but:

* **How relatable the responses sound to Indian users**
* **How much script-switching, emotional nuance, and day-to-day phrasing** the model can handle post-finetuning

This makes Indic Vault a strong fit for building deployable assistants that "sound right" in real user environments.

---

## 📦 Dataset Updates

Currently, Indic Vault includes QA pairs in **Hindi**, **Hinglish**, and **Telugu**, with all responses written in native scripts. More languages such as Tamil, Marathi, and Bengali are planned for upcoming releases. Our goal is to continuously expand coverage across Indian languages, while preserving everyday realism in tone and phrasing.

## 🤝 Contribution & Feedback

We welcome contributions and feedback to enhance Indic Vault further. If you're interested in adding more topics, languages, or improving existing entries, please reach out or submit a pull request on our GitHub repository.

---

This dataset card provides a clear, concise, and engaging overview of Indic Vault, highlighting its unique value in the conversational AI space. By focusing on real-world language usage, Indic Vault is a practical and deployable resource for anyone building Indian-language assistants in 2025.
