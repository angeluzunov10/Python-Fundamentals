def password_validation(some_password: str) -> list:
    list_of_errors = []
    digits = 0
    if not 6 <= len(some_password) <= 10:
        list_of_errors.append("Password must be between 6 and 10 characters")

    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")

    for element in some_password:
        if element.isdigit():
            digits += 1
    if digits < 2:
        list_of_errors.append("Password must have at least 2 digits")

    return list_of_errors


password = input()
validated_password = password_validation(password)

if len(validated_password) == 0:
    print("Password is valid")
else:
    print("\n".join(validated_password))
