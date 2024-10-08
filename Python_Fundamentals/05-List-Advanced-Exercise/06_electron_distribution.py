number_of_electrons = int(input())
filled_shells_list = []

for shell in range(1, number_of_electrons + 1):
    max_electrons_for_shell = 2 * (shell ** 2)
    if number_of_electrons >= max_electrons_for_shell:
        filled_shells_list.append(max_electrons_for_shell)
        number_of_electrons -= max_electrons_for_shell
        if number_of_electrons == 0:
            break
    else:
        filled_shells_list.append(number_of_electrons)
        break

print(filled_shells_list)
