# > **Write a program that:**
# > - Takes a word as input
# > - Creates a dictionary with each letter as key
# > - And count of that letter as value


def word_dict():
    word = input("Enter a word: ")

    count_letters = {}
    for letter in word:
        if letter in count_letters.keys():
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1
    
    for letter, count in count_letters.items():
        print(f"{letter} -> {count}")

word_dict()