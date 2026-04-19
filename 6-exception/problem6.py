# Write a program that:

# Takes two numbers as input
# Handles these exceptions:

# ValueError (letters instead of numbers)
# ZeroDivisionError
# Shows success message if no error
# Always prints "Program ended" at end

def solve():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        result = a/b
    except ValueError:
        print("Enter a number")
    except ZeroDivisionError:
        print("Number can't be divided by zero")
    else:
        print(f"Result: {result}")
    finally:
        print("Program ended")

solve()