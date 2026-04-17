# Try to open a file called data.txt. If it doesn't exist, print a friendly message.

def open_file(filename):
    try:
        f = open(filename, "r")
        f.read()

    except FileNotFoundError:
        print("File does not exist. Kindly check the file name again.")

open_file("data.txt")