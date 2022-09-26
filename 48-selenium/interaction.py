
from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/johnahnz0rs/00 - JAHN PROJECTS/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#bodyContent #mp-welcomecount #articlecount a[title='Special:Statistics']")
print(article_count.text)


driver.quit()
