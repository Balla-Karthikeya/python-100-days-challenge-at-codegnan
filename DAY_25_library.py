# books and users

books = {
    101: ["The Alchemist", "Paulo Coelho", 12],
    102: ["Atomic Habits", "James Clear", 20],
    103: ["Rich Dad Poor Dad", "Robert Kiyosaki", 15],
    104: ["Think and Grow Rich", "Napoleon Hill", 10],
    105: ["The Power of Habit", "Charles Duhigg", 8],
    106: ["Deep Work", "Cal Newport", 14],
    107: ["Clean Code", "Robert C. Martin", 6],
    108: ["Python Crash Course", "Eric Matthes", 18],
    109: ["1984", "George Orwell", 9],
    110: ["To Kill a Mockingbird", "Harper Lee", 11]
}

Users={
    1001: {"name": "karthik", 'books_id': [101,103, 108] },
    1002: {"name": "karthikeya", 'books_id': [101,104, 109] }
}

# person class
class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    
    def add_book(self, book_obj:Book, quantity:int):
        if book_obj.id not in books:
            books[book_obj.id]=[book_obj.name, book_obj.author, quantity]
            return f"{book_obj.name} added successfully"
        else:
            return f"Book id already exists"
      
    pass

# book class 
class Book:
    def __init__(self, id, name, author):
        self.id=id
        self.name=name
        self.author=author
    #def show():
        #f"person ID is {self.Id} and NAME is {self.Name} and  AUTHOR is {self.Author}"

    pass

# users class

class Users(Person):
    def __init__(self,id,name):
        super().__init__(id,name)

    pass

# admin class
class Admin(Person):
    def __init__(self,id:int,name:str):
        super().__init__(id,name)

    def add_book(self, book_obj:Book, quantity:int):
        if book_obj.id not in books:
            books[book_obj.id]=[book_obj.name, book_obj.author, quantity]
            return f"{book_obj.name} added successfully"
        else:
            return f"Book id already exists"

    # add user to library
    def add_user(self,user_obj:Users):
        if user_obj.id not in Users:
            Users[user_obj.id]={'name':user_obj.name,'book_id':[]}
            return "User added successfully"
        # if user already exists
        return "User id already exists"

    
    def del_book(self, book_id):
        if book_id in books:
            # deleting book from books
            books.pop(book_id)
            return f"Book is {book_id} remove successfully"
        # if bookid not present in books
        return "Book id not found"
    
    def barrow_book(self, user_id, *book_ids):
        if user_id in Users:
            avialable_books=[]
            unavialable_books=[]
            for book_id in book_ids:
                if book_id in books:
                    quantity=books[book_id][2]
                    if quantity > 0:
                        # updating quantity 
                        books[book_id][2] -= 1
                        # add book to user
                        Users[user_id]['book_id'].append(book_id)
                        avialable_books.append({book_id:books[book_id][0]})
                    else:
                        unavialable_books.append({book_id:books[book_id][0]})
                else:
                    unavialable_books.append({book_id:books[book_id][0]})
            return f"Avaialable books are: {avialable_books} and unavialable books are :{unavialable_books}"
        return "user not found"
       

    def return_book(self, user_id, *book_ids):
        if user_id in Users:
            for book_id in book_ids:
                if book_id in books and Users[user_id]['book_ids']:   
                    # updating quantity 
                    books[book_id][2] += 1
                    # remove book from user
                    Users[user_id]['book_id'].remove(book_id)
            return f"all books returned successfully"
        return "user not found"


    def all_book(self):
        return books

    def total_users(self):
        return len(Users)


# main 

if __name__=="__main__":
    print("Welcome to the library")
    admin = Admin(101,"Karthikeyaa")
    while True:
        print("Select your operations: 1. Add Book /n 2. Register User /n 3.Barrow Books /n 4. Return Books /n 5. View All Books /n. 6.Total Users /n 7. Delete Book /n 8. Exit From Library")
        choice = int(input("Enter Your choice"))
        if choice == 1:
            book_id=int(input("Enter Bookid: "))
            book_name=input("Enter Book Name: ")
            author=input("Enter Author Name: ")
            stock=int(input("Enter the book quantity"))
            # creating books object
            book_obj=Book(id=book_id, name=book_name, author = author) 
            # add this book into library
            admin.add_book(book_obj=book_obj, quantity=stock)
            # add this book into library
            print(admin.add_book(book_obj=book_obj,quantity=stock))
        elif choice == 2:
            user_id=int(input("Enter User id: "))
            username=input("Enter User name:")
            user_object=Users(id=user_id,name=username)
            print(admin.add_user(user_obj=user_object))
        elif choice == 3:
            print("Your selected option is 3. Barrow Books")
            user_id=int(input("Enter User id: "))
            books_ids = list(map(int, input("Enter books ids").split()))
            print(admin.baroow_book(user_id=user_id, * books_ids))
        elif choice == 4:
            print("Your selected for return books")
            user_id=int(input("Enter User id: "))
            books_ids = list(map(int, input("Enter books ids").split()))
            print(admin.baroow_book(user_id=user_id, * books_ids))
        
        elif choice == 5:
            print("Your are selected option is 5. View all books")
            all_books=admin.all_book()
            print(f"BOOK ID | Book NAME | AUTHOR NAME  |  QUNATITY ")
            for book_id, details in all_books.items():
                print(f"{book_id} | {details[0]} | {details[1] | {details[2]}} ")

        elif choice == 6:
            print("your selected option is 6. Total users ")
            print(admin.total_users())

        elif choice == 7:
            print("your selected option is 7. Delete Book")
            book_id=int(input("Enter bookid: "))

        elif choice == 8:
            print("Your selected option is : 8. exit")
            print("Bye, your exited from library")
            break
        
        else:
            print("Invalid choice, Enter choice in between 1 to 8")




        



