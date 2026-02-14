class Book:
    def __init__(self, bookid, title, author):
        self.bookid = bookid
        self.title = title
        self.author=author
        self.is_available=True

    # get book details 
    def book_details(self):
        return f"Book name is {self.title} and author name is {self.author}"
    
    # convert book details to dictionary 
    def to_dict(self):
        book = {}        
        book["bookid"] = self.book_id
        book['title']=self.title
        book['author']=self.author
        book['is_available']=True
        return book
        pass
