import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code == 200:
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
elif response.status_code == 404:
    raise Exception("Error: Invalid latitude and longitude - " + str(response.status_code))

