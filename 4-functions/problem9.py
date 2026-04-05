# > **Write a recursive function:**
# > - Takes a list of numbers
# > - Finds maximum number
# > - Using recursion only!
# > - No max() or sort()!


def find_max(ls):
    if len(ls) == 0:
        return None
    if len(ls) == 1:
        return ls[0]
    
    rest_max = find_max(ls[1:])
    if ls[0] > rest_max:
        return ls[0]
    else:
        return rest_max 

print(find_max([3, 7, 1, 9, 4, 6]))