# Write a program that:

# Reads a file
# Counts:

# Total lines
# Total words
# Total characters
# Most frequent word


# Handles file not found error

def file_stats(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            count = 0
            words = 0
            chars = 0
            word_dict = {}
            for line in lines:
                count += 1
                chars += len(line.strip())
                words += len(line.strip().split())

                for word in line.strip().split():
                    if word not in word_dict:
                        word_dict[word] = 1
                    else:
                        word_dict[word] += 1
            most_frequent_word = max(word_dict, key=word_dict.get)          

        print("==== File Analysis ====")
        print(f"Total lines: {count}")
        print(f"Total words: {words}")
        print(f"Total characters: {chars}")
        print(f"most frequent word: {most_frequent_word} ({word_dict[most_frequent_word]} times)")
    except FileNotFoundError:
        print("File doesn't exist")

file_stats("test.txt")