from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

LINKEDIN_EMAIL = os.environ["MY_DUMMY_LINKEDIN_EMAIL"]
LINKEDIN_PASS = os.environ["MY_DUMMY_LINKEDIN_PASS"]
MY_PHONE = "1144521964"
TIMEOUT = 10

driver = Firefox()
jobs_url = "https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python%20developer"
driver.get(jobs_url)

sleep(TIMEOUT)
print("first page loaded")

sign_in_but = driver.find_element_by_link_text("Sign in")
sign_in_but.click()

sleep(TIMEOUT)
print("sign in page loaded")

username_box = driver.find_element_by_id("username")
username_box.send_keys(LINKEDIN_EMAIL)
password_box = driver.find_element_by_id("password")
password_box.send_keys(LINKEDIN_PASS)
password_box.send_keys(Keys.ENTER)

sleep(TIMEOUT)
print("jobs page loaded")
sleep(TIMEOUT)

all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

for idx, job in enumerate(all_jobs):
    print(f"get job {idx}")
    job.click()
    sleep(TIMEOUT)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        sleep(TIMEOUT)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        phone.send_keys(MY_PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            sleep(TIMEOUT)

            discard_button = driver.find_elements_by_class_name(
                "artdeco-modal__confirm-dialog-btn"
            )[1]
            discard_button.click()

            print("Complex application!")
            continue
        else:
            submit_button.click()

        sleep(TIMEOUT)

        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
        sleep(TIMEOUT)

    except NoSuchElementException:
        print("No application button!")
        continue
