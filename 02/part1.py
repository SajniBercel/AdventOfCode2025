def getCodeRanges() -> list[[int, int]]:
    filePath = input("filePath:")
    file = open(filePath, "r")

    output = []
    for line in file:
        codeRanges = line.split(',')
        for codeRange in codeRanges:
            parts = codeRange.split('-')
            partA = int(parts[0])
            partB = int(parts[1])

            if len(parts) > 2:
                print("valami baj van")
                exit(67)

            output.append([partA, partB])

    return output

# part2
def isValid(sCode: str) -> bool:
    for splitLen in range(1, len(sCode)//2):
        partA = sCode[:splitLen]
        for i in range(splitLen, len(sCode), splitLen):

            if i+splitLen < len(sCode):
                partB = sCode[i:i+splitLen]
            else:
                partB = sCode[i:]

            if partA == partB:
                return True
    return False

def main():
    codeRanges = getCodeRanges()
    # part1

    sum = 0
    for codeRange in codeRanges:
        for code in range(codeRange[0], codeRange[1]+1):
            sCode = str(code)
            half = len(sCode) // 2
            if sCode[:half] == sCode[half:]:
                sum += int(sCode[half:])

    print("part1:",sum)

    # part2
    sum = 0
    for codeRange in codeRanges:
        for code in range(codeRange[0], codeRange[1]+1):
            sCode = str(code)
            if not isValid(sCode):
                sum += int(sCode)

    print("part2:",sum)



main()