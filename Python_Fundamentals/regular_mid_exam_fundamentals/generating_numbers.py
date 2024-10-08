sequence_of_integers = [int(i) for i in input().split()]
is_valid = False
while True:
    command = input()

    if command == "END":
        break

    if "add to start" in command:
        command = command.split()
        for index in range(len(command) - 1, 2, -1):
            sequence_of_integers.insert(0, int(command[index]))

    elif "remove greater than" in command:
        command = command.split()
        value = int(command[-1])
        for index in range(len(sequence_of_integers), 0, -1):
            if sequence_of_integers[index] > value:
                sequence_of_integers.remove(sequence_of_integers[index])

    elif "replace" in command:
        action, value, replacement = command.split()

        value = int(value)
        replacement = int(replacement)
        if value not in sequence_of_integers:
            continue
        for index in range(0, len(sequence_of_integers)):
            if sequence_of_integers[index] == value:
                sequence_of_integers[index] = replacement
                break

    elif "remove at index" in command:
        command = command.split()
        index = int(command[-1])
        if 0 <= index <= len(sequence_of_integers):
            is_valid = True
        if not is_valid:
            continue
        sequence_of_integers.remove(sequence_of_integers[index])

    elif command == "find even":
        even_numbers = []
        for integer in sequence_of_integers:
            if integer % 2 == 0:
                even_numbers.append(integer)
        print(*even_numbers)
    elif command == "find odd":
        odd_numbers = []
        for integer in sequence_of_integers:
            if integer % 2 != 0:
                odd_numbers.append(integer)
        print(*odd_numbers)

string_list = [str(i) for i in sequence_of_integers]
print(", ".join(string_list))
