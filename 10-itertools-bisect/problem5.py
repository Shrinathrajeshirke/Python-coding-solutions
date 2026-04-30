# Take a word as input
# Generate all permutations
# Find how many are valid English words
# (use a simple word list)

word = "ATE"
valid_words = ["ATE", "EAT", "TEA", "ETA"]

import itertools

def word_permuts(word, valid_words):
    perms = list(itertools.permutations(word))
    word_perms = []
    valid_count = 0
    for perm in perms:
        word_perms.append("".join(perm))
    print("Output")
    print("All permutations of 'ATE':")
    for w in word_perms:
        print(w)
    print("\nValid English words")
    for w in word_perms:
        if w in valid_words:
            valid_count += 1
            print(w)

    print(f"\nValid words found: {valid_count} out of {len(word_perms)}")

word_permuts(word, valid_words)