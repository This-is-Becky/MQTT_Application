# MQTT_Application
Demonstrate a MQTT server and connection setting, sending message from publisher and receive from subcriber.

## Note
This application is using MQTTX platform

- Open `Publisher.py`, and `Subcriber.py`, install the necessary libraries,  Run both code, in different windows.
- Following shows the result for both



 Content | Publisher | Subscriber |
|-----|------|------|
| When connected | Type a value and press Enter (type 'exit' to quit): <br> > ✅ Connected to broker via WebSocket (ws://) | ✅ Connected via WebSocket (ws://) |
| Type Input(e.g.) | hello world~!  | - |
| Terminal appear | 📤 Published: hello world~! | 📥 [sensor/3/pos] QoS=1 Retained=False → hello world~! |

## Additional reference
https://www.emqx.com/en/blog/the-easiest-guide-to-getting-started-with-mqtt

