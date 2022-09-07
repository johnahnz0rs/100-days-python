
# https://pixe.la/v1/users/johnahnz0rs/graphs/python-dr-yu.html

import os
from dotenv import load_dotenv
from datetime import datetime
import requests

load_dotenv()
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

headers = {
    "X-USER-TOKEN": TOKEN
}
today_date = datetime.now()
today = today_date.strftime("%Y%m%d")
graph_params = {
    "date": today,
    "quantity": input("how many minutes did you study python today?"),
}

new_entry_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
new_entry = requests.post(url=new_entry_endpoint, json=graph_params, headers=headers)
print(new_entry.text)

# update_entry_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# update_entry = requests.put(url=update_entry_endpoint, json=graph_params, headers=headers)
# print(update_entry.text)

# delete_entry_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# delete_entry = requests.delete(url=delete_entry_endpoint, headers=headers)
# print(delete_entry.text)



