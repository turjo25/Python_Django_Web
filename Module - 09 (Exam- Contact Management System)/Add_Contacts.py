from Read_Write_Contacts import read_contacts
from Read_Write_Contacts import write_contacts


def get_valid_phone():
    while 1:
        phone = input("Enter Phone Number: ").strip()
        if phone.isdigit() and len(phone) == 11:
            return phone
        else:
            print("Invalid phone number. It must be exactly 11 digits.")


def add_contact():
    name = input("Enter Name: ")
    phone = get_valid_phone()
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts = read_contacts()

    if any(c['phone'] == phone for c in contacts):
        print("Error: Phone number already exists for another contact.")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    write_contacts(contacts)
    print("Contact added successfully!")
