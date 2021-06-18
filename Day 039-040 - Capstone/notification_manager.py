import os
from twilio.rest import Client
import smtplib

CURRENCY_SYMBOL = "£"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        ACCOUNT_SID = os.environ["ACCOUNT_SID"]
        AUTH_TOKEN = os.environ["AUTH_TOKEN"]
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def notify_sms(self, flight):
        self.client.messages.create(
            body=f"\nLow price alert! Only {CURRENCY_SYMBOL}{flight['price']} to fly from {flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}, from {flight['dateFrom']} to {flight['dateTo']}.",
            from_="+17372143842",
            to="+201144521964",
        )

    def notify_email(self, flight, users):
        MY_EMAIL = "omarkimo80@gmail.com"
        MY_PASS = os.environ["MY_PASS"]
        flight_link = f"https://www.google.co.uk/flights?hl=en#flt={flight['flyFrom']}.{flight['flyTo']}.{flight['dateFrom']}*{flight['flyTo']}.{flight['flyFrom']}.{flight['dateTo']}"
        for user in users:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASS)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user["email"],
                    msg=str(
                        f"Subject: Fight Club deal!\n\nDear {user['firstName']} {user['lastName']},\nWe're happy to notify you of a new flight deal!\nOnly {CURRENCY_SYMBOL}{flight['price']} to fly from {flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}, from {flight['dateFrom']} to {flight['dateTo']}.\n{flight_link}",
                        encoding="utf-8",
                    ),
                )