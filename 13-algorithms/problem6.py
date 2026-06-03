# Implement quick sort algorithm from scratch.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x<=pivot]
    right = [x for x in arr[:-1] if x> pivot]
    mid = [x for x in arr if x==pivot]

    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([38, 27, 43, 3, 9, 82, 10]))

print(quick_sort([5, 4, 3, 2, 1]))
