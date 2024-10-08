initial_health = 100
initial_bitcoins = 0

dungeons_rooms = input().split("|")
current_health = initial_health
current_bitcoins = initial_bitcoins
for room in dungeons_rooms:
    current_room = room.split()
    command = current_room[0]
    number = int(current_room[1])
    if command == "potion":
        if current_health + number > initial_health:
            number = initial_health - current_health
            current_health = initial_health
        else:
            current_health += number

        print(f"You healed for {number} hp.")
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        current_bitcoins += number
    else:
        current_health -= number
        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {dungeons_rooms.index(room) + 1}")
            break

if current_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {current_bitcoins}")
    print(f"Health: {current_health}")
