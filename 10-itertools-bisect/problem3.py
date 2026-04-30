# Take 3 lists of numbers
# Combine them efficiently
# Find sum, max, min of combined list

import itertools

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]

def combine_lists(*args):
    cmb_ls = list(itertools.chain.from_iterable(args))
    print("Output")
    print(f"Combined: {cmb_ls}")
    print(f"Sum: {sum(cmb_ls)}")
    print(f"Max: {max(cmb_ls)}")
    print(f"Min: {min(cmb_ls)}")

combine_lists(list1, list2, list3)
