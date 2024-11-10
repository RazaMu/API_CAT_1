# Class for representing a book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

# Class for representing a library member
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books and book.mark_as_returned():
            self.borrowed_books.remove(book)
            print(f"{self.name} successfully returned '{book.title}'.")
        else:
            print(f"'{book.title}' is not borrowed by {self.name}.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")

# Sample books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Sample library member
member = LibraryMember("Alice", "M001")

# Interactive menu function
def menu():
    while True:
        print("\nLibrary System Menu")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the title of the book to borrow: ")
            if title == "1984":
                member.borrow_book(book1)
            elif title == "To Kill a Mockingbird":
                member.borrow_book(book2)
            elif title == "The Great Gatsby":
                member.borrow_book(book3)
            else:
                print("Book not found.")
        
        elif choice == '2':
            title = input("Enter the title of the book to return: ")
            if title == "1984":
                member.return_book(book1)
            elif title == "To Kill a Mockingbird":
                member.return_book(book2)
            elif title == "The Great Gatsby":
                member.return_book(book3)
            else:
                print("Book not found.")
        
        elif choice == '3':
            member.list_borrowed_books()
        
        elif choice == '4':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid option. Please try again.")

# Run the menu function to start the program
menu()
