from transformers import pipeline
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Load pre-trained LLM for abstractive summarization (this uses this model: facebook/bart-large-cnn model!)
abstractive_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Extractive Summarization Function (uses TextRank Alg. from sumy)
def extractive_summary(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentences_count=2)
    return " ".join(str(sentence) for sentence in summary)

# Abstractive Summarization Function (uses LLM)
def abstractive_summary(text):
    max_chunk_size = 1000  # Safe input size for the model
    if len(text) <= max_chunk_size:
        summary = abstractive_summarizer(text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    else:
        # Split long text into manageable chunks
        chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        combined_summary = ""
        for chunk in chunks:
            summary = abstractive_summarizer(chunk, max_length=150, min_length=50, do_sample=False)
            combined_summary += summary[0]['summary_text'] + " "
        return combined_summary.strip()

# Read inputs and generate summaries (this is the main func. of the project)
with open("inputs.txt", "r") as infile, open("summaries.txt", "w") as outfile:
    texts = infile.read().split("\n\n")
    for idx, text in enumerate(texts):
        if text.strip():  # Skip empty blocks
            outfile.write(f"Text {idx+1}:\n")
            outfile.write("Extractive: " + extractive_summary(text) + "\n")
            outfile.write("Abstractive: " + abstractive_summary(text) + "\n")
            outfile.write("--------------------------\n")

print("Summaries generated in summaries.txt")