first_number = int(input())
second_number = int(input())
third_number = int(input())

def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number, third_number):
    return sum_numbers(first_number, second_number) - third_number


def add_and_subtract(first_number, second_number, third_number):
    return subtract(first_number, second_number, third_number)


print(add_and_subtract(first_number, second_number, third_number))
