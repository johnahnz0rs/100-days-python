import os
from dotenv import load_dotenv
import requests

load_dotenv()
TEQUILA_KEY = os.getenv("TEQUILA_KEY")
HEADERS = {
    "apikey": TEQUILA_KEY
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_airport_code(self, city_name):
        
        iata_params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": "1",
            "active_only": "true",
        }
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=iata_params, headers=HEADERS)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]
        return iata_code


