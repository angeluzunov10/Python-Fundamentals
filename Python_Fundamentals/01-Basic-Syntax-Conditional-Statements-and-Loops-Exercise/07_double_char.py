command = input()

while command != "End":
    if command != "SoftUni":
        new_text = ""
        for character in command:
            new_text += character * 2
        print(new_text)

    command = input()
