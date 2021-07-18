from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Firefox
from time import sleep


def process_link(link):
    if "http" not in link:
        link = f"https://www.zillow.com{link}"
    return link


form_url = "https://forms.gle/zmSB9Aa3TVcKytg59"
scraping_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
browser_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
}
TIMEOUT = 3

response = requests.get(scraping_url, headers=browser_headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

address_elements = soup.find_all(name="address", class_="list-card-addr")
addresses = [address.text for address in address_elements]

price_elements = soup.find_all(name="div", class_="list-card-price")
prices = [price.text.split("/")[0].split("+")[0] for price in price_elements]

links = [process_link(address.parent["href"]) for address in address_elements]

driver = Firefox()

for i in range(len(links)):
    driver.get(form_url)
    sleep(TIMEOUT)
    address_input = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
    )
    price_input = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
    )
    link_input = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
    )

    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])

    link_input.send_keys(links[i])
    submit = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span"
    )
    submit.click()

    sleep(TIMEOUT)
