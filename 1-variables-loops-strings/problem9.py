# > **Write a program that:**
# > - Takes a sentence as input
# > - Reverses each word individually
# > - But keeps the word order same

def reverse_by_word():
    sent = input("Enter a sentence: ")

    words = sent.split(" ")

    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    reversed_sent = " ".join(reverse_words)

    print(reversed_sent)

reverse_by_word()