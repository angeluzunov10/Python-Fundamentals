orders_count = int(input())
order_price = 0
total_price = 0

for orders in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        order_price = (price_per_capsule * capsules_per_day) * days
        print(f"The price for the coffee is: ${order_price:.2f}")
    else:
        continue
    total_price += order_price

print(f"Total: ${total_price:.2f}")