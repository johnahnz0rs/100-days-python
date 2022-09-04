import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()
LAT = os.getenv("LAT")
LONG = os.getenv("LONG")
API_KEY = os.getenv("API_KEY")

TWILIO_ID = os.getenv("TWILIO_ID")
TWILIO_KEY = os.getenv("TWILIO_KEY")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
JAHN_PHONE = os.getenv("JAHN_PHONE")

# 1. get lat/long from latlong.net
# 2. call the onecall api_version
# 3. print the response's http status code
# 4. print(response)
# 5. use a json reader
# 6. find the HOURLY FORECAST FOR NEXT 48
# 7. if it's bright out, wear shades

my_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY
}
response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast?", params=my_params) # this api endpoint gets the forecast for every 3 hours for 5 days == 40 forecasts
response.raise_for_status()
data = response.json()
1
forecast_12_hr = data["list"][:4]
txt_msg = ""

will_be_sunny = False
for f in forecast_12_hr:
    if f["weather"][0]["id"] >= 800:
        will_be_sunny = True

if will_be_sunny:
    client = Client(TWILIO_ID, TWILIO_KEY)
    message = client.messages.create(body="Wear shades today 🕶", from_=TWILIO_PHONE,to=JAHN_PHONE)
    print(message.status)



