import Helper.util as UTIL

class Plot:
    def __init__(self, number, points):
        self.number = number
        self.points = points
        self.minMaxX = self.calcMinMax(points, 'x')
        self.minMaxY = self.calcMinMax(points, 'y')
        self.subplots = []
        self.tagTimes = {}
        self.numberTags = 0
        self.name = "Plot " + str(number)
    
    def __eq__(self, other):
        return (self.number == other.number)

    def calcMinMax(self, points, axis):
        values = []
        for point in points:
            if axis == 'x':
                values.append(point.x)
            else:
                values.append(point.y)
        minVal = min(values)
        maxVal = max(values)
        return [minVal, maxVal]

    def isWithinPlot(self, point):
        if UTIL.withinValues(point.x, self.minMaxX) and UTIL.withinValues(point.y, self.minMaxY):
            return True
        return False
    
    def addSubplot(self, subplot):
        self.subplots.append(subplot)

    def addSubplots(self, subplots):
        self.subplots.extend(subplots)

    def addTagTime(self, tag, time):
        self.tagTimes[tag] = time
        self.numberTags += 1

    def getTraces(self):
        xTrace = []
        yTrace = []
        for point in self.points:
            xTrace.append(point.x)
            yTrace.append(point.y)

        return { 'x': xTrace, 'y': yTrace, 'name': self.name }
    
class Point:
    def __init__(self, x = None, y = None):
        if(type(x)==int and type(y)==int):
            self.x = y
            self.y = y
        else:
            self.x = 0
            self.y = 0
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)