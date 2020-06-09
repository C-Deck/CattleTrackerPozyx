# CattleTracker-Pozyx Python

A basic way to connect to the Pozyx system and receive the data. It has it's own interface that we can track the tags in, but if we want to do more on the data it wouldn't work. With this, we can extract that data to do more with it.

## Setup

### Prerequisites

To run this project, you will need:

* Python 3
* Pozyx software
* Paho MQTT (We will install this)

### Installation

Download the code from this repository. Then, you must open the command line. Once you are in the command line you must run the following command in order to get Paho MQTT.

`pip install paho-mqtt`

Paho MQTT for Python is now installed.

## Running the Project

Once you have Pozyx running and connected to your device, navigate to the python file. Simply click on main.py and windows will launch the program in the background. When you are finished, simply close the running window or `ctrl+c` which also ends the program.

## Implementation

When connecting through MQTT there are a set of callbacks that you can set. Each callback is a function that is called when a certain event happens. In the bottom of the code, we set the callbacks to our values.

```
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
```

Fur our purposes, the main callback that we use is the `on_message` callback. This function gets called every time the Pozyx devices send data through the MQTT connection. Our function takes the data that is sent and writes it to our json file.

```
def on_message(client, userdata, msg):
    print("Positioning update:", msg.payload.decode())
    jsonFile.write(msg.payload.decode())
```

In the beginning of the file, we open the file to write to. Then, as the call is called, we continually add to the file until we stop the program.