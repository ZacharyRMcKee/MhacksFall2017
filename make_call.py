from twilio.rest import Client


account_sid = "AC03ce2462c1bd0758ac44b1426c8b2246"
auth_token = "88297a67d59a47fcb0cb3e0a95fdc991"

client = Client(account_sid,auth_token)

call = client.api.account.calls\
        .create(to="+17088906859",
        from_="+13126267493",
        url="https://tinyurl.com/MBroke")




print(call.sid)
