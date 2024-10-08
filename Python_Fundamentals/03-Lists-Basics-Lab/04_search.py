number = int(input())
word = input()
string_list = []

for numbers in range(number):
    string = input()
    string_list.append(string)
print(string_list)

filtered_string = []

for current_string in string_list:
    if word in current_string:
        filtered_string.append(current_string)
print(filtered_string)

# my_list = [1, 2, [3, 4], 5]
# print(my_list[2][0]) ------> Това ще ми принтира '3'. Учи се в матрици!
