import random

class Point: 
    def __init__(self, x = None, y = None):
        if(type(x)==int and type(y)==int):
            self.x = y
            self.y = y
        else:
            self.x = 0
            self.y = 0
    
    def __eq__(self, other):
        # Note: generally, floats should not be compared directly
        # due to floating-point precision
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)

    def movePointRandom(self, avgDistanceCovered):
        randomX = random.randint(-avgDistanceCovered, avgDistanceCovered)
        randomY = random.randint(-avgDistanceCovered, avgDistanceCovered)
        self.x += randomX
        self.y += randomY
    
    def getStr(self):
        return "{0}, {1}".format(self.x, self.y)