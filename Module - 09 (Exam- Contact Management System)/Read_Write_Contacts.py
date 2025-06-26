import csv
import os

confile = "contacts.csv"

def ensure_file():
    if not os.path.exists(confile):
        with open(confile, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "email", "address"])


# read contacts 
def read_contacts():
    contacts = []
    try:
        with open(confile, "r") as file:
            for line in file:
                if line.strip():
                    name, phone, email, address = line.strip().split(",", 3)

                    if [name, phone, email, address] == ["name", "phone", "email", "address"]:
                        continue
                    address = address.strip('"')
                    contacts.append({
                        "name": name.strip('"'),
                        "phone": phone.strip('"'),
                        "email": email.strip('"'),
                        "address": address
                    })
    except FileNotFoundError:
        open(confile, "w").close()
    return contacts

# write contacts 
def write_contacts(contacts):
    file_empty = not os.path.exists(confile) or os.stat(confile).st_size == 0

    with open(confile, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])

        if file_empty:
            writer.writeheader()
        writer.writerows(contacts)