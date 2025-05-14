# adjective_analysis_nltk.py

import nltk
nltk.download('punkt', download_dir='/Users/michaeloliveri/nltk_data')
nltk.download('averaged_perceptron_tagger_eng', download_dir='/Users/michaeloliveri/nltk_data')
nltk.data.path.append('/Users/michaeloliveri/nltk_data')

from nltk import word_tokenize
from nltk.tag import PerceptronTagger
from collections import Counter
import matplotlib.pyplot as plt

# Load and clean text
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # Strip Project Gutenberg headers/footers (optional)
    start_marker = "*** START"
    end_marker = "*** END"
    start = text.find(start_marker)
    end = text.find(end_marker)
    if start != -1 and end != -1:
        text = text[start:end]
    return text

# Extract adjectives from text
def extract_adjectives(text):
    words = word_tokenize(text)
    tagger = PerceptronTagger()
    tagged = tagger.tag(words)
    adjectives = [word.lower() for word, tag in tagged if tag in ('JJ', 'JJR', 'JJS')]
    return adjectives

# Only include your POTO file
authors = {
    "Leroux": "frank.txt"
}

all_adjectives = {}

for author, file_path in authors.items():
    print(f"Processing {author}...")
    text = load_text(file_path)
    adjectives = extract_adjectives(text)
    freq = Counter(adjectives)
    all_adjectives[author] = freq

    # Show top 10 adjectives
    print(f"\nTop adjectives for {author}:")
    for word, count in freq.most_common(40):
        print(f"{word}: {count}")
