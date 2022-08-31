from email.mime.text import MIMEText
import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 34.057710 # Your latitude
MY_LONG = -118.299800 # Your longitude

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()

# iss_latitude = float(data["iss_position"]["latitude"])
# iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True
    else:
        return False


def is_it_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)

    if is_it_dark() and is_iss_close():
        sender = "John Ahn <johnahn123@gmail.com>"
        receiver = f"John Ahn <johnahn123@gmail.com>"
        send_msg = MIMEText("Hey the ISS is overhead; go outside and take a look.")
        send_msg["Subject"] = "ISS is overhead now"
        send_msg["From"] = sender
        send_msg["To"] = receiver

        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.starttls()
            server.login("12f821306a538f", "8a2caa23910244")
            server.sendmail(sender, receiver, send_msg.as_string())
    else:
        print("it's not close, homie")

