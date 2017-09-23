from twilio.rest import Client

account_sid = "XX"
auth_token = "AA"
client = Client(accout_sid,auth_token)

for message in client.messages.list():
    if(message.body == "911"):
        print("Calling the cops!")
