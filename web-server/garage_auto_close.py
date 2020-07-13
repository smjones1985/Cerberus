# importing the requests library 
import requests 
import time
from datetime import datetime

# api-endpoint 
URL = "http://0.0.0.0:80/check_door_status"
URL_Activate = "http://0.0.0.0:80/24/on"

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
        requests.get(url = URL_Activate)
        #eventually push message to let me know auto resolve occurred and status of attempt
    
    time.sleep(1800)
    
    