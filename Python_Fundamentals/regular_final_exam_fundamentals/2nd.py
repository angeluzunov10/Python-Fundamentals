import re
count_of_inputs = int(input())

for n in range(count_of_inputs):
    encrypted_password = input()
    pattern = r"^([^\>]+)\>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^\>]+)\<\1$"
    matches = re.findall(pattern, encrypted_password)
    if not matches:
        print("Try another password!")
    else:
        for match in matches:
            encrypted_password = ""
            numbers = match[1]
            letters = match[2] + match[3]
            symbols = match[4]
            encrypted_password += numbers + letters + symbols
            print(f"Password: {encrypted_password}")
