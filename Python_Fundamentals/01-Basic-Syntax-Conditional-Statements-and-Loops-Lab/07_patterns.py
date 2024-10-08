# number = int(input())
#
# for i in range(1, number + 1):
#     for j in range(0, i):
#         print("*", end="")
#     print()                         #това преминава на следващия ред
# for i in range (number - 1, 0, -1):
#     for j in range(0, i):           #този цикъл е с 1 ред по-малко, защото ще се повтори реда с най-многото звезди
#         print("*", end="")
#     print()
#


number = int(input())

for i in range(1, number + 1):
    for j in range(0, i):
        print("*", end="")
    print()
for i in range(number - 1, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()

