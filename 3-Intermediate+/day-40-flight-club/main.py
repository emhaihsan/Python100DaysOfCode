from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager

def find_cheapest_flight(flights_data):
    if not flights_data:
        print("No flights found.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", 0)
    
    flight = flights_data[0] # cheapest at index 0
    price = flight["price"]["total"]
    origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination_airport = flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
    out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = flight["itineraries"][-1]["segments"][-1]["arrival"]["at"].split("T")[0]
    stops = len(flight["itineraries"][0]["segments"]) - 1
    
    return FlightData(price, origin_airport, destination_airport, out_date, return_date, stops)
    
def main():
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    sheet_data = data_manager.get_destination_data()
    customer_emails = data_manager.get_customer_emails()
    tomorrow = datetime.now() + timedelta(days=1)
    six_months_from_today = datetime.now() + timedelta(days=(6 * 30))
    departure_date = tomorrow.strftime("%Y-%m-%d")
    return_date = six_months_from_today.strftime("%Y-%m-%d")
    for data in sheet_data:
        # city = data['city']
        iata_code = flight_search.get_destination_code(data['city'])
        if iata_code == "N/A":
            continue
        data['iataCode'] = iata_code
        print(f"Getting Flight prices for {data['city']}....")
        # Search for direct flights
        flights_data = flight_search.search_flights("LON", iata_code, departure_date, return_date, is_direct=True)
        cheapest_flight = find_cheapest_flight(flights_data)
        # If no direct flight found, search for indirect flights
        if cheapest_flight.price == "N/A":
            flights_data = flight_search.search_flights("LON", iata_code, departure_date, return_date, is_direct=False)
            cheapest_flight = find_cheapest_flight(flights_data)
        print(f"{data['city']}: £{cheapest_flight.price}")
        if cheapest_flight.price != "N/A" and float(cheapest_flight.price) < float(data['lowestPrice']):
            print(f"Better deal found! {data['city']}: £{cheapest_flight.price}\nSending message...")
            if cheapest_flight.stops == 0:
                message = (
                    f"Low price alert! Only GBP {cheapest_flight.price} to fly from "
                    f"{cheapest_flight.departure_airport} to {cheapest_flight.arrival_airport}, "
                    f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
                )
            else:
                message = (
                    f"Low price alert! Only GBP {cheapest_flight.price} to fly from "
                    f"{cheapest_flight.departure_airport} to {cheapest_flight.arrival_airport}, "
                    f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}.\n\n"
                    f"Note: This flight has {cheapest_flight.stops} stop(s)."
                )
            subject = "New Low Price Flight Deal!"
            notification_manager.send_whatsapp(message)
            notification_manager.send_emails(customer_emails, subject, message)
            print(message)
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

if __name__ == "__main__":
    main()