
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

#define globals
temperature = 15
person_list = []       #lists all persons
temperature_list = []  #lists all temperatures
inside_list = []       #lists persons inside

print("Starting Thermostat\n")


def on_message(client, userdata, msg):  #message received callback
  
  print("Message received from topic: "+msg.topic)
  
  if msg.topic=="/data/preference": #handle set temperature prefrence
  
    input = msg.payload.decode()
    if ',' in input:                  #check that we have a delimeter
      name, temp = input.split(',')   #split by delimeter
      if not len(name):
        print("invalid preference, no name specified")
      elif not len(temp):
        print("invalid preference, no temperature specified")
      else:
        #input is valid, update temperature preferences
        if name in person_list: #if name is already in person_list, update temperature
          temperature_list[ person_list.index(name) ] = float(temp)
        else: #else append new person and temperature
          person_list.append(name)
          temperature_list.append(float(temp))
        #output
        print("preferences updated\npreferences: ", end='')
        for x in person_list:
          print(x+":"+str(temperature_list[person_list.index(x)])+", ", end='')
        print()
          
    else: #else if delimeter not present in message
       print("no delimeter found, correct format is: name,temperature")
  
  elif msg.topic=="/data/enter":  #handle person entered/left
    
    print("Person has entered: " + msg.payload.decode())
    
    input = msg.payload.decode()
    if ',' in input:                  #check that we have a delimeter
    
      name, state = input.split(',')   #split by delimeter
      if not len(name):
        print("invalid input, no name specified")
      elif state=='e':  #handle entering
        if not name in inside_list:
          inside_list.append(name)
          calculate_temperature()
        #output
        print("people inside: ", end='')
        print(inside_list)
        print("temperature set to: "+str(temperature))
      elif state=='l':  #handle leaving
        if name in inside_list:
          inside_list.remove(name)
          calculate_temperature()
        #output
        print("people inside: ", end='')
        print(inside_list)
        print("temperature set to: "+str(temperature))
      else: #handle invalid input
        print("invalid input, format must be: name,e or name,l")
      
    else: #else if delimeter not present in message
       print("no delimeter found, correct format is: name,e or name,l")

  print()   #print line space between output blocks
  
def calculate_temperature():

  sum = 0
  count = 0
  global temperature
  for x in inside_list:
    if x in person_list:
      sum += temperature_list[ person_list.index(x) ]
      count += 1
  
  if count>0:
    temperature = sum/count
  else:
    temperature = 15

th_client = mqtt.connect_mqtt()             #connect to MQTT server and return a client object
th_client.subscribe("/data/#")              #subscribe to a topic
th_client.on_message = on_message           #set on_message callback to run when message is received

th_client.loop_forever()    #maintain network traffic flow with the broker, blocks execution



