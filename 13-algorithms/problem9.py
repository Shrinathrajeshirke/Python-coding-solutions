# Write a function that finds all duplicate elements 
# in a list using sorting approach.

def find_duplicates(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    duplicates = []

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] not in duplicates:
            duplicates.append(arr[i])
    return duplicates

print(find_duplicates([4, 2, 7, 2, 9, 4, 1, 7]))

print(find_duplicates([1, 2, 3, 4, 5]))

print(find_duplicates([1, 1, 1, 1]))