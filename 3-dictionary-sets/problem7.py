# # > **Write a program that:**
# # > - Takes a paragraph as input
# # > - Finds top 3 most frequent words
# # > - Ignores common words like
# # >   "the", "is", "a", "an", "and", "in"
# # > - Prints word frequency of top 3


def top_3_words():
    ignore_words = ["the", "is", "a", "an", "and", "in"]

    input_para = input("Enter a paragraph: ")

    word_count = {}

    for word in input_para.split(" "):
        if word not in ignore_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    word_count = sorted(word_count.items(),
           key=lambda x:x[1],
           reverse=True)

    top_3 = word_count[:3]
    
    print("Top 3 most frequent words: ")
    for count, (key, value) in enumerate(top_3, 1):
        print(f"{count}. {key} -> {value} times")
        
top_3_words()


# # 1. Dictionaries CANNOT be sliced!
# dict[:3]   # TypeError
# list[:3]   # Works!

# # 2. enumerate() for automatic counting!
# for i, item in enumerate(list, 1):
#     # i starts from 1 automatically!

# # 3. Always define counter OUTSIDE loop!
# count = 1          # outside 
# for item in list:
#     print(count)
#     count += 1