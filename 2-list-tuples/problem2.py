# > **Write a program that:**
# > - Creates a list of 5 numbers
# > - Adds a number at end
# > - Adds a number at position 2
# > - Removes a specific number
# > - Prints length of list
# > - Prints final list

def list_ops():
    original_list = [10, 20, 30, 40, 50]
    print(f"Original list: {original_list}")

    original_list.append(60)

    print(f"After append 60: {original_list}")

    original_list.insert(2, 99)

    print(f"After insert at 2: {original_list}")

    original_list.remove(30)

    print(f"After remove 30: {original_list}")

    print(f"Length: {len(original_list)}")

    print(f"Final list: {original_list}")

list_ops()
