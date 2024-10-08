line = input().split()
stock = {}

for n in range(0, len(line), 2):
    product = line[n]
    quantity = line[n + 1]

    stock[product] = quantity

products_to_search = input().split()

for current_product in products_to_search:
    if current_product in stock.keys():
        print(f"We have {stock[current_product]} of {current_product} left.")
    else:
        print(f"Sorry, we don't have {current_product}.")