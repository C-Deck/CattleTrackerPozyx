# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from plotly.figure_factory import create_2d_density

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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

for filename in allFiles:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

df = frame.loc[(frame['time'] * 1.0) % 60 == 0]

fig = px.scatter(frame, x="x", y="y", color="tag", title="Scatter attempt")

fig2 = create_2d_density(
    frame.x, frame.y, colorscale=colorscale,
    hist_color='rgb(255, 237, 222)', point_size=1, title='2D Density Plot', 
    height=600, width=600
)

fig3 = px.scatter(df, x="x", y="y", animation_frame="time", animation_group="tag", color="tag", hover_name="tag", size="time", size_max=1)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Cattle Tracker',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children=['Tracking of the movements of the cows',
        dcc.Graph(figure=fig),

        dcc.Graph(figure=fig2),

        dcc.Graph(figure=fig3)],
        
        style={
        'textAlign': 'center',
        'color': colors['text']
    })
])


if __name__ == '__main__':
    #global tagCount
    #print("Enter the number of tags: ")
    #tagCount = input()
    app.run_server(debug=True)