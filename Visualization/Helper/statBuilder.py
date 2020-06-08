import dash_html_components as html

from Helper.util import withinValues, isWithinPlot, getSubPlots
from Helper.Classes import Plot, Point

"""
    Gives the amount of time 
    tagFrame = pandas dataFrame
    plot = [[xMin, xMax], [yMin, yMax]]
"""
def getPlotTime(tagFrame, plot):
    totalTime = 0
    currentTime = 0
    for k in range(tagFrame['x'].size):
        point = Point(tagFrame['x'][k], tagFrame['y'][k])
        if plot.isWithinPlot(point):
            currentTime += 5
        else:
            totalTime += currentTime
            currentTime = 0
    
    return totalTime

"""
        Gets the amount of time the tag spends in each plot
"""
def getPlotTimes(tagNumber, tagFrame, plots):
    for plot in plots:
        timeForPlot = getPlotTime(tagFrame, plot)
        plot.addTagTime(tagNumber, timeForPlot)

"""
        Gets the subplots for the plot
"""
def getSubplotsForPlot(plot):
    subplots = getSubPlots(plot.minMaxX, plot.minMaxY, 3, 6)
    plot.addSubplots(subplots)

"""
        Gets all the plots and subplots with their times
"""
def getPlots(xMinMax, yMinMax, squareSize, doGetSubPlots):
    plots = getSubPlots([-xMinMax, xMinMax], [-yMinMax, yMinMax], squareSize, squareSize)

    if doGetSubPlots == True:
        for plot in plots:
            getSubplotsForPlot(plot)

    return plots

def getPlotsWithTimes(tagFrameList, xMinMax, yMinMax, squareSize, doGetSubPlots):
    plots = getPlots(xMinMax, yMinMax, squareSize, getSubPlots)

    for i in range(len(tagFrameList)):
        getPlotTimes(i, tagFrameList[i], plots)

    return plots

def getTimesForTag(tagNumber, plots):
    times = [0] * len(plots)
    for plot in plots:
        times[plot.number] = plot.tagTimes[tagNumber]
    
    return times

"""
        Generate a Dash html table
"""
def generatePlotTimeTable(plots, numberTags):
    rows = []
    for i in range(numberTags):
        row = [html.Td("Tag " + str(i + 1))]

        times = getTimesForTag(i, plots)
        for value in times:
            row.append(html.Td(str(value) + " seconds"))

        rows.append(html.Tr(row))

    return html.Table([
        html.Thead(
            html.Tr([html.Th("Tag Number")] + [html.Th("Plot " + (str(col + 1))) for col in range(len(plots))])
        ),
        html.Tbody(rows)
    ])

def generateSubplotTimeTable(plot, numberTags):
    return generatePlotTimeTable(plot.subplots, numberTags)