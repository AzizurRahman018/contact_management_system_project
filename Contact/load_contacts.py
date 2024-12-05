# import csv
#
# def load_all_contacts():
#     try:
#         with open('contacts.csv', 'r') as file:
#             reader = csv.DictReader(file)
#             return [row for row in reader]
#     except FileNotFoundError:
#         print("No previous contacts found. Starting with an empty contact list.")
#         return []

import csv

def load_all_contacts():
    """Load contacts from the CSV file."""
    contacts = []
    try:
        with open('contacts.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ensure all fields are read as strings
                contacts.append({
                    'name': row['Name'],
                    'email': row['Email'],
                    'phone': row['Phone'],
                    'address': row['Address']
                })
    except FileNotFoundError:
        print("No previous contacts found. Starting with an empty contact list.")
    return contacts
