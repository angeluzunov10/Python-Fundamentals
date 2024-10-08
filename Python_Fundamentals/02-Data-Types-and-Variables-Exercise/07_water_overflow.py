capacity = 255
water_inside = 0
number_of_lines = int(input())

for line in range(number_of_lines):
    liters_of_water = int(input())
    if liters_of_water > capacity:
        print("Insufficient capacity!")
        continue
    water_inside += liters_of_water
    capacity -= liters_of_water
print(water_inside)
