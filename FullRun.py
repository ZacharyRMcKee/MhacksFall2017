import os
import time
import RPi.GPIO as GPIO
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

#Account SID from twilio.com/console for Brett
account_sid = "AC03ce2462c1bd0758ac44b1426c8b2246"
auth_token = "88297a67d59a47fcb0cb3e0a95fdc991"
client = Client(account_sid, auth_token)
alarmArmed = False
#GPIO.setwarnings(False)      #Diables warnings on the sensor
GPIO.setmode(GPIO.BOARD)      #Enables the board on the pi
GPIO.setup(11,GPIO.IN)        #Enables the input from the sensor

#enable the reply webapp to check for messages
app = Flask(__name__)

def activate_alarm():
    message = client.messages.create(
            to="+17088906859",
            from_="+13126267493",
            body="Your PiAlarm has been activated")
    print(message.sid)
    alarmArmed=True
    while alarmArmed:
        SensorInput=GPIO.input(11) # updates the sensor's input each run through the loop
        if(SensorInput == 0):
            print("Nothing Detected")
            time.sleep(0.5)
        elif(SensorInput == 1):
            message = client.messages.create(
                    to="+17088906859",
                    from_="+13126267493",
                    body="An Intruder has been detected from your sensor! Type FALSE POSITIVE to reset the alarm, or 911 to alert local authorities.")
            print(message.sid)
            print("Something Detected, Warning message sent!")
            alarmArmed=False

@app.route("/sms", methods=['GET','POST'])
def handler():
    body = request.values.get('Body',None)
    resp = MessagingResponse()
    if body == 'START':
        activate_alarm()
        resp.message("Alarm Deactivated.")
    elif body == 'STOP':
        alarmArmed = False
        resp.message("Deactivating alarm.")
    elif body == '911':
        resp.message("Alerting local authorities.")
    elif body == "FALSE POSITIVE":
        resp.message("False positive -- Resetting alarm.")
    else:
        resp.message("Please enter START, STOP, 911, or FALSE POSITIVE")
    return str(resp)
app.run(debug=True)

#os.system('aplay alarm.wav')

def call911():
    call = client.api.account.calls\
            .create(to="17088906859",
                    from_="+13126267493",
                    url="https://tinyurl.com/yb2jnmek")

def callUser():
    call = client.api.account.calls\
            .create(to="17088906859",
                    from_="+13126267493",
                    url="https://tinyurl.com/MBroke")
def warnUser():
    message = client.messages.create(
                to="+17088906859",
                from_="+13126267493",
                body="An Intruder has potentially been detected. Please reply with" +
                        " '911' or contact local authorities if the linked picture" +
                        " indicates there is in fact a break-in. If you believe "   + 
                        " there is a false positive, reply 'FALSE POSITIVE' and"    +
                        " your PiAlarm will be reset.")
def soundAlarm():
    # This is a good candidate for a second process. Low-priority
    system("aplay alarm.wav")
