# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from plotly.figure_factory import create_2d_density
from Helper.figureBuilder import getInitialData, getFrames, getAllInitialData, getAllFrames, addTracesToFigure
from Helper.statBuilder import generateTagPlotTimeTable, getPlots, buildTags, buildTagData

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

"""
-------------------------------------------------------------------------------
----------------------------Global Variables Used------------------------------
-------------------------------------------------------------------------------
"""
xMinMax = 27
yMinMax = 69
squareSize = 3

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF'
}

colorscale = ['#7A4579', '#D56073', 'rgb(236,158,105)', (1, 1, 0.2), (0.98,0.98,0.98)]

tagCount = 5

"""
-------------------------------------------------------------------------------
----------------------------CSV and dataFrame stuff----------------------------
-------------------------------------------------------------------------------
"""
allFiles = []
for tag in range(tagCount):
    allFiles.append("csvs/tag{0}.csv".format(tag+1))

frameList = []
MinuteFrameList = []

# Combine all the frames into one
for filename in allFiles:
    df = pd.read_csv(filename, index_col=None, header=0)
    frameList.append(df)

# Combine all the frames into one on each minute
for dframe in frameList:
    df = dframe.loc[(dframe['time'] * 1.0) % 60 == 0]
    MinuteFrameList.append(df)

combinedFrame = pd.concat(frameList, axis=0, ignore_index=True)

df = combinedFrame.loc[(combinedFrame['time'] * 1.0) % 60 == 0]

df2 = frameList[0].loc[(combinedFrame['time'] * 1.0) % 60 == 0]

plots = getPlots(xMinMax, yMinMax, squareSize, True)
tags = buildTags(frameList, 9, 90, 15)
buildTagData(tags, plots)


"""
-------------------------------------------------------------------------------
--------------------------Creating the plotly figures--------------------------
-------------------------------------------------------------------------------
"""
scatterPointFigure = px.scatter(combinedFrame, x="x", y="y", color="tag", title="Scatter attempt")

heatmapFigure = create_2d_density(
    combinedFrame.x, combinedFrame.y, colorscale=colorscale,
    hist_color='rgb(255, 237, 222)', point_size=1, title='2D Density Plot', 
    height=1200, width=1200
)

trackingFigureAnimated = go.Figure(
    data=getAllInitialData(MinuteFrameList, len(MinuteFrameList)),
    layout=go.Layout(
        xaxis=dict(range=[-xMinMax - 10, xMinMax + 10], autorange=False),
        yaxis=dict(range=[-yMinMax - 10, yMinMax + 10], autorange=False),
        title="All Tag Tracker",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])],
        height=800
    ),
    frames=getAllFrames(MinuteFrameList, 12, MinuteFrameList[0]['x'].size)
)

# Add the Plots into the figures
addTracesToFigure(heatmapFigure, plots)
addTracesToFigure(trackingFigureAnimated, plots)


"""
-------------------------------------------------------------------------------
----------------------------Dash Building the webpage--------------------------
-------------------------------------------------------------------------------
"""
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Cattle Tracker',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children=['Scatter Plot of all the points',
            dcc.Graph(figure=scatterPointFigure)
        ],

        style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(children=['HeatMap',
            dcc.Graph(figure=heatmapFigure)
        ],

        style={
        'width': '100%',
        'display': 'inline-block'
    }),

    html.Div(children=[generateTagPlotTimeTable(tags)]),

    html.Div(children=['Tracking of the movements of the cows',

            dcc.Graph(figure=trackingFigureAnimated)
        ],

        style={
        'textAlign': 'center',
        'color': colors['text'],
        'display': 'inline-block',
        'width': '100%',
        'height': '100%'
    })
])


if __name__ == '__main__':
    app.run_server(debug=True)