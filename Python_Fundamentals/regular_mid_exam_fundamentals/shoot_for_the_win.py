targets = [int(i) for i in input().split()]
shot_targets = 0
while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {shot_targets} ->", end=" ")
        for target in targets:
            print(target, end=" ")
        break

    index = int(command)

    if index < len(targets) and targets[index] != -1:
        current_target = targets[index]
        targets[index] = -1
        shot_targets += 1
        for index in range(len(targets)):
            if targets[index] == -1:
                continue
            if targets[index] > current_target:
                targets[index] -= current_target
            else:
                targets[index] += current_target
    else:
        continue

