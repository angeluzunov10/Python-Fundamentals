text = input()
rage_message = ""
repetitions = ""
current_symbol = ""

for index in range(len(text)):
    if not text[index].isdigit():   # We have non-numeric character
        current_symbol += text[index].upper()
    else: # We have digit here. Now it's time for repeating
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        repetitions = int(repetitions)
        rage_message += current_symbol * repetitions
        current_symbol = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)