# Implement binary search algorithm from scratch.

def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

arr = [11, 12, 22, 25, 34, 64, 90]

print(binary_search(arr, 25)) 
print(binary_search(arr, 90))  
print(binary_search(arr, 100))  

