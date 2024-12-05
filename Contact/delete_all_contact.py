import save_contacts
from view_all_contacts import view_contacts


def delete_contactss(contacts):
    if not contacts:
        print("No contacts to delete.")
        return contacts

    view_contacts(contacts)
    try:
        selection = int(input("Enter the number of the contact to delete (or 0 to cancel): "))
        if selection == 0:
            return contacts
        elif 1 <= selection <= len(contacts):
            deleted = contacts.pop(selection - 1)
            print(f"Contact '{deleted['name']}' deleted successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Error: Please enter a valid number.")

    save_contacts.save_to_file(contacts)
    return contacts
