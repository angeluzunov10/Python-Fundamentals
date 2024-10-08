number = input()


def odd_and_even_sum(number):
    odd_numbers_sum = 0
    even_numbers_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_numbers_sum += int(digit)
        else:
            odd_numbers_sum += int(digit)
    print(f"Odd sum = {odd_numbers_sum}, Even sum = {even_numbers_sum}")


odd_and_even_sum(number)
