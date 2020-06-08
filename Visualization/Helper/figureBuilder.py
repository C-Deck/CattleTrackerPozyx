import pandas as pd

import plotly.graph_objects as go

"""
    Returns initial data for one frame
"""
def getInitialData(pandasFrame):
    xArray = pandasFrame['x']
    yArray = pandasFrame['y']
    data = data=[go.Scatter(
                x = [xArray[0]],
                y = [yArray[0]],
                mode="markers",
                marker={
                    "sizemode": "area",
                    "sizeref": 200000,
                    "size": 1
                },
                name = "tag"
            )]

    return data

"""
    Returns frames for the animation
"""
def getFrames(pandasFrame, increment):
    list_of_frames = []

    xArray = pandasFrame['x']
    yArray = pandasFrame['y']

    for k in range(xArray.size):
        list_of_frames.append(
            go.Frame(
                data=[go.Scatter(
                    x = [xArray[k * increment]],
                    y = [yArray[k * increment]],
                    mode="markers",
                    marker={
                        "size": 6,
                        "line": {
                            "width":2, 
                            "color": 'DarkSlateGrey'
                        }
                    },
                    name = "tag"
                )]
            )
        )


    return list_of_frames

def getAllInitialData(pandasFrame, length):
    data = []
    for k in range(length):
        xArray = pandasFrame[k]['x']
        yArray = pandasFrame[k]['y']
        data.append(go.Scatter(
            x = [xArray[0]],
            y = [yArray[0]],
            mode="markers",
            marker={
                "size": 6,
                    "line": {
                    "width": 2, 
                    "color": 'DarkSlateGrey'
                }
            },
            name = "tag" + str(k)
        ))

    return data

def getCurrentData(allFrames, idx):
    data = []
    for k in range(len(allFrames)):
        xArray = allFrames[k]['x']
        yArray = allFrames[k]['y']
        data.append(
            go.Scatter(
                x = [xArray[idx]],
                y = [yArray[idx]],
                mode="markers",
                marker={
                    "size": 6,
                    "line": {
                        "width": 2, 
                        "color": 'DarkSlateGrey'
                    }
                },
                name = "tag" + str(k + 1)
            )
        )
    
    return data

def getAllFrames(allFrames, increment, length):
    list_of_frames = []

    for k in range(length):
        list_of_frames.append(
            go.Frame(
                data=getCurrentData(allFrames, k * increment)
            )
        )


    return list_of_frames


def createTraces(plots):
    allTraces = []

    for plot in plots:
        plot.printPlot()
        traces = plot.getTraces()
        allTraces.append(traces)

    return allTraces

def addTracesToFigure(figure, plots):
    traces = createTraces(plots)
    print(traces)

    for i in range(len(traces)):
        figure.add_trace(go.Scatter(
            x = traces[i]['x'],
            y = traces[i]['y'],
            showlegend = False,
            name = traces[i]['name']
        ))