##> **Write a program that:**
##> - Takes a sentence as input
##> - Counts how many words are in it
##> - Prints the longest word
##> - Prints each word with its length

def sent_info():
    sent = input("Enter a sentence: ")

    words = sent.split(" ")

    print(f"Number of words: {len(words)}")
    
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    
    max_length = max(word_lengths.values())
    for k,v in word_lengths.items():
        if v==max_length:
            print(f"longest word: {k}")

    for word in words:
        print(f"{word}: {len(word)}")

sent_info()