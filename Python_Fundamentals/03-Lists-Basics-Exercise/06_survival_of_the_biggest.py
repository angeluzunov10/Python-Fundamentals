numbers_string = input().split()
number = int(input())

numbers_in_integers = []

for numbers in numbers_string:
    current_number = int(numbers)
    numbers_in_integers.append(current_number)

for num in range(number):
    numbers_in_integers.remove(min(numbers_in_integers))

new_list = map(str, numbers_in_integers)

print(", ". join(new_list))

