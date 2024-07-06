import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

CUSTOMER_ENDPOINT = "https://api.sheety.co/5e6a32d9d8641c50966dadf66c0db39b/myFlightDeals/users"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.endpoint = "https://api.sheety.co/5e6a32d9d8641c50966dadf66c0db39b/myFlightDeals/prices"
        self.headers = {
            "Authorization": os.environ.get("SHEETY_AUTH")
        }

    def get_destination_data(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.endpoint}/{city['id']}", json=new_data, headers=self.headers)
            response.raise_for_status()

    def get_customer_data(self):
        response = requests.get(url=CUSTOMER_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.users_data = data["users"]
        return self.users_data
    
    def add_user(self, first_name, last_name, email):
        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=CUSTOMER_ENDPOINT, json=new_data, headers=self.headers)
        response.raise_for_status()

    def get_customer_emails(self):
        response = requests.get(url=CUSTOMER_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        emails = [user["whatIsYourEmail"] for user in data["users"]]
        return emails


    
