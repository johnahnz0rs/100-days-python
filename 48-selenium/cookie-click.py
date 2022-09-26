
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
time_to_check_purchase_options = time.time() + 5

# page to scrape
driver = webdriver.Chrome("/Users/johnahnz0rs/00 - JAHN PROJECTS/chromedriver")
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# static elements
cookie = driver.find_element(By.ID, "cookie")
def purchase_most_expensive():
    purchase_options_list = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store > div:not(.grayed)")
    most_expensive_purchase_index = len(purchase_options_list) - 1
    purchase_this = purchase_options_list[most_expensive_purchase_index]
    print(f"purchased {purchase_this.text}")
    purchase_this.click()



# h4x d4 cookie clicker
while True:
    # every 5 seconds
    if time.time() - time_to_check_purchase_options > 0:
        print("it has been 5 seconds")
        # check for purchase options
        purchase_most_expensive()
        time_to_check_purchase_options = time.time() + 5
    # otherwise, click da cookie
    else:
        cookie.click()
        

