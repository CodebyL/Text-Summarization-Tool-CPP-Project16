# 📝 Text Summarization Tool using LLM
**Project 16**

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

### **Test 2**
```bash
Global initiatives are being launched to combat climate change and promote renewable energy sources worldwide.
```

**Output**
```bash
Text 2:
Extractive: Climate change remains one of the biggest global challenges. Governments are working together to reduce carbon emissions and promote green energy.
Abstractive: Climate change remains one of the biggest global challenges. Governments are working together to reduce carbon emissions and promote green energy.

```

## 🔧 Additional Test Runs

### **Test 3**
```bash
Researchers have discovered that regular exercise significantly boosts mental health and cognitive function.
```

**Output**
```bash
Text 3:
Extractive: A new study shows that a balanced diet and regular exercise can significantly improve mental health and productivity.
Abstractive: A balanced diet and regular exercise can significantly improve mental health and productivity. A new study shows that a balanced diet can significantly improved mental health.

```

### **Test 4**
```bash
Technological advancements in healthcare are enabling faster diagnostics and more personalized treatments for patients.
```

**Output**
```bash
Text 1:
Extractive: Advancements in healthcare technology are leading to better patient outcomes and more efficient treatments.
Abstractive: Advancements in healthcare technology are leading to better patient outcomes and more efficient treatments, according to the World Health Organisation.

```

### **Test 5**
```bash
The adoption of electric vehicles is accelerating as governments offer incentives and infrastructure improves.
```

**Output**
```bash
Text 1:
Extractive: The rise of electric vehicles is transforming the automotive industry, with major manufacturers shifting towards sustainable solutions.
Abstractive: The rise of electric vehicles is transforming the automotive industry. Major manufacturers are shifting towards sustainable solutions. Electric vehicles are becoming more and more popular with consumers.
```

### **Test 6 (longer text)**
```bash
The global economy has faced numerous challenges over the past decade, including financial crises, pandemics, and geopolitical tensions. These events have disrupted supply chains, increased inflation rates, and shifted the dynamics of international trade. In response, governments and central banks around the world have implemented various monetary and fiscal policies to stabilize markets and support economic recovery.
```

**Output**
```bash
Text 1:
Extractive: The global economy has faced numerous challenges over the past decade, including financial crises, pandemics, and geopolitical tensions. In response, governments and central banks around the world have implemented various monetary and fiscal policies to stabilize markets and support economic recovery.
Abstractive: The global economy has faced numerous challenges over the past decade, including financial crises, pandemics, and geopolitical tensions. These events have disrupted supply chains, increased inflation rates, and shifted the dynamics of international trade. In response, governments and central banks around the world have implemented various monetary and fiscal policies to stabilize markets.
```

---
## 💾 **Data Structures & Functions**
- Libraries Used:
  - transformers for abstractive summarization (LLM).
	- sumy for extractive summarization (TextRank algorithm).
- Key Functions:
	- extractive_summary(text) – Picks key sentences from the input.
	- abstractive_summary(text) – Generates a rephrased summary using LLM.

---

## 📂 **Files Included**
- summarizer.py — Main Python script.
- inputs.txt — Contains 5 sample texts (articles/research snippets).
- summaries.txt — Output file with generated summaries.
- requirements.txt — Lists required Python libraries.
- README.md — Project documentation.
