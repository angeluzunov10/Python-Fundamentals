bakery = {}
line = input().split()

for index in range(0, len(line), 2):
    food = line[index]
    quantity = line[index + 1]

    bakery[food] = quantity

print(bakery)