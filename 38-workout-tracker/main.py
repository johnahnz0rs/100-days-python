
import os


import os
from dotenv import load_dotenv
from datetime import datetime
import requests


load_dotenv()
NUTRITIONIX_ID = os.getenv("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.getenv("NUTRITIONIX_KEY")
SHEET_ID = os.getenv("SHEET_ID")
SHEET_TITLE = os.getenv("SHEET_TITLE")
SHEET_AUTH = os.getenv("SHEET_AUTH")

right_meow = datetime.now()
date = right_meow.strftime("%m/%d/%Y")
time = right_meow.strftime("%I:%M %p")
exercise = input("what exercise did you do? ")


exercise_headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 138,
    "height_cm": 190,
    "age": 35 
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_response = requests.post(url=exercise_endpoint, headers=exercise_headers, json=exercise_params)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()["exercises"][0]


log_exercise = exercise_data["name"].title()
duration = round(exercise_data["duration_min"])
calories = round(exercise_data["nf_calories"])

log_headers = {
    "Authorization": SHEET_AUTH
}
log_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": log_exercise,
        "duration": duration,
        "calories": calories,
    }
}
log_endpoint = f"https://api.sheety.co/{SHEET_ID}/{SHEET_TITLE}/workouts"
log_response = requests.post(url=log_endpoint, headers=log_headers, json=log_params)
log_response.raise_for_status()
# print(log_response.text)





