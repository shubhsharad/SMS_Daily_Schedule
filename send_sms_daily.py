from datetime import datetime
import os
from twilio.rest import Client


client = Client("ACd2113dde29f8eb50abb6af2d13938ca5", "2d65eb4adae4761437ab805c5ea1adb0")
# message = client.messages \
#     .create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='+15618234485',
#          media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
#          to='+15179801560'
#      )

# print(message.sid)
monday_schedule = "PHY191: 11:30-2:20 in Biomedical and CSE 260: 3:00-4:30"
tuesday_schedule = "IBIO 150 : 11:30-12:20 in Akers Hall and CSE 232: 3:00- 4:50"
wednesday_schedule = "CSE 260: 3:00-4:30"
thursday_schedule = "MTH 234 : 9:10-10:00 online and IBIO 150 : 11:30-12:20 in Akers Hall and CSE 232: 3:00- 4:50"
friday_schedule = "IBIO 150 : 11:30-12:20 in Biomedical and CSE 232: 3:00- 4:50"
saturday_schedule = "Homework"
sunday_schedule = "Homework"
# get current datetime
dt = datetime.now()
print('Datetime is:', dt)

# get day of week as an integer
day = dt.weekday()
print('Day of a week is:', day)

if day == 0:
    message = client.messages \
    .create(
         body="Todays schedule is: "+monday_schedule,
         from_='+15618234485',
         to='+15179801560'
     )
elif day == 1:
    message = client.messages \
    .create(
         body="Todays schedule is: "+tuesday_schedule,
         from_='+15618234485',
         to='+15179801560'
     )
elif day == 2:
    message = client.messages \
    .create(
         body="Todays schedule is: "+wednesday_schedule,
         from_='+15618234485',
         to='+15179801560'
     )
elif day == 3:
    message = client.messages \
    .create(
         body="Todays schedule is: "+thursday_schedule,
         from_='+15618234485',
         to='+15179801560'
     )
elif day == 4:
    message = client.messages \
    .create(
         body="Todays schedule is: "+friday_schedule,
         from_='+15618234485',
         to='+15179801560'
     )
elif day == 5:
    message = client.messages \
    .create(
         body="Todays schedule is: "+saturday_schedule,
         from_='+15618234485',
         to='+15179801560'
     )
elif day == 6:
    message = client.messages \
    .create(
         body="Todays schedule is: "+sunday_schedule,
         from_='+15618234485',
         to='+15179801560'
     )




