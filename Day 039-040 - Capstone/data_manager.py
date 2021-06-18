import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
        SHEETY_BASIC_AUTH = os.environ["SHEETY_BASIC_AUTH1"]
        project_name = "flightDeals"
        self.cities_endpoint = (
            f"https://api.sheety.co/{SHEETY_USERNAME}/{project_name}/prices"
        )
        self.users_endpoint = (
            f"https://api.sheety.co/{SHEETY_USERNAME}/{project_name}/users"
        )
        self.sheety_header = {"Authorization": SHEETY_BASIC_AUTH}

    def get_data(self):
        response = requests.get(url=self.cities_endpoint, headers=self.sheety_header)
        # print(response.json())
        return response.json()["prices"]

    def update_data(self, cities):
        for city in cities:
            response = requests.put(
                url=f"{self.cities_endpoint}/{city['id']}",
                headers=self.sheety_header,
                json={"price": city},
            )
            response.raise_for_status()

    def get_user_data(self):
        response = requests.get(url=self.users_endpoint, headers=self.sheety_header)
        # print(response.json())
        return response.json()["users"]

    def post_user_data(self, dic):
        response = requests.post(
            url=self.users_endpoint, headers=self.sheety_header, json={"user": dic}
        )
        response.raise_for_status()
