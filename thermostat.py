
#thermostat client, data receiver

import mqtt


def on_message(client, userdata, msg):  #message received callback
        print(f"Message received: `{msg.payload.decode()}`")



th_client = mqtt.connect_mqtt()             #connect to MQTT server and return a client object
th_client.subscribe("/python/mqtt")         #subscribe to a topic
th_client.on_message = on_message           #set on_message callback to run when message is received

th_client.loop_forever()    #maintain network traffic flow with the broker, blocks execution



