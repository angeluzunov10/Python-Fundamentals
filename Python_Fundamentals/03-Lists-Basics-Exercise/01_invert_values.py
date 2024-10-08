numbers = input().split()
numbers_in_integers = (int(s) for s in numbers)
inverted_numbers = []

for num in numbers_in_integers:
    number = - num
    inverted_numbers.append(number)

print(inverted_numbers)


