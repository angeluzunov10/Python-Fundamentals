number = int(input())
numbers_list = []
filtered_list = []

for numbers in range(number):
    current_number = int(input())
    numbers_list.append(current_number)

command = input()

if command == "even":
    for current_number in numbers_list:
        if current_number % 2 == 0:
            filtered_list.append(current_number)
elif command == "odd":
    for current_number in numbers_list:
        if current_number % 2 != 0:
            filtered_list.append(current_number)
elif command == "negative":
    for current_number in numbers_list:
        if current_number < 0:
            filtered_list.append(current_number)
elif command == "positive":
    for current_number in numbers_list:
        if current_number >= 0:
            filtered_list.append(current_number)

print(filtered_list)