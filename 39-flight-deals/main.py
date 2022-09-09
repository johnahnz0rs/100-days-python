#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# 1. DM - grab all the threshold prices from gsheet
# 1a. update the IATA codes
# 2. FS - grab new prices
# 3. FD - will sort & analyze the new data
# 4. NM - has the method(s) that will ping me if there's a better deal.







# ===================

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


my_dm = DataManager()
sheet_data = my_dm.get_current_data()


