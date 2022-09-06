import os
from dotenv import load_dotenv
import requests

load_dotenv()
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")


headers = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "date": "20220904",
    "quantity": "180",
}
endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

new_graph = requests.post(url=endpoint, json=graph_params, headers=headers)
print(new_graph.text)




