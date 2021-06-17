from html import unescape
import requests


response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

question_data = response.json()["results"]
# print(question_data)
for i in range(len(question_data)):
    question_data[i]["question"] = unescape(question_data[i]["question"])
# print(question_data)
