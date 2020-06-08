# CattleTracker-Pozyx Visualization

Here is where we will finally see the data visualized. This is done using Dash and Plotly together to display the data.

## Setup

In order to run program, you will need to do some installing. There are a couple libraries that are needed in order for it to work.

### Prerequisites

To run this project, you will need:

* Python 3

### Installing the libraries

For visualization, we are using a combination of Dash and Plotly with Python. In order to use them, you need to install them for Python. We will be following the instructions from `https://dash.plotly.com/installation`. Those instructions are more in depth and you can go look at them if you want to. For the purpose of using this system, you don't need to go there though. Also, some code I am using requires one more install.

First, you must open commmand line. Then run this command:

`pip install dash==1.12.0`

After that is over, we need to install one more thing. It is a library called Pandas that helps read data. Just run

`pip install pandas==1.0.1`

Now you are good to go

## Running

Simply double click on app.py and it will run if you are in windows. Otherwise, you must go to the directory in terminal and type `python3 app.py`. Afterwards, it will ask you the number of tags that we have data on. In order for this to work, you will need to move the `tag_.csv` files to the `csvs` folder in the same directory as `app.py`. Otherwise, it will try to open the files and fail. Furthermore, they all have to be named in that format with "tag" and the number of the tag following it.

## Implementation

Our `app.py` is the main file were everything comes together. It combines everything from the data to the graphs and handles them all. In this file, there is a line that states

```
tagCount = 5
```

This value must be changed to the number of tags/csv files that you are using in order to get the data for all of them.

### Classes

For this implementation, we have created two classes to use. The first is just a simple `Point` class that only has an x and y. It doesn't do much besides act as a wrapper to contain the x and y in an easily readible object.

Our `Plot` class is where a lot of the data handling happens. Subplots are also considered plots, but they are contained within the main plot. This is the `subplots` value. 

A plot contains a list of points that are the vertexes of the plot and the edges run along them in that order. The minMax values are just the highest and lowest x and y that are within the plot. They are used to tell whether a point read in is within that plot. That is important for telling the amount of time that a tag has been within the plot.

Using those values, the plot also contains a dictionary connecting the tag number and the amount of time that it spent in that plot. We use that value to display some of the statistics that each plot has.

The functions with in the Plot class are used to help gather information based on the plots values. `getTraces` is a function that we use combined with plotly in order to draw the lines around the plot on a graph. It provides a step by step walk around the vertexes of the plot in order to draw lines around it in plotly. In the `figureBuilder` file there is a `addTracesToFigure` function that gets all the drawings for each plot and adds them to a graph that is passed into the function.

### StatBuilder

The `statBuilder.py` file is where all the statistic data is gathered. There are a lot of functions gather stats about each plot. They create the plots based on data passed in and use the tag data to build statistics on each plot. 

A main function in the file is `generatePlotTimeTable`. This function builds a dash data table using html for us to display. It takes in a list of plots and the number of tags we have. Using dash's html components, it builds a data table about the tags and plots to display how much time each tag spent in each plot. It can be used with an list of plots and we can use it to create tables about the subplots and their data.

### FigureBuilder

This is where the graphs we use are dynamically created based on the data we get from the CSV files. The `addTracesToFigure` draws the edges of the plots (called traces in plotly). The `getAllFrames` function creates a list of "Frames". These Frames are what we use to follow where the tags each went. Each frame represents a time and where the tag was at during that time. These functions gather all of that in order to be used in a Plotly graph animation.