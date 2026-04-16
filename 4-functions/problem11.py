# Write a recursive function that:

# Takes a string as input
# Checks if it is palindrome
# Using recursion only!
# No slicing like [::-1]!

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Then print with original word!
word = "NAYAN"
if is_palindrome(word):
    print(f"{word} is palindrome!")
else:
    print(f"{word} is not palindrome!")