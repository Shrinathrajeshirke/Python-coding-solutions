# Using defaultdict:

# Take a list of words
# Group words by their first letter
# Display grouped words

words = ['apple', 'ant', 'ball', 'bat', 'cat', 'cow', 'dog', 'apple', 'bear']

from collections import defaultdict

def group_by_first_letter(words):
    grouped = defaultdict(list)

    for word in words:
        grouped[word[0]].append(word)

    print('Output: ')
    print("Grouped by first letter: ")
    for letter, words_list in grouped.items():
        print(f"{letter} -> {words_list}")

group_by_first_letter(words)
