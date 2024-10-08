# def repeat_string(s, c):
#     return s * c
#
#
# string = input()
# counter = int(input())
#
# print(repeat_string(string, counter))


repeated_string = lambda string, counter: string * counter
string = input()
counter = int(input())

print(repeated_string(string, counter))

