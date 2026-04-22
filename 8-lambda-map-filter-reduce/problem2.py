# Using lambda and filter():

# Take a list of words
# Filter words that:

# Are longer than 4 letters
# Start with a vowel

def words_fn(words):
    print("Output: ")
    print(f"Words: {words}")

    print(f"Words longer than 4 letters: {list(filter(lambda x: len(x)>4, words))}")
    print(f"Words starting with vowels: {list(filter(lambda x: x[0].lower() in ['a','e','i','o','u'], words))}")

words_fn(["apple","cat","orange","is","elephant","an","umbrella","dog"])