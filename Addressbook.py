import csv
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

    # Convert contact to dictionary for CSV serialization
    def to_list(self):
        return [
            self.first_name,
            self.last_name,
            self.address,
            self.city,
            self.state,
            self.zip_code,
            self.phone_number,
            self.email
        ]

    # Create a contact from a list (CSV deserialization)
    @classmethod
    def from_list(cls, data):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])


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

    # Save contacts to a CSV file
    def save_to_file(self, file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Address", "City", "State", "Zip Code", "Phone Number", "Email"])  # Header
            for contact in self.contacts:
                writer.writerow(contact.to_list())
        print(f"Contacts saved to {file_name}.")

    # Load contacts from a CSV file
    def load_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    contact = Contact.from_list(row)
                    self.add_contact(contact)
            print(f"Contacts loaded from {file_name}.")
        except FileNotFoundError:
            print(f"{file_name} not found.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts.")
        else:
            sorted_contacts = sorted(self.contacts)  # Sort contacts alphabetically
            for contact in sorted_contacts:
                print(contact)

    # Sort contacts by City
    def sort_by_city(self):
        sorted_contacts = sorted(self.contacts, key=lambda contact: contact.city.lower())
        for contact in sorted_contacts:
            print(contact)

    # Sort contacts by State
    def sort_by_state(self):
        sorted_contacts = sorted(self.contacts, key=lambda contact: contact.state.lower())
        for contact in sorted_contacts:
            print(contact)

    # Sort contacts by Zip Code
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

    # Save all address books to CSV files
    def save_all_books(self):
        for name, address_book in self.address_books.items():
            file_name = f"{name}.csv"
            address_book.save_to_file(file_name)

    # Load all address books from CSV files
    def load_all_books(self):
        for name in self.address_books:
            file_name = f"{name}.csv"
            self.address_books[name].load_from_file(file_name)

    # Search by city or state across books
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
        print("4. Save All Address Books to File")
        print("5. Load Address Books from File")
        print("6. Search Across Address Books by City or State")
        print("7. Exit")
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
                    print("6. Back to Main Menu")
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
                        print("\n1. Sort by City")
                        print("2. Sort by State")
                        print("3. Sort by Zip Code")
                        sort_choice = input("Choice: ")
                        if sort_choice == '1':
                            selected_book.sort_by_city()
                        elif sort_choice == '2':
                            selected_book.sort_by_state()
                        elif sort_choice == '3':
                            selected_book.sort_by_zip()
                        else:
                            print("Invalid choice.")
                    elif sub_choice == '6':
                        break
                    else:
                        print("Invalid choice.")

        elif choice == '4':
            system.save_all_books()

        elif choice == '5':
            system.load_all_books()

        elif choice == '6':
            city = input("Enter city to search: ")
            state = input("Enter state to search: ")
            results = system.search_across_books(city, state)
            if results:
                for name, matches in results:
                    print(f"\nAddress Book: {name}")
                    for contact in matches:
                        print(contact)
            else:
                print("No matches found.")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
                    
