"""
phonebook_lookup_voorbeeld.py

Instructies:
Implement function lookup() that implements a phone book lookup
application. Your function takes, as input, a dictionary representing a phone book,
mappingtuples (containing the
first and last name) to strings
(containing phone numbers)
"""

# The phone book (thanks chatgpt)
phonebook = {
    ('John', 'Doe'): '123-456-7890',
    ('Jane', 'Smith'): '987-654-3210',
    ('Alice', 'Johnson'): '555-123-4567',
    ('Bob', 'Brown'): '444-987-6543'
}

def lookup(phonebook):
    # Ask their name
    first = input("What is your first name? ")
    last = input("What is your last name? ")

    # Construct the full name, use capitalization (like in the phonebook itself)
    full_name = (first.capitalize(), last.capitalize())

    # Met de get-methode krijgen we nu óf een telefoonnummer of None
    number = phonebook.get(full_name)

    # Als number None is
    if not number:
        print(f"Sorry, we could not find {first.capitalize()} {last.capitalize()}")
    else:
        print(f"{first.capitalize()} {last.capitalize()} has phone number {number}")


lookup(phonebook)