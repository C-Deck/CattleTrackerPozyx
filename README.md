# CattleTracker-Pozyx

A basic way to connect to the Pozyx system and receive the data. It has it's own interface that we can track the tags in, but if we want to do more on the data it wouldn't work. With this, we can extract that data to do more with it.

## Setup

### Prerequisites

To run this project, you will need:

* Java and Maven. The project was developed targeting Java bytecode 1.8 using 4.0.0.

## Running the project

You can find the main function in `src/main/java/Main.java`. The main has been separated, so that connectivity is apart from any other functionality we might want.

```java
public class Main {

    public static void main(String[] args) {
        runPozyxMqtt();
    }

    public static void runPozyxMqtt() {
        PozyxMqtt connection = new PozyxMqtt();
        connection.run();
    }
}
```

As soon as we press play, data should be run as long as we run and are connected to the pozyx system locally. In order to get it wirelessly, we will need to set up cloud connectivity. The code only require a few adjustments though.

## Inside the code

The important code is run in `src/main/java/PozyxMqtt.java`.
It connects to the MQTT stream of data that is sent by Pozyx and prints the positioning. It also captures the data for each packet received. We can use this for further functionality later.

### Connecting to the MQTT client

For the MQTT, I use the [Eclipse Paho Java Client](https://www.eclipse.org/paho/clients/java/). It is needed because the Pozyx devices work on the MQTT and TCP protocol.


```java
public class PozyxMqtt implements MqttCallback {
    // ...
}
```

Due to the fact we are using the Palo library, I had to implement the MqttCallback interface. It is pretty easy to implement though. If you check the code, you will see three functions of connectionLost, messageArrived and deliveryComplete.

In the running portion of the code. The main things we must do are call the `client.connect`, `client.setCallback`, and `subscribe`. These are the code functions that do the work that we want.

```java
    void run() {
        String topic = "tags";
        String address = "tcp://localhost:1883";
        Random random = new Random();
        String clientId = String.format("%d", random.nextInt(1000));
        MemoryPersistence memoryPersistance = new MemoryPersistence();

        try {
            MqttClient client = new MqttClient(address, clientId, memoryPersistance);

            MqttConnectOptions connectOptions = new MqttConnectOptions();
            connectOptions.setCleanSession(true);

            client.connect(connectOptions);
            System.out.println("Connected");

            client.setCallback(this);
            client.subscribe(topic);
        } catch (MqttException mqttException) {
            // ...
        }
    }
```


### Parsing the MQTT messages

The main work is done on the `messageArrived` callback. When we called run and did the `client.setCallback(this)`, it sets it up so that every time a message arrives to the running program, it calls `messageArrived` with that data.

The tag data comes in as an array of individual packets. I use Google's [Gson library](https://github.com/google/gson) to parse JSON.
There are classes related to the JSON in `src/main/java/structures`. I talk more about those later on.

```java
    @Override
    public void messageArrived(String topic, MqttMessage message)
            throws Exception, IOException {
//        System.out.println(message);

        Gson gson = new Gson();
        TagPosition[] tagPositions = gson.fromJson(message.toString(), TagPosition[].class);

        for (TagPosition tagPosition : tagPositions) {
            if (tagPosition.success) {
                System.out.println(String.format("%s;%d;%d;%d", tagPosition.tagId, tagPosition.data.coordinates.x, tagPosition.data.coordinates.y, tagPosition.data.coordinates.z));
            }
        }
    }
```

### Structures package

For the structures package, it is simply the different types of data with the values separated into classes. If you look at the [Pozyx API Documentation](http://api-docs.pozyx.io/1.X/01-mqtt.html#pozyx-mqtt-api-v2-0), it gives you all the types of data and the variables they hold. I broke those down into separate classes that can be used later on if we want to add functionality. It also allows us to logically keep track of how the data is broken down. 

## Going forward

From here, I was planning on using data visualization libraries in order to visual the data that we are receiving. From the looks of it, the other group is doing theirs in Python, so I don't know if we will use this. Because I know how to do it now, it won't be difficult for me to get it to work on Python to use with them.
