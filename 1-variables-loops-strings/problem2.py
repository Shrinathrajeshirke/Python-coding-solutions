## **Write a program that:**
## Takes a number N as input
## Prints multiplication table of that number till 10

def table_of_num():
    n = int(input("Enter a number: "))

    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

table_of_num()