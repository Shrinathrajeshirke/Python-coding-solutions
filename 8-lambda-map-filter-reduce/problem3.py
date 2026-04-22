# Find product of all numbers
# Find maximum number
# Find minimum number
# All using reduce() only!
# No max(), min(), or loops!

from functools import reduce

def number_fn(numbers):
    product = reduce(lambda x,y : x*y, numbers, 1)
    max_num = reduce(lambda x,y : x if x>y else y, numbers)
    min_num = reduce(lambda x,y: x if  x<y else y, numbers)
    return product, max_num, min_num

product_of_numbers, maximum_number, minimum_number = number_fn([3, 7, 2, 9, 4, 6])
print(f"Product: {product_of_numbers}")
print(f"Maximum number: {maximum_number}")
print(f"Minimum number: {minimum_number}")