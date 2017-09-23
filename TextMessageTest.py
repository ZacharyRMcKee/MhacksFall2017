from twilio.rest import Client

#Your Account SID from twilio.com/console
account_sid = "Enter yours here"
auth_token "Enter yours here"

client = Client(account_sid, auth_token)

message = client.messages.create(
        to="+17088906859",
        from_="enter yours here",
        body="Hello from Python!")

print(message.sid)

