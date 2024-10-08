def is_even(number):
    return number % 2 == 0


sequence_of_numbers = list(map(int, input().split()))
even_numbers = list(filter(is_even, sequence_of_numbers))

print(even_numbers)
