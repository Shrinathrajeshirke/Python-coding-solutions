# > **Write a program that:**
# > - Creates a phone book dictionary
# > - Supports these operations:
# >   - Add a contact
# >   - Search a contact
# >   - Delete a contact
# # >   - Display all contacts

def contact_book():

    phone_book = {"a":12345, "b": 78910, "c":879467}

    while True:
        print("1. Add contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. All Contacts")
        print("5. Good Bye")
        try:
            choice = int(input("Choose: "))
        except:
            print("please enter a number 1-5")
            continue

        if choice == 1:
            name = input("Enter a name: ")
            number = input("Enter mobile number: ")

            phone_book[name] = number
        
        elif choice == 2:
            name = input("Enter a name: ")
            if name in phone_book.keys():
                print(f"{name} -> {phone_book[name]}")
            else:
                print(f"{name} not found")
        
        elif choice == 3:
            name = input("Enter a name: ")
            if name in phone_book.keys():
                phone_book.pop(name)
                print(f"{name} deleted")
            else:
                print(f"{name} not found")
        
        elif choice == 4:
            if not phone_book:
                print("Phone book is empty!")
            else:
                print("All contacts: ")
                for name, number in phone_book.items():
                    print(f"{name} -> {number}")

        elif choice == 5:
            print("Good Bye!")
            break

contact_book()



