import requests
from datetime import datetime
import smtplib
from time import sleep
import os

MY_LAT = 30.047020  # Nahia latitude
MY_LONG = 31.130740  # Nahia longitude
MY_EMAIL = "omarkimo80@gmail.com"
MY_PASS = os.environ["MY_PASS"][1:-1]
#print(MY_PASS)

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    return time_now.hour >= sunset or time_now.hour < sunrise

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if is_iss_overhead():
        if is_dark():
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject: ISS is overhead!\n\n It's dark now and the ISS is overhead.\nGo look up for it. ^_^",
                )
        else:
            print("It's not dark now.")
    else:
        print("ISS is far from your position.")
    sleep(5)
