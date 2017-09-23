from twilio.rest import Client

#Your Account SID from twilio.com/console
account_sid = "AC03ce2462c1bd0758ac44b1426c8b2246"
auth_token = "88297a67d59a47fcb0cb3e0a95fdc991"

client = Client(account_sid, auth_token)

message = client.messages.create(
        to="+17088906859",
        from_="+13126267493",
        body="Hello from Python!")

print(message.sid)
