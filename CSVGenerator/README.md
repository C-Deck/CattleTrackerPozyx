# CSV Geneator

This is a program that files the JSON file created previously and creates a CSV file for each cow. The CSV file format is `tag, time, x, y`. For our purposes, this is all we need. The tag number is necessary later for the visualization. 

The JSON files is just a giant amount of JSON values that we need to parse and decide what to do with. For our purposes, we decide to only take a point for each tag every time. In the JSON, there will sometimes be multiple points every second. We don't need that many points or that often.

## Looking at the code

The JSON values are in the following format:

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

As you can see, there are a lot of values given in each data value. We only need the tag, time, x, and y. We will be ignoring everything besides the `success` value. If it is not a successful value, there is no point in recording it.

We have two core functions in t
*createCSV
*checkAddValue

`createCSV` is done after we have finished gathering all the data for a tag. It takes in a Tag object created by the tag class described below and writes the values to the csv file.

`checkAddValue` is the function where we add the value to the list of values for the tag. It checks the `timestamp` value and makes sure that the value is 5 seconds or more later. Hopefully, in the future we can configure the Pozyx system to only send the points every 5 seconds. That way, we don't have to worry about this. Next, it gets the coordinates and converts the x and y to meters from millimeters. It is much easier to work with meters and just use decimal points. Otherwise, our x and y's go into the 10000s. Finally, this value is added to the list of values for the tag.

### Classes

In this program, we use two classes.
*Tag
*TagValue

The `TagValue` class is a simple class that is a "wrapper" for our value. It contains the tag number, x, y, and the time. There are some helpful functions to print it or compare values that it has. The most important function is the `getArr` function. It returns a value in the format ["tagnumber", "time, "x", "
y"]. This is the format that is needed to write for a row to the CSV file.

The `Tag` class is to handle the data on each tag. It keeps a list of all the `TagValue`s in it. This way we have each set of values separated specifically to each tag. It also keeps track of the last time value entered so we can check and make sure that the next one to enter is not too soon.

Its main function is the `getValueArr` function. This function builds up a list of all the points in the correct format returned in the `getArr` function described above. This is called in the `createCSV` to get all the data for each tag that we will use.