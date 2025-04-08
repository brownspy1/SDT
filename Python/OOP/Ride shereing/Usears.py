from abc import ABC ,abstractmethod
from datetime import datetime

class user(ABC):
    def __init__(self,name,email,Nid,current_location):
        self.name=name
        self.email=email
        self.Nid=Nid
        self.current_location = current_location
        self.__id = Ride_Share.ID+1
        
    @abstractmethod
    def user_profile(self):
        raise NotImplementedError
    
class Rider(user):
    def __init__(self, name, email, Nid, current_location):
        super().__init__(name, email, Nid, current_location)
        self.Current_ride = None
        self.wallet = 0
        self.current_location = current_location
        
    def user_profile(self):
        print(f"Rider Id: {self.__id} \nRider Name: {self.name} \nRider Email: {self.email}")
    
    def cash_in(self,amount):
        if amount > 0:
            self.wallet+=amount
        else:
            print(" Warning:Amount not Negative or Zero ")
    
    def update_location(self,location):
        self.current_location = location
    
    def ride_request(self, destination , ride_shering ):
        if not self.Current_ride:
            ride_requested = Ride_request(self,destination)
            Ride_matcher = Ride_match(ride_shering.Drivers)
            self.Current_ride = Ride_matcher.find_driver(ride_requested)
            # self.Current_ride = f"{self.current_location} - {Destination}"
    def show_Current_ride(self):
        print(self.Current_ride)
            
class Driver(user):
    def __init__(self, name, email, Nid, current_location):
        super().__init__(name, email, Nid,current_location)
        self.current_location = current_location
        self.wallet = 0
    def user_profile(self):
        print(f"Driver Id: {self.__id} \nDriver Name: {self.name} \nDriver Email: {self.email}")
        
    def accept_ride(self,Ride):
        Ride.start_ride()
        Ride.set_driver(self)   
        
    def reach_declination(self,Ride):
        Ride.end()

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
        self.start_time = datetime.now()
    
    def end_ride(self,Rider,Driver):
        self.end_time = datetime.now()
        Rider.wallet -= self.cost_amount
        Driver.wallet += self.cost_amount
    
    def __repr__(self):
        return f"Ride details : {self.start_location} - {self.end_location}"

class Ride_request():
    def __init__(self,Rider,Destination):
        self.Rider = Rider
        self.end_location = Destination 

class Ride_match():
    def __init__(self,drivers) -> None:
        self.available_Driver = drivers
        
    def find_driver(self,ride_request):
        if len(self.available_Driver) > 0:
            driver = self.available_Driver[0]
            ride = Ride(ride_request.Rider.current_location , ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        else:
            return None
        
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
    