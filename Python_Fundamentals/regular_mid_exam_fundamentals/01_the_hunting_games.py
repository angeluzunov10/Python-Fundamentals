days_of_the_adventure = int(input())
players_count = int(input())
groups_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())

total_water_supplies = water_per_person_per_day * days_of_the_adventure * players_count
total_food_supplies = food_per_person_per_day * days_of_the_adventure * players_count

current_energy = groups_energy
current_water = total_water_supplies
current_food = total_food_supplies

for day in range(1, days_of_the_adventure + 1):
    if current_energy <= 0:
        print(f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")
        break
    energy_lost_from_chopping_wood = float(input())
    current_energy -= energy_lost_from_chopping_wood

    if day % 2 == 0:
        current_energy = current_energy + (0.05 * current_energy)
        current_water = current_water - (0.30 * current_water)
    if day % 3 == 0:
        current_food = current_food - (current_food / players_count)
        current_energy = current_energy + (0.1 * current_energy)

if current_energy > 0:
    print(f"You are ready for the quest. You will be left with - {current_energy:.2f} energy!")

