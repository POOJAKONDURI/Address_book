'''

    @Author:pooja
    @Date:24-09-2024
    @last modified by:pooja
    @last modified time:24-09-2024
    @title: to delete Contact in Address Book 

'''


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

    def __str__(self):
        return (f"{self.first_name} {self.last_name}\n"
                f"{self.address}, {self.city}, {self.state}, {self.zip_code}\n"
                f"Phone: {self.phone_number}\nEmail: {self.email}")

class AddressBook:
    def __init__(self):
        self.contacts = [] # act as collection class

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts.")
        else:
            for contact in self.contacts:
                print(contact)
    def find_contact(self,first_name,last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None
    def edit_contact(self,first_name,last_name):
        contact = self.find_contact(first_name,last_name)
        if contact:
            print("editing conatct")
            print(contact)   
            contact.first_name = input("Enter new First Name : ") or contact.first_name
            contact.last_name = input("Enter new Last Name: ") or contact.last_name
            contact.address = input("Enter new Address : ") or contact.address
            contact.city = input("Enter new City: ") or contact.city
            contact.state = input("Enter new State: ") or contact.state
            contact.zip_code = input("Enter new Zip Code : ") or contact.zip_code
            contact.phone_number = input("Enter new Phone Number: ") or contact.phone_number
            contact.email = input("Enter new Email : ") or contact.email

            
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    def delete_contact(self,first_name,last_name):
        contact = self.find_contact(first_name,last_name)
        if contact:
            self.contacts.remove(contact)
            print(f"{first_name},{last_name} is deleted now")
        else:
            print("no contact found")

    def search_by_city_or_state(self, city=None, state=None):
        results = []
        for contact in self.contacts:
            if (city and contact.city == city) or (state and contact.state == state):
                results.append(contact)
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

class AddressBookSystem:
    
    def __init__(self) :
        self.address_books = {}

    def add_address_books(self,name):
        if name in self.address_books:
            print(f'{name} allready exists')
        else:
            self.address_books[name] = AddressBook()
            print("addrress book added succesfully")
    

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
            matches = address_book.search_by_city_or_state(city, state)
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
                    print("5. Back to Main Menu")
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
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '4':
            city = input("Enter City (or leave blank to skip): ") or None
            state = input("Enter State (or leave blank to skip): ") or None

            if not city and not state:
                print(" enter either a City or a State.")
            else:
                results = system.search_across_books(city, state)
                if not results:
                    print("No matching contacts .")
                else:
                    print("\nSearch Results:")
                    for book_name, contacts in results:
                        print(f"\n Address Book: {book_name} ---")
                        for contact in contacts:
                            print(contact)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.") 


if __name__ == "__main__":
    main()