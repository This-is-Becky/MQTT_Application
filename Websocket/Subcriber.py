
from paho.mqtt import client as mqtt
import random

BROKER = "broker.emqx.io"
PORT = 8083                 # WebSocket (ws://)
TOPIC = "sensor/+/pos"
CLIENT_ID = f"subscriber-ws-{random.randint(1000,9999)}"
KEEPALIVE = 60

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected via WebSocket (ws://)")
        # Subscribe once connected
        client.subscribe(TOPIC, qos=1)
        print(f"🔔 Subscribed to {TOPIC}")
    else:
        print("❌ Connect failed:", rc, "-", mqtt.error_string(rc))

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8", errors="replace")
    print(f"📥 [{msg.topic}] QoS={msg.qos} Retained={msg.retain} → {payload}")

def on_disconnect(client, userdata, rc):
    print("🔌 Disconnected, rc =", rc)

client = mqtt.Client(client_id=CLIENT_ID, transport="websockets")
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# No username/password and no TLS for ws://
client.connect(BROKER, PORT, keepalive=KEEPALIVE)

# Blocking loop to process network events
client.loop_forever()
