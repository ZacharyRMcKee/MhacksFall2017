from twilio.rest import Client


account_sid = "REDACTED"
auth_token = "REDACTED"



client = Client(account_sid,auth_token)





message = client.api.account.messages.create(to="+REDACTED",
                                 from_="+13126267493",
                                 media_url=['https://demo.twilio.com/owl.png','https://demo.twilio.com/logo.png'])

