from Usears import Rider,Driver
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
        Rider.wallet -= self.cost_amount
        Driver.wallet += self.cost_amount
    
    def __repr__(self):
        print(f"Ride details : {self.start_location} - {self.end_location}")

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
            Driver.accept_ride(ride)
            return ride 
        
class Ride_Share:
    ID = 1000
    def __init__(self,Company_name):
        self.company_Name = Company_name
        self.riders = []
        self.Drivers = []
        self.rides = []
        
    def add_rider(self,rider):
        self.riders.append(rider) #! add riders object in list
        
    def add_Driver(self,Driver):
        self.Drivers.append(Driver) #! add Driver object in list
        
    def add_ride(self,Ride): #! add Rides object in list
        self.rides.append(Ride)
    