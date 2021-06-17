import requests
import os
from datetime import datetime

PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]

user_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": PIXELA_TOKEN,
    "username": "omarkimo",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=user_endpoint, json=user_parameters)
print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{user_parameters['username']}/graphs"
graph_parameters = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
    "timezone": "Africa/Cairo",
}
header = {"X-USER-TOKEN": PIXELA_TOKEN}
response = requests.post(url=graph_endpoint, headers=header, json=graph_parameters)
print(response.text)

pixel_endpoint = f"https://pixe.la/v1/users/{user_parameters['username']}/graphs/{graph_parameters['id']}"
pixel_parameters = {"date": datetime.now().strftime("%Y%m%d"), "quantity": "5"}
response = requests.post(url=pixel_endpoint, headers=header, json=pixel_parameters)
print(response.text)

