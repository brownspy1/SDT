class Food_item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Burger(Food_item):
    def __init__(self, name, price, meat, ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients

class Pizza(Food_item):
    def __init__(self, name, price, size, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings

class Drinks(Food_item):
    def __init__(self, name, price, isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold