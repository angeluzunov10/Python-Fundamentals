money_as_string = input().split(", ")        # separated by ", "
beggars_count = int(input())
money_as_integers = []
for current_money in money_as_string:
    money_as_integers.append(int(current_money))

final_sums = []

starting_index = 0

while starting_index < beggars_count:
    current_beggar_sum = 0
    for current_index in range(starting_index, len(money_as_integers), beggars_count):
        current_beggar_sum += money_as_integers[current_index]
    final_sums.append(current_beggar_sum)
    starting_index += 1

print(final_sums)
