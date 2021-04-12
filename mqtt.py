
#mqtt functions to be reused

import random

from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!\n")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic, message):
    result = client.publish(topic, message)
    status = result[0]    # result: [0, 1]
    if status == 0:
        print(f"Sent `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic: {topic}")
        
        
def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        print(f"Message received: `{msg.payload.decode()}`")

    client.subscribe(topic)
    client.on_message = on_message







