number = input()

for i in range(len(number) - 1, -1, -1):
    if number[i] > number[i - 1]:
        print(number[i], end="")
else:
    print(number[i - 1], end="")
