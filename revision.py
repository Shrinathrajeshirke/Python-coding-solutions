# Write a function that takes a string and returns 
# how many vowels are in it. Case insensitive.
print("Program 1")
def count_vowels(word):
    count = 0
    for letter in word:
        if letter.upper() in 'AEIOU':
            count += 1
    return count

print(count_vowels("Hello World"))
print(count_vowels("Python"))   
print(count_vowels("AEIOU"))    

print("=========================================")

# Write a function that takes a list of numbers and 
# returns a tuple containing:
# - minimum value
# - maximum value  
# - average (rounded to 2 decimal places)

print("Program 2")

def list_stats(input_ls):
    min_val = min(input_ls)
    max_val = max(input_ls)
    avg = round(sum(input_ls)/len(input_ls),2)
    stats = (min_val, max_val, avg)
    return stats

print(list_stats([4, 7, 2, 9, 1, 5]))
print(list_stats([10, 20, 30]))
print(list_stats([5]))

print("=========================================")

# Write a function that takes two lists and returns 
# a dictionary with:
# - "common": elements that appear in both lists
# - "only_in_first": elements only in first list
# - "only_in_second": elements only in second list

print("Program 3")

def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    result = {}
    result["common"] = set1.intersection(set2)
    result["only_in_first"] = set1.difference(set2)
    result["only_in_second"] = set2.difference(set1)
    return result

print(compare_lists([1,2,3,4,5], [3,4,5,6,7]))

print("=========================================")

print("Program 4")

# Write a recursive function that calculates 
# the sum of digits of a number.

def sum_digits(number):
    if number < 10:
        return number
    else:
        return (number%10) + sum_digits(number//10)
    
print(sum_digits(123))
print(sum_digits(9999))
print(sum_digits(0))
print(sum_digits(105))  

print("=========================================")

# Create a class BankAccount with:
# - Attributes: owner, balance (default 0)
# - deposit(amount) - adds to balance
# - withdraw(amount) - deducts from balance, 
#   raises ValueError if insufficient funds
# - __str__ - returns "owner's account: $balance"

print("Program 5")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        try: 
            if self.balance < amount:
                raise ValueError("ValueError: Insufficient funds")
            self.balance -= amount
        except ValueError as e:
            print(f"{e}")
    
    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"
    
acc = BankAccount("John")
acc.deposit(500)
acc.withdraw(200)
print(acc)          
acc.withdraw(500) 

print("=================================================")

print("Program 6")

# Write a function that reads a file safely and 
# returns its word count. Handle all possible errors.

def count_words_in_file(filename):
        if not filename:
                return "Error: No filename provided"
        try:
            with open(filename, "r") as f:
                content = f.read()
                return len(content.strip().split())
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"

print(count_words_in_file("existing.txt")) 
print(count_words_in_file("nonexistent.txt"))
print(count_words_in_file(""))  

print("=================================================")

print("Program 7")

# Using only lambda, map, filter and reduce solve these:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def squares(numbers):
    return list(map(lambda x: x**2, numbers))

def odds(numbers):
    return list(filter(lambda x: x%2!= 0, numbers))

from functools import reduce
def mult(numbers):
    res = reduce(lambda x,y: x*y, numbers, 1)
    return res

print(squares(numbers))
print(odds(numbers))
print(mult(numbers))
# 1. Square all numbers → [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 2. Keep only odd numbers → [1, 3, 5, 7, 9]
# 3. Multiply all numbers together → 3628800

print("=================================================")

print("Program 8")
# Given a list of words, use Collections module to:
# 1. Count frequency of each word
# 2. Find 3 most common words
# 3. Group words by their first letter using defaultdict
from collections import Counter, defaultdict
words = ["apple", "banana", "avocado", "blueberry", 
         "cherry", "apricot", "banana", "apple", 
         "cherry", "apple"]

def freq_word(words):
    first_letter_dict = defaultdict(list)
    word_freq = Counter(words)
    for word in words:
        first_letter_dict[word[0]].append(word)
    print(f"Word frequencies: \n{word_freq}")
    print(f"Three most common: \n{word_freq.most_common(3)}")
    print(f"Grouped by first letter: \n{dict(first_letter_dict)}")

freq_word(words)


print("=================================================")

print("Program 9")
# Using itertools solve these:

# 1. Find all possible 2-person teams
# 2. Find all possible arrangements of the team
# 3. Find all possible pairs of (team member, role) where 
from itertools import combinations, permutations, product

team = ["Alice", "Bob", "Charlie"]
roles = ["Dev", "Designer"]

def team_arrangements(team, roles):
    combine_teams = list(combinations(team, 2))
    permute_teams = list(permutations(team))
    all_pairs = list(product(team, roles))

    return combine_teams, permute_teams, all_pairs

person_teams, arrange_teams, all_possible_pairs = team_arrangements(team, roles)
print(f"All possible 2-person teams: {person_teams}")
print(f"All possible arrangements: {arrange_teams}")
print(f"All possible (member, role) pairs: {all_possible_pairs}")

print("=================================================")

print("Program 10")
# Write a function that validates an email address 
# and extracts its components.

import re
def parse_email(email):
    pattern = r"(?P<user>[a-zA-Z0-9._]+)@(?P<domain>[a-zA-Z0-9.-]+)\.(?P<extension>[a-zA-Z]{2,6})"
    result = {}
    match = re.match(pattern, email)
    if not match:
        result['valid'] = False
    if match:
        result['valid'] = True
        result['user'] = match.group('user')
        result['domain'] = match.group('domain')
        result['extension'] = match.group('extension')
    return result

print(parse_email("user.name@example.com"))

print(parse_email("invalid@email"))

print(parse_email("test@site.org"))

print("=================================================")

print("Program 11")

# Write a decorator called uppercase that converts 
# the return value of a function to uppercase.

def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"hello, {name}!"

@uppercase
def get_city():
    return "new york"

print(greet("john"))  
print(get_city())  

print("=================================================")

print("Program 12")

# Write a generator function called number_range that 
# mimics Python's range() but yields only numbers 
# divisible by a given divisor.

def number_range(start, stop, divisor):
    for num in range(start, stop):
        if num%divisor == 0:
            yield num

for n in number_range(1, 20, 3):
    print(n, end=" ")
print("\n")

for n in number_range(0, 50, 10):
    print(n, end=" ")