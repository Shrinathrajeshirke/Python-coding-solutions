# Write a function that converts a string to an integer. Use try, except, else, and finally in one block.

def string_to_int():
    

    try: 
        user_input = input("Enter a number: ")
        user_input = int(user_input)
    except ValueError:
        print("Enter a number again")
    else:
        print(user_input)
    finally:
        print("it's done")

string_to_int()