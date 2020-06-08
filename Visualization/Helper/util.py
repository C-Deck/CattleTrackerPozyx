from Helper.Classes import Plot, Point

"""
    Checks if the given point is in the plot
    point = x (format)
    plot = [valMin, valMax]
"""
def withinValues(val, vals):
    return vals[0] <= val and vals[1] >= val

"""
    Checks if the given point is in the plot
    point = [x,y] format
    plot = [[xMin, xMax], [yMin, yMax]]
"""
def isWithinPlot(point, plot):
    if withinValues(point[0], plot[0]) and withinValues(point[1], plot[1]):
        return True
    return False

"""
    Gives a dict of subplots
    xVals = [xMin, xMax]
    yVals = [yMin, yMax]
    widthCount = number of subplots wide
    heightCount = number of subplots high
"""
def getSubPlots(xVals, yVals, widthCount, heightCount):
    subplots = []
    subplotNumber = 0
    xIncrement = (xVals[1] - xVals[0]) / widthCount
    yIncrement = (yVals[1] - yVals[0]) / heightCount

    currentX = xVals[0]
    currentY = yVals[0]

    for i in range(widthCount):
        for k in range(heightCount):
            subplotNumber += 1
            points = [Point(currentX, currentY), Point(currentX + xIncrement, currentY), Point(currentX + xIncrement, currentY + yIncrement), Point(currentX, currentY + yIncrement)]
            currentY += yIncrement
            plot = Plot(subplotNumber, points)
            subplots.append(plot)
        currentY = yVals[0]
        currentX += xIncrement

    return subplots