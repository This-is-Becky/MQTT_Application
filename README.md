# MQTT_Application
Demonstrate a MQTT server and connection setting, sending message from publisher and receive from subcriber.
Folder "Websocket" suitable for testing/ initall connection or for debug.
Folder"SerialToMqtt" is a complete Class funtion code, which can enable the sensor value push to Mqtt via serial com port.

## Note
This application is using MQTTX platform

- Open `Publisher.py`, and `Subcriber.py`, install the necessary libraries,  Run both code, in different windows.
- Following shows the result for both



 Content | Publisher | Subscriber |
|-----|------|------|
| When connected | Type a value and press Enter (type 'exit' to quit): <br> > ✅ Connected to broker via WebSocket (ws://) | ✅ Connected via WebSocket (ws://) |
| Type Input(e.g.) | hello world~!  | - |
| Terminal appear | 📤 Published: hello world~! | 📥 [sensor/3/pos] QoS=1 Retained=False → hello world~! |

## Download the MQTTX 
- Result will be the same no matter the message is sent from PC python, or directly on Publisher on MQTTX platform, as long as the publish/ subcribe Topic are the same
<img width="1916" height="844" alt="image" src="https://github.com/user-attachments/assets/7be47022-1371-4f87-b1d1-3299c7c83119" />

## Additional reference
https://www.emqx.com/en/blog/the-easiest-guide-to-getting-started-with-mqtt

