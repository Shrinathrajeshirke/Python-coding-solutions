##> **Write a program that:**
##> - Takes N numbers from user and stores in a list
##> - Prints:
##>   - Smallest number
##>   - Largest number
##>   - Sum of all numbers
##>   - Average of all numbers

def num_calc():
    n = int(input("How many numbers: "))
    ls = []

    for i in range(n):
        ls.append(int(input("enter a number: ")))
    
    print(f"Smallest: {min(ls)} \nLargest: {max(ls)} \nsum: {sum(ls)} \nAverage: {sum(ls)/n}")
    
num_calc()