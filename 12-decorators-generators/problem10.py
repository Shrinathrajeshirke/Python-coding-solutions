# Combine decorators and generators together.
# Stack multiple decorators on a single function.

# Write two decorators:
# 1. timer - measures execution time
# 2. logger - logs function name, args and return value

# Then write a function that uses a generator internally
# to process a list of numbers.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time: .6f} seconds")
        return result
    return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@timer
@logger
def sum_of_squares(numbers):
    def squares_gen(nums):
        for n in nums:
            yield n ** 2
    return sum(squares_gen(numbers))

result = sum_of_squares([1, 2, 3, 4, 5])
print(f"Result: {result}")