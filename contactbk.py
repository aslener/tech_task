import json
with open("D:\\tech_tribe\\tech_task\\contactbook.json") as f:
    data = json.load(f)
def add_new_contact():
    name=input("Enter name: ").capitalize()
    phone=int(input("Enter phone number: "))
    new_contact = {"name":name, "phone_no":phone}
    data["contacts"].append(new_contact)
def list_of_contacts():
    for contact in data["contacts"]:
        print(contact)
def delete_contact():
    name=input("Enter name to delete: ").capitalize()
    for contact in data["contacts"]:
        if contact["name"]==name:
            data["contacts"].remove(contact)
with open("contactbook.json", "w") as f:
    json.dump(data, f)
list_of_contacts()