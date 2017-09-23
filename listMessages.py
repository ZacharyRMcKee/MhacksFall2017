from twilio.rest import Client



account_sid = "AC03ce2462c1bd0758ac44b1426c8b2246"
auth_token = "88297a67d59a47fcb0cb3e0a95fdc991"

client = Client(account_sid,auth_token)

for message in client.api.account.messages.list():
    #if(message.body == "911"):
    #    print("Calling the cops!")
    print(message.body)
