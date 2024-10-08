all_friends_list = input().split(", ")
command = input().split()
is_valid = False
blacklisted_names_count = 0
lost_names_count = 0
index = 0
while command[0] != "Report":

    if command[0] == "Error" or command[0] == "Change":
        if 0 <= int(command[1]) < len(all_friends_list):
            is_valid = True

    if command[0] == "Blacklist":
        if command[1] not in all_friends_list:
            print(f"{command[1]} was not found.")
        for name in all_friends_list:
            if name == command[1]:
                print(f"{command[1]} was blacklisted.")
                all_friends_list[index] = "Blacklisted"
                blacklisted_names_count += 1
            index += 1

    if command[0] == "Error":
        if is_valid is True and all_friends_list[int(command[1])] != "Blacklisted" and all_friends_list[int(command[1])] != "Lost":
            print(f"{all_friends_list[int(command[1])]} was lost due to an error.")
            all_friends_list[int(command[1])] = "Lost"
            lost_names_count += 1
        else:
            command = input().split()
            continue

    if command[0] == "Change":
        if is_valid is True:
            print(f"{all_friends_list[int(command[1])]} changed his username to {command[2]}")
            all_friends_list[int(command[1])] = command[2]
        else:
            command = input().split()
            continue

    command = input().split()

print(f"Blacklisted names: {blacklisted_names_count}")
print(f"Lost names: {lost_names_count}")
print(*all_friends_list)
