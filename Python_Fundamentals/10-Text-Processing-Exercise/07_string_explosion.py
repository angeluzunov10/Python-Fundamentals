some_string = input()
new_text = ""
explosion_strength = 0
for index in range(len(some_string)):

    # Тук сме в процес на експлозия, влизаме и не пипаме текста, защото така или иначе няма да стигнем до добавянето
    # на символа заради elif типа на проверката
    if explosion_strength > 0 and some_string[index] != ">":
        explosion_strength -= 1

    # Тук имаме експлозия, влизаме и не пипаме текста, защото така или иначе няма да стигнем до добавянето на символа
    # заради elif типа на проверката
    elif some_string[index] == ">":
        new_text += some_string[index]
        explosion_strength += int(some_string[index + 1])

    # Тук вече нито имаме знак за експлозия, нито сме в процес на такава. Добавяме вече достигнатия символ от текста
    else:
        new_text += some_string[index]

print(new_text)