parking = {}

number_of_commands = int(input())

for n in range(1, number_of_commands + 1):
    registration_type = input().split()
    if "register" in registration_type:
        username = registration_type[1]
        license_plate_number = registration_type[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif "unregister" in registration_type:
        username = registration_type[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for user, license_plate in parking.items():
    print(f"{user} => {license_plate}")

