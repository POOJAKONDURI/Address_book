'''

    @Author:pooja
    @Date:24-09-2024
    @last modified by:pooja
    @last modified time:24-09-2024
    @title: edit Contact to Address Book , Use Console to add 

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
        self.contacts = []

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
     

def main():
    print("Welcome to Address Book Program")
    address_book = AddressBook()

    while True:
        print("\nEnter 1 to Add Contact, 2 to View Contacts, 3 Edit contact,4 to exit:")
        choice = input("Choice: ")

        if choice == '1':
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            zip_code = input("Enter Zip: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")

            contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            address_book.add_contact(contact)

        elif choice == '2':
            address_book.view_contacts()

        elif choice == '3':
            first_name = input("Enter the First Name of the contact to edit: ")
            last_name = input("Enter the Last Name of the contact to edit: ")
            address_book.edit_contact(first_name, last_name)

        elif choice == '4':
            print("exit")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

    