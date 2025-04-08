from Users import Rider,Driver
from time import time

class Ride():
    def __init__(self,start,end):
        self.start_location = start
        self.end_location = end
        self.cost_amount = None
        self.Driver = None
        self.start_time = None
        self.end_time = None
        
    def set_driver(self,Driver):
        self.Driver = Driver
        
    def start_ride(self):
        self.start_time = time.now()
    
    def end_ride(self,Rider,Driver):
        self.end_time = time.now()
        self.Rider.wallet -= self.cost_amount
        self.Driver.wallet += self.cost_amount
    
    def __repr__(self):
        print("This is ride class d'not print it!")

class Ride_request():
    def __init__(self,Rider,Destination):
        self.Rider = Rider
        self.end_location = Destination 

class Ride_match():
    def __init__(self,Drivers) -> None:
        self.available_Driver = Drivers
        
    def find_driver(self,ride_request):
        if len(self.available_Driver) > 0:
            Driver = self.available_Driver
            ride = Ride(ride_request.Rider.current_location , ride_request.end_location)
            Driver.accept_ride()