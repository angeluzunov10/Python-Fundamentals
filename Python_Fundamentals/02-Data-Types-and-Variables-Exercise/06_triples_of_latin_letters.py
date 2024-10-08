number_of_triples = int(input())
char_one = 0
char_two = 0
char_three = 0

for char_one in range(0, number_of_triples):
    for char_two in range(0, number_of_triples):
        for char_three in range(0, number_of_triples):
            print(f"{chr(97 + char_one)}{chr(97 + char_two)}{chr(97 + char_three)}")
