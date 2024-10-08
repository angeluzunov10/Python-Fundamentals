arrays = [int(element) for element in input().split()]
for i in range(len(arrays)):
    arrays[i] = int(arrays[i])


while True:
    command = input()

    if command == "end":
        break

    if "swap" in command:
        _, first_index, second_index = command.split()
        first_index = int(first_index)
        second_index = int(second_index)
        first_element = arrays[first_index]
        second_element = arrays[second_index]
        arrays[first_index] = second_element
        arrays[second_index] = first_element

    if "multiply" in command:
        _, first_index, second_index = command.split()
        first_index = int(first_index)
        second_index = int(second_index)
        first_element = arrays[first_index]
        second_element = arrays[second_index]
        arrays.insert(1, first_element * second_element)

    if command == "decrease":
        for element in arrays:
            element -= 1

print(*arrays)
