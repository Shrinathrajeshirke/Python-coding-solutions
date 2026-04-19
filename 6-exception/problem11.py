# Write a program that:

# Creates a simple note taking app
# Saves notes to "notes.txt"
# Operations:

# Add note
# View all notes
# Clear all notes
# Exit

def notes(filename):
    while True:
        try: 
            user_input = int(input("Choose option: 1-Add notes, 2-View notes, 3-Clear notes, 4-get out of loop: \n"))
        except ValueError:
            print("Enter a number between 1-4")

        if user_input == 1:
            with open(filename, "a") as f:
                note = input("Enter a note: \n")
                f.write(note + '\n')
            print("note saved")
        
        elif user_input == 2:
            try:
                with open(filename, "r") as f:
                    lines = f.readlines()
                    if not lines:
                        print("no lines yet")
                    else:
                        print("==== Your notes ====")
                        for i, line in enumerate(lines,1):
                            print(f"{i}: {line}")
            except FileNotFoundError:
                print("File not found")

        elif user_input == 3:
            with open(filename, "w") as f:
                pass
            print('Note cleared')
        
        elif user_input==4:
            print("Good Bye!")
            break
            
        else:
            print("Invalid input")

notes("notes.txt")    