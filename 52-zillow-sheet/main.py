import os
from dotenv import load_dotenv
import time
# import json
import requests
# from bs4 import BeautifulSoup
from seleniumwire import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
CHROME_DRIVER = os.getenv("CHROME_DRIVER")
ZILLOW_SEARCH = os.getenv("ZILLOW_SEARCH")
GOOGLE_FORM = "https://forms.gle/fgrsxnJa6bvUwnSJ6"
# MY_HEADERS = {
#     "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# }


class ZillowSearcher():
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER)
        self.driver.request_interceptor = self.interceptor
        self.prices = []
        self.links = []
        self.addresses = []

    def interceptor(self, request): 
        request.headers["Accept-Language"] = "en-US,en;q=0.9,ko;q=0.8"
        request.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

    # scrape zillow - selenium
    # scrape zillow - selenium
    # scrape zillow - selenium
    def scrapeZillow(self):
        print("starting scrapeZillow()")
        self.driver.get(ZILLOW_SEARCH)


        temp_prices = None
        while not temp_prices:
            print("starting temp_prices")
            try: 
                temp_prices = self.driver.find_elements(By.CSS_SELECTOR, "#grid-search-results ul li article div div span[data-test='property-card-price']")
            except NoSuchElementException:
                print("DNE - waiting 10s")
                time.sleep(10)
        for i in temp_prices:
            if "+" in i.text:
                price = i.text.split()[0].split("+")[0]
            else:
                price = i.text.split()[0]
            self.prices.append(price)
        print(f"self.prices: \n{self.prices}")


        temp_links = None
        while not temp_links:
            print("starting temp_links")
            try: 
                temp_links = self.driver.find_elements(By.CSS_SELECTOR, "#grid-search-results ul li article div div:first-child a[data-test='property-card-link']")
            except NoSuchElementException:
                print("DNE - waiting 10s")
                time.sleep(10)
        for i in temp_links:
            self.links.append(i.get_attribute("href"))
        print(f"self.links: \n{self.links}")


        temp_addresses = None        
        while not temp_addresses:
            print("starting temp_addresses")
            try: 
                temp_addresses = self.driver.find_elements(By.CSS_SELECTOR, "#grid-search-results ul li article div a address[data-test='property-card-addr']")
            except NoSuchElementException:
                print("DNE - waiting 10s")
                time.sleep(10)
        for i in temp_addresses:
            if "|" in i.text:
                self.addresses.append(i.text.split(" | ", 1)[1])
            else:
                self.addresses.append(i.text)


        
    def submitGoogleForm(self, address, price, link):
        self.driver.get(GOOGLE_FORM)
        input_address = None
        while not input_address:
            try:
                input_address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            except NoSuchElementException:
                print("waiting for form input - 2s")
                time.sleep(2)
        input_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        input_link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        print("pause before click")
        time.sleep(2)
        input_address.send_keys(address)
        input_price.send_keys(price)
        input_link.send_keys(link)
        submit_button.click()





zillow = ZillowSearcher()
zillow.scrapeZillow()
listings_length = len(zillow.addresses)
# print(listings_length, len(zillow.prices), len(zillow.links))
for i in listings_length:
    print(i)
# zillow.submitGoogleForm()

# exit()




# .property-card-data
# .property-card-price





# scrape zillow - bs (can't, bc it's a js site)
# response = requests.get(ZILLOW_SEARCH, headers=MY_HEADERS)
# print(response.text)


# soup = BeautifulSoup(response.content, "html.parser")
# data = json.loads(
#     soup.select_one("script[data-zrr-shared-data-key]")
#     # .contents[0]
#     # .strip("!<>-")
# )

# print(json.dumps(data, indent=4))
# zillow_html = BeautifulSoup(zillow_response.text, "html.parser")
# print(f"zillow:\n{zillow_response.text}")

# scrape zillow - selenium
# zillow = ZillowSearcher()
# zillow.scrapeZillow()





# exit()

# print(zillow_response)
# exit()
# prices_list = zillow_html.select("#grid-search-results ul li article .property-card-data span")
# print(prices_list)

# submit google form


# generate google sheet

