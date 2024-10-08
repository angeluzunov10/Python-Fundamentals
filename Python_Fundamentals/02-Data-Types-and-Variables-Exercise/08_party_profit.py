group_size = int(input())
days = int(input())
coins = 0
coins_spent_for_food = 0
coins_spent_for_motivational_party = 0
for day in range(1, days + 1):
    if day % 15 == 0:
        group_size += 5
    if day % 10 == 0:
        group_size -= 2
    if day % 3 == 0:
        coins_spent_for_motivational_party += group_size * 3
    if day % 5 == 0:
        coins += group_size * 20
        if day % 3 == 0:
            coins_spent_for_motivational_party += group_size * 2
    coins += 50
    coins_spent_for_food += group_size * 2


total_coins_spend = coins_spent_for_motivational_party + coins_spent_for_food
coins -= total_coins_spend
coins_per_companion = coins / group_size
print(f"{group_size} companions received {int(coins_per_companion)} coins each.")
