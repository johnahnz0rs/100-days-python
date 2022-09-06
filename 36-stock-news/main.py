







import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client
from datetime import date, timedelta

load_dotenv()
ALPHA_ADVANTAGE = os.getenv("ALPHA_ADVANTAGE")
NEWSAPI = os.getenv("NEWSAPI")
TWILIO_ID = os.getenv("TWILIO_ID")
TWILIO_KEY = os.getenv("TWILIO_KEY")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
JAHN_PHONE = os.getenv("JAHN_PHONE")
STONK = "TSLA"
COMPANY_NAME = "Tesla Inc"


# STEP 1A - api call & response
stonk_params = {
    "function": "TIME_SERIES_DAILY",
    "apikey": ALPHA_ADVANTAGE,
    "symbol": STONK,
}
stonk_response = requests.get(url="https://www.alphavantage.co/query", params=stonk_params)
stonk_response.raise_for_status()
stonk_data = stonk_response.json()

# STEP 1B - get today's & yesterday's closing prices
def get_the_day_before(before_what_date: date):
    return before_what_date - timedelta(days=1)
# today
today_date = date.today()
today_str = str(today_date)
stonk_today = None
while not stonk_today:
    try:
        stonk_today = float( stonk_data["Time Series (Daily)"][today_str]["4. close"] )
    except KeyError:
        today_date = get_the_day_before(today_date)
        today_str = str(today_date)
# yesterday
yesterday_date = get_the_day_before(today_date)
yesterday_str = str(yesterday_date)
stonk_yesterday = None
while not stonk_yesterday:
    try:
        stonk_yesterday = float( stonk_data["Time Series (Daily)"][yesterday_str]["4. close"] )
    except KeyError:
        yesterday_date = get_the_day_before(yesterday_date)
        yesterday_str = str(yesterday_date)


# STEP 2 - analyze: 5% diff 
if stonk_today and stonk_yesterday:
    difference = round( (stonk_today - stonk_yesterday) / stonk_yesterday, 2)

    # if difference >= 0.05 or difference <= -0.05:
    if difference >= 0.01 or difference <= -0.01: # dev - send alerts if 1% diff
        # get the news
        news_date = str(date.today())
        news_params = {
            "apiKey": NEWSAPI,
            "q": COMPANY_NAME,
            "to": news_date,
            "pageSize": 3,
            "sortBy": "publishedAt"
        }
        news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
        news_response.raise_for_status()
        news_data = news_response.json()
        news_snippets = news_data["articles"]


        # prep the news alerts (sms msg's)
        news_alerts = []
        if difference < 0:
            difference_str = str(difference*100).replace("-", "🔻")
        else:
            difference_str = "🔼" + str(difference*100)

        for i in news_snippets:
            alert_msg = f"{STONK}: {difference_str}%\n\nHeadline: {i['title']}\n\nBrief: {i['description']}"
            news_alerts.append(alert_msg)



        # send the alerts to my phone
        if len(news_alerts) >= 1:
            client = Client(TWILIO_ID, TWILIO_KEY)
            for i in news_alerts:
                message = client.messages.create(body=i, from_=TWILIO_PHONE, to=JAHN_PHONE)
                print(message.status)


