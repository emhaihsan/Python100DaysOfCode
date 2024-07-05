import os
from datetime import datetime
import requests

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")

# Endpoint untuk Nutritionix API
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Headers untuk request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# Input dari pengguna
exercise_text = input("Enter the exercises you did: ")

# Body untuk request
body = {
    "query": exercise_text,
    "gender": "male",  # Sesuaikan dengan data pengguna
    "weight_kg": 75,   # Sesuaikan dengan data pengguna
    "height_cm": 166,  # Sesuaikan dengan data pengguna
    "age": 27          # Sesuaikan dengan data pengguna
}

# Membuat request POST
response = requests.post(exercise_endpoint, json=body, headers=headers)
result = response.json()

# Mengambil tanggal dan waktu saat ini
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

# Endpoint untuk Sheety API
sheety_endpoint = "https://api.sheety.co/5e6a32d9d8641c50966dadf66c0db39b/myWorkoutsWorksheet/workouts"

# Headers untuk Sheety request
sheety_headers = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json"
}

# Menyimpan setiap latihan ke Google Sheets
for exercise in result["exercises"]:
    sheety_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_body, headers=sheety_headers)