import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

load_dotenv()
AMAZON_URL = "https://www.amazon.com/MRE-Ready-Genuine-Military-Surplus/dp/B005I5ML0O"
AMAZON_HEADERS = {
    "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
# TARGET_PRICE = 150
TARGET_PRICE = 1500
MAIL_PROVIDER_SMTP_ADDRESS = os.getenv("MAIL_PROVIDER_SMTP_ADDRESS")
PORT = os.getenv("PORT")
MAILTRAP_ID = os.getenv("MAILTRAP_ID")
MAILTRAP_KEY = os.getenv("MAILTRAP_KEY")
SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")



# grab html from amazon item
response = requests.get(AMAZON_URL, headers=AMAZON_HEADERS)
response.raise_for_status()
page_html = BeautifulSoup(response.text, "html.parser")
# scrape for price
price = page_html.select_one("#apex_desktop .a-offscreen")
price_float = float(price.getText().strip("$"))
price_string = "{:.2f}".format(price_float)


if price_float <= TARGET_PRICE:
    print(f"price is lower; is now ${price_string}")

    message = MIMEText(f"MRE (Meals Ready-to-Eat Box A, Genuine U.S. Military Surplus, Menus 1-12 by Rothco is now ${price_string}\n{AMAZON_URL}")
    message["Subject"] = "Amazon Price Alert!"
    message["From"] = SENDER
    message["To"] = RECEIVER
    print("starting send")
    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, PORT) as server:
        server.starttls()
        server.login(MAILTRAP_ID, MAILTRAP_KEY)
        server.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=message.as_string())

    print("finished sending")


