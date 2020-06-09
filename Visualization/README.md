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

Our `app.py` is the main file were everything comes together. It combines everything from the data to the graphs and handles them all. In this file, there is a line that states.

```
tagCount = 5
```

This value must be changed to the number of tags/csv files that you are using in order to get the data for all of them.

In the `app.py` the core data for the statistics is gathered in three lines:

```
plots = getPlots(xMinMax, yMinMax, squareSize, True)
tags = buildTags(frameList, 9, 90, 15)
buildTagData(tags, plots)
```

`getPlots` gets the plots because on the number of plots, the height of the land, and width of the land. The last value states whether to break these further into subplots or not.

`buildTags` creates a list of Tag objects (described later in the document). The handle the data for each tag. 

`buildTagData` uses the Tag objects and the plot list to gather the amount of time spent by each tag in every plot and subplot.

### Classes

For this implementation, we have created two classes to use. The first is just a simple `Point` class that only has an x and y. It doesn't do much besides act as a wrapper to contain the x and y in an easily readible object.

Our `Plot` class is where a lot of the data handling happens. Subplots are also considered plots, but they are contained within the main plot. This is the `subplots` value. 

A plot contains a list of points that are the vertexes of the plot and the edges run along them in that order. The minMax values are just the highest and lowest x and y that are within the plot. They are used to tell whether a point read in is within that plot. That is important for telling the amount of time that a tag has been within the plot.

The functions with in the Plot class are used to help gather information based on the plots values. `getTraces` is a function that we use combined with plotly in order to draw the lines around the plot on a graph. It provides a step by step walk around the vertexes of the plot in order to draw lines around it in plotly. In the `figureBuilder` file there is a `addTracesToFigure` function that gets all the drawings for each plot and adds them to a graph that is passed into the function.

Finally, we have a `Tag` class. It is how we keep track of the stats and data for each tag along with holding the Pandas dataFrame. In the tag class, we keep track of the number of plots, the number of subplots per a plot, and the num of species per a subplot. Later on, we use these, the points of the tag, and the plots/subplots to record the amount of time that a tag spends in each. For each point in a plot/subplot, the tag time for that plot/subplot gets increased by 5 seconds. When a point is in the subplot, it figures out which species it was and adds 5 seconds to the total time for that species.

### Util

We have a file called `util.py` that contains a functions that we consider "utility" functions.

The most important function is the `getSubPlots` function. This is used to create our plots/subplots. It takes a [minumum x, maximum x] array, [minumum y, maximum y] array, the number of plots wide we are, and the number of plots tall. It then creates our plots starting from the top left going to the right and then down. It numbers them as such from 1 to n. For our mental model, that is how we will be thinking of the ordering. 

There is also another function called `getSubPlotsBottom` that is the same thing but starts from the bottom left going right and then up instead. It is here in case we choose to switch the mental model of numbering.

### StatBuilder

The `statBuilder.py` file is where all the statistic data is gathered. There are a lot of functions gather stats about each plot. They create the plots based on data passed in and use the tag data to build statistics on each plot. 

A main function in the file is `generateTagPlotTimeTable`. This function builds a dash data table using html for us to display. It takes in a list of Tag objects. Using dash's html components, it builds a data table about the tags and plots to display how much time each tag spent in each plot. It can be used with an list of plots and we can use it to create tables about the subplots and their data. A simular function was created to get the data for a specific plots subplot and for the species.

The core statistic function is `buildTagData`:

```
def buildTagData(tags, plots):
    for tag in tags:
        for k in range(tag.frame['x'].size):
            point = Point(tag.frame['x'][k], tag.frame['y'][k])
            for plot in plots:
                if k == 0:
                    plot.addTagTime(tag.number, 0)
                if plot.isWithinPlot(point):
                    tag.plotTimes[plot.number - 1] += 5
                    plot.addTagTime(tag.number, 0)
                    for subplot in plot.subplots:
                        if subplot.isWithinPlot(point):
                            tag.subplotTimes[plot.number - 1][subplot.number - 1] += 5
                            tag.speciesTimes[(subplot.number - 1) % tag.numSpecies] += 5
```

Here we go through every Tag object in the tag list, and go through each of its points. With these points, we check every plot and subplot of that plot to check if the point is in that plot/subplot. If it is, we increase the Tag's record of the time in that plot/subplot. We only check the subplots of a plot if the point was within that plot. We know that if it is not in the plot, it won't be in one of the subplots of that plot. Therefore, there is no need to check each subplot which speeds things up. Also, when we are checking subplots, we increase the time in a species based on the number of species. For our purpose, there are 90 subplots and 15 species. We are assuming that these 15 species go in order 4 times in a row. Therefore, if we do the (subplot / number of species) and take the remainder, it will tell us which species it is. That is the `tag.speciesTimes[(subplot.number - 1) % tag.numSpecies]`.

### FigureBuilder

This is where the graphs we use are dynamically created based on the data we get from the CSV files. The `addTracesToFigure` draws the edges of the plots (called traces in plotly). The `getAllFrames` function creates a list of "Frames". These Frames are what we use to follow where the tags each went. Each frame represents a time and where the tag was at during that time. These functions gather all of that in order to be used in a Plotly graph animation.

In order to create each frame, for each time we get the point of each tag. Using that point, we create a list of Plotly `Scatter` dots that will represent the Tag at that point in time. That will then be that frame. `getAllFrames` does this for every time value.