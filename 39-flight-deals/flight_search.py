import os
from dotenv import load_dotenv
import requests

load_dotenv()
TEQUILA_KEY = os.getenv("TEQUILA_KEY")
SEARCH_KEY = os.getenv("SEARCH_KEY")
HEADERS = {
    "apikey": TEQUILA_KEY
}
HEADERS_SEARCH = {
    "apikey": SEARCH_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_airport_code(self, city_name):
        
        iata_params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "limit": "1",
            "active_only": "true",
        }
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=iata_params, headers=HEADERS)
        response.raise_for_status()
        # iata_code = response.json()
        # iata_code = response.json()["locations"][0]["id"]
        iata_code = response.json()["locations"][0]["city"]["code"]

        # return city_name
        return iata_code


    def get_flights(self, fly_from, fly_to, date_from, date_to):
        trip_params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": "10/09/2022",
            "date_to": "11/03/2023",
            # "date_from": date_from,
            # "date_to": date_to,
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "flight_type": "round",
            "one_for_city": "1",
            "curr": "USD",
            "locale": "en",
            "max_stopovers": "0"
        }

        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=trip_params, headers=HEADERS_SEARCH)
        response.raise_for_status()
        return response.json()

