
#thermostat client, data receiver

"""
-automatically adjust the room’s temperature based on the learned user’s routine and preferences
-must obtain information regarding the people living in the house, their preferable temperature, and the house occupancy in a given moment
-if the house is empty, it should set the temperature to 15° C
-If there is only one person in the house, it should set the temperature to the one that person prefers
-if more than one person is in the house, the thermostat should set the average
-The output of this entity will be the temperature displayed on the screen
"""


import mqtt


def on_message(client, userdata, msg):  #message received callback
        print(f"Message received: `{msg.payload.decode()}`")



th_client = mqtt.connect_mqtt()             #connect to MQTT server and return a client object
th_client.subscribe("/python/mqtt")         #subscribe to a topic
th_client.on_message = on_message           #set on_message callback to run when message is received

th_client.loop_forever()    #maintain network traffic flow with the broker, blocks execution



