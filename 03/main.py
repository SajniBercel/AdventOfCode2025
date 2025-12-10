def getData() -> list[str]:
    filePath = input("filePath:")
    file = open(filePath, "r")

    output = []
    for line in file:
        output.append(line)

    return output


# def bubbleSort(numList: list[(int, int)]) -> list[(int, int)]:
#     changed = True
#     while changed:
#         changed = False
#         for i in range(len(numList) - 1):
#             current = numList[i]
#             if current[0] > numList[i+1][0]:
#                 numList[i], numList[i+1] = numList[i+1], current
#                 changed = True
#
#     return numList


def getMaxWithIndex(line: str) -> tuple[int, int]:
    maxValue = int(line[0])
    maxIndex = 0
    for i in range(len(line)):
        if maxValue < int(line[i]):
            maxValue = int(line[i])
            maxIndex = i

    return (maxValue, maxIndex)


def getMaxPossibleValue(line: str, codeLength: int) -> int:
    numList = []
    for i in range(len(line)):
        numList.append((int(line[i]), i))

    maxValuesWithIndexes = []
    maxValue = int(line[0])
    maxIndex = 0
    for i in range(codeLength):
        maxValue, maxIndex = getMaxWithIndex(line)

        if(maxIndex < len(maxValuesWithIndexes)):
            maxValuesWithIndexes.insert(maxIndex, maxValue)
        else:
            maxValuesWithIndexes.append(maxValue)

    stringForm = ""
    for i in maxValuesWithIndexes:
        stringForm += str(i)

    return int(stringForm)


def main():
    data = getData()

    # part1
    sum = 0
    for line in data:
        maxValue1, maxIndex1 = getMaxWithIndex(line)

        split = ""
        if maxIndex1 == len(line)-1:
            maxValue2, maxIndex2 = getMaxWithIndex(line[:-1])
            maxValue1, maxValue2 = maxValue2, maxValue1
        else:
            maxValue2, maxIndex2 = getMaxWithIndex(line[maxValue1:])

        sum = int(str(maxValue1) + str(maxValue2))

    print("part1", sum)

    #part2
    sum = 0
    for line in data:
        sum += getMaxPossibleValue(line, 12)

    print("part2", sum)

main()