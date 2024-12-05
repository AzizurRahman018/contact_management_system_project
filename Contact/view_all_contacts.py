def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print(f"{'Name':<20}{'Email':<30}{'Phone':<15}{'Address':<20}")
    print("=" * 85)
    for contact in contacts:
        print(f"{contact['name']:<20}{contact['email']:<30}{contact['phone']:<15}{contact['address']:<20}")
