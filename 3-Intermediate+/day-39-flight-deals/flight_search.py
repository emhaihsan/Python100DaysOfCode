import os
import requests
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-dates"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self.get_access_token()
        
    def get_access_token(self):
        # This method will return the access token for the API.
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        access_token_payload = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=access_token_payload)
        access_token = response.json()["access_token"]
        return access_token
    
    
    
    def get_destination_code(self, city):
        # This method will return the IATA code for the given city.
        location_headers = {
            "Authorization": f"Bearer {self._token}"
        }

        # Parameter untuk request Airports and City Search
        location_params = {
            "keyword": city,
            "max": 2,
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, headers=location_headers, params=location_params)
        try:
            results = response.json()["data"]
            code = results[0]["iataCode"]
        except IndexError:
            print(f"IndexError: No IATA code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No IATA code found for {city}.")
            return "Not Found"
        return code

    
    def search_flights(self, departure_city, arrival_city, departure_date, return_date):
        # This method will return a list of flight options for the given parameters.
        payload = {
            "originLocationCode": departure_city,
            "destinationLocationCode": arrival_city,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP"
        }
        flight_headers = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=flight_headers, params=payload)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            return []
        
        
if __name__ == "__main__":
    flight_search = FlightSearch()
    print(flight_search.get_access_token())
    print(flight_search.get_destination_code("Jakarta"))
    pprint(flight_search.search_flights("LON", "NYC", "2024-07-10","2024-07-20"))