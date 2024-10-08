budget = float(input())

flour_price_per_kilo = float(input())
eggs_price_per_pack = 0.75 * flour_price_per_kilo
milk_price_per_liter = flour_price_per_kilo * 1.25
used_milk_price = milk_price_per_liter / 4                      # 250 ml za 1 pitka
coloured_eggs = 0
bread_count = 0
bread_price = flour_price_per_kilo + eggs_price_per_pack + used_milk_price

while True:
    if coloured_eggs < 0:
        break
    if budget < bread_price:
        break

    bread_count += 1
    coloured_eggs += 3

    if bread_count % 3 == 0:
        coloured_eggs -= (bread_count - 2)

    budget -= bread_price


print(f"You made {bread_count} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
