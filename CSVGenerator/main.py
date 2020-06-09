
# Imports
from Classes import Tag.Tag
import csv

# Helper Functions

def createCSV(tag):
    filename = tag.getFilename()
    data = [["tag", "time", "x", "y"]]
    data = data + tag.getValueArr()
    csvfile = open(fileName, 'w', newline='')
    # creating a csv writer object  
    csvwriter = csv.writer(filename)  
        
    # writing the fields  
    csvwriter.writerows(data)
    csvfile.close()


def checkAddValue(json, tag):
    newTime = json.get("timestamp")
    if newTime > (tag.getLatestTime() + 5):
        coords = json.get("data").get("coordinates")
        x = coords['x'] / 1000.0                        # Convert to meters from millimeters
        y = coords['y'] / 1000.0                        # Convert to meters from millimeters
        tag.addValue(newTime, x, y)

def parseValue(json, tagsDict):
    if json['success'] == True:
        tagNumber = json['tagId']
        if tagNumber in tagsDict:
            tag = tagsDict.get(tagNumber)
            checkAddValue(json, tag)
        else:
            tag = Tag(tagNumber)
            checkAddValue(json, tag)


# Main function
if __name__ == '__main__':
    tags = {}

    jsonFile = open("output.json", "r")
    data = json.load(jsonFile)

    for value in data:
        parseValue(json, tags)
    jsonFile.close()

    for tag in tags:
        createCSV(tag)