import requests
import time
import pytz
from pytz import timezone
from datetime import datetime
import os


# api-endpoint
URL = "http://0.0.0.0:80/check_door_status"
URL_Activate = "http://0.0.0.0:80/24/on"
URL_Push = "https://api.pushover.net/1/messages.json"
TOKEN= os.environ['PUSH_TOKEN']
USER= os.environ['PUSH_USER']

doorIsOpened = False
central = pytz.timezone('US/Central')

while True:
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    # extracting data in json format
    data = r.json()
    currentState = data['garageDoorStatus']
    currentTime = datetime.now(central)

    if currentState == "Open" and (currentTime.hour >= 21 or currentTime.hour <= 7):
        sendNotification("Garage Door was left open! Attempting Close in 1 minute")
        time.sleep(60)
        activateResponse = requests.get(url = URL_Activate)
        sendNotification(str(activateResponse))
        #eventually push message to let me know auto resolve occurred and status of attempt
    time.sleep(1800)

def sendNotification(message):
  requests.post(url = URL_Push, data = {
          "token": TOKEN,
          "user": USER,
          "message": message,
          "device": "sean-s9"
        })
