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
        xTrace.append(self.points[0].x)
        yTrace.append(self.points[0].y)

        return { 'x': xTrace, 'y': yTrace, 'name': self.name }

    def printPlot(self):
        print("Plot")
        print("\tNumber: {0} - MumberTags".format(self.number, self.numberTags))
        print("\tPoints")
        for point in self.points:
            print(point)
        print("\tMinMaxes")
        print(self.minMaxX)
        print(self.minMaxY)
        print("\tTag Times")
        print(self.tagTimes)
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)