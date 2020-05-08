import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;
import dataClasses.TagPosition;

import java.io.IOException;
import java.util.Random;

import com.google.gson.Gson;

public class PozyxMqtt implements MqttCallback {

    public static void main(String[] args) {
        new PozyxMqtt().run();
    }

    void run() {
        String topic = "tags";
        String address = "tcp://localhost:1883";
        Random random = new Random();
        String clientId = String.format("JavaMQTTExample %d", random.nextInt(1000));
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
            System.out.println("Could not connect to local MQTT");
            System.out.println("Reason code " + mqttException.getReasonCode());
            mqttException.printStackTrace();
        }
    }

    @Override
    public void connectionLost(Throwable throwable) {
        System.out.println("Connection to the devices has been lost");
    }

    @Override
    public void messageArrived(String topic, MqttMessage message)
            throws Exception, IOException {
        Gson gson = new Gson();
        TagPosition[] tagPositions = gson.fromJson(message.toString(), TagPosition[].class);

        for (TagPosition tagPosition : tagPositions) {
            if (tagPosition.success) {
                System.out.println(String.format("%s;%d;%d;%d", tagPosition.tagId, tagPosition.data.coordinates.x, tagPosition.data.coordinates.y, tagPosition.data.coordinates.z));
            } else {
                System.out.println(String.format("Error from devices: %s", tagPosition.errorCode));
            }
        }
    }

    @Override
    public void deliveryComplete(IMqttDeliveryToken iMqttDeliveryToken) {

    }
}
