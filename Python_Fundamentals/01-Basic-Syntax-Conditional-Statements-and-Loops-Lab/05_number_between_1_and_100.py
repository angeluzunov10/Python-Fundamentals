# number = float(input())
# while not number >= 1 and number <= 100:
#     number = float(input())
# print(f"The number {number} is between 1 and 100")

#докато числото не е между 1 и 100 чети ново число, ако ли не принтирай

while True:
    number = float(input())
    if 1 <= number <= 100:
        print(f"The number {number} is between 1 and 100")
        break
