import save_contacts

def update_contactss(contacts):
    """Update contact information."""
    if not contacts:
        print("No contacts found to update.")
        return contacts

    # Display contacts for selection
    print("\nExisting Contacts:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Email: {contact['email']}, "
              f"Phone: {contact['phone']}, Address: {contact['address']}")

    # Select a contact to update
    try:
        selection = int(input("\nEnter the number of the contact you want to update: "))
        if selection < 1 or selection > len(contacts):
            print("Invalid selection. Please try again.")
            return contacts
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        return contacts

    # Get the contact to update
    contact_to_update = contacts[selection - 1]

    # Prompt user for new details (or keep existing details)
    print("\nLeave a field blank to keep the current value.")
    new_name = input(f"New Name ({contact_to_update['name']}): ").strip()
    new_email = input(f"New Email ({contact_to_update['email']}): ").strip()
    new_phone = input(f"New Phone ({contact_to_update['phone']}): ").strip()
    new_address = input(f"New Address ({contact_to_update['address']}): ").strip()

    # Validate phone number uniqueness
    if new_phone and any(contact['phone'] == new_phone for contact in contacts if contact != contact_to_update):
        print("Error: This phone number is already assigned to another contact.")
        return contacts

    # Update the contact details
    contact_to_update['name'] = new_name if new_name else contact_to_update['name']
    contact_to_update['email'] = new_email if new_email else contact_to_update['email']
    contact_to_update['phone'] = new_phone if new_phone else contact_to_update['phone']
    contact_to_update['address'] = new_address if new_address else contact_to_update['address']

    print("Contact updated successfully!")

    # Save updated contacts to the file
    save_contacts.save_to_file(contacts)

    return contacts
