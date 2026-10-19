"""Assignment 1: a simple contact book using a dictionary."""

# The contact name is the key and the phone number is the value.
contacts = {}


def show_menu():
    print("\nCONTACT BOOK")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Show all contacts")
    print("0. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        if name and phone:
            contacts[name] = phone
            print("Contact added.")
        else:
            print("Name and phone number cannot be empty.")

    elif choice == "2":
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to update: ").strip()
        if name in contacts:
            contacts[name] = input("Enter new phone number: ").strip()
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        if contacts:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("There are no contacts yet.")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Please choose a number from the menu.")
