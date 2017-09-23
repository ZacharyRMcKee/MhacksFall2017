import RPi.GPIO as GPIO
import time
from twilio.rest import Client

#Account SID from twilio.com/console for Brett
account_sid = "AC03ce2462c1bd0758ac44b1426c8b2246"
auth_token = "88297a67d59a47fcb0cb3e0a95fdc991"

client = Client(account_sid, auth_token)
#GPIO.setwarnings(False)      #Diables warnings on the sensor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

MessageNotSent = True
while MessageNotSent:
    SensorInput=GPIO.input(11) # updates the sensor's input each run through the loop
    if(SensorInput == 0):
        print("Nothing Detected")
        time.sleep(0.5)
    elif(SensorInput == 1):
        MessageNotSent = False
        message = client.messages.create(
                to="+17088906859",
                from_="+13126267493",
                body="An Intruder has been detected from your sensor!")
        print(message.sid)
        print("Something Detected, Warning message sent!")
