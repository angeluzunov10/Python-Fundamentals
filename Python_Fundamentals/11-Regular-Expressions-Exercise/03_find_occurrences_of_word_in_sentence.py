import re
text = input()
word = input()
pattern = fr"\b{word}\b"

variables = re.findall(pattern, text, re.IGNORECASE)

print(len(variables))
