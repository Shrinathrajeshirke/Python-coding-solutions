# Ask for two numbers and divide them. Handle the error if the user divides by zero.

def divide_two_nums():

    try:
        num1 = int(input("Enter a number to divide: "))
        num2 = int(input("Enter a number for division: "))
        result = num1/num2
    except ZeroDivisionError:
        print("Division by 0 is not possible")

divide_two_nums()

    