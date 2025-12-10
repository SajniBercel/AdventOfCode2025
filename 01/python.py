def getRotations() -> list[int]:
    filePath = input("filepath:")
    file = open(filePath)

    rotations = []

    for line in file:
        multip = 1
        if line[0].upper() == 'L':
            multip = -1

        rotations.append(int(line[1:]) * multip)
    file.close()

    return rotations


def rotate(angle: int, currentCode: int) -> tuple[int, int]:
    counter = 0

    while angle > 0:
        currentCode += 1
        angle -= 1

        if currentCode == 100: currentCode = 0
        if currentCode == 0: counter += 1

    while angle < 0:
        currentCode -= 1
        angle += 1

        if currentCode == 100: currentCode = 0
        if currentCode == 0: counter += 1

    currentCode = currentCode % 100

    return tuple((counter, currentCode))


def main():
    rotations = getRotations()

    # part1
    currentRotation = 50
    counter = 0
    for rotation in rotations:
        currentRotation = (currentRotation + rotation) % 100
        if currentRotation == 0:
            counter += 1

    print("part1:", counter)

    # part2
    currentRotation = 50
    counter = 0
    for rotation in rotations:
        (counter, currentRotation) = rotate(rotation, currentRotation)

    print("part2:", counter)


main()