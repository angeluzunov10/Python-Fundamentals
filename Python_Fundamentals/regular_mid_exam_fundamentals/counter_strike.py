initial_energy = int(input())
battles_won = 0
current_energy = 0
while True:
    command = input()
    current_energy = initial_energy
    if command == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {current_energy}")
        break

    distance = int(command)

    initial_energy -= distance

    if initial_energy < 0:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {current_energy} energy")
        break

    battles_won += 1
    if battles_won % 3 == 0:
        initial_energy += battles_won
