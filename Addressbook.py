import json
from collections import defaultdict

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __lt__(self, other):
        return (self.first_name + " " + self.last_name).lower() < (other.first_name + " " + other.last_name).lower()

    def __str__(self):
        return (f"{self.first_name} {self.last_name}\n"
                f"{self.address}, {self.city}, {self.state}, {self.zip_code}\n"
                f"Phone: {self.phone_number}\nEmail: {self.email}")

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'phone_number': self.phone_number,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            data['first_name'],
            data['last_name'],
            data['address'],
            data['city'],
            data['state'],
            data['zip_code'],
            data['phone_number'],
            data['email']
        )


class AddressBook:
    def __init__(self):
        self.contacts = []  # Act as a collection class
        self.city_dict = defaultdict(list)  # Dictionary to store contacts by city
        self.state_dict = defaultdict(list)  # Dictionary to store contacts by state

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.city_dict[contact.city].append(contact)
        self.state_dict[contact.state].append(contact)
        print("Contact added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts.")
        else:
            sorted_contacts = sorted(self.contacts)  # Sort contacts alphabetically
            for contact in sorted_contacts:
                print(contact)

    def sort_by_city(self):
        sorted_contacts = sorted(self.contacts, key=lambda contact: contact.city.lower())
        for contact in sorted_contacts:
            print(contact)

    def sort_by_state(self):
        sorted_contacts = sorted(self.contacts, key=lambda contact: contact.state.lower())
        for contact in sorted_contacts:
            print(contact)

    def sort_by_zip(self):
        sorted_contacts = sorted(self.contacts, key=lambda contact: contact.zip_code)
        for contact in sorted_contacts:
            print(contact)

    def find_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    def edit_contact(self, first_name, last_name):
        contact = self.find_contact(first_name, last_name)
        if contact:
            print("Editing contact")
            print(contact)   
            contact.first_name = input("Enter new First Name: ") or contact.first_name
            contact.last_name = input("Enter new Last Name: ") or contact.last_name
            contact.address = input("Enter new Address: ") or contact.address
            contact.city = input("Enter new City: ") or contact.city
            contact.state = input("Enter new State: ") or contact.state
            contact.zip_code = input("Enter new Zip Code: ") or contact.zip_code
            contact.phone_number = input("Enter new Phone Number: ") or contact.phone_number
            contact.email = input("Enter new Email: ") or contact.email

            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, first_name, last_name):
        contact = self.find_contact(first_name, last_name)
        if contact:
            self.contacts.remove(contact)
            self.city_dict[contact.city].remove(contact)
            self.state_dict[contact.state].remove(contact)
            print(f"{first_name}, {last_name} is deleted now.")
        else:
            print("No contact found.")

    def search_by_city(self, city):
        return self.city_dict.get(city, [])

    def search_by_state(self, state):
        return self.state_dict.get(state, [])

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json_contacts = [contact.to_dict() for contact in self.contacts]
            json.dump(json_contacts, f)
        print(f"Address Book saved to {filename}.")

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as f:
                json_contacts = json.load(f)
                self.contacts = [Contact.from_dict(data) for data in json_contacts]
                self.city_dict.clear()
                self.state_dict.clear()
                for contact in self.contacts:
                    self.city_dict[contact.city].append(contact)
                    self.state_dict[contact.state].append(contact)
                print(f"Address Book loaded from {filename}.")
        except FileNotFoundError:
            print("File not found. Please check the filename.")


class AddressBookSystem:
    
    def __init__(self):
        self.address_books = {}

    def add_address_books(self, name):
        if name in self.address_books:
            print(f'{name} already exists')
        else:
            self.address_books[name] = AddressBook()
            print("Address book added successfully")

    def select_address_book(self, name):
        if name in self.address_books:
            return self.address_books[name]
        else:
            print(f"Address Book '{name}' does not exist.")
            return None

    def list_address_books(self):
        if not self.address_books:
            print("No Address Books available.")
        else:
            print("Available Address Books:")
            for name in self.address_books:
                print(f"- {name}")

    def search_across_books(self, city=None, state=None):
        results = []
        for name, address_book in self.address_books.items():
            if city:
                matches = address_book.search_by_city(city)
                if matches:
                    results.append((name, matches))
            if state:
                matches = address_book.search_by_state(state)
                if matches:
                    results.append((name, matches))
        return results


def add_multiple_contacts(address_book):
    while True:
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip Code: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        address_book.add_contact(contact)

        more_contacts = input("Would you like to add another contact? (yes/no): ").lower()
        if more_contacts != 'yes':
            break


def main():
    print("Welcome to Address Book System")
    system = AddressBookSystem()

    while True:
        print("\n1. Add New Address Book")
        print("2. List Address Books")
        print("3. Select Address Book")
        print("4. Search Across Address Books by City or State")
        print("5. Exit")
        choice = input("Choice: ")

        if choice == '1':
            name = input("Enter the name for the new Address Book: ")
            system.add_address_books(name)

        elif choice == '2':
            system.list_address_books()

        elif choice == '3':
            name = input("Enter the name of the Address Book to select: ")
            selected_book = system.select_address_book(name)
            if selected_book:
                while True:
                    print(f"\n--- Address Book: {name} ---")
                    print("1. Add Contact")
                    print("2. View Contacts")
                    print("3. Edit Contact")
                    print("4. Delete Contact")
                    print("5. Sort Contacts")
                    print("6. Save Address Book to JSON")
                    print("7. Load Address Book from JSON")
                    print("8. Back to Main Menu")
                    sub_choice = input("Choice: ")

                    if sub_choice == '1':
                        add_multiple_contacts(selected_book)
                    elif sub_choice == '2':
                        selected_book.view_contacts()
                    elif sub_choice == '3':
                        first_name = input("Enter the First Name of the contact to edit: ")
                        last_name = input("Enter the Last Name of the contact to edit: ")
                        selected_book.edit_contact(first_name, last_name)
                    elif sub_choice == '4':
                        first_name = input("Enter the First Name of the contact to delete: ")
                        last_name = input("Enter the Last Name of the contact to delete: ")
                        selected_book.delete_contact(first_name, last_name)
                    elif sub_choice == '5':
                        print("1. Sort by Name")
                        print("2. Sort by City")
                        print("3. Sort by State")
                        print("4. Sort by Zip Code")
                        sort_choice = input("Choice: ")
                        if sort_choice == '1':
                            selected_book.view_contacts()
                        elif sort_choice == '2':
                            selected_book.sort_by_city()
                        elif sort_choice == '3':
                            selected_book.sort_by_state()
                        elif sort_choice == '4':
                            selected_book.sort_by_zip()
                        else:
                            print("Invalid choice.")
                    elif sub_choice == '6':
                        filename = input("Enter the filename to save the Address Book: ")
                        selected_book.save_to_json(filename)
                    elif sub_choice == '7':
                        filename = input("Enter the filename to load the Address Book from: ")
                        selected_book.load_from_json(filename)
                    elif sub_choice == '8':
                        break
                    else:
                        print("Invalid choice.")

        elif choice == '4':
            city = input("Enter city to search: ")
            state = input("Enter state to search: ")
            results = system.search_across_books(city, state)
            if results:
                for name, matches in results:
                    print(f"Address Book: {name}")
                    for match in matches:
                        print(match)
            else:
                print("No contacts found.")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
