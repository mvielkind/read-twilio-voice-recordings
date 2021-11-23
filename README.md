# Reading Transcripts from Twilio Call Recordings

This repo contains the code example for this [YouTube video](https://www.youtube.com/watch?v=L1CfSTAPf6M) demonstrating how you can create a voice mailbox using Twilio Studio.

The `get_transcripts.py` file is a short Python script that shows how you can read transcripts of call recordings made to your Twilio number.

To use the script first make sure you fill out the contents of the `twilio.env` file with your Twilio account secrets and store them as environment variables. You can find your `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in your Twilio console. Your phone number should be entered in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (i.e. +1234567890) More details about securely storing your Twilio secrets are [here](https://www.twilio.com/docs/usage/secure-credentials).

You will also need to make sure you install the `twilio` library in the `requirements.txt` file.

Hope you enjoy!