numbersPainting = list(map(int, input().split()))
while True:
    command = input()
    if command == "END":
        break

    if command[0] == "Change":
        firstValue = int(command[1])
        changedValue = int(command[2])
        if firstValue in numbersPainting:
            indexFirstValue = numbersPainting.index(firstValue)
            numbersPainting[indexFirstValue] = changedValue
    elif command[0] == "Hide":
        numPaintToHide = int(command[1])
        if numPaintToHide in numbersPainting:
            numbersPainting.remove(numPaintToHide)
    elif command[0] == "Switch":
        firstNum = int(command[1])
        secondNum = int(command[2])
        if firstNum in numbersPainting and secondNum in numbersPainting:
            indexOne = numbersPainting.index(firstNum)
            indexTwo = numbersPainting.index(secondNum)
            valueOne = numbersPainting[indexOne]
            valueTwo = numbersPainting[indexTwo]
            numbersPainting[indexOne] = valueTwo
            numbersPainting[indexTwo] = valueOne
    elif command[0] == "Insert":
        index = int(command[1])
        paintingNum = int(command[2])
        if index + 1 < len(numbersPainting):
            numbersPainting.insert(index + 1, paintingNum)
    elif command[0] == "Reverse":
        numbersPainting.reverse()

for num in numbersPainting:
    print(num, end=" ")
