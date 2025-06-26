from Add_Contacts import add_contact
from View_Contact import view_contacts
from Search_contact import search_contact
from Remove_contact import remove_contact
from Read_Write_Contacts import ensure_file

ensure_file()

# program startup
print("Welcome to the Contact Book CLI System!")
print("Loading contacts from contacts.csv... Done!")

# Menu and input
while 1:
    print("=========== MENU ===========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("============================")
    option = input("Enter your choice:")
    if option == "5":
        break
    elif option == "1":
        add_contact()
    elif option == "2":
        view_contacts()
    elif option == "3":
        search_contact()
    elif option == "4":
        remove_contact()

# After exit 
print("Thank you for using the Contact Book CLI System. Goodbye!")