from library.models import Book

class LibraryServices:
    def __init__(self):
        self.books = {}

    def addBook(self, title, author):
        book_id = len(self.books) 
        book = Book(book_id, title, author)
        self.books[book_id] = book
        return f"Book '{title}' added successfully. ID: {book_id}"

    def removeBook(self, bookid):
        if bookid in self.books:
            del self.books[bookid]
            return "Book removed successfully"
        return "Book not found"

    def borrowBook(self, bookid):
        if bookid in self.books:
            book = self.books[bookid]
            if book.is_available:
                book.is_available = False
                return "Book borrowed successfully"
            return "Book is already borrowed"
        return "Book not found"

    def returnBook(self, bookid):
        if bookid in self.books:
            book = self.books[bookid]
            if not book.is_available:
                book.is_available = True
                return "Book returned successfully"
            return "Book was not borrowed"
        return "Book not found"

    def get_available_books(self):
        available = [
            book.to_dict()
            for book in self.books.values()
            if book.is_available
        ]
        return available