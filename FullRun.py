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

@app.route("/sms", methods=['GET','POST'])

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
                    body="An Intruder has been detected from your sensor!")
            print(message.sid)
            print("Something Detected, Warning message sent!")
            MessageSent=False
            resp = MessagingResponse()
            resp.message("Please contact Authorities for further action on your part")
            return str(resp) 

#@app.route("/sms", methods=['GET','POST'])

#def sms_reply():
#    resp = MessagingResponse()
#    resp.message("Your PiAlarm has been activated")
#    return str(resp)


@app.route("/sms", methods=['GET','POST'])
def handler():
    body = request.values.get('Body',None)

    if body == 'START':
        activate_alarm()
    elif body == 'STOP':
        alarmArmed = False
    elif body == '911':
        resp = MessagingResponse()
        resp.message("Alerting local authorities.")
        return str(resp)
    elif body == "FALSE POSITIVE"
        resp = MessagingResponse()
        resp.message("False positive -- Resetting alarm.")
        return str(resp)
app.run(debug=True)

#os.system('aplay alarm.wav')



