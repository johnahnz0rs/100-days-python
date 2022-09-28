import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

load_dotenv()
EMAIL = os.getenv("EMAIL")
PW = os.getenv("PW")
driver = webdriver.Chrome("/Users/johnahnz0rs/00 - JAHN PROJECTS/chromedriver")

# load tinder.com
driver.get("https://tinder.com")
time.sleep(2)

# click login
login_button = driver.find_element(By.LINK_TEXT, "Log in")
login_button.click()
time.sleep(1)

# click sign in w google
google_sign_in_button = driver.find_element(By.XPATH, '//*[@id="s-365721967"]/main/div/div[1]/div/div/div[3]/span/div[1]/div/button')
google_sign_in_button.click()
time.sleep(2)

# switch to google SSO window
window_tinder = driver.window_handles[0]
window_google_sso = driver.window_handles[1]
driver.switch_to.window(window_google_sso)
time.sleep(1)

# enter email
gmail_email = driver.find_element(By.CSS_SELECTOR, "input#identifierId")
gmail_email.send_keys(EMAIL)
gmail_email.send_keys(Keys.ENTER)
time.sleep(1)

# enter pw
gmail_pw = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
gmail_pw.send_keys(PW)
gmail_pw.send_keys(Keys.ENTER)
time.sleep(1)

# switch back to tinder window
driver.switch_to.window(window_tinder)
time.sleep(3)

# allow location
allow_location = driver.find_element(By.XPATH, '//*[@id="s-365721967"]/main/div/div/div/div[3]/button[1]')
allow_location.click()

# disallow notifications
disallow_notifications = driver.find_element(By.XPATH, '//*[@id="s-365721967"]/main/div/div/div/div[3]/button[2]')
disallow_notifications.click()

# allow cookies
accept_cookies = driver.find_element(By.XPATH, '//*[@id="s1362659109"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()
time.sleep(10)

# start swiping
like_button = None
while not like_button:
    try:
        print("trying to find like button")
        like_button = driver.find_element(By.XPATH, '//*[@id="s1362659109"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
    except NoSuchElementException:
        print("waiting to find like button")
        time.sleep(5)


for i in range(0,100):
    print(i)
    try:
        like_button.click()
    except ElementClickInterceptedException:
        try: 
            dismiss_match_back_to_tinder = driver.find_element(By.PARTIAL_LINK_TEXT, "BACK TO TINDER")
            dismiss_match_back_to_tinder.click()
        except NoSuchElementException:
            add_tinder_to_home_screen_not_interested = driver.find_element(By.PARTIAL_LINK_TEXT, "Not interested")
            add_tinder_to_home_screen_not_interested.click()
        finally:
            time.sleep(1)

    finally:
        time.sleep(1)

