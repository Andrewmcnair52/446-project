
#managment app client, data publisher

"""
-takes console input
-send information(name, prefered temperature) of each resident of the house
"""

import time
import mqtt

ma_client = mqtt.connect_mqtt()           #connect to MQTT server and return a client object
ma_client.loop_start()                    #maintain network traffic flow with the broker, does not block

while True:
  mqtt.publish(ma_client, "/python/mqtt", "this is a message")   #send message, publish(client, topic, message)
  time.sleep(1)                                                  #delay 1s


