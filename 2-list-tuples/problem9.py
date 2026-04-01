# > **Write a program that:**
# > - Creates a list of numbers
# > - Rotates the list by K positions to the left
# > - Without using any built-in rotate functions


def rotate_list_by_k_positions():
    original_list = [1,2,3,4,5]

    k = int(input("enter a value to rotate list: "))

    k = k % len(original_list)
    rotated_list = original_list[k:]+original_list[:k]
    print(f"Original list: {original_list}")
    print(f"Output: {rotated_list}")

rotate_list_by_k_positions()