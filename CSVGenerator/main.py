
# Imports
from Classes import Tag.Tag

# Helper Functions

def createCSV(tag):
    filename = tag.getFilename()
    file = open(fileName, 'wb')
    for line in data:
        file.write(line)
        file.write('\n')
    file.close()


def checkAddValue(json, tag):
    newTime = json.get("timestamp")
    if newTime > tag.getLatestTime() + 5:
        coords = json.get("data").get("coordinates")
        x = coords['x']
        y = coords['y']
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