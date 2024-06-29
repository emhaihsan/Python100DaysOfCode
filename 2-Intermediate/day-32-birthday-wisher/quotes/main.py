import smtplib
import datetime as dt
import random

my_email = "YOUR EMAIL"
password = "YOUR PASS"

day_of_week = dt.datetime.now().weekday()
if day_of_week == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="DESTINATION EMAIL",
            msg=f"Subject: Today's Quote!\n\n{quote}"
        )