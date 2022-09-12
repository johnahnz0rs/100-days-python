import os
from dotenv import load_dotenv
import requests


load_dotenv()
SHEET_AUTH = os.getenv("SHEET_AUTH")
SHEET_ID = os.getenv("SHEET_ID")
HEADERS = {
    "Authorization": SHEET_AUTH
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_current_data(self):
        get_endpoint = f"https://api.sheety.co/{SHEET_ID}/prices"
        sheety_get = requests.get(url=get_endpoint, headers=HEADERS)
        sheety_get.raise_for_status()
        return sheety_get.json()["prices"]

    def set_iata_city_code(self, id, city_iata_code):
        put_endpoint = f"https://api.sheety.co/{SHEET_ID}/prices/{id}"
        put_params = {
            "price": {
                "iataCode": city_iata_code
            }
        }
        sheety_put = requests.put(url=put_endpoint, json=put_params, headers=HEADERS)
        sheety_put.raise_for_status()
        print(sheety_put.text)

    def set_lowest_price(self, id, lowest_price):
        put_endpoint = f"https://api.sheety.co/{SHEET_ID}/prices/{id}"
        put_params = {
            "price": {
                "lowestPrice": lowest_price
            }
        }
        sheety_put = requests.put(url=put_endpoint, json=put_params, headers=HEADERS)
        sheety_put.raise_for_status()
        print(sheety_put.text)

