from view_all_contacts import view_contacts


def search_contacts(contacts):
    query = input("Enter a name, email, or phone number to search: ").strip().lower()
    results = [contact for contact in contacts if
               query in contact['name'].lower() or query in contact['email'].lower() or query in contact['phone']]

    if results:
        print("\nSearch Results:")
        view_contacts(results)
    else:
        print("No matching contacts found.")
