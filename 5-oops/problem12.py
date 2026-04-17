# Create a class Calculator with:

# No attributes in init
# Methods: add, subtract, multiply, divide
# Each method takes 2 numbers
# Returns result
# Divide should handle zero division

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return "denominator can't be 0."
    

cl = Calculator()

print(cl.add(4,5))

print(cl.subtract(4,5))

print(cl.multiply(4,5))

print(cl.divide(4,5))

print(cl.divide(4,0))
    
