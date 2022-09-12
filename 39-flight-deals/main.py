#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# x1. DM - grab all the threshold prices from gsheet
# 1a. update the IATA codes
# 2. FS - grab new prices
# 3. FD - will sort & analyze the new data
# 4. NM - has the method(s) that will ping me if there's a better deal.



# https://api.sheety.co/c62e59a29010cd6d206cec57d5f4f043/copyOfFlightDeals100DaysOfPythonDrYu/prices



# ===================

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime, timedelta

my_dm = DataManager()
my_fs = FlightSearch()
my_fd = FlightData()
my_nm = NotificationManager()

sheet_data = my_dm.get_current_data()
date_from = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
date_to = (datetime.today() + timedelta(days=181)).strftime("%d/%m/%Y")

# check for city codes
for row in sheet_data:
    if row["iataCode"] == "":
        city_iata_code = my_fs.get_airport_code(row["city"])
        my_dm.set_iata_city_code(id=row["id"], city_iata_code=city_iata_code)
    # else:
    #     print(row["iataCode"])




# lol = my_fs.get_flights(fly_from="city:LAX", fly_to="city:NYC", date_from=date_from, date_to=date_to)

# print(lol["data"][0]["price"])


for row in sheet_data:
    # price = my_fd.get_flights(fly_from="city:LAX", fly_to=f"city:{row['iataCode']}", date_from=date_from, date_to=date_to)
    flight_data = my_fd.get_flights(fly_from="city:LAX", fly_to=f"city:{row['iataCode']}", date_from=date_from, date_to=date_to)

    # if flight_data["data"]:
    #     print(flight_data)
    # print(f"{row['iataCode']}\n{flight_data}")
    


    # price
    # departure city name
    # departure airport iata code
    # arrival city name
    # arrival airport iata code
    # outbound date
    # inbound date

    if(flight_data["data"]):
        price = flight_data["data"]["price"]
        departure_city_name = flight_data["data"]["route"][0]["cityFrom"]
        departure_airport_iata_code = flight_data["data"]["route"][0]["cityCodeFrom"]
        arrival_city_name = flight_data["data"]["route"][0]["cityTo"]
        arrival_airport_iata_code = flight_data["data"]["route"][0]["cityCodeTo"]
        outbound_date = flight_data["data"]["route"][0]["local_departure"][:10]
        inbound_date = flight_data["data"]["route"][1]["local_departure"][:10]

        my_dm.set_lowest_price(id=row["id"], lowest_price=price)
        message = f"w00t lower price to {row['city']} ${price}\n\n{departure_city_name} ({departure_airport_iata_code}) to/from {arrival_city_name} ({arrival_airport_iata_code})\nLeave on {outbound_date}, Return on {inbound_date}"
        # my_nm.send_alert(message=message)
        print(message)

    # print(f"{row['city']}: ${price}")

    # if int(price) < int(row["lowestPrice"]):
    #     my_dm.set_lowest_price(id=row["id"], lowest_price=price)
    #     price_diff = int(row["lowestPrice"]) - int(price)
    #     message = f"w00t lower price to {row['city']}: ${price}"
    #     my_nm.send_alert(message=message)

