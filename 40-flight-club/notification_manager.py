import os
from dotenv import load_dotenv
import smtplib
from twilio.rest import Client

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_ID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_KEY")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_PHONE")
TWILIO_VERIFIED_NUMBER = os.getenv("JAHN_PHONE")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.mailtrap.io"
MAILTRAP_ID = os.getenv("MAILTRAP_ID")
MAILTRAP_KEY = os.getenv("MAILTRAP_KEY")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )


# # sender = "johnahnz0rs <johnahnz0rsisl33t@outlook.com>"
# # receiver = "johnahn123 <johnahn123@gmail.com>"
# # message = f"""\
# # Subject: Hi Mailtrap
# # To: {receiver}
# # From: {sender}

# # {random_quote}"""

# # my_msg = MIMEText(message)
# # my_msg["Subject"] = "Motivational Quote"
# # my_msg["From"] = "johnahnz0rs <johnahnz0rsisl33t@outlook.com>"
# # my_msg["To"] = "johnahn123 <johnahn123@gmail.com>"


# with smtplib.SMTP(, 2525) as server:
    
#     server.starttls()
#     server.login(MAILTRAP_ID, "")
#     server.sendmail(sender, receiver, my_msg.as_string())
    







