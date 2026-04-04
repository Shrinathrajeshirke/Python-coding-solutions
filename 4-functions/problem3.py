# > **Write a function using \*args:**
# > - Function called `calculate`
# > - Takes operation and any numbers
# > - Performs that operation on all numbers


def calculate(operation, *args):
    result = 1
    
    if operation == "sum":
        total = sum(args)
        return total
    elif operation == "multiply":
        for num in args:
            result *= num
        return result
    elif operation == "average":
        avg = sum(args)/len(args)
        return avg
    else:
        return "incorrect operation provided"

print(calculate("sum", 1, 2, 3, 4, 5))
print(calculate("multiply", 2, 3, 4))
print(calculate("average", 10, 20, 30))