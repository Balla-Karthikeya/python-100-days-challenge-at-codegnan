class Book:
    def __init__(self, bookid, title, author):
        self.bookid = bookid
        self.title = title
        self.author = author
        self.is_available = True

    def book_details(self):
        return f"Book name is {self.title} and author name is {self.author}"

    def to_dict(self):
        return {
            "bookid": self.bookid,
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available
        }