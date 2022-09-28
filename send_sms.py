import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#TWILIO_ACCOUNT_SID = "ACd2113dde29f8eb50abb6af2d13938ca5"
#TWILIO_AUTH_TOKEN = "2d65eb4adae4761437ab805c5ea1adb0"
#account_sid = os.environ[TWILIO_ACCOUNT_SID]
#auth_token = os.environ[TWILIO_AUTH_TOKEN]
client = Client("ACd2113dde29f8eb50abb6af2d13938ca5", "2d65eb4adae4761437ab805c5ea1adb0")

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+15618234485',
         media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
         to='+15179801560'
     )

print(message.sid)
while True:
    x = input("enter as many as you want")