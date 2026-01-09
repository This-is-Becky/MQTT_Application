
import random
import ssl
import time
import serial
from paho.mqtt import client as mqtt


class SerialMQTTSubscriber:
    def __init__(self, broker, port, topic):
        self.broker = broker
        self.port = port
        self.topic = topic


        # MQTT
        client_id = f"publisher-wss-{random.randint(1000,9999)}"
        self.client = mqtt.Client(client_id=client_id, transport="websockets")
        self.client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
        self.client.ws_set_options(path="/mqtt")

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message  # NEW: ensure messages are handled

        # self.client.connect(broker, port, keepalive=60)
        # self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("✅ Connected" if rc == 0 else f"❌ Connect failed rc={rc}")
        client.subscribe(self.topic, qos=1)
        print(f"📡 Subscribed to topic: {self.topic} (QoS 1)")

    def on_disconnect(self, client, userdata, rc):
        print("🔌 Disconnected")

    def on_message(self, client, userdata, msg):
        try:
            payload = msg.payload.decode("utf-8", errors="replace")
            print(f"📥 [{msg.topic}] QoS={msg.qos} Retained={msg.retain} → {payload}")
        
        except Exception as e:
            print(f"error:{e}")

    def run(self):
        try:
            # CHANGED: connect and start loop here
            self.client.connect(self.broker, self.port, keepalive=60)
            self.client.loop_start()
            print("🚀 MQTT loop started. Press Ctrl+C to exit.")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n Stopping...")
        finally:
            # CHANGED: clean shutdown
            self.client.loop_stop()
            self.client.disconnect()
            # REMOVED: self.ser.close() (no serial port is opened in this version)
            print("✅ Clean exit.")


#config
broker="broker.emqx.io"
port=8084
topic="dis/+/value"



if __name__ == "__main__":
    SerialMQTTSubscriber(broker, port, topic).run()
