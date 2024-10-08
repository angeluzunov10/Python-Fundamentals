train_ticket_price = 150
markup = 1.40
items_list = input().split("|")
budget = float(input())

max_price_of_clothes = 50.00
max_price_of_shoes = 35.00
max_price_of_accessories = 20.50
successfully_bought = True

items_bought = []

spendings = 0

profit = 0

for items in items_list:
    type_of_item, item_price = items.split("->")
    item_price = float(item_price)
    if type_of_item == "Clothes":
        if item_price > max_price_of_clothes:
            continue
        else:
            successfully_bought = False
    elif type_of_item == "Shoes":
        if item_price > max_price_of_shoes:
            continue
        else:
            successfully_bought = False
    elif type_of_item == "Accessories":
        if item_price > max_price_of_accessories:
            continue
        else:
            successfully_bought = False

    if budget >= item_price:
        budget -= item_price
        spendings += item_price
        items_bought.append(item_price*markup)

for prices in items_bought:
    print(f"{prices:.2f}", end=" ")

print()

bought_items_sum = sum(items_bought)

profit = bought_items_sum - spendings

print(f"Profit: {profit:.2f}")
budget = budget + bought_items_sum

if budget >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
