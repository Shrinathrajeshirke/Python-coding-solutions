# Write a decorator called timer that measures and prints
# how long a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result  = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Done!"

@timer
def fast_function():
    return sum(range(10000))

slow_function()
fast_function()