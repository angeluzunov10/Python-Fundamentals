def ascii_code_into_char(word):
    string = list(word)
    numbers_as_string = []

    while string[0].isdigit():
        numbers_as_string.append(string[0])
        string.pop(0)

    ascii_code = int(''.join(numbers_as_string))
    string.insert(0, chr(ascii_code))
    return ''.join(string)


def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]

    return ''.join(letters)


print(' '.join([switch_letters(ascii_code_into_char(word)) for word in input().split()]))
