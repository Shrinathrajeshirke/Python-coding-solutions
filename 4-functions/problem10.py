# > **Write a function based calculator:**
# > - Separate function for each operation
# > - add, subtract, multiply, divide
# > - One main function that takes
# >   operation name and numbers
# > - Uses functions as dictionary values!

def calculate(operation, x,y):
    operations = {
        "add" : lambda x, y: x+y,
        "subtract": lambda x,y : x-y,
        "multiply": lambda x,y: x*y,
        "divide": lambda x,y: "Can't divide by 0" if y==0 else x/y
    }

    if operation in operations:
        return operations[operation](x, y)
    else:
        return "operation not found"
    
print(calculate("add", 10, 5))       
print(calculate("subtract", 10, 5))
print(calculate("multiply", 10, 5))
print(calculate("divide", 10, 5))
print(calculate("divide", 10, 0))   
print(calculate("power", 10, 5))    