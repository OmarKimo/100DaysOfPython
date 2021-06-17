import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = os.environ["OWM_API_KEY"]
MY_LAT = 59.21  # raining latitude      30.047020  # Nahia latitude
MY_LONG = 123.45  # raining longitude   31.130740  # Nahia longitude
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts",
    "units": "metric",
    # "lang": "ar",
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters
)
response.raise_for_status()
# print(response.url)
# print(response.json())

next_12_hours = response.json()["hourly"][:12]
will_rain = False
for hour in next_12_hours:
    if hour["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    # if running on PythonAnywhere
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. You need to bring an umbrella ☂.",
        from_="+17372143842",
        to="+201144521964",
    )
    # print("rain")
