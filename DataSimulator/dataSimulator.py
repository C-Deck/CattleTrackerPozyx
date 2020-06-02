from Classes import Point as p
import csv

tagCount = 5
numberOfPoints = 14400
secondIncrement = 5
avgDistanceCovered = 1.5    # 1.5 meters meters over 5 seconds if the cow is moving
minMaxX = 27                # The plot is 54 meters wide so 27 meters to the left and right
minMaxY = 69                # The plot is 138 meters wide so 69 meters up and down

def writeToFile(fileName, data):
    csvfile = open(fileName, 'w', newline='')
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerows(data)
    csvfile.close()


def createPointString(tagNumber):
    data = [["tag", "time", "x", "y"]]
    point = p.Point(minMaxX, minMaxY)
    time = 0
    for x in range(numberOfPoints + 1):
        point.movePointRandom(avgDistanceCovered)
        newLine = [str(tagNumber), str(time), str(point.x), str(point.y)]
        data.append(newLine)
        time += 5

    return data


def createTagData(tagNumber):
    fileName = "tag{0}.csv".format(tagNumber)
    data = createPointString(tagNumber)
    writeToFile(fileName, data)

if __name__ == '__main__':
    for tagNumber in range(tagCount):
        createTagData(tagNumber + 1)
    print("Created data for tags")