guests = {}
unliked_meals_count = 0

while True:
    command = input()
    if command == "Stop":
        break

    action, guest, meal = command.split('-')

    if action == "Like":
        if guest not in guests:
            guests[guest] = []
        if meal not in guests[guest]:
            guests[guest].append(meal)

    elif action == "Dislike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
        elif meal not in guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            guests[guest].remove(meal)
            unliked_meals_count += 1
            print(f"{guest} doesn't like the {meal}.")

for guest, meals in guests.items():
    print(f"{guest}: {', '.join(meals)}")
print(f"Unliked meals: {unliked_meals_count}")