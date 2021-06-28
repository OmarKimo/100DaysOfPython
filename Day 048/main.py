from selenium.webdriver import Firefox
import datetime

driver = Firefox()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id('cookie')
store_elements = driver.find_elements_by_css_selector("#store div")

check_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
to_reach = datetime.datetime.now() + datetime.timedelta(minutes=5)

while datetime.datetime.now() < to_reach:
    cookie.click()

    if datetime.datetime.now() >= check_time:
        store_prices = driver.find_elements_by_css_selector("#store b")
        prices = [(int("0" + price.text.strip().split('-')[-1].replace(",", "").strip()), idx) for idx, price in enumerate(store_prices)]
        prices.sort(reverse=True)
        my_money = int("0" + driver.find_element_by_id("money").text.strip().split('-')[-1].replace(",", "").strip())

        for i in range(len(prices)):
            if my_money >= prices[i][0] and prices[i][0]:
                store_prices[prices[i][1]].click()
                break

        check_time = datetime.datetime.now() + datetime.timedelta(seconds=10)

print(driver.find_element_by_id('cps').text)