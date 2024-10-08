dictionary = {}

count_of_pairs = int(input())

for _ in range(count_of_pairs):
    name = input()
    grade = float(input())
    if name not in dictionary.keys():
        dictionary[name] = []
    dictionary[name].append(grade)

for name in dictionary.keys():
    average_grade = sum(dictionary[name]) / len(dictionary[name])
    dictionary[name] = average_grade

for name, average_grade in dictionary.items():
    if dictionary[name] >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
