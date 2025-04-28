# 📝 Text Summarization Tool using LLM
**Project 16 — Python Implementation**

**Course:** **420 Artificial Intelligence**  
**Date:** **4/28/25**

---

## 📖 **Project Description**
This project implements a **Text Summarization Tool** that summarizes news articles or research papers using two methods:
- **Extractive Summarization** with the **TextRank** algorithm.
- **Abstractive Summarization** using a pre-trained **LLM** (`facebook/bart-large-cnn`).

The app reads multiple texts from a file, applies both summarization techniques, and outputs the results.

---

## ⚙️ **How It Works**
- **Language:** Python
- **Techniques:**
  1. **Extractive Summarization:** Selects key sentences using the `sumy` library (TextRank).
  2. **Abstractive Summarization:** Generates human-like summaries using HuggingFace's `transformers` library with a pre-trained LLM.
- **Process Flow:**
   - Reads articles from `inputs.txt`.
   - Generates both summaries.
   - Saves output to `summaries.txt`.

---

## 🚀 **How to Run**
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the summarization app:
```bash
python summarizer.py
```
3. View the results in summaries.txt.

---

## 🧪 **Test Runs**

### **Test 1**
```bash
Artificial Intelligence is transforming industries by automating tasks and improving decision-making processes.
```

**Output**
```bash
Text 1:
Extractive: Artificial Intelligence is rapidly changing industries across the world. Companies are investing heavily in AI research to stay competitive.
Abstractive: Artificial Intelligence is rapidly changing industries across the world. Companies are investing heavily in AI research to stay competitive. The rise of AI has led to a surge in the number of companies using the technology.
```
