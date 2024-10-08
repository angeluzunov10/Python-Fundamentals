legendary_item = ""
obtained = False
items = {"shards": 0, "fragments": 0, "motes": 0}

current_items = input().split()

while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1]
        if key not in items.keys():
            items[key] = 0
        items[key] += value

        if items["shards"] >= 250:
            legendary_item = "Shadowmourne"
            obtained = True
            items["shards"] -= 250
        elif items["fragments"] >= 250:
            legendary_item = "Valanyr"
            obtained = True
            items["fragments"] -= 250
        elif items["motes"] >= 250:
            legendary_item = "Dragonwrath"
            obtained = True
            items["motes"] -= 250
        if obtained:
            break
    if obtained:
        break
    current_items = input().split()

print(f"{legendary_item} obtained!")

for material, quantity in items.items():
    print(f"{material}: {quantity}")

