import os
from dotenv import load_dotenv
import requests


load_dotenv()

SEARCH_KEY = os.getenv("SEARCH_KEY")
HEADERS = {
    "apikey": SEARCH_KEY
}


class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self):
        pass

    def get_flights(self, fly_from, fly_to, date_from, date_to):
        trip_params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            # "date_from": "13/09/2022",
            # "date_to": "11/03/2023",
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "flight_type": "round",
            "one_for_city": "1",
            "curr": "USD",
            "locale": "en",
            "max_stopovers": "0"
        }

        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=trip_params, headers=HEADERS)
        response.raise_for_status()
        # data = response.json()
        # lowest_price = data["data"][0]["price"] if data["data"] else "No flights available"
        # if data["data"]:
        #     lowest_price = data["data"][0]["price"]
        # else:
        #     lowest_price = "No flights available"
        # return lowest_price
        return response.json()

