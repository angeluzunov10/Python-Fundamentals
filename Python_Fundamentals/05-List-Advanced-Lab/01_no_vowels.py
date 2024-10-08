some_string = input()

sorted_string = [char for char in some_string if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(sorted_string))
