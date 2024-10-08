integers_list_in_string = input().split(", ")
integers_list_in_integer = [int(n) for n in integers_list_in_string]
move_element = 0

for integer in integers_list_in_integer:
    current_index = integers_list_in_integer.index(integer)
    if integer == 0:
        move_element = integers_list_in_integer.pop(current_index)
        integers_list_in_integer.append(move_element)

print(integers_list_in_integer)