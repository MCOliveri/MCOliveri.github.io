# adjective_analysis_nltk.py
# This script processes a text file to extract and analyze adjectives using NLTK.
# It uses tagging to identify adjectives, then counts and displays the most frequent ones.

import nltk
from nltk import word_tokenize
from nltk.tag import PerceptronTagger
from collections import Counter
import matplotlib.pyplot as plt  # Imported in case you want to visualize later

# Download necessary NLTK models and taggers to a specific local directory
nltk.download('punkt', download_dir='/Users/michaeloliveri/nltk_data')  # Tokenizer for breaking text into words
nltk.download('averaged_perceptron_tagger_eng', download_dir='/Users/michaeloliveri/nltk_data')  # POS tagger
nltk.data.path.append('/Users/michaeloliveri/nltk_data')  # Add the download directory to NLTK’s search path

# Function to load and clean a text file
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Identify and trim Project Gutenberg markers if they exist
    start_marker = "*** START"
    end_marker = "*** END"
    start = text.find(start_marker)
    end = text.find(end_marker)

    # Slice the text to exclude headers/footers
    if start != -1 and end != -1:
        text = text[start:end]

    return text

# Function to extract adjectives from a block of text
def extract_adjectives(text):
    words = word_tokenize(text)  # Break the text into word tokens
    tagger = PerceptronTagger()  # Initialize POS tagger
    tagged = tagger.tag(words)   # Assign POS tags to each token

    # Extract words with adjective tags (JJ: base, JJR: comparative, JJS: superlative)
    adjectives = [word.lower() for word, tag in tagged if tag in ('JJ', 'JJR', 'JJS')]
    return adjectives

# Dictionary of authors and their corresponding text files
# You can expand this to include more authors and books
authors = {
    "Leroux": "POTO.txt"  # Gaston Leroux's *The Phantom of the Opera*
}

# Dictionary to store adjective frequency counters for each author
all_adjectives = {}

# Process each author and their text file
for author, file_path in authors.items():
    print(f"Processing {author}...")

    text = load_text(file_path) # Load and clean the text
    adjectives = extract_adjectives(text)# Extract adjectives
    freq = Counter(adjectives)# Count adjective frequency
    all_adjectives[author] = freq# Store the results

    # Display the top adjectives used by the author
    print(f"\nTop adjectives for {author}:")
    for word, count in freq.most_common(22):# Adjust the number for a broader or narrower view
        print(f"{word}: {count}")
