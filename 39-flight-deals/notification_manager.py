import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()
TWILIO_ID = os.getenv("TWILIO_ID")
TWILIO_KEY = os.getenv("TWILIO_KEY")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
JAHN_PHONE = os.getenv("JAHN_PHONE")

client = Client(TWILIO_ID, TWILIO_KEY)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_alert(self, message):
        send_this_msg = client.messages.create(body=message, from_=TWILIO_PHONE, to=JAHN_PHONE)
        print(send_this_msg.status)


