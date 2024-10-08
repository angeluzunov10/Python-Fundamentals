command = input()
coffees_count = 0

while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            coffees_count += 1
        else:
            coffees_count += 2
    command = input()

if coffees_count > 5:
    print("You need extra sleep")
else:
    print(coffees_count)
