numbers_of_paintings = [int(i) for i in input().split()]

while True:
    command = input()

    if command == "END":
        break

    if "Change" in command:
        action, painting_number, new_number = command.split()
        painting_number = int(painting_number)
        new_number = int(new_number)

        if painting_number not in numbers_of_paintings:
            continue
        else:
            for index in range(0, len(numbers_of_paintings)):
                if numbers_of_paintings[index] == painting_number:
                    numbers_of_paintings[index] = new_number

    elif "Hide" in command:
        action, painting_number = command.split()
        painting_number = int(painting_number)

        if painting_number not in numbers_of_paintings:
            continue
        else:
            numbers_of_paintings.remove(painting_number)

    elif "Switch" in command:
        action, first_painting_number, second_painting_number = command.split()
        first_painting_number = int(first_painting_number)
        second_painting_number = int(second_painting_number)

        if (first_painting_number not in numbers_of_paintings) or (second_painting_number not in numbers_of_paintings):
            continue
        else:
            for index in range(0, len(numbers_of_paintings)):
                if numbers_of_paintings[index] == first_painting_number:
                    numbers_of_paintings[index] = second_painting_number
                elif numbers_of_paintings[index] == second_painting_number:
                    numbers_of_paintings[index] = first_painting_number

    elif "Insert" in command:
        action, index, painting_number = command.split()
        index = int(index)
        painting_number = int(painting_number)
        if 0 <= index <= len(numbers_of_paintings):
            numbers_of_paintings.insert(index + 1, painting_number)
        else:
            continue

    elif "Reverse" in command:
        numbers_of_paintings.reverse()

print(*numbers_of_paintings)
