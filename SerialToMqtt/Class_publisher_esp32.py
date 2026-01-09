
import random
import ssl
import time
import serial
from paho.mqtt import client as mqtt


class SerialMQTTPublisher:
    def __init__(self, broker, port, topic, serial_port, baudrate):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.serial_port = serial_port
        self.baudrate = baudrate

        # Serial
        self.ser = serial.Serial(serial_port, baudrate, timeout=1)
        self.ser.reset_input_buffer()

        # MQTT
        client_id = f"publisher-wss-{random.randint(1000,9999)}"
        self.client = mqtt.Client(client_id=client_id, transport="websockets")
        self.client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
        self.client.ws_set_options(path="/mqtt")

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

        self.client.connect(broker, port, keepalive=60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("✅ Connected" if rc == 0 else f"❌ Connect failed rc={rc}")

    def on_disconnect(self, client, userdata, rc):
        print("🔌 Disconnected")

    def run(self):
        try:
            while True:
                line = self.ser.readline().decode("utf-8", errors="replace").strip()
                if not line:
                    continue

                self.client.publish(self.topic, line, qos=1)
                print(f"📤 {line}")
        except KeyboardInterrupt:
            pass
        finally:
            self.client.loop_stop()
            self.client.disconnect()
            self.ser.close()

#config
broker="broker.emqx.io"
port=8084
topic="dis/1/value"
serial_port="COM9"
baudrate=115200


if __name__ == "__main__":
    SerialMQTTPublisher(broker, port, topic, serial_port, baudrate).run()
