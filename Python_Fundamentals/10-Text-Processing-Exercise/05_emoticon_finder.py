string = list(input())
emoticon = ""
index = 0
for char in string:
    if char == ":":
        emoticon = char + string[index + 1]
        print(emoticon)
    index += 1

# Друго решение:

# single_string = input()
# for index in range(len(single_string)):
#     if single_string[index] == ":":
#         print(f":{single_string[index + 1]}")
