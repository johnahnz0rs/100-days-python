







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


## ================
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

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








# ======================
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# STEP 1C - analyze: 5% diff
if stonk_today and stonk_yesterday:
    difference = round( (stonk_today - stonk_yesterday) / stonk_yesterday, 2)
    if difference >= 0.05 or difference <= -0.05:
        print(f"yooooo {difference*100}% difference since yesterday yesterday's prices, dogg")
    else:
        print(f"no big changes since yesterday, homie. {difference*100}%")

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
news_alerts = []

if difference < 0:
    difference_str = str(difference*100).replace("-", "🔻")
else:
    difference_str = "🔼" + str(difference*100)

for i in news_snippets:
    # print(type(i))
    # print(f"{i}\n\n")
    alert_msg = f"{STONK}: {difference_str}\nHeadline: {i['title']}\nBrief: {i['description']}"
    news_alerts.append(alert_msg)


# print(news_alerts)

if len(news_alerts) >= 1:
    client = Client(TWILIO_ID, TWILIO_KEY)
    for i in news_alerts:
        # print(f"newsalert newsalert {i}")
        message = client.messages.create(body=i, from_=TWILIO_PHONE, to=JAHN_PHONE)
        print(message.status)

# if will_be_sunny:
#     client = Client(TWILIO_ID, TWILIO_KEY)
#     message = client.messages.create(body="Wear shades today 🕶", from_=TWILIO_PHONE,to=JAHN_PHONE)
#     print(message.status)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this: 
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

# - or -

# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.



