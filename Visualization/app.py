# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from plotly.figure_factory import create_2d_density
from Helper.createFigure import getInitialData, getFrames, getAllInitialData, getAllFrames

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

xMinMax = 27
yMinMax = 69

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

colorscale = ['#7A4579', '#D56073', 'rgb(236,158,105)', (1, 1, 0.2), (0.98,0.98,0.98)]

tagCount = 5

allFiles = []
for tag in range(tagCount):
    allFiles.append("csvs/tag{0}.csv".format(tag+1))

li = []
li2 = []

for filename in allFiles:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

for dframe in li:
    df = dframe.loc[(dframe['time'] * 1.0) % 60 == 0]
    li2.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

df = frame.loc[(frame['time'] * 1.0) % 60 == 0]

df2 = li[0].loc[(frame['time'] * 1.0) % 60 == 0]

fig = px.scatter(frame, x="x", y="y", color="tag", title="Scatter attempt")

fig2 = create_2d_density(
    frame.x, frame.y, colorscale=colorscale,
    hist_color='rgb(255, 237, 222)', point_size=1, title='2D Density Plot', 
    height=600, width=1200
)

#fig3 = px.scatter(df, x="x", y="y", animation_frame="time", animation_group="tag", color="tag", hover_name="tag", size="time", size_max=1)
fig3 = go.Figure(
    data=getInitialData(df2),
    layout=go.Layout(
        xaxis=dict(range=[-xMinMax, xMinMax], autorange=False),
        yaxis=dict(range=[-yMinMax, yMinMax], autorange=False),
        title="Tag 1 Tracker",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])],
        height=1600,
        width=1200
    ),
    frames=getFrames(df2, 12)
)

fig4 = go.Figure(
    data=getAllInitialData(li2, len(li2)),
    layout=go.Layout(
        xaxis=dict(range=[-xMinMax, xMinMax], autorange=False),
        yaxis=dict(range=[-yMinMax, yMinMax], autorange=False),
        title="All Tag Tracker",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])],
        height=1600,
        width=1200
    ),
    frames=getAllFrames(li2, 12, li2[0]['x'].size)
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Cattle Tracker',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children=['Tracking of the movements of the cows',
            dcc.Graph(figure=fig)
        ],

        style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(figure=fig2),

    dcc.Graph(figure=fig3),

    dcc.Graph(figure=fig4)
])


if __name__ == '__main__':
    #global tagCount
    #print("Enter the number of tags: ")
    #tagCount = input()
    app.run_server(debug=True)