import requests
import os
import datetime as dt


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
        self.header = {"apikey": TEQUILA_API_KEY}
        self.location_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        today = dt.datetime.now() + dt.timedelta(1)
        after_today = today + dt.timedelta(3 * 60)  # 6 months
        self.DATE_FROM = today.strftime("%d/%m/%Y")
        self.DATE_TO = after_today.strftime("%d/%m/%Y")
        self.CURRENCY = "GBP"
        self.FLIGHT_TYPE = "round"
        self.MIN_DAYS = 7
        self.MAX_DAYS = 28

    def get_flight(self, cityFrom: str, cityTo: str, maxPrice: int):
        response = requests.get(
            url=self.search_endpoint,
            headers=self.header,
            params={
                "fly_from": cityFrom,
                "fly_to": cityTo,
                # "price_to": maxPrice,
                "date_from": self.DATE_FROM,
                "date_to": self.DATE_TO,
                "flight_type": self.FLIGHT_TYPE,
                "curr": self.CURRENCY,
                "nights_in_dst_from": self.MIN_DAYS,
                "nights_in_dst_to": self.MAX_DAYS,
                "max_stopovers": 0,
            },
        )
        response.raise_for_status()
        return response.json()["data"]

    def get_iataCode(self, city: str) -> str:
        response = requests.get(
            url=self.location_endpoint, headers=self.header, params={"term": city}
        )
        response.raise_for_status()
        return response.json()["locations"][0]["code"]
