from email.mime.text import MIMEText
import smtplib
import datetime as dt
from random import choice

# my_email = "johnahnz0rsisl33t@outlook.com"
# my_password = "l33th4x0rsOMGwtf!!"
# to_address = "johnahn123@gmail.com"
# my_msg = "Subject:Hello\n\nhelloworld"
# smtp_server = "smtp://smtp.mailtrap.io:2525"

# print("before connection")
# try:
#     connection = smtplib.SMTP(smtp_server, port=588)
#     connection.starttls()
# except Exception as e:
#     print(e)

# print("connection started")

# try:
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=my_msg)
# except Exception as e:
#     print(e)    

# print('am i executed?')
# connection.close()
# with smtplib.SMTP("smtp.office365.com", port=588) as connection:
    # connection.starttls()
    # try:

    #     connection.login(user=my_email, password=my_password)
    #     connection.sendmail(from_addr=my_email, to_addrs="johnahn123@gmail.com", msg="Subject:Hello\n\nhelloworld")
    # except Exception:
    #     print(Exception)

# sender = "johnahnz0rs test <from@example.com>"
# receiver = "John Ahn <johnahn123@gmail.com>"


# ======================================
# dev notes
# i tried the way dr yu suggested, but i hit blockers with every email provider i tried (gmail, yahoo, outlook)
# so i ended up using this other test service (mailtrap.io) ... it works
# ======================================




now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:

    with open("quotes.txt") as data:
        quotes = data.readlines()
        random_quote = choice(quotes).strip()

    sender = "johnahnz0rs <johnahnz0rsisl33t@outlook.com>"
    receiver = "johnahn123 <johnahn123@gmail.com>"
    message = f"""\
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}

    {random_quote}"""

    my_msg = MIMEText(message)
    my_msg["Subject"] = "Motivational Quote"
    my_msg["From"] = "johnahnz0rs <johnahnz0rsisl33t@outlook.com>"
    my_msg["To"] = "johnahn123 <johnahn123@gmail.com>"
    

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        
        server.starttls()
        server.login("12f821306a538f", "8a2caa23910244")
        server.sendmail(sender, receiver, my_msg.as_string())
        



# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}

# This is a test e-mail message."""


# with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#     server.login("6fe99dc39a6cf4", "00746670526db2")
#     server.sendmail(sender, receiver, message)

# my_dob = dt.datetime(year=1987, month=2, day=8)
# now = dt.datetime.now()
# year = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)


