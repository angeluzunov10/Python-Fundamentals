pirate_ship_status = [int(s) for s in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
max_health_capacity_for_section = int(input())
command = input().split()
while command[0] != "Retire":
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index >= len(warship_status):
            continue
        else:
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break
            else:
                warship_status[index] -= damage

    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index >= len(warship_status) or end_index >= len(warship_status):
            continue
        else:
            for section in range(warship_status[start_index], warship_status[end_index]):
                section -= damage
                if section <= 0:
                    print("You lost! The pirate ship was sunken.")
                    break
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index >= len(pirate_ship_status):
            continue
        else:
            pirate_ship_status[index] += health
            if health > max_health_capacity_for_section:
                health = max_health_capacity_for_section

    elif command[0] == "Status":
        def is_less_than_20_percent():
            for current_section in pirate_ship_status:
                if current_section <= pirate_ship_status
        sections_for_repair = list(filter())
        print(f"{len()} sections need repair")
