orders = {}

while True:
    product_info = input()
    if product_info == "buy":
        break
    name, price, quantity = product_info.split()
    price = float(price)
    quantity = int(quantity)

    if name not in orders.keys():
        orders[name] = [price, quantity]
    else:
        orders[name][0] = price
        orders[name][1] += quantity
total_price = 0
for name, info in orders.items():
    print(f"{name} -> {info[0] * info[1]:.2f}")
