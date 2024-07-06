class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport, arrival_airport, out_date, return_date):
        self.price = price
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.out_date = out_date
        self.return_date = return_date

    def __repr__(self):
        return f"FlightData({self.price}, {self.departure_airport}, {self.arrival_airport}, {self.out_date}, {self.return_date})"
    
