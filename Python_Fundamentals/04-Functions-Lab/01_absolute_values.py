numbers_string_list = input().split()
numbers_integer_list = [float(element) for element in numbers_string_list]


def absolute_value():
    numbers_to_print = []
    for number in numbers_integer_list:
        numbers_to_print.append(abs(number))
    return numbers_to_print


print(absolute_value())

# Това е второ възможно условие за решаване на задачата, тъй като не се изисква използване на функции в момента
#
# numbers = list(map(float, input().split()))
#
# absolute_values = []
#
# for number in numbers:
#     absolute_values.append(abs(number))
#
# print(absolute_values)
