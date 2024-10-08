def characters_in_range(character_one, character_two):
    char_one_code = ord(character_one)
    char_two_code = ord(character_two)

    characters_between_both_characters_codes = list(range(char_one_code + 1, char_two_code))
    characters_between_both_characters = []

    for code in characters_between_both_characters_codes:
        character = chr(code)
        characters_between_both_characters.append(character)

    print(*characters_between_both_characters)


character_one = input()
character_two = input()

characters_in_range(character_one, character_two)
