from twilio.rest import Client

#Your Account SID from twilio.com/console
account_sid = "REDACTED"
auth_token = "REDACTED"

client = Client(account_sid, auth_token)

message = client.messages.create(
        to="+REDACTED",
        from_="+13126267493",
        body="Hello from Python!")

print(message.sid)
