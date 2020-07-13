'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

'''

import RPi.GPIO as GPIO
from pytz import timezone
import pytz
import time
import json

from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   24 : {'name' : 'GPIO 24', 'state' : GPIO.LOW} #9th facing outside
   }
error = ""
garageDoorStatus = "Unknown"
doorStatusDictionary = {
   0: "Open",
   1: "Closed"
}
central = pytz.timezone('US/Central')
garageDoorStatusTimeStamp = datetime.now(central).strftime("%d/%m/%Y %H:%M:%S")
# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

DOOR_SENSOR_PIN = 18 #6th facing outside, 7th is ground
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP) 


@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   sensorPin = GPIO.input(DOOR_SENSOR_PIN)
   garageDoorStatus = doorStatusDictionary[sensorPin]
   garageDoorStatusTimeStamp = datetime.now(central).strftime("%d/%m/%Y %H:%M:%S")
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins,
      'garageDoorStatus' : garageDoorStatus,
      'garageDoorStatusTimeStamp' : garageDoorStatusTimeStamp,
      'message' : ''
   }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   originalDoorState = doorStatusDictionary[GPIO.input(DOOR_SENSOR_PIN)]
   # If the action part of the URL is "on," execute the code indented below:
      # Set the pin high:
   GPIO.output(changePin, GPIO.HIGH)
   time.sleep(3)
   GPIO.output(changePin, GPIO.LOW)
   time.sleep(5)
   newStateOfDoor = doorStatusDictionary[GPIO.input(DOOR_SENSOR_PIN)]
   currentTime = datetime.now(central).strftime("%d/%m/%Y %H:%M:%S")

   garageDoorStatus = doorStatusDictionary[newStateOfDoor]

   garageDoorStatusTimeStamp = currentTime

   if originalDoorState == newStateOfDoor:
      message = "Garage door call failed! " + currentTime
   message = "Success! " + currentTime 

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins,
      'garageDoorStatus' : garageDoorStatus,
      'garageDoorStatusTimeStamp' : garageDoorStatusTimeStamp,
      'message' : message
   }

   return render_template('main.html', **templateData)

@app.route("/check_door_status")
def statusCheck():
   originalDoorState = doorStatusDictionary[GPIO.input(DOOR_SENSOR_PIN)]
   currentTime = datetime.now(central).strftime("%d/%m/%Y %H:%M:%S")

   templateData = {
      'garageDoorStatus' : originalDoorState,
      'garageDoorStatusTimeStamp' : currentTime
   }
   return json.dumps(templateData)
   
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
