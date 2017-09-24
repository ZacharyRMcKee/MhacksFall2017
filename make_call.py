from twilio.rest import Client


account_sid = "REDACTED"
auth_token = "REDACTED"

client = Client(account_sid,auth_token)

call = client.api.account.calls\
        .create(to="REDACTED",
        from_="+13126267493",
        url="https://tinyurl.com/MBroke")




print(call.sid)
