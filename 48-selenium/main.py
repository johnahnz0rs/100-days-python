
from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/johnahnz0rs/00 - JAHN PROJECTS/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

# page to scrape
driver.get("https://www.python.org")
# get a list of dates
event_dates_raw = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li time")
event_dates_list = [date.text for date in event_dates_raw]
#get a list of event names
event_names_raw = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu a")
event_names_list = [event.text for event in event_names_raw]


final_dict = {}
for i, val in enumerate(event_dates_list):
    final_dict[i] = {
        "time": val,
        "name": event_names_list[i]
    }






print(final_dict)


# driver.quit()