import requests
from datetime import datetime

MY_LAT = -7.795580
MY_LONG = 110.369492

parameters = {
    "lat": MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
    "tzid":"Asia/Jakarta"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)