
#smart door locker client, data publisher

"""
-takes console input
-publish when a new user enters the house
-publish data should be user name
"""

import time
import mqtt

print("Starting Smart Door Locker\n")

dl_client = mqtt.connect_mqtt()           #connect to MQTT server and return a client object
dl_client.loop_start()                    #maintain connection without blocking

time.sleep(1)

while True:
  print("enter <name>,<e or l> for entering or leaving: ", end='')  #prompt user
  person_name = input()                                     #take console input
  mqtt.publish(dl_client, "/data/enter", str(person_name))  #publish input data
  print() #print new line for prettyness
