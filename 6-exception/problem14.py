# Write a program that:

# Creates a ContactBook class
# Saves contacts to "contacts.txt"
# Operations:

# Add contact (name, phone, email)
# Search contact by name
# Delete contact
# Display all contacts


# Data persists between runs!

class ContactBook:
    def __init__(self, filename):
        self.filename = filename

    def add(self, name, phone, email):
        with open(self.filename, "a") as f:
            contact = f"{name},{phone},{email}\n"
            f.write(contact)

    def display(self):
        with open(self.filename, "r") as f:
            print("=== Contacts ===")
            lines = f.readlines()
            for contact in lines:
                name, phone, email = contact.strip().split(",")
                print(f"{name: ^10} | {phone: ^20} | {email: ^20}")

    def search(self, search_name):
        found = False
        try:
            with open(self.filename, "r") as f:
                contacts = f.readlines()
                for contact in contacts:
                    name, phone, email = contact.strip().split(",")
                    if name == search_name:
                        print(f"Found! {name: ^10} | {phone: ^20} | {email: ^20}")  
                        found = True
                        break
                if not found:
                    print("not found")
        except FileNotFoundError:
            print("File not found")        
    
    def delete(self, name):
        with open(self.filename, "r") as f:
            contact_list = []
            contacts = f.readlines()
            for contact in contacts:
                if name not in contact.strip().split(","):
                    contact_list.append(contact)

        with open(self.filename, "w") as f:
            for contact in contact_list:
                f.write(contact)


cb = ContactBook("contacts.txt")
cb.add("Ram", "9876543210", "ram@gmail.com")
cb.add("Sam", "8765432109", "sam@gmail.com")
cb.display()
cb.search("Ram")
cb.delete("Sam")
cb.display()

