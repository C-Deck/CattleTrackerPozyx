import random

class Point:
    def __init__(self, minMaxX, minMaxY, x = None, y = None):
        if(type(x)==int and type(y)==int):
            self.x = y
            self.y = y
        else:
            randomStartPoints = self.getRandomStartPoint(minMaxX, minMaxY)
            self.x = randomStartPoints[0]
            self.y = randomStartPoints[1]
        self.minMaxX = minMaxX
        self.minMaxY = minMaxY
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)

    def movePointRandom(self, avgDistanceCovered):
        secure_random = random.SystemRandom()
        doMove = random.randint(0,4)
        if doMove == 1:
            randomX = secure_random.uniform(-avgDistanceCovered, avgDistanceCovered)
            randomY = secure_random.uniform(-avgDistanceCovered, avgDistanceCovered)
            if self.checkMinMax(randomX, randomY):
                self.x += randomX
                self.y += randomY

    def getRandomStartPoint(self, minMaxX, minMaxY):
        secure_random = random.SystemRandom()
        randomX = secure_random.uniform(-minMaxX, minMaxX)
        randomY = secure_random.uniform(-minMaxY, minMaxY)
        return [randomX, randomY]
    
    def getStr(self):
        return "{0}, {1}".format(self.x, self.y)

    def checkMinMax(self, addedX, addedY):
        if (self.x + addedX > self.minMaxX or self.x + addedX < (-self.minMaxX)):
            return False
        if (self.y + addedY > self.minMaxY or self.y + addedY < (-self.minMaxY)):
            return False
        else:
            return True