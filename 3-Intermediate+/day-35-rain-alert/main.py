import requests
import os
from twilio.rest import Client

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
TWILIO_WHATSAPP_NUMBER = os.environ.get('TWILIO_WHATSAPP_NUMBER')
YOUR_TWILIO_VERIFIED_NUMBER = os.environ.get('YOUR_TWILIO_VERIFIED_NUMBER')
OWM_API_KEY = os.environ.get('OWM_API_KEY')
MY_LAT = -7.795580 # Your latitude
MY_LONG = 110.369492 # Your longitude

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWM_API_KEY,
    "cnt": 4,
    }
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
def is_raining(datas: dict)->bool:
    for data in datas["list"]:
        for weather in data['weather']:
            if weather['id'] < 700:
                print("Bring an umbrella, it's going to rain!")
                return True
            
account_sid = ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)



if is_raining(weather_data):
    message = client.messages.create(
    body="Bring an umbrella, it's going to rain!",
    from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
    to=f"whatsapp:{YOUR_TWILIO_VERIFIED_NUMBER}",
    )
    print(message.status)