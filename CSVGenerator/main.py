
# Imports
from Classes.Tag import Tag
import csv
import json

# Helper Functions

def createCSV(tag):
    filename = tag.getFilename()
    data = [["tag", "time", "x", "y"]]
    data = data + tag.getValueArr()
    csvfile = open(filename, 'w', newline='')
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerows(data)
    csvfile.close()


def checkAddValue(value, tag):
    newTime = value["timestamp"]
    if newTime > (tag.getLatestTime() + 5):
        coords = value.get("data").get("coordinates")
        x = coords['x'] / 1000.0                        # Convert to meters from millimeters
        y = coords['y'] / 1000.0                        # Convert to meters from millimeters
        tag.addValue(newTime, x, y)

def parseValue(value, tagsDict):
    if value['success'] == True:
        tagNumber = value['tagId']
        if tagNumber in tagsDict:
            tag = tagsDict.get(tagNumber)
            checkAddValue(value, tag)
        else:
            tag = Tag(tagNumber)
            tagsDict[tagNumber] = tag
            checkAddValue(value, tag)

# Main function
if __name__ == '__main__':
    tags = {}

    jsonFile = open("output.json", "r")
    data = json.load(jsonFile)

    for value in data:
        parseValue(value, tags)
    jsonFile.close()

    for tag in tags.values():
        createCSV(tag)