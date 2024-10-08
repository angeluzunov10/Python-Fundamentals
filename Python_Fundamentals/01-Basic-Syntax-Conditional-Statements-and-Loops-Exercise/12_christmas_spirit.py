decorations_count = int(input()) #vseki put
days_left = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

total_spirit = 0
total_cost = 0

for current_day in range (1, days_left + 1):
    if current_day % 11 == 0:           #тази проверка трябва да е първа, защото се отнася за началото на деня
        decorations_count += 2          #и като минем през останалите проверки за 11-тите дни ще имаме повече количество
                                        #украси за закупуване, които ще влияят на крайната цена

    if current_day % 2 == 0:
        total_cost += decorations_count * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += decorations_count * (tree_skirt_price + tree_garland_price)
        total_spirit += 10 + 3
    if current_day % 5 == 0:
        total_cost += decorations_count * tree_lights_price
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price +tree_garland_price + tree_lights_price

if days_left % 10 == 0:                 #тук вече сме изляли от цикъла и сме сигурни, че сме на последния ден
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
