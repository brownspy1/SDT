from abc import ABC ,abstractmethod
from ride import Ride,Ride_request,Ride_match

class user(ABC):
    def __init__(self,name,email,Nid):
        self.name=name
        self.email=email
        self.Nid=Nid
        # TODO: Add id in Dynamic
        self.__id = 0

    #! implement this in next inheritance class
    @abstractmethod
    def user_details(self):
        raise NotImplementedError
    
class Rider(user):
    def __init__(self, name, email, Nid, current_location):
        super().__init__(name, email, Nid)
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
    
    def ride_request(self, Destination ,location = None ):
        if not self.ride_request:
            #TODO: set ride request properly 
            #* set current ride via ride match
            self.Ride_request = Ride_request(self,Destination)
            self.Ride_macher = Ride_match()
            self.Current_ride = self.Ride_macher.find_driver(Ride_request)
            
class Driver(user):
    def __init__(self, name, email, Nid):
        super().__init__(name, email, Nid)
        self.current_location = None
        self.wallet = 0
    def user_profile(self):
        print(f"Driver Id: {self.__id} \nDriver Name: {self.name} \nDriver Email: {self.email}")
        
    def accept_ride(self,Ride):
        Ride.start_ride()
        Ride.set_driver(self)   
        
    def reach_declination(self,Ride):
        Ride.end()
