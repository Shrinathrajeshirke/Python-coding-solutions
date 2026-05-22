# Write a decorator called validate_range that accepts 
# min_val and max_val parameters and raises ValueError 
# if the function's return value is outside the range.

def validate_range(min_val, max_val):
    def decorator(func):
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            if result < min_val or result > max_val:
                raise ValueError(f"{result} is out of range ({min_val}, {max_val})")
            return result
        return wrapper
    return decorator

@validate_range(min_val=0, max_val=100)
def get_score(score):
    return score

@validate_range(min_val=0, max_val=100)
def calculate_percentage(value, total):
    return (value / total) * 100
try:
    print(get_score(85))        # valid
except ValueError as e:
    print(f"ValueError: {e}")
try:
    print(get_score(105))       # should raise ValueError
except ValueError as e:
    print(f"ValueError: {e}")
try:
    print(calculate_percentage(45, 50))   # valid
except ValueError as e:
    print(f"ValueError: {e}")
try:
    print(calculate_percentage(55, 50)) 
except ValueError as e:
    print(f"ValueError: {e}")