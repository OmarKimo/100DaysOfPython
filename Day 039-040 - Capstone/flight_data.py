class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.flight_data = []
        self.filter_keys = ["price", "cityFrom", "flyFrom", "cityTo", "flyTo"]

    def add(self, flight, maxPrice):
        to_append = {key: flight[key] for key in self.filter_keys}
        to_append["maxPrice"] = maxPrice
        to_append["dateFrom"] = flight["route"][0]["local_departure"].split("T")[0]
        to_append["dateTo"] = flight["route"][1]["local_arrival"].split("T")[0]
        self.flight_data.append(to_append)
