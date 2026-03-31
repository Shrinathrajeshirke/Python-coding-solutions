##> **Write a program that:**
##> - Takes a string as input
##> - Prints following things:
##>   - Length of string
##>   - String in UPPERCASE
##>   - String in lowercase
##>   - String reversed
##>   - Count of vowels in string

def string_details():
    word = input("enter a string: ")

    length_of_string = len(word)
    string_in_upper = word.upper()
    string_in_lower = word.lower()
    string_reversed = word[::-1]
    count_vowels = 0
    for letter in word:
        if letter.lower() in ['a','e','i','o','u']: ## missed lower case letters
            count_vowels+=1
    
    print(f"Length: {length_of_string} \nuppercase: {string_in_upper} \nlowercase: {string_in_lower} \nreversed: {string_reversed} \nvowel count: {count_vowels}")

string_details()