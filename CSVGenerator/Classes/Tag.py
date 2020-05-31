from .TagValue import TagValue

class Tag:
    def __init__(self, tagNumber):
        self.tagNumber = tagNumber
        self.latestTime = 0
        self.values = []

    def getFilename(self):
        return "tag{0}.csv".format(self.tagNumber)

    def addValue(self, time, x, y):
        tagValue = TagValue(time, x, y)
        self.values.append(tagValue)
        self.latestTime = tagValue.time

    def addTagValue(self, tagValue):
        self.values.append(tagValue)
        self.latestTime = tagValue.time

    def getValueString(self):
        outputString = ""
        for val in self.values:
            outputString = outputString + val.getStr()
        return outputString

    def getLatestTime(self):
        return self.latestTime