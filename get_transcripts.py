import os
from datetime import datetime
from twilio.rest import Client


# Setup the Twilio client.
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
to_number = os.environ['TO_NUMBER']
client = Client(account_sid, auth_token)


# Get the calls to our phone number.
calls = client.calls.list(
    to=to_number
)

# Iterate over the calls to retrieve the transcripts.
for c in calls:
    for r in c.recordings.list():
        recording = client.recordings(r.sid).fetch()
        for t in recording.transcriptions.list():
            print(c.sid, t.transcription_text)
