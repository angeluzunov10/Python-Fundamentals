string = input()
occurrences = {}
for symbol in string:
    if symbol == " ":
        continue
    if symbol not in occurrences.keys():
        occurrences[symbol] = 0
    occurrences[symbol] += 1

for char, count in occurrences.items():
    print(f"{char} -> {count}")
