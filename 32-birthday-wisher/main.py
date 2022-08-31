##################### Extra Hard Starting Project ######################

# x1. Update the birthdays.csv

# x2. Check if today matches a birthday in the birthdays.csv
    # a. get today's date
    # b. open & read the csv
    # c. check for matches in month and day

# x3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# x4. Send the letter generated in step 3 to that person's email address.

import smtplib
from email.mime.text import MIMEText
import datetime as dt
from random import choice
import pandas as pd

def select_random_letter():
    i = choice([1,2,3])
    return f"letter_templates/letter_{i}.txt"

today = dt.datetime.now()
today_month = today.month
today_day = today.day
# print(f"today: {today_month}/{today_day}")

df = pd.read_csv("birthdays.csv")
for _, row in df.iterrows():
    if row["month"] == today_month and row["day"] == today_day:
        # print(f"yes, it's this person's birthday today\n{row}")
        bday_name = row["name"]
        bday_email = row["email"]

        letter = select_random_letter()
        with open(letter) as file:
            content = file.read()
            msg = content.replace("[NAME]", bday_name)
            # print(msg)

        sender = "John Ahn <johnahn123@gmail.com>"
        receiver = f"{bday_name} <{bday_email}>"
        send_msg = MIMEText(msg)
        send_msg["Subject"] = "Happy Birthday!!!"
        send_msg["From"] = sender
        send_msg["To"] = receiver

        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.starttls()
            server.login("12f821306a538f", "8a2caa23910244")
            server.sendmail(sender, receiver, send_msg.as_string())




