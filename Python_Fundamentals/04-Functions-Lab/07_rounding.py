def rounding():
    numbers = list(map(float, input().split()))
    rounded_numbers = []
    for number in numbers:
        rounded_numbers.append(round(number))
    return rounded_numbers


print(rounding())

