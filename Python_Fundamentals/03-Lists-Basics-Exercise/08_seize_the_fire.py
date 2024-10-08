burning_cell = input().split("#")
water_quantity = int(input())
effort = 0
total_effort = 0
total_fire = 0
cells_put_out = []
cell_is_valid = True

for cell in burning_cell:
    cell_is_valid = True
    type_of_fire, value_of_cell = cell.split(" = ")
    value_of_cell = int(value_of_cell)
    if water_quantity < value_of_cell:
        continue

    if type_of_fire == "High":
        if 81 <= value_of_cell <= 125:
            water_quantity -= value_of_cell
        else:
            cell_is_valid = False

    elif type_of_fire == "Medium":
        if 51 <= value_of_cell <= 80:
            water_quantity -= value_of_cell
        else:
            cell_is_valid = False
    elif type_of_fire == "Low":
        if 1 <= value_of_cell <= 50:
            water_quantity -= value_of_cell
        else:
            cell_is_valid = False

    if cell_is_valid:
        cells_put_out.append(value_of_cell)
        effort = value_of_cell * 0.25
        total_effort += effort
        total_fire += value_of_cell

print("Cells:")
for cells in cells_put_out:
    print(f" - {cells}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
