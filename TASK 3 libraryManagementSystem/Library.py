class Library:
    def __init__(self):
        self.book = []
        
    def addBook(self, book):
        self.book.append(book)
    
    def displayBooks(self):
        for book in self.book:
            print(f"ID: {book.id}, Book Name: {book.book_name}, Author Name: {book.author_name}, Availability: {book.availability}")
    
    def searchBookById(self, id):
        for book in self.book:
            if book.id == id:
                return book
        return None
    def borrowBook(self, id):
        book = self.searchBookById(id)
        if book and book.availability:
            book.availability = False
            print(f"You have borrowed the book: {book.book_name}")
        else:
            print("Book not available for borrowing.")
    
    def returnBook(self, id):
        book = self.searchBookById(id)
        if book and not book.availability:
            book.availability = True
            print(f"You have returned the book: {book.book_name}")
        else:
            print("Book not found or already available.")