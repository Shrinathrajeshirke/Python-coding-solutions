# Build a word stream analyzer
# Keeps last 10 words in stream
# Shows:

# Current top 3 frequent words
# Words grouped by count
# Unique word count

from collections import deque, Counter, defaultdict

class WordAnalyzer:
    def __init__(self, window_size):
        self.window_size = window_size
        self.words_dq = deque(maxlen=window_size)

    def add(self, word):
        self.words_dq.append(word)
    
    def show(self):
        print("Output:")
        print("Last 10 words: ")
        print(", ".join(self.words_dq))
        counter = Counter(self.words_dq)
        print("Top 3 frequent (in window): ")
        for word, freq in counter.most_common(3):
            print(f"{word}: {freq}")
        grouped = defaultdict(list)
        for word, freq in counter.items():
            grouped[freq].append(word)
        print("Grouped by frequency: ")
        for freq, word_list in self.grouped.items():
            print(f"{freq} times: {", ".join(word_list)}")
        print(f"total unique words: {len(counter)}")

analyzer = WordAnalyzer(window_size=10)
words = ["apple","ball","cat","apple","dog",
         "ball","apple","cat","elephant","ball",
         "dog","cat"]

for word in words:
    analyzer.add(word)

analyzer.show()