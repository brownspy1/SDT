from abc import ABC,abstractmethod
class shop(ABC):
    def __init__(self):
        self.shop_name = "ITBagar"
        self.contact = "+880123456"

    @abstractmethod
    def add_to_cart(self,item,price):
        pass
    @abstractmethod
    def buy_now(self):
        pass
    @abstractmethod
    def calculat_amount(self):
        pass
class implimaent(shop):
    order_id = 1000
    product = {}
    def add_to_cart(self,item,price):
        if self.order_id not in self.product:
            self.product[self.order_id] = {}
        self.product[self.order_id][item] = price

    def calculat_amount(self):
        if self.order_id in self.product:
            return  sum(self.product[self.order_id].values())
        return 0
    def pay(self,taka,order_id):
        while True:
            try:
                self.amunt = int(input("Entar Taka: "))
                self.pin = int(input("Entar Pin: "))
            except Exception as e:
                print(e)
            if self.taka == self.amunt and self.pin == order_id:
                return True
            else:
                print("Payment failed! Try again.")
                retry = input("Do you want to retry? (y/n): ")
                if retry.lower() != 'y':
                    return False



    def buy_now(self):
        self.taka = self.calculat_amount()
        print("\n")
        print("------------------------------------------------------------------------")
        print(f"Your Ordar ID:#{self.order_id}")
        print("Your purchase item is:" , ','.join(self.product[self.order_id].keys()))

        print(f"Price is :",self.taka)
        if self.pay(self.taka,self.order_id):
            print(f"Payment successful TrXID:TB{self.order_id+self.taka+65}")
            print("------------------------------------------------------------------------")
            print("\n \n")
            self.product = {}
            self.__class__.order_id +=1
        else:
            print("failed plx try again later!")



s1 = implimaent()
s1.add_to_cart("cake",25)
s1.add_to_cart("ice-cream",50)
s1.buy_now()

s2 = implimaent()
s2.add_to_cart("pizza",200)
s2.add_to_cart("KFC",100)
s2.buy_now()

