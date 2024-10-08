import re
string = input()
occurrences = {}
string_to_print = ""
while True:
    command = input()

    if command == "Done":
        break

    if "Change" in command:
        action, character, replacement = command.split()
        pattern = fr"{character}"
        matches = re.findall(pattern, string)
        string_to_print = re.sub(matches[0], replacement, string)
        print(string_to_print)

    elif "Includes" in command:
        action, substring = command.split()
        if substring in string_to_print:
            print(True)
        else:
            print(False)

    elif "End" in command:
        action, substring = command.split()
        pattern = fr"{substring}$"
        matches = re.findall(pattern, string_to_print)
        if matches:
            print(True)
        else:
            print(False)

    elif "Uppercase" in command:
        string_to_print = string_to_print.upper()
        print(string_to_print)

    elif "FindIndex" in command:
        action, character = command.split()
        pattern = fr"{character}"
        matches = re.findall(pattern, string_to_print, re.IGNORECASE)

        for index in range(len(string_to_print)):
            if string_to_print[index] == matches[0]:
                print(index)
                break

    elif "Cut" in command:

        action, start_index, count = command.split()

        start_index, count = int(start_index), int(count)

        string_to_print = string_to_print[start_index:start_index + count]

        print(string_to_print)

# input_string = input()
#
# while True:
#     command = input().split()
#
#     if command[0] == "Done":
#         break
#
#     if command[0] == "Change":
#         char, replacement = command[1], command[2]
#         input_string = input_string.replace(char, replacement)
#         print(input_string)
#
#     elif command[0] == "Includes":
#         substring = command[1]
#         print("True" if substring in input_string else "False")
#
#     elif command[0] == "End":
#         substring = command[1]
#         print("True" if input_string.endswith(substring) else "False")
#
#     elif command[0] == "Uppercase":
#         input_string = input_string.upper()
#         print(input_string)
#
#     elif command[0] == "FindIndex":
#         char = command[1]
#         print(input_string.find(char))
#
#     elif command[0] == "Cut":
#         start_index, count = int(command[1]), int(command[2])
#         input_string = input_string[start_index:start_index+count]
#         print(input_string)