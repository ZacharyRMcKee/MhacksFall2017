from flask import Flask
from twilio.twiml.voice_response import VoiceReponse

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = VoiceReponse()
    resp.say("Hello Monkey")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


