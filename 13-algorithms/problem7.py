# Implement linear search that returns all indices 
# where target is found.

def linear_search(arr, target):
    result = []
    for i, ele in enumerate(arr):
        if ele == target:
            result.append(i)
    return result
        
print(linear_search([4,2,7,2,9,2,1], 2))

print(linear_search([1,2,3,4,5], 6))

print(linear_search([5,5,5,5], 5)) 
