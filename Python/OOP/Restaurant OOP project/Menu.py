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
        

class Menu:
    def __init__(self):
        self.pizzas = []
        self.burgers = []
        self.drinks = []
        
    def add_menu_item(self,item_type,item):
        if item_type.lower() == "pizza":
            self.pizzas.append(item)
        elif item_type.lower() == 'burger':
            self.burgers.append(item)
        elif item_type.lower() == 'drinks':
            self.drinks.append(item)
            
    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'name: {pizza.name} price: {pizza.price}')
        for burger in self.burgers:
            print(f'name: {burger.name} price: {burger.price}')
        for drink in self.drinks:
            print(f'name: {drink.name} price: {drink.price}')