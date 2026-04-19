# Write a program that:

# Creates a list of 5 numbers
# Asks user for an index
# Handles these exceptions:

# IndexError (index out of range)
# ValueError (not a number)
# TypeError (wrong type)

def list_exceptions(ls):
    try:
        index = int(input("Enter a index position: "))
        result = ls[index]
    except IndexError:
        print("Index out of range")
    except ValueError:
        print("Incorrect input. Enter a number as index: ")
    except TypeError:
        print("input provided type is wrong")
    else:
        print(f"Element at {index}: {result}")
    finally:
        print("Program ended")

list_exceptions([1,2,3,4,5])