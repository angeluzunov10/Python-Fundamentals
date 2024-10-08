string = input()
digits = ""
letters = ""
other_characters = ""

for char in string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other_characters += char

print(digits)
print(letters)
print(other_characters)
