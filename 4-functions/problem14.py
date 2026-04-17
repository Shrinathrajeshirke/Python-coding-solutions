# Write a function that:

# Takes a sentence as input
# Using lambda and functions
# Performs all these operations:

# Remove extra spaces
# Capitalize first letter of each word
# Count words
# Reverse each word
# Find longest word

def lambda_functions():
    sentence = input("Enter a sentence: ")

    clean = lambda s: " ".join(s.split())
    count = lambda s: len(s.split())
    capitalize_sent = lambda s: " ".join(w.capitalize() for w in s.split())
    reversed_sentence = lambda s: " ".join(w[::-1] for w in s.split())
    longest_word = lambda s: max(s.split(), key=len)

    cleaned = capitalize_sent(clean(sentence))
    print("Output: ")
    print(f"Cleaned: {cleaned}")
    print(f"count: {count(cleaned)}")
    print(f"capitalize: {cleaned}")
    print(f"reversed: {reversed_sentence(cleaned)}")
    print(f"longest word: {longest_word(cleaned)}")

lambda_functions()

