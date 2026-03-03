from library.services.auth_services import AuthServices
from library.services.library_services import LibraryServices

auth = AuthServices()
library = LibraryServices()


def main_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Register User")
    print("2. Register Admin")
    print("3. Login")
    print("4. Add Book (Admin only)")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. View Available Books")
    print("8. Logout")
    print("9. Exit")


while True:
    main_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        print(auth.registerUser(name, email, password))

    elif choice == "2":
        name = input("Enter admin name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        print(auth.registerAdmin(name, email, password))

    elif choice == "3":
        user_id = int(input("Enter user ID: "))
        password = input("Enter password: ")
        print(auth.login(user_id, password))

    elif choice == "4":
        if auth.current_user and auth.current_user.manage_book():
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            print(library.addBook(title, author))
        else:
            print("Only Admin can add books!")

    elif choice == "5":
        book_id = int(input("Enter Book ID: "))
        print(library.borrowBook(book_id))

    elif choice == "6":
        book_id = int(input("Enter Book ID: "))
        print(library.returnBook(book_id))

    elif choice == "7":
        books = library.get_available_books()
        if books:
            for book in books:
                print(book)
        else:
            print("No available books")

    elif choice == "8":
        print(auth.logout())

    elif choice == "9":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")