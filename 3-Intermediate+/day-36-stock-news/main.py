import requests
import os
from datetime import date, timedelta
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("YOUR_TWILIO_VERIFIED_NUMBER")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, params={"function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": STOCK_API_KEY})
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday = date.today() - timedelta(days=1)
yesterday_closing = response.json()["Time Series (Daily)"][str(yesterday)]["4. close"]
print(f"yesterday_closing: {yesterday_closing}")
#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday = date.today() - timedelta(days=2)
day_before_yesterday_closing = response.json()["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
print(f"day_before_yesterday_closing: {day_before_yesterday_closing}")
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
possitive_difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
print(f"possitive_difference: {possitive_difference}")
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (possitive_difference / float(yesterday_closing)) * 100
print(f"percentage_difference: {percentage_difference}")
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    news_response.raise_for_status()
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    articles = news_response.json()["articles"][:3]
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    messages = [article["title"] + " - " + article["description"] for article in articles]
#TODO 9. - Send each article as a separate message via Twilio. 
    for message in messages:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        status = "UP" if yesterday_closing > day_before_yesterday_closing else "DOWN"
        formatted = f"Subject: {STOCK_NAME}: {status} {percentage_difference}%\n\nHeadline: {message}"
        message = client.messages.create(
            body=formatted,
            from_=f"whatsapp:{TWILIO_VIRTUAL_NUMBER}",
            to=f"whatsapp:{TWILIO_VERIFIED_NUMBER}"
        )



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

