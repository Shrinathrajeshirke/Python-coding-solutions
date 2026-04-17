# Create a number analysis tool:

def analyze(*args):
    numbers = list(args)

    def factorial(n):
        if n==0:
            return 1
        return n*factorial(n-1)
    
    n = len(numbers)
    
    results = {
        "numbers": numbers,
        "Sum": sum(numbers),
        "Average": sum(numbers)/len(numbers),
        "Even nums": list(filter(lambda x: x%2==0, numbers)),
        "Odd nums": list(filter(lambda x: x%2!=0, numbers)),
        "Squares": list(map(lambda x:x**2, numbers)),
        "Factorial 5" : factorial(5) 
    }

    for key, value in results.items():
        print(f"{key}: {value}")

analyze(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)