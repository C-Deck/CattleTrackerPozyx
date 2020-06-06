# CattleTracker-Pozyx

In cooperation with the College of Agriculture, Food, and Environmental Studies, Dr. Marc Horney desired the development of a system capable of tracking the whereabouts of an amount of cattle within a specified plot. We acquired a system called Pozyx to use. Pozyx provides the ability to track an individual cow at real time, which allows the ability to differentiate cow activity within a specified plot. This will be achieved by isolating the x-coordinate and y-coordinate along with the time to track the activity such as grazing or resting. In regards to our client, this will be beneficial for his project needs as he will be able to employ this system to continuously track his cattle to determine which grass species plot cattle tend to spend the majority of their time in as well as what kind of grass they prefer to eat.

## Introduction

The Cal Poly College of Agriculture, Food, and Environmental Science (CAFES) reached out to our team in order to develop an intuitive way to gather information on their cattle and make data-driven decisions. If CAFES does not decide to make more data-driven decisions, they will not be able to scale their system and employees will continue to perform inefficiently. The team has been working with two faculty members from the Animal Science Department of the College of Agriculture, Food, and Environmental Sciences to develop a portable and scalable system. The system requirements are to track the amount of time their cattle spend grazing in each specific 3 x 3m grass cell contained in a larger 18 x 46m treatment plot. This project will give great assistance to the Animal Science Department to accurately discover which grass species are most preferable among Cal Poly’s herd of cattle. It will also be a scalable foundation to provide for the future collection of additional cattle metrics, which could be implemented by the department, small scale dairy farms, or beef cattle ranchers. The cost of implementing such a system goes for upwards of hundreds of thousands of dollars along with yearly subscription payments to use their software and server power. Creating a cheaper, more accurate solution that does not include features that smaller operations do not require will help fill the middle market between industrial-sized cattle tracking and individual pet monitoring.

## Background

Currently, cattle are grazing at two different ranches at Cal Poly. Every morning, dairy students are sent out over hundreds of acres to “check” on a total of 170 cattle. After discussing the current method for collecting data on the cattle with sponsor Marc Horney and Luke Jelmini (an employed student), it was discovered that contemporary methods are too unregimented, labor-intensive, and full of error. For example, Luke must individually count the cattle with their eyesight and record the data by hand, leading to miscounting and misconstrued data. Luke also explained that his tasks will vary completely upon the day, weather, cattle location, and cattle health. For example, rainy days are considerably more difficult to track the cattle due to poor visibility and dangerous conditions for the employees, leading to null data. Having this variation makes it extremely difficult or even impossible for him as an employee to get consistent data each shift. Once a worker arrives for his shift, either early in the morning or in the afternoon, he/she is assigned an area to check on and count cattle. Once he/she has covered the whole area, they return back to the dispatch point. According to an interviewed employee, total driving time to and from the fields takes on average 25 minutes and the total record keeping time of the cows takes on average 40 minutes.

## Implementation

The implementation was broken up into four parts.

* Code to gather the data
* Code to build CVS files for each cow
* Code to build theoretical data (This is for testing purposes)
* Code to visualize and display the data

They are all broken up into subfolders. Each of them has their own README document explaining how to set them up and run them along with how they work. 

### Gathering the data

The subfolder for gathering data is [PozyxMQTT-Python](PozyxMQTT-Python/README.md). There is also a Java version, but we will no longer be using that in order to keep everything linear. The rest of the work is in Python, so we are sticking to that.

The Pozyx system has a messaging protocol called MQTT that we are able to connect to in order to receive messages. As it gathers data, it sends out JSON (JavaScript Object Notation) values to anything connected to it through MQTT. Those values come out in the following format.

```
[{
  {
  "version": "1",
  "tagId": "24576",
  "success": true,
  "timestamp": 1524496105.895,
  "data": {
    "tagData": {
      "gyro": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "magnetic": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "quaternion": {
        "x": 0,
        "y": 0,
        "z": 0,
        "w": 0
      },
      "linearAcceleration": {
        "x": 0,
        "y": 0,
        "z": 0
      },
      "pressure": 0,
      "maxLinearAcceleration": 0
    },
    "anchorData": [],
    "coordinates": {
      "x": 1000,
      "y": 1000,
      "z": 0
    },
    "acceleration": {
      "x": 0,
      "y": 0,
      "z": 0
    },
    "orientation": {
      "yaw": 0,
      "roll": 0,
      "pitch": 0
    },
    "metrics": {
      "latency": 2.1,
      "rates": {
        "update": 52.89,
        "success": 52.89
      }
    }
  }
}
}]
```

Using these values, we can extract data about the different cows that we are tracking. For the purpose of this project, we will be using the time, x, and y values. Using these values, we can figure out where on the plot the cows are spending their time. The program for gathering the data will connect to the Pozyx system and create a JSON file containing all of the data which will be later turned into CSV files for each of the cows.

### Build CSV Files

The subfolder for building CSV files is [CSVGenerator](CSVGenerator/README.md).

This is a program that files the JSON file created previously and creates a CSV file for each cow. The CSV file format is `tag, time, x, y`. For our purposes, this is all we need. The tag number is necessary later for the visualization.

### Theoretical Data

The subfolder for creating theoretical data is [DataSimulator](DataSimulator/README.md).

This is a program that creates movement data and CSV files for a set number of cows. In order to develop the visualization, data is needed to test it. This program creates that data. It creates a fake cow and has it move within a constrained field. As it moves (or doesn't), the program records that and eventually outputs all of that data into a CSV file. 

### Visualization

The subfolder for creating theoretical data is [Visualization](Visualization/README.md).

This program uses Dash and Plotly in order to display the data. There is some setup involved that is described in the folders README. Using these tools, it creates a webpage displaying graphs and data about the movement of the cows. 

## Reflection

Overall, the outcome of this project is not quite what we would hope. There were many external factors that caused problems with the ability to work. Due to the coronavirus situation, we were not able to do any testing with the Pozyx devices.

### Speed

One of the major problems with this program is the speed. We are working with many libraries that we have no control over how they handle the data to make sure it is fast. When programming, there are small things that can affect how fast the program runs. When using external libraries, we have no control over these. 

Another problem is that we are using Python. Python is an interpretted language which runs slow. Faster programming languages such as C or Java are compiled and run much faster. We would be better off developing in one of those in the future for more speed. The problem with those languages is that they don't have as many external libraries for us to use for data. We would have to write those on our own which would be a lot more work.

### Precision

With our data, it is difficult to be precise on whether or not the cows are grazing when they are at their location. Due to this, we will just have to assume that the cows prefer the plots that they have spent more time on. Another problem is that it is difficult to display which grass plot is which on our land.