import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = os.environ["ALPHA_VANTAGE_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
INCREASE_SYMBOL = "🔺"
DECREASE_SYMBOL = "🔻"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY,
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

print(response.url)

all_days_data = list(response.json()["Time Series (Daily)"].values())
yesterday_price = float(list(all_days_data[0].values())[3])
before_yesterday_price = float(list(all_days_data[1].values())[3])

# print(yesterday_price)
# print(before_yesterday_price)

percentage = (yesterday_price - before_yesterday_price) / yesterday_price

# if abs(percentage) >= 0.05:

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# print("Get News")

parameters = {"q": COMPANY_NAME, "apikey": NEWS_API_KEY}

response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
response.raise_for_status()

# print(response.url)

first_3_news = response.json()["articles"][-3:]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
client = Client(account_sid, auth_token)

for article in first_3_news:
    client.messages.create(
        body=f"\nTSLA: {DECREASE_SYMBOL if percentage < 0 else INCREASE_SYMBOL}{round(abs(percentage)*100,2)}%\nHeadline: {article['title']}.\nBrief: {article['description']}",
        from_="+17372143842",
        to="+201144521964",
    )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
