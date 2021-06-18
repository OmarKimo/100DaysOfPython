# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint


dataManager = DataManager()
flightSearch = FlightSearch()
flightData = FlightData()
notifier = NotificationManager()

sheet_data = dataManager.get_data()
users_data = dataManager.get_user_data()
# pprint(sheet_data)

flag = False
for row in sheet_data:
    if not row["iataCode"]:
        row["iataCode"] = flightSearch.get_iataCode(row["city"])
        flag = True

if flag:
    print("Bruh")
    dataManager.update_data(sheet_data)
    sheet_data = dataManager.get_data()

HOME_CITY = flightSearch.get_iataCode("London")

# pprint(dataManager.get_user_data())

# print("Welcome to My Fight Club.\nWe find the best flight deals and email you.")
# new_user = {}
# new_user["firstName"] = input("what is your first name?\n")
# new_user["lastName"] = input("what is your last name?\n")
# new_user["email"] = input("what is your email?\n")

# dataManager.post_user_data(new_user)

# print("You're in the club!")


for row in sheet_data:
    flights = flightSearch.get_flight(
        cityFrom=HOME_CITY, cityTo=row["iataCode"], maxPrice=row["lowestPrice"]
    )
    if flights:
        flightData.add(flights[0], row["lowestPrice"])

# pprint(flightData.flight_data)

for flight in flightData.flight_data:
    if flight["maxPrice"] > flight["price"]:
        # notifier.notify_sms(flight)
        notifier.notify_email(flight, users_data)
