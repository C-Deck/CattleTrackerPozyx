class TagValue: 
    def __init__(self, time, x, y):
        self.time = time
        self.x = y
        self.y = y
    
    def __eq__(self, other):
        return (self.time == other.time) and (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "time: {0}, x: {1}, y: {2}".format(self.time, self.x, self.y)
    
    def getStr(self):
        return "{0}, {1}, {2}\n".format(self.time, self.x, self.y)
