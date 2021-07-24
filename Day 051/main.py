from selenium.webdriver import Firefox
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASS = os.environ["TWITTER_PASS"]
TIMEOUT = 5
PROMISED_UP = 50
PROMISED_DOWN = 300


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = Firefox()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(TIMEOUT)
        start_but = self.driver.find_element_by_class_name("js-start-test")
        start_but.click()
        sleep(12 * TIMEOUT)
        download_result = self.driver.find_element_by_class_name("download-speed")
        upload_result = self.driver.find_element_by_class_name("upload-speed")
        print(download_result.text)
        print(upload_result.text)
        self.down = float(download_result.text)
        self.up = float(upload_result.text)

    def tweet_at_provider(self):
        tweet = f"Hey @EtisalatMisr, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        self.driver.get("https://twitter.com/login")
        sleep(TIMEOUT)
        try:
            username = self.driver.find_element_by_name("username")
            username.send_keys(TWITTER_EMAIL)
        except:
            username = self.driver.find_element_by_name("session[username_or_email]")
            username.send_keys(TWITTER_EMAIL)
        try:
            password = self.driver.find_element_by_name("password")
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)
        except:
            password = self.driver.find_element_by_name("session[password]")
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)
        sleep(TIMEOUT)
        editor = self.driver.find_element_by_class_name("public-DraftEditor-content")
        editor.send_keys(tweet)
        ActionChains(self.driver).key_down(Keys.CONTROL).key_down(Keys.ENTER).key_up(
            Keys.CONTROL
        ).key_up(Keys.ENTER).perform()

    def check(self):
        return self.up >= PROMISED_UP and self.down >= PROMISED_DOWN


obj = InternetSpeedTwitterBot()

obj.get_internet_speed()

if not obj.check():
    obj.tweet_at_provider()