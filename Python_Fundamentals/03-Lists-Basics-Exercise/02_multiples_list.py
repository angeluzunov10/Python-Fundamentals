factor = int(input())
count = int(input())

multiples_list = []

for numbers in range(1, count + 1):
    number = factor * numbers
    multiples_list.append(number)

print(multiples_list)

