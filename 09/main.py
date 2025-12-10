import math

def getData() -> list[tuple[int, int]]:
    filePath = input("filePath: ")
    file = open(filePath, "r")

    points = []
    for line in file:
        parts = line.split(',')
        if len(parts) != 2:
            raise "haloooo?"

        partA = int(parts[0])
        partB = int(parts[1])
        points.append((partA, partB))

    return points


def distance(A: tuple[int, int], B: tuple[int, int]) -> float:
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def getClosest(A, listOfPoints) -> tuple[int, int]:
    closestPoint = listOfPoints[0]
    currentDistance = distance(A, closestPoint)

    for point in listOfPoints:
        tempDistance = distance(A, point)
        if tempDistance < currentDistance:
            currentDistance = tempDistance
            closestPoint = point

    return closestPoint


def rectArea(A: tuple[int, int], B: tuple[int, int]) -> int:
    x = abs((A[0] - B[0]))+1
    y = abs((A[1] - B[1]))+1
    return x*y


def main():
    points = getData()
    # maxX = points[0][0]
    # maxY = points[0][1]
    # for i in points:
    #     if maxX < i[0]: maxX = i[0]
    # for i in points:
    #     if maxY < i[1]: maxY = i[1]
    #
    # cornerUL = getClosest((0,0), points)
    # cornerUR = getClosest((maxX, 0), points)
    # cornerBL = getClosest((0, maxY), points)
    # cornerBR = getClosest((maxY, maxY), points)
    #
    # print(cornerUL, cornerUR, cornerBL, cornerBR)
    #
    # print("-----")
    # print("distance1: ", distance(cornerUL, cornerBR))
    # print("area1: ", rectArea(cornerUL, cornerBR))
    #
    # print("distance2: ", distance(cornerUR, cornerBL))
    # print("area2: ", rectArea(cornerUR, cornerBL))
    # print("-----")
    #
    # if distance(cornerUL, cornerBR) > distance(cornerUR, cornerBL):
    #     print("distance: ", distance(cornerUL, cornerBR))
    #     print(f"points: {cornerUL}; {cornerBR}")
    #     print("area: ", rectArea(cornerUL, cornerBR))
    # else:
    #     print("distance: ", distance(cornerUR, cornerBL))
    #     print(f"points: {cornerUR}; {cornerBL}")
    #     print("area: ", rectArea(cornerUR, cornerBL))

    maxDis = distance(points[0], points[1])
    currentPoint = points[0]
    tempPoint = points[1]
    #TODO: még egy for a point léptetésre
    for point in points:
        tempDis = distance(currentPoint, point)
        if(tempDis > maxDis):
            maxDis = tempDis
            tempPoint = point

main()