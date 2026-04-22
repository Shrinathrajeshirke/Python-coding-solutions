# Using map() and filter():

# Take a list of sentences
# Filter sentences that have
# more than 5 words
# Map to get word count of each
# Sort by word count!

sentences = [
    "Python is great",
    "I love coding in Python every day",
    "Hello World",
    "Learning programming is fun and rewarding",
    "Hi",
    "Map filter and reduce are powerful tools in Python"
]

def sort_sent(sent):
    sent_more_than_5_words = list(filter(lambda x: len(x.split())>5 , sent))

    sent_len = list(map( lambda x: (x,len(x.split())), sent_more_than_5_words))

    sorted_sent = sorted(sent_len, key = lambda x: x[1])

    print("Output: ")
    print("longest sentences: ")
    for sent, length in sent_len:
        print(f"{sent} -> {length}")

    print("Sorted by word count: ")
    for sent, length in sorted_sent:
        print(f"{sent} -> {length}")

sort_sent(sentences)

