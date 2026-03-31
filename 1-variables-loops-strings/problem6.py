##> **Write a program that:**
##> - Takes a list of numbers
##> - Removes all duplicates
##> - Prints original list and new list
##> - Prints which numbers were duplicates

def duplicates():
    user_input = input("enter numbers separated by space: ")

    ls = user_input.split(" ")

    original_list = []

    for val in ls:
        original_list.append(int(val))

    new_list = []

    duplicate_nums = []

    for val in original_list:
        if val not in new_list:
            new_list.append(val)
        else:
            duplicate_nums.append(val)

    print(f"oringal list: {original_list}")
    print(f"new list: {new_list}")
    print(f"duplicate numbers: {duplicate_nums}")

duplicates()

