from Classes import Point as p

tagCount = 11
numberOfPoints = 14400
secondIncrement = 5
avgDistanceCovered = 3000

def writeToFile(fileName, data):
    file = open(fileName, 'wb')
    for line in data:
        file.write(line)
        file.write('\n')
    file.close()


def createPointString(tagNumber):
    data = ""
    point = p.Point()
    for x in range(numberOfPoints + 1):
        point.movePointRandom(avgDistanceCovered)
        newLine = str(tagNumber) + ", " + point.getStr() + "\n"
        data = data + newLine

    return data


def createTagData(tagNumber):
    fileName = "tag{0}.csv".format(tagNumber)
    data = createPointString(tagNumber)
    writeToFile(fileName, data)

if __name__ == '__main__':
    for tagNumber in range(tagCount + 1):
        createTagData(tagNumber)
    print("Created data for tags")