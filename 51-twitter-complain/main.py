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
GUARANTEED_DOWN = 40.0
GUARANTEED_UP = 10.0

# driver = webdriver.Chrome(CHROME_DRIVER)
# driver.get(TWITTER_LOGIN_URL)
# exit()


class InternetSpeedTwitterBot():
    
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER)
        self.down = None
        self.up = None

    def tweeter_a_complaint(self, down, up):
        print("tweeter_a_complaint()") # dev
        self.driver.get(TWITTER_LOGIN_URL)
        # enter login username
        login_username = None
        while not login_username:
            try:
                login_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            except NoSuchElementException:
                print("sleep - no login_username") # dev
                time.sleep(1)
        login_username.send_keys(T_ID)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        # enter pw
        login_pw = None
        while not login_pw:
            try:
                login_pw = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            except NoSuchElementException:
                print("sleep - no login_pw") # dev
                time.sleep(1)
        login_pw.send_keys(T_PW)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()
        # write a tweet
        tweet_textarea = None
        while not tweet_textarea:
            try:
                tweet_textarea = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            except NoSuchElementException:
                print("sleep - no tweet_texarea")
                time.sleep(1)
        tweeter_msg = f"ew my internet speed is so slow. i'm only getting {down} down and {up} up. lagging like a mahfuqa"
        tweet_textarea.send_keys(tweeter_msg)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()




    def get_internet_speed(self):
        print("get_internet_speed()") # dev
        self.driver.get(SPEED_TEST_URL)
        # start the speed test
        start_speed_test_button = None
        while not start_speed_test_button:
            try:
                start_speed_test_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
            except NoSuchElementException:
                print("sleep - start_speed_test_button") # dev
                time.sleep(1)
        start_speed_test_button.click()
        # wait for test to finish then get results
        results_div = None
        while not results_div:
            try:
                results_div = self.driver.find_element(By.CSS_SELECTOR, "div.result-container-speed.result-container-speed-active")
            except NoSuchElementException:
                print("sleep - no results_div") # dev
                time.sleep(5)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        return_dict = {
            "down_speed": float(self.down.text),
            "up_speed": float(self.up.text)
        }
        print("returning up/down speeds") # dev
        # self.driver.quit()
        return return_dict




t_bot = InternetSpeedTwitterBot()

# get my internet up/down speeds
my_internet_speeds = t_bot.get_internet_speed()
# print(f"speeds:\n{my_internet_speeds}")


# if internet is slow, then tweeter at whomstever
# if my_internet_speeds["down_speed"] < GUARANTEED_DOWN or my_internet_speeds["up_speed"] < GUARANTEED_UP:
if my_internet_speeds["down_speed"] < 9999 or my_internet_speeds["up_speed"] < 100: # dev
    t_bot.tweeter_a_complaint(down=my_internet_speeds["down_speed"], up=my_internet_speeds["up_speed"])




