from abc import ABC,abstractmethod
# Note: Base class for Users and make Customer class
class user(ABC):
    def __init__(self,name,email,number):
        self.name = name
        self.email = email
        self.number = number
    @abstractmethod
    def profile(self):
        pass

class Customer(user):
    def __init__(self, name, email, number, wallet):
        super().__init__(name, email, number)
        self.__wallet = wallet
        self.__order = None 
        
    def status(self):
        if self.__order is None:
            return "Empty"
        else:
            return "Order ongoing"
    
    def profile(self):
        print(f'''Dear Customer Your name is : {self.name}
              \nYour Email is : {self.email}
              \nYour Number is : {self.number}
              \nYour Order Status is {self.status()}''')
    #note: getter setter
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order = order
    
    def TopUP(self, balance):
        if balance <= 0:
            return
        self.__wallet += balance  
    
    def place_order(self, order):
        self.order = order
        print(f'Your order place successful!\nYour order item is {order.item}')
    
    def pay_for_order(self,amount):
        pass
    def pay_tips(self,amount):
        pass
    def write_review(self,stars):
        pass