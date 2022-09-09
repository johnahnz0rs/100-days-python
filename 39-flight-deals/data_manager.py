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
        self.sheety_get = requests.get(url=get_endpoint, headers=HEADERS)
        self.sheety_get.raise_for_status()
        # self.sheety_json = self.sheety_get.json()
        return self.sheety_get.json()["prices"]

    
    # log_headers = {
    # "Authorization": SHEET_AUTH
    # }
    # log_params = {
    #     "workout": {
    #         "date": date,
    #         "time": time,
    #         "exercise": log_exercise,
    #         "duration": duration,
    #         "calories": calories,
    #     }
    # }
    # log_endpoint = f"https://api.sheety.co/{SHEET_ID}/{SHEET_TITLE}/workouts"
    # log_response = requests.post(url=log_endpoint, headers=log_headers, json=log_params)
    # log_response.raise_for_status()