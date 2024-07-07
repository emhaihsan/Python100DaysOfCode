import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser

try:
    date = input("Type in year in yyyy-mm-dd format: ")
    date = datetime.strptime(date, "%Y-%m-%d").date()
except ValueError:
    print("Error: Invalid date format. Please enter a date in the format yyyy-mm-dd.")
    exit()

url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.select("li ul li h3")

