class ContactManagement:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            print("Contact already exists!")
        else:
            self.contacts[name] = phone
            print(f"Contact '{name}' added.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found!")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print("Contact not found!")

    def display_all(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("All Contacts:")
            for name, phone in self.contacts.items():
                print(f"  {name}: {phone}")


# Main
cm = ContactManagement()
cm.add_contact("Rahul", "9876543210")
cm.add_contact("Priya", "9123456789")
cm.add_contact("Amit", "9001234567")
cm.display_all()
cm.search_contact("Priya")
cm.delete_contact("Amit")
cm.display_all()