#Start by importing all necessary libraries and packages 
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import datetime
import time
import json
import pytz
import os

IST = pytz.timezone('Asia/Kolkata')

BROKER_URL = os.environ.get('BROKER_URL')
USER_ID = os.environ.get('USER_ID')

client = paho.Client()
client.connect(BROKER_URL, 1883)
client.loop_start()

#Set the GPIO to BCM Mode
GPIO.setmode(GPIO.BCM)

#Set Pin 4 to be our Sniffer Pin, We want this to be an Input so we set it as such
GPIO.setup(10,GPIO.IN)

#This variable will be used to determine if pressure is being applied or not
prev_input = 0

#Create a Loop that goes on as long as the script is running
while True:

    #take a reading from the pressure pad (based on the voltage able to get to pin 4)
    input = GPIO.input(10)

    #if the last reading was low and this one high the pressure pad is being pressed!
    if ((not prev_input) and input):

    #Print that fact to the shell, RIP David Bowie
        print("Under Pressure")

        data = {
            "sensor": "pressure",
            "user_id": USER_ID,
            "message": "Under Pressure",
            "timestamp": str(datetime.datetime.now(IST))
          }

        print(data)
        (rc, mid) = client.publish(f'/{USER_ID}/alert', json.dumps(data), qos=1)
        time.sleep(1)
    prev_input = input

    # For publishing status messages
    # if int(datetime.datetime.now().strftime("%S")) % 5 == 0:
    #     data = {
    #         "sensor": "pressure",
    #         "user_id": USER_ID,
    #         "data": {
    #             "status": "running"
    #         },
    #         "timestamp": str(datetime.datetime.now(IST))
    #     }
    #     print(data)
    #     (rc, mid) = client.publish(f'/{USER_ID}/data_stream/pressure', json.dumps(data), qos=1)

#	time.sleep(0.10)
    #update previous input so we can avoid spamming the Shell with messages, 
    #this section of the script is also a perfect place to add threshold values to active other devices 
    

    #Have a slight pause here, also to avoid spamming the shell with data
    
