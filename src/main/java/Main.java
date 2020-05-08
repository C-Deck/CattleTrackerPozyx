public class Main {

    public static void main(String[] args) {
        runPozyxMqtt();
    }

    public static void runPozyxMqtt() {
        PozyxMqtt connection = new PozyxMqtt();
        connection.run();
    }
}