import os
from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
T_ID = os.getenv("T_ID")
T_PW = os.getenv("T_PW")
CHROME_DRIVER = "/Users/johnahnz0rs/00 - JAHN PROJECTS/chromedriver"
TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"
SPEED_TEST_URL = "https://www.speedtest.net/"
GUARANTEED_DOWN = 40
GUARANTEED_UP = 10



class InternetSpeedTwitterBot():
    
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        # print("get_internet_speed()")
        self.driver.get(SPEED_TEST_URL)
        # start the speed test
        start_speed_test_button = None
        while not start_speed_test_button:
            try:
                start_speed_test_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
            except NoSuchElementException:
                time.sleep(1)
            finally:
                start_speed_test_button.click()
        # wait for test to finish then get results
        results_div = None
        while not results_div:
            try:
                results_div = self.driver.find_element(By.CSS_SELECTOR, "div.result-container-speed.result-container-speed-active")
            except NoSuchElementException:
                time.sleep(5)
            finally:
                self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
                self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
                return_dict = {
                    "down_speed": self.down.text,
                    "up_speed": self.up.text
                }
        self.driver.quit()
        return return_dict




t_bot = InternetSpeedTwitterBot()
my_internet_speeds = t_bot.get_internet_speed()
print(f"speeds:\n{my_internet_speeds}")


