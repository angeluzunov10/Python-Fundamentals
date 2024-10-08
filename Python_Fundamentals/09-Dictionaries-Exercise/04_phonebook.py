phonebook = {}
while True:
    contact_info = input()
    if "-" not in contact_info:
        number = int(contact_info)
        break
    name, phone_number = contact_info.split("-")
    phonebook[name] = phone_number

for n in range(number):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")