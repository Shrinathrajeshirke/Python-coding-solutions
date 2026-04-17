# Ask for a number. If the user types a string, catch the error and ask again.

def input_number():
    try:
        user_input = int(input("Enter a number: "))
    except ValueError:
        print("Incorrect input. Enter a number again.")
    
input_number()