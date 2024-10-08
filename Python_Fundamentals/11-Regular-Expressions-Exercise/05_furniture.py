import re
pattern = r"(^>>([A-Z][A-Za-z]+)<<([0-9]*[\.0-9]*)\!([0-9]+)$)"
text_to_print = "Bought furniture:\n"
total_price = 0
while True:
    command = input()
    if command == "Purchase":
        break
    bought_items = re.findall(pattern, command)
    for bought_item in bought_items:
        text_to_print += f"{bought_item[1]}\n"
        current_bought_item_price = float(bought_item[2])
        current_bought_item_quantity = float(bought_item[3])
        total_price += current_bought_item_price * current_bought_item_quantity

text_to_print += f"Total money spend: {total_price:.2f}"

print(text_to_print)
