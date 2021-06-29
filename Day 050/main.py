from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)
from time import sleep
import os

MY_FACEBOOK_EMAIL = os.environ["MY_FACEBOOK_EMAIL"]
MY_FACEBOOK_PASS = os.environ["MY_FACEBOOK_PASS"]
TIMEOUT = 10


driver = Firefox()
driver.get(url="https://tinder.com/")

sleep(TIMEOUT)
print("Tinder page loaded")

try:
    cookies = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div/div/div[1]/button"
    )
    cookies.click()
except NoSuchElementException:
    print("cookies not loaded yet")

login = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a"
)
login.click()

print("Log in is clicked")
sleep(TIMEOUT)

login_facebook = driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button"
)
login_facebook.click()

print("Log in with facebook is clicked")
sleep(2 * TIMEOUT)

driver.switch_to.window(driver.window_handles[1])
print(driver.title)

sleep(TIMEOUT)

email = driver.find_element_by_id("email")
email.send_keys(MY_FACEBOOK_EMAIL)
password = driver.find_element_by_id("pass")
password.send_keys(MY_FACEBOOK_PASS)
password.send_keys(Keys.ENTER)

print("Log in form is filled")
sleep(TIMEOUT)

driver.switch_to.window(driver.window_handles[0])
print(driver.title)

sleep(TIMEOUT)

while True:
    try:
        allow_location = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/button[1]"
        )
        allow_location.click()
        break
    except NoSuchElementException:
        sleep(TIMEOUT)

print("Location is allowed")
sleep(TIMEOUT)

while True:
    try:
        disallow_notifications = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/button[2]"
        )
        disallow_notifications.click()
        break
    except NoSuchElementException:
        sleep(TIMEOUT)

print("Notifiation is disallowed")
sleep(2 * TIMEOUT)

try:
    cookies = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div/div/div[1]/button"
    )
    cookies.click()
except NoSuchElementException:
    print("cookies not loaded yet or pressed earlier")

while True:
    sleep(TIMEOUT)
    try:
        like = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button"
        )
        like.click()
        print("person found and liked")
    except NoSuchElementException:
        try:
            like = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button"
            )
            like.click()
            print("person found and liked")
        except NoSuchElementException:
            sleep(TIMEOUT)
            print("No person found, wait")
    except ElementClickInterceptedException:
        sleep(TIMEOUT)
        print("match found")
