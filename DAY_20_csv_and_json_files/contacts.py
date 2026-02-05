# contact book library management system

def add_contact(name, phone):
    try:
        with open('contacts.txt', 'r') as f:
            contact_lines = f.readlines()
    except FileNotFoundError:
        contact_lines = []
    
    for contact in contact_lines:
        contact = contact.strip()
        contact_name, contact_number = contact.strip().split(maxsplit=1)
        if contact_name == name:
            return "Contact already exists"

    with open('contacts.txt', 'a') as f:
                f.write(f'{name} {phone}\n')
    return "Contact added successfully"

def view_contacts():
    try:
        with open('contacts.txt', 'r') as f:
            contact_lines = f.readlines()
    except:
        return "Error in view_contacts"
    
    if not contact_lines:
        print("no contacts found")
    else:
        for contact in contact_lines:
            contact = contact.strip()
            contact_name, contact_number = contact.split(maxsplit=1)
            print(f'{contact_name} : {contact_number}')

def delete_contact(name):
    try:
        with open('contacts.txt', 'r') as f:
            contact_lines = f.readlines()
    except:
        return "Error in delete_contact"
     
    with open('contacts.txt', 'w') as f:
        found = False
        for contact in contact_lines:
            contact = contact.strip()
            contact_name, contact_number = contact.split(maxsplit=1)
            if contact_name != name:
                f.write(f'{contact_name} {contact_number}\n')
            else:
                found = True
        if not found:
            return "Contact not found"
        return "Contact deleted successfully"

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        print(add_contact(name, phone))
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name to delete: ")
        print(delete_contact(name))
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")