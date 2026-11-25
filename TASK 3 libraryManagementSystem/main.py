from Book import Book
from Library import Library

library = Library()


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer ID.")


while True:
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book by ID")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = get_integer_input("Enter book ID: ")
        if library.searchBookById(id):
            print("Book with this ID already exists. Please use a different ID.")
            continue
        book_name = input("Enter book name: ")
        author_name = input("Enter author name: ")
        availability_status = True  # New books are available by default
        new_book = Book(id, book_name, author_name, availability_status)
        library.addBook(new_book)
        print("Book added successfully.")

    elif choice == "2":
        library.displayBooks()

    elif choice == "3":
        id = get_integer_input("Enter book ID to search: ")
        book = library.searchBookById(id)
        if book:
            print(f"ID: {book.id}, Book Name: {book.book_name}, Author Name: {book.author_name}, Availability: {book.availability}")
        else:
            print("Book not found.")

    elif choice == "4":
        id = get_integer_input("Enter book ID to borrow: ")
        library.borrowBook(id)

    elif choice == "5":
        id = get_integer_input("Enter book ID to return: ")
        library.returnBook(id)

    elif choice == "6":
        break

    else:
        print("Invalid choice. Please try again.")