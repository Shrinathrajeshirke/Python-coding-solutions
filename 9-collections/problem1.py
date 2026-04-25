# Take a string as input
# Count frequency of each character
# Find the 3 most common characters
# Find characters that appear only once


text = "hello world programming"

from collections import Counter

def text_counter(text):
    char_count = Counter(text)
    most_common_3 = char_count.most_common(3)

    print("Output: ")
    print("Character count: ")
    print(dict(char_count))
    print("Top 3 most common")
    for letter, count in most_common_3:
        print(f"{letter} -> {count}")
    print("Character appearing once: ")
    once = []
    for letter, count in char_count.items():
        if count == 1:
            once.append(letter)
    print(", ".join(once))

text_counter(text)