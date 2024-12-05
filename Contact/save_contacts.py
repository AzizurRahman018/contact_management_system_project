import csv

def save_to_file(contacts):
    """Save all contacts to the CSV file."""
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Email', 'Phone', 'Address'])
        writer.writeheader()
        for contact in contacts:
            writer.writerow({
                'Name': contact['name'],
                'Email': contact['email'],
                'Phone': contact['phone'],
                'Address': contact['address']
            })
