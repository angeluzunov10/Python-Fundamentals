def calculate(operator, a, b):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


operator = input()
first_number = int(input())
second_number = int(input())

print(int(calculate(operator, first_number, second_number)))
