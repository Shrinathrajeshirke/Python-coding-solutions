## Write a program that:

## Takes your name as input
## Takes your age as input
## Prints: "Hello [name]! In 10 years you will be [age+10] years old"

def welcome():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"Hello {name}! In 10 years you will be {age+10} years old")

welcome()