class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact.name} - {contact.phone_number}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if (
                keyword.lower() in contact.name.lower() or
                keyword in contact.phone_number
            ):
                results.append(contact)

        if not results:
            print("No matching contacts found.")
        else:
            print("Matching Contacts:")
            for index, result in enumerate(results, start=1):
                print(f"{index}. {result.name} - {result.phone_number}")

        return results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact
        print("Contact updated successfully!")

    def delete_contact(self, index):
        deleted_contact = self.contacts.pop(index)
        print(f"Contact '{deleted_contact.name}' deleted successfully!")

def get_user_input(prompt):
    return input(prompt).strip()

def get_valid_index(prompt, max_index):
    while True:
        try:
            index = int(input(prompt))
            if 1 <= index <= max_index:
                return index - 1
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = get_user_input("Enter name: ")
            phone_number = get_user_input("Enter phone number: ")
            email = get_user_input("Enter email: ")
            address = get_user_input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            keyword = get_user_input("Enter name or phone number to search: ")
            contact_manager.search_contact(keyword)

        elif choice == "4":
            contact_manager.view_contact_list()
            index = get_valid_index("Enter the index of the contact to update: ", len(contact_manager.contacts))
            name = get_user_input("Enter new name: ")
            phone_number = get_user_input("Enter new phone number: ")
            email = get_user_input("Enter new email: ")
            address = get_user_input("Enter new address: ")
            updated_contact = Contact(name, phone_number, email, address)
            contact_manager.update_contact(index, updated_contact)

        elif choice == "5":
            contact_manager.view_contact_list()
            index = get_valid_index("Enter the index of the contact to delete: ", len(contact_manager.contacts))
            contact_manager.delete_contact(index)

        elif choice == "6":
            print("Thanks for using the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
