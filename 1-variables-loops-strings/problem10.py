# > **Write a program that:**
# > - Takes a list of numbers as input
# > - Without using sort() or sorted()
# > - Sort the list using **Bubble Sort**

def sort_a_list():
    user_input = input("enter numbers with space: ")

    ls = [int(val) for val in user_input.split(" ")]

    print(f"Before: {ls}")
    for j in range(len(ls)):                              # repeat N times
        for i in range(len(ls)-1):                        # compare adjacent pairs
            if ls[i] > ls[i+1]:                           # if left > right
                ls[i], ls[i+1] = ls[i+1], ls[i]           # swap them
    
    print(f"After: {ls}")

sort_a_list()
