# Using Counter and defaultdict together:

# Take a list of words
# Find word frequency
# Group words by frequency
# Display in organized format

words = ['apple', 'ball', 'cat', 'apple', 'dog', 'ball', 'apple', 'cat', 'elephant', 'ball']

from collections import Counter, defaultdict

def word_freq(words):
    freq_words = dict(Counter(words))
    word_dict = defaultdict(list)

    for word, freq in freq_words.items():
        word_dict[freq].append(word)
    
    print("Output:")
    print("Word frequency")
    for word, freq in freq_words.items():
        print(f"{word} -> {freq}")
    print("")
    print("Grouped by frequency: ")
    for freq, word_list in word_dict.items():
        print(f"{freq} -> {", ".join(word_list)}")
    
word_freq(words)