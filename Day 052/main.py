from selenium.webdriver import Firefox
import os
from time import sleep
from selenium.webdriver.common.keys import Keys


TIMEOUT = 5
INSTAGRAM_EMAIL = os.environ["INSTAGRAM_EMAIL"]
INSTAGRAM_PASS = os.environ["INSTAGRAM_PASS"]
TEST_NUMBER = 5


class InstaFollower:
    def __init__(self) -> None:
        self.driver = Firefox()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(TIMEOUT)
        username = self.driver.find_element_by_name("username")
        username.send_keys(INSTAGRAM_EMAIL)
        password = self.driver.find_element_by_name("password")
        password.send_keys(INSTAGRAM_PASS)
        password.send_keys(Keys.ENTER)
        sleep(TIMEOUT)

    def find_followers(self, user_name):
        self.driver.get(f"https://www.instagram.com/{user_name}")
        sleep(TIMEOUT)
        followers = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"
        )
        followers.click()
        scrolldiv = self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[2]"
        )
        for _ in range(TEST_NUMBER):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scrolldiv
            )
            sleep(TIMEOUT)

    def follow(self):
        buttons = self.driver.find_elements_by_css_selector("li button")
        for button in buttons:
            if button.text == "Follow":
                button.click()
                sleep(1)


obj = InstaFollower()
obj.login()
obj.find_followers("chefsteps")
obj.follow()
