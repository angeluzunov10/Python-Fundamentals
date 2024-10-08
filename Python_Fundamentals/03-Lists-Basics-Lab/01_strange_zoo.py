tail = input()
body = input()
head = input()

animal_order = [tail, body, head]

animal_order[0], animal_order[2] = animal_order[2], animal_order[0]

print(animal_order)
