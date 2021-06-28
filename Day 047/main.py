import requests
from bs4 import BeautifulSoup
import smtplib
import os

product_url = "https://www.amazon.com/HP-17-by3063st-Display-Notebook-i3-1005G1/dp/B08FH4H4FB/ref=pd_sbs_1/144-2207339-6401145?pd_rd_w=KjBon&pf_rd_p=43345e03-9e2a-47c0-9b70-a50aa5ecbd5c&pf_rd_r=VP6SYJW5AGSA98AXND77&pd_rd_r=96b51993-e608-47ef-8dda-0297f8c1ba40&pd_rd_wg=44fLn&pd_rd_i=B08MDMCTHD&th=1"

browser_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
}

response = requests.get(url=product_url, headers=browser_headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")
price_span = soup.find(name="span", class_="a-color-price")

price = float(price_span.string.strip()[1:])

# print(price)
target_price = 700.0  # input("Enter your target price: ")

if price <= target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=os.environ["MY_FACULTY_EMAIL"],
            password=os.environ["MY_FACULTY_EMAIL_PASS"],
        )
        connection.sendmail(
            from_addr=os.environ["MY_FACULTY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subject: Amazon Price Tracker Alert!\n\nYour product price ({price}) is currently below your target price ({target_price}).\nCheck it now: {product_url}",
        )
