from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,Vehicle_type,license_plate):
        self.type = Vehicle_type
        self.license = license_plate
        self.status = "Available"
    
    @abstractmethod
    def start_driving(self):
        pass
    
class car(Vehicle):
    def __init__(self, Vehicle_type, license_plate):
        super().__init__(Vehicle_type, license_plate)
        
    def start_driving(self):
        self.status = "Unavailable"

class bike(Vehicle):
    def __init__(self, Vehicle_type, license_plate):
        super().__init__(Vehicle_type, license_plate)
    
    def start_driving(self):
        self.status = "Unavailable"
        