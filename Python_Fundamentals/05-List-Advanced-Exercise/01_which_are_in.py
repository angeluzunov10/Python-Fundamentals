first_sequence = input().split(", ")
second_sequence = input().split(", ")

substrings = []

for string_from_first in first_sequence:
    for string_from_second in second_sequence:
        if string_from_first in string_from_second:
            break

print(substrings)
