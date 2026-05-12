# Extract and Count Words:

# Extract all words from text
# Count frequency of each word
# Show top 5 most common words
# Case insensitive

text = """
Python is great. Python is easy to learn.
I love Python programming. Python makes coding fun.
"""

import re
from collections import Counter

def word_analyzer(text):
    pattern = r"\w+"

    words = re.findall(pattern, text.lower())

    words_dict = Counter(words)
    
    print("Output")
    print(f"Total words: {len(words)}\n")
    print("Word frequency")
    for w, f in words_dict.items():
        print(f"{w} -> {f}")
    print("\n")
    
    print("Top 5 words")
    top_5 = words_dict.most_common(5)
    for t in top_5:
        word, freq = t
        print(f"{word} -> {freq}")
       

word_analyzer(text)
