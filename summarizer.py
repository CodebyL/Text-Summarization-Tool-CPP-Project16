from transformers import pipeline
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Load pre-trained LLM for abstractive summarization
abstractive_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function for extractive summarization
def extractive_summary(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentences_count=2)
    return " ".join(str(sentence) for sentence in summary)

# Function for abstractive summarization
def abstractive_summary(text):
    result = abstractive_summarizer(text, max_length=50, min_length=25, do_sample=False)
    return result[0]['summary_text']

# Read inputs and generate summaries
with open("inputs.txt", "r") as infile, open("summaries.txt", "w") as outfile:
    texts = infile.read().split("\n\n")  # Separate texts by empty lines
    count = 1
    for text in texts:
        outfile.write(f"Text {count}:\n")
        outfile.write("Extractive: " + extractive_summary(text) + "\n")
        outfile.write("Abstractive: " + abstractive_summary(text) + "\n")
        outfile.write("--------------------------\n")
        count += 1

print("Summaries generated in summaries.txt")