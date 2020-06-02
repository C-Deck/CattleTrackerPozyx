class TagValue: 
    def __init__(self, tagNumber, time, x, y):
        self.time = time
        self.x = y
        self.y = y
        self.tagNumber = tagNumber
    
    def __eq__(self, other):
        return (self.time == other.time) and (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "Tag: {0}, time: {1}, x: {2}, y: {3}".format(self.tagNumber, self.time, self.x, self.y)
    
    def getStr(self):
        return "{0}, {1}, {2}, {3}\n".format(self.tagNumber, self.time, self.x, self.y)

    def getArr(self):
        return [str(self.tagNumber), self.time, self.x, self.y]
