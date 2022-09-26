
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/johnahnz0rs/00 - JAHN PROJECTS/chromedriver")

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email_address = driver.find_element(By.NAME, "email")
submit_button = driver.find_element(By.TAG_NAME, "button")

first_name.send_keys("Angela")
last_name.send_keys("Yu")
email_address.send_keys("angela@mail.com")
submit_button.click()

# driver.quit()
