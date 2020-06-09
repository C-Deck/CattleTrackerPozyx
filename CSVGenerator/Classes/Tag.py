from Classes.TagValue import TagValue

class Tag:
    def __init__(self, tagNumber):
        self.tagNumber = tagNumber
        self.latestTime = 0
        self.values = []
        self.currentTime = 0

    def getFilename(self):
        return "tag{0}.csv".format(self.tagNumber)

    def addValue(self, time, x, y):
        tagValue = TagValue(self.tagNumber, self.currentTime, x, y)
        self.values.append(tagValue)
        self.latestTime = tagValue.time
        self.currentTime += 5

    def addTagValue(self, tagValue):
        self.values.append(tagValue)
        self.latestTime = tagValue.time
        self.currentTime += 5

    def getValueArr(self):
        outputString = []
        for val in self.values:
            outputString.append(val.getArr())
        return outputString

    def getLatestTime(self):
        return self.latestTime