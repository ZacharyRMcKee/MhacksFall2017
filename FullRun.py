import os
import time
import RPi.GPIO as GPIO
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from multiprocessing import Process


#Account SID from twilio.com/console for Brett
account_sid = "AC03ce2462c1bd0758ac44b1426c8b2246"
auth_token = "88297a67d59a47fcb0cb3e0a95fdc991"
client = Client(account_sid, auth_token)
alarmArmed = False
#GPIO.setwarnings(False)      #Diables warnings on the sensor. Uncomment if warnings are a problem.
GPIO.setmode(GPIO.BOARD)      #Enables the board on the pi
GPIO.setup(11,GPIO.IN)        #Enables the input from the sensor

#enable the reply webapp to check for messages
app = Flask(__name__)


def soundAlarm():
    os.system("aplay alarm.wav")

def call911(): #Sends a message to authorities with the user's address
    call = client.api.account.calls\
            .create(to="17088906859",
                    from_="+13126267493",
                    url="https://tinyurl.com/yb2jnmek")

def callUser(): #Call the user warning them of an intruder
    call = client.api.account.calls\
            .create(to="17088906859",
                    from_="+13126267493",
                    url="https://tinyurl.com/MBroke")

def sendImage(): #Send a (placeholder) image of the intruder
    message = client.messages.create(
            to="+17088906859",
            from_="+13126267493",
            body="https://i.imgur.com/xVwml6Kr.jpg")

def activate_alarm(): #Runs through a loop checking for an intruder until interrupted
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
            print(message.sid)
            p = Process(target=soundAlarm)
            p.start()
            callUser()
            sendImage()
            print("Something Detected, Warning message sent!")
            alarmArmed=False

@app.route("/sms", methods=['GET','POST'])
def handler():
    body = request.values.get('Body',None)
    resp = MessagingResponse()
    if body == 'START':
        activate_alarm()
        resp.message("An Intruder has potentially been detected. Reply with" +
                    " '911' or contact the police if the linked picture" +
                    " indicates there's a break-in. If you believe "   + 
                    " it's a false positive, reply 'FALSE POSITIVE' to" +
                    " reset the alarm.")
    elif body == 'SHUTDOWN':
        alarmArmed = False
        resp.message("Deactivating alarm.")
    elif body == '911':
        resp.message("Alerting local authorities.")
        call911()
    elif body == "FALSE POSITIVE":
        activate_alarm()
        resp.message("False positive -- Resetting alarm.")
    else:
        resp.message("Please enter START, SHUTDOWN, 911, or FALSE POSITIVE")
    return str(resp)
app.run(debug=True)
