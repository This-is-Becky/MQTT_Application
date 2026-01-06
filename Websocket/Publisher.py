
from paho.mqtt import client as mqtt
import time
import random

# -------------------------
# Broker settings (EMQX public WebSocket)
# -------------------------
BROKER = "broker.emqx.io"
PORT = 8083               # WebSocket (ws://), non-TLS, For wss>> 8084+tls.set
TOPIC = "sensor/3/pos"

CLIENT_ID = f"publisher-ws-{random.randint(1000,9999)}"
KEEPALIVE = 60


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to broker via WebSocket (ws://)")
    else:
        print("❌ Connection failed, rc =", rc, "-", mqtt.error_string(rc))

def on_disconnect(client, userdata, rc):
    print("🔌 Disconnected, rc =", rc)

# -------------------------
# Create WebSocket client
# -------------------------
client = mqtt.Client(client_id=CLIENT_ID, transport="websockets")


client.on_connect = on_connect
client.on_disconnect = on_disconnect

# No TLS for ws:// (non-secure WebSocket)
# client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
# client.tls_set()
# EMQX WebSocket path for MQTT
# client.ws_set_options(path="/mqtt")

# Connect and start network loop
client.connect(BROKER, PORT, keepalive=KEEPALIVE)
client.loop_start()

print("Type a value and press Enter (type 'exit' to quit):")

try:
    while True:
        value = input("> ")

        if value.lower() == "exit":
            break

        # Publish message
        info = client.publish(
            topic=TOPIC,
            payload=value,
            qos=1,
            retain=False   # set True only if you want a retained 'last known' value
        )
        # Optional: wait for publish result
        info.wait_for_publish()
        print(f"📤 Published: {value}")

except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()
    print("Disconnected")
