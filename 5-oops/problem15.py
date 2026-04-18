# Create a class Library with:

# Attributes: name, books (dictionary)

# key = book name
# value = available copies


# Method: add_book(book, copies)
# Method: issue_book(book)

# reduces copy by 1
# prints "Not available" if 0 copies


# Method: return_book(book)

# increases copy by 1


# Method: show_books()

# shows all books and copies


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book, copies):
        if book in self.books.keys():
            self.books[book] += copies
        else:
            self.books[book] = copies

    def issue_book(self, book):
        if book in self.books.keys():
            if self.books[book] >0:
                self.books[book] -= 1
                print(f"{book} issued")
            else:
                print(f"{book} is not availabel")
        else:
            return "Book not found"
    
    def return_book(self, book):
        if book in self.books.keys():
            self.books[book] += 1
            print(f"{book} returned")
        else:
            print(f"{book} is not avaialable")


    def show_books(self):
        print("Output: ")
        print(f"=== {self.name} ===")
        for book, copies in self.books.items():
            print(f"{book} -> {copies} copies")

lib = Library("City Library")
lib.add_book("Python", 3)
lib.add_book("Java", 2)
lib.issue_book("Python")
lib.show_books()