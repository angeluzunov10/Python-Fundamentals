string = input()
single_letters = ""
last_char = ""
for char in string:
    if last_char == char:
        continue
    single_letters += char
    last_char = char

print(single_letters)
