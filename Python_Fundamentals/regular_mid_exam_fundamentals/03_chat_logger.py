chat = []
command = input().split()
while command[0] != "end":
    if command[0] == "Chat":
        chat.append(command[1])
    elif command[0] == "Delete":
        if command[1] in chat:
            chat.remove(command[1])
        else:
            pass
    elif command[0] == "Edit":
        if command[1] in chat:
            message_index = chat.index(command[1])
            chat.remove(command[1])
            chat.insert(message_index, command[2])
        else:
            pass
    elif command[0] == "Pin":
        if command[1] in chat:
            message_index = chat.index(command[1])
            chat.pop(message_index)
            chat.append(command[1])
        else:
            pass
    elif command[0] == "Spam":
        first_message_index = 1
        last_message_index = len(command)
        for index in range(first_message_index, last_message_index):
            chat.append(command[index])

    command = input().split()

for message in chat:
    print(f"{message}")

