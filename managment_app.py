
#managment app client, data publisher

"""
-takes console input
-send information(name, prefered temperature) of each resident of the house
"""

import time
import mqtt

print("Starting Managment App\n")

ma_client = mqtt.connect_mqtt()           #connect to MQTT server and return a client object
ma_client.loop_start()                    #maintain network traffic flow with the broker, does not block

time.sleep(1)

while True:
  print("Enter 'name,temp' without quotes: ", end='')                                   #prompt user
  person_preference = input()                                          #take console input
  mqtt.publish(ma_client, "/data/preference", str(person_preference))  #publish input data
  print() #print new line for prettyness


