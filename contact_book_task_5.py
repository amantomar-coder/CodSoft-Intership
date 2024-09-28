class ContactBook:
  def __init__(self):
      self.contacts = []

  def add_contact(self, name, phone, email, address):
      contact = {
          'name': name,
          'phone': phone,
          'email': email,
          'address': address
      }
      self.contacts.append(contact)
      print(f'Contact "{name}" added.')

  def view_contacts(self):
      if self.contacts:
          for i, contact in enumerate(self.contacts, 1):
              print(f'{i}. {contact["name"]} - {contact["phone"]}')
      else:
          print("No contacts in the list.")

  def search_contact(self, search_term):
      found_contacts = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower()]
      if found_contacts:
          for contact in found_contacts:
              print(contact)
      else:
          print("No contact found.")

  def update_contact(self, index, name=None, phone=None, email=None, address=None):
      if 0 <= index < len(self.contacts):
          if name:
              self.contacts[index]['name'] = name
          if phone:
              self.contacts[index]['phone'] = phone
          if email:
              self.contacts[index]['email'] = email
          if address:
              self.contacts[index]['address'] = address
          print("Contact updated.")
      else:
          print("Invalid contact number.")

  def delete_contact(self, index):
      if 0 <= index < len(self.contacts):
          removed_contact = self.contacts.pop(index)
          print(f'Contact "{removed_contact["name"]}" deleted.')
      else:
          print("Invalid contact number.")

if __name__ == "__main__":
  book = ContactBook()

  while True:
      print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
      choice = input("Choose an option: ")

      if choice == '1':
          name = input("Enter name: ")
          phone = input("Enter phone number: ")
          email = input("Enter email: ")
          address = input("Enter address: ")
          book.add_contact(name, phone, email, address)
      elif choice == '2':
          book.view_contacts()
      elif choice == '3':
          search_term = input("Enter name to search: ")
          book.search_contact(search_term)
      elif choice == '4':
          contact_number = int(input("Enter the contact number to update: ")) - 1
          name = input("Enter new name (leave blank to keep current): ")
          phone = input("Enter new phone (leave blank to keep current): ")
          email = input("Enter new email (leave blank to keep current): ")
          address = input("Enter new address (leave blank to keep current): ")
          book.update_contact(contact_number, name, phone, email, address)
      elif choice == '5':
          contact_number = int(input("Enter the contact number to delete: ")) - 1
          book.delete_contact(contact_number)
      elif choice == '6':
          break
      else:
          print("Invalid option.")
