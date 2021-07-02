import requests
import os
from datetime import datetime

Nutritionix_APP_ID = os.environ["Nutritionix_APP_ID"]
Nutritionix_API_KEY = os.environ["Nutritionix_API_KEY"]
project_name = "workoutTrackingProjectMyWorkouts"
sheet_name = "workouts"
sheety_endpoint = (
    f"https://api.sheety.co/{os.environ['SHEETY_USERNAME']}/{project_name}/{sheet_name}"
)
SHEETY_BASIC_AUTH = os.environ["SHEETY_BASIC_AUTH"]
TEST_CASE = "Ran 2 miles and walked for 3Km."

ex_text = TEST_CASE  # input("Tell me which exercises you did: ")

x_parameters = {"query": ex_text}

x_header = {
    "x-app-id": Nutritionix_APP_ID,
    "x-app-key": Nutritionix_API_KEY,
    "x-remote-user-id": "0",
}

response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    headers=x_header,
    json=x_parameters,
)
# print(response.text)
# print(response.json())

exercises = response.json()["exercises"]
# print(exercises)

now = datetime.now()
for exercise in exercises:
    sheety_parameters = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(
        url=sheety_endpoint,
        json=sheety_parameters,
        headers={"Authorization": SHEETY_BASIC_AUTH},
    )
    # print(response)
