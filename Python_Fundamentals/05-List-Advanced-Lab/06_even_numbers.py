numbers_string_list = list(map(int, input().split(", ")))
indices_list = []
index = 0

for number in numbers_string_list:
    if number % 2 == 0:
        indices_list.append(index)
    index += 1

print(indices_list)
