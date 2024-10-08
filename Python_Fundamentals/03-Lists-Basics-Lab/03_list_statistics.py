number = int(input())
positives = []
negatives = []
positives_count = 0
negatives_count = 0

for _ in range(number):
    integer = int(input())
    if integer >= 0:
        positives_count += 1
        positives.append(integer)
    else:
        negatives_count += 1
        negatives.append(integer)
print(positives)
print(negatives)
print(f"Count of positives: {positives_count}")
print(f"Sum of negatives: {sum(negatives)}")
