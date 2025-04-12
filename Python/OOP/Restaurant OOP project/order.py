class order:
    def __init__(self,Customer,items=[]):
        self.customer = Customer
        self.items = items
        self.total = 0
        for item in items:
            self.total+=item.price
        self.bill = self.total
    def show_order(self):
        print(f"Dear {self.customer.name} your order item is :",end=' ')
        for item in self.items:
            print(f"{item.name} Price:{item.price}",end=",")
    