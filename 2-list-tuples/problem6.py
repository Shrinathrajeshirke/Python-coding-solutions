# > **Write a program that:**
# > - Takes 2 lists from user
# > - Prints common elements between them
# > - Prints elements only in list 1
# > - Prints elements only in list 2
# > - Prints combined unique elements


def elements():
    list_1= [1, 2, 3, 4, 5]
    list_2= [4, 5, 6, 7, 8]

    print(f"common elements: {list(set(list_1).intersection(set(list_2)))}")

    print(f"Only elements in list 1: {list(set(list_1).difference(set(list_2)))}")

    print(f"Only elements in list 2: {list(set(list_2).difference(set(list_1)))}")    
    
    print(f"Combined unique elements: {list(set(list_1).union(set(list_2)))}")

elements()