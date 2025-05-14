import nltk

# Load text from a file
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

print(words[:10])  # Print first 10 words
