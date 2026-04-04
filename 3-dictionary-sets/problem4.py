# > **Write a program that:**
# > - Takes a sentence as input
# > - Creates a dictionary where:
# >   - Key = word length
# >   - Value = list of words with that length
# > - Prints grouped words

def word_length():
    sent = input("enter a sentence: ")

    words = sent.split(" ")

    word_groups = {}

    for word in words:
        length = len(word)

        if length in word_groups:
           word_groups[length].append(word)
        else:
            word_groups[length] = [word]

    for length, words in sorted(word_groups.items()):
        print(f"Length {length} : {words}")

word_length()
