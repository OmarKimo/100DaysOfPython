##################### Extra Hard Starting Project ######################
import pandas as pd
import random
from datetime import datetime
import smtplib
import os

LETTERS_DIR = "letter_templates"
MY_EMAIL = "omarkimo80@gmail.com"
MY_PASS = os.environ["MY_PASS"]
#print(MY_PASS)

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
df = pd.read_csv("birthdays.csv")
dic = df.to_dict(orient="records")
# print(dic)
filter_fun = lambda dic: dic["month"] == today.month and dic["day"] == today.day
today_birthdays = list(filter(filter_fun, dic))
# print(l)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letters = [
    os.path.join(LETTERS_DIR, filename)
    for filename in os.listdir(LETTERS_DIR)
    if os.path.isfile(os.path.join(LETTERS_DIR, filename))
]
for birthday in today_birthdays:
    if not letters:
        print("Sorry, there's no available birthday letters!")
    else:
        letter = random.choice(letters)
        # 4. Send the letter generated in step 3 to that person's email address.
        letter_text = ""
        with open(letter) as f:
            letter_text = "".join(f.readlines())
            letter_text = letter_text.replace("[NAME]", birthday["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject: Happy Birthday!\n\n{letter_text}",
            )
            # print("sent")
