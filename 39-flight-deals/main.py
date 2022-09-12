# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# x1. DM - grab all the threshold prices from gsheet
# x1a. update the IATA codes
# x2. FS - grab new prices
# x3. FD - will sort & analyze the new data
# x4. NM - has the method(s) that will ping me if there's a better deal.
# ===================

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

my_dm = DataManager()
my_fs = FlightSearch()
my_fd = FlightData()
my_nm = NotificationManager()

sheet_data = my_dm.get_current_data()
date_from = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
date_to = (datetime.today() + timedelta(days=181)).strftime("%d/%m/%Y")


for row in sheet_data:

    # check for city codes
    if row["iataCode"] == "":
        city_iata_code = my_fs.get_airport_code(row["city"])
        my_dm.set_iata_city_code(id=row["id"], city_iata_code=city_iata_code)
    # else:
    #     print(row["iataCode"])


    # get cheapest flight
    flight_data = my_fd.get_flights(fly_from="city:LAX", fly_to=f"city:{row['iataCode']}", date_from=date_from, date_to=date_to)

   
    # if new cheapest flight costs less than previous price
    if(flight_data["data"]):
        price = flight_data["data"][0]["price"]

        if int(price) < int(row["lowestPrice"]):
            departure_city_name = flight_data["data"][0]["route"][0]["cityFrom"]
            departure_airport_iata_code = flight_data["data"][0]["route"][0]["cityCodeFrom"]
            arrival_city_name = flight_data["data"][0]["route"][0]["cityTo"]
            arrival_airport_iata_code = flight_data["data"][0]["route"][0]["cityCodeTo"]
            outbound_date = flight_data["data"][0]["route"][0]["local_departure"][:10]
            inbound_date = flight_data["data"][0]["route"][1]["local_departure"][:10]

            my_dm.set_lowest_price(id=row["id"], lowest_price=price)
            message = f"Low price alert! Only ${price} to fly {departure_city_name}-{departure_airport_iata_code} to {arrival_city_name}-{arrival_airport_iata_code}, from {outbound_date} to {inbound_date}."
            my_nm.send_alert(message=message)

