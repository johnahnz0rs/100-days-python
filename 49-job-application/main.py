
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

load_dotenv()
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
LINKEDIN_JOBS_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3266477377&f_AL=true&f_PP=102448103&f_TPR=r2592000&keywords=python%20developer&refresh=true&sortBy=R"
driver = webdriver.Chrome("/Users/johnahnz0rs/00 - JAHN PROJECTS/chromedriver")

# load jobs page
driver.get(LINKEDIN_JOBS_URL)
time.sleep(1)

# click sign in button
sign_in_button = driver.find_element(By.CSS_SELECTOR, "header nav div a.btn-secondary-emphasis")
sign_in_button.click()
time.sleep(1)

# enter email
input_email = driver.find_element(By.CSS_SELECTOR, "input#username")
input_email.send_keys(LINKEDIN_EMAIL)
# enter password
input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
input_password.send_keys(LINKEDIN_PASSWORD)
# sign in (click da button)
input_sign_in = driver.find_element(By.CSS_SELECTOR, "form.login__form div.login__form_action_container button")
input_sign_in.click()
time.sleep(1)

# get job listings
jobs_listings = driver.find_elements(By.CSS_SELECTOR, "section.scaffold-layout__list div.jobs-search-results-list ul li div.job-card-container")

# print(jobs_listings[3].text)
# jobs_listings[3].click()
# time.sleep(1)

for job in jobs_listings[0:10]:
    job.click()
    time.sleep(1)

    # click to start easy apply 
    try:
        easy_apply_button = driver.find_element(By.CSS_SELECTOR, "section.scaffold-layout__detail button.jobs-apply-button")
        easy_apply_button.click()
        time.sleep(1)

        # easy apply screen 1
        next_button = driver.find_element(By.CSS_SELECTOR, "div.jobs-easy-apply-content form footer button")
        next_button_text = driver.find_element(By.CSS_SELECTOR, "div.jobs-easy-apply-content form footer button span").text

        # is it ready to submit right away (i.e. no other next steps)
        if "Submit" in next_button_text:
            print("this easy apply has no other steps; ready to apply meow")
            follow_checkbox = driver.find_element(By.CSS_SELECTOR, "div.jobs-easy-apply-content div.relative.mt5.ph5")
            follow_checkbox.click()
            next_button.click()
        else:
            # if there is a next step/next button - easy apply screen 2
            next_button.click()
            time.sleep(1)

            try:
                review_button = driver.find_element(By.CSS_SELECTOR, "div.jobs-easy-apply-content form footer button")
                review_button_text = driver.find_element(By.CSS_SELECTOR, "div.jobs-easy-apply-content form footer button span").text

                # if the next step is NOTreview
                if "Review" not in review_button_text:
                    exit_this_extra_long_apply_button = driver.find_element(By.CSS_SELECTOR, "div#artdeco-modal-outlet div button.artdeco-modal__dismiss")
                    exit_this_extra_long_apply_button.click()
                    time.sleep(1)
                    discard_button = driver.find_element(By.CSS_SELECTOR, "div#artdeco-modal-outlet div button.artdeco-modal__confirm-dialog-btn")
                    discard_button.click()

                else:
                    # if the next step is review
                    print("tihs button says review")
                    review_button.click()
                    time.sleep(1)

                    # review & submit
                    follow_checkbox = driver.find_element(By.CSS_SELECTOR, "div.jobs-easy-apply-content div.relative.mt5.ph5")
                    follow_checkbox.click()

                    submit_button = driver.find_element(By.CSS_SELECTOR, "div.jobs-easy-apply-content footer button.artdeco-button--primary")
                    submit_button.click()

                    try:
                        success_modal_exit_button = driver.find_element(By.CSS_SELECTOR, "div#artdeco-modal-outlet div button.artdeco-modal__dismiss")
                        success_modal_exit_button.click()
                    except:
                        pass
            except:
                pass


    except:
        pass
    

    