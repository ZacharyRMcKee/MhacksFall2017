from twilio.rest import Client



account_sid = "REDACTED"
auth_token = "REDACTED"

client = Client(account_sid,auth_token)

for message in client.api.account.messages.list():
    #if(message.body == "911"):
    #    print("Calling the cops!")
    print(message.body)
