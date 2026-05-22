# Write a decorator called retry that automatically retries 
# a function if it raises an exception.

# The decorator takes a parameter for number of retries.

import random

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {i+1} Connection failed with an error: {e}.")
            print("All retries exhausted")
            raise last_exception 
        return wrapper
    return decorator
    
@retry(times=3)
def unstable_function():
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Connection failed!")
    return "Success!"

result = unstable_function()
print(result)
