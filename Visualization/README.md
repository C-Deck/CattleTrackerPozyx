# CattleTracker-Pozyx Visualization

Here is where we will finally see the data visualized. This is done using Dash and Plotly together to display the data.

## Setup

In order to run program, you will need to do some installing. There are a couple libraries that are needed in order for it to work.

### Prerequisites

To run this project, you will need:

* Python 3

### Installing the libraries

For visualization, we are using a combination of Dash and Plotly with Python. In order to use them, you need to install them for Python. We will be following the instructions from `https://dash.plotly.com/installation`. Those instructions are more in depth and you can go look at them if you want to. For the purpose of using this system, you don't need to go there though.

First, you must open commmand line. Then run this command:

`pip install dash==1.12.0`

Now you are good to go

## Running

Simply double click on app.py and it will run. Afterwards, it will ask you the number of tags that we have data on. In order for this to work, you will need to move the `tag_.csv` files to the directory that you have `app.py` in. Otherwise, it will try to open the files and fail. Furthermore, they all have to be named in that format with "tag" and the number of the tag following it.