# > **Write a program that:**
# > - Creates 2 sets of numbers
# > - Prints union, intersection, difference
# > - Checks if one set is subset of another
# > - Adds and removes elements from set

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"union: {set1 | set2}")

print(f"intersection: {set1 & set2}")

print(f"difference: {set1 - set2}")

set3 = {4,5}

print(f"is set3 subsset of set1? {set3.issubset(set1)}")

set1.add(9)
print(f"after adding 9 to set1: {set1}")

set1.remove(1)
print(f"after removing 1 from set1: {set1}")


# remove()  - throws error if element not found!
#set1.remove(99)   # KeyError!

# discard()  - safe, no error if not found!
#set1.discard(99)  # no error!