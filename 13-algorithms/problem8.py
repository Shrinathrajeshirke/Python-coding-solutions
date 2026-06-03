# Write a function that takes an unsorted list, 
# sorts it using any sorting algorithm, then uses 
# binary search to find a target.

def sort_and_search(arr, target):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            return (arr, mid)
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return (arr,-1)

print(sort_and_search([64, 34, 25, 12, 22, 11, 90], 25))
print(sort_and_search([64, 34, 25, 12, 22, 11, 90], 100))