import os
from dotenv import load_dotenv
import time
import json
import requests
from bs4 import BeautifulSoup
from seleniumwire import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
ZILLOW_SEARCH = os.getenv("ZILLOW_SEARCH")
GOOGLE_FORM = os.getenv("GOOGLE_FORM")
CHROME_DRIVER = os.getenv("CHROME_DRIVER")
MY_HEADERS = {
    "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


class ZillowSearcher():
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER)
        self.driver.request_interceptor = self.interceptor

    def interceptor(self, request): 
        request.headers["Accept-Language"] = "en-US,en;q=0.9,ko;q=0.8"
        request.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

    # scrape zillow - selenium
    def scrapeZillow(self):
        self.driver.get(ZILLOW_SEARCH)
        listings = None
        while not listings:
            try:
                listings = self.driver.find_elements(By.CSS_SELECTOR, "#grid-search-results ul li article .property-card-data span")
            except NoSuchElementException:
                time.sleep(1)
        for i in listings:
            print(i.text)
        


# scrape zillow - bs (can't bc it's a js site)
response = requests.get(ZILLOW_SEARCH, headers=MY_HEADERS)
print(response.text)


soup = BeautifulSoup(response.content, "html.parser")
data = json.loads(
    soup.select_one("script[data-zrr-shared-data-key]")
    # .contents[0]
    # .strip("!<>-")
)

print(json.dumps(data, indent=4))
# zillow_html = BeautifulSoup(zillow_response.text, "html.parser")
# print(f"zillow:\n{zillow_response.text}")

# scrape zillow - selenium
# zillow = ZillowSearcher()
# zillow.scrapeZillow()





exit()

# print(zillow_response)
# exit()
# prices_list = zillow_html.select("#grid-search-results ul li article .property-card-data span")
# print(prices_list)

# submit google form


# generate google sheet

