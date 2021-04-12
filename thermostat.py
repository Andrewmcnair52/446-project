
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

print("Starting Thermostat\n")


def on_message(client, userdata, msg):  #message received callback
  
  print("Message received from topic: "+msg.topic)
  
  if msg.topic=="/data/preference": #handle temperature prefrence
  
    input = msg.payload.decode()
    if ',' in input:                  #check that we have a delimeter
      name, temp = input.split(',')   #split by delimeter
      if not len(name):
        print("invalid preference, no name specified")
      elif not len(temp):
        print("invalid preference, no temperature specified")
      else:
        print("name: "+name)
        print("temperature: "+temp)
    else:
       print("no delimeter found, correct format is: name,temperature")
  
  elif msg.topic=="/data/enter":  #handle person entered

    print("Person has entered: " + msg.payload.decode())

  print()   #print line space between outpu blocks

th_client = mqtt.connect_mqtt()             #connect to MQTT server and return a client object
th_client.subscribe("/data/#")              #subscribe to a topic
th_client.on_message = on_message           #set on_message callback to run when message is received

th_client.loop_forever()    #maintain network traffic flow with the broker, blocks execution



