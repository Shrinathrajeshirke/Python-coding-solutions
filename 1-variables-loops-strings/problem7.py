# > **Write a program that:**
# > - Takes a number N as input
# > - Prints this exact pattern:

# **Example:**
# ```
# Input: 5

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def pattern():
    n = int(input("enter a number: "))

    for i in range(1,n+1):
        print(f"{'* '*i}")

    for i in range(1,n):
        print(f"{'* '*(n-i)}")

pattern()