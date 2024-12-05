import add_contacts
import view_all_contacts
import update_contacts
import delete_all_contact
import load_contacts
import save_contacts
import search_contacts

# Load contacts at the start
all_contacts = load_contacts.load_all_contacts()

while True:
    print("\nContact Book Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("0. Exit")

    choice = input("Select an option: ")
    if choice == "1":
        all_contacts = add_contacts.add_contactss(all_contacts)
    elif choice == "2":
        view_all_contacts.view_contacts(all_contacts)
    elif choice == "3":
        all_contacts = update_contacts.update_contactss(all_contacts)
    elif choice == "4":
        all_contacts = delete_all_contact.delete_contactss(all_contacts)
    elif choice == "5":
        search_contacts.search_contacts(all_contacts)
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")


