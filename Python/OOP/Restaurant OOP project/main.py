from User import Customer,Manager,Server
from Restaurant import Restaurant
from order import order
from Menu import Pizza, Burger, Drinks, Menu

def main():
    menu = Menu()
    #note creating pizza objects
    pizza_1 = Pizza(name="meat machine", price=3000, size="medium", toppings=["meatball", "capsicum", "mushroom"])
    pizza_2 = Pizza('Alu Vorta Pizza', 4000, 'large', ['potato', 'onion', 'oil'])
    pizza_3 = Pizza('Dal Pizza', 5000, 'large', ['dal', 'oil'])
    
    #! adding pizza in menu
    
    menu.add_menu_item('pizza',pizza_1) 
    menu.add_menu_item('pizza',pizza_2) 
    menu.add_menu_item('pizza',pizza_3) 
    
    #note creating burger objects
    burger_1 = Burger(name="beef BBQ Burger", price=2000, meat = 'chicken',  ingredients=['bread', 'chili'])
    burger_2 = Burger('Beef Burger', 5200, 'beef', ['meat', 'kolixa'])
    
    #! adding Burger in menu
    menu.add_menu_item("burger",burger_1)
    menu.add_menu_item("burger",burger_2)
    
    #note creating Drink objects
    drink_1 = Drinks("Lemon",900,True)
    drink_2 = Drinks("Coffee",800,False)
    drink_3 = Drinks("Milk shake",1200,True)
    
    #! adding Drinks in menu
    menu.add_menu_item('drinks',drink_1)
    menu.add_menu_item('drinks',drink_2)
    menu.add_menu_item('drinks',drink_3)
    
    #task creating Restaurant class 
    restaurant = Restaurant("CineLove",10000,menu)
    
    #task add manager
    manager = Manager("M.Mahadi","mahadi@hasan.com","01732652365","Tomar moner maje","Head of commend",20000)
    restaurant.add_Employee("manager",manager)
    
    #task add server
    server_1 = Server("Koi samsu", "koi@samsu.com", "01745632145", "kailla maiahr moner vitor", "Waiter", 500)
    server_2 = Server("Jho Doe", "jhon@doe.com", "01712345678", "Random Address 1", "Waiter", 600)
    server_3 = Server("Jane Smith", "jane@smith.com", "01787654321", "Random Address 2", "Waitress", 550)
    server_4 = Server("Alice Brown", "alice@brown.com", "01711223344", "Random Address 3", "Waitress", 580)
    
    restaurant.add_Employee("server",server_1)
    restaurant.add_Employee("server",server_2)
    restaurant.add_Employee("server",server_3)
    restaurant.add_Employee("server",server_4)
    
    #task make and add some castomar to returent
    
    #todo customer 01 place order
    
    user_1 = Customer("Mahir", "mahir@bissas.com", "01765321452", 1000)
    order_1 = order(user_1, [burger_1, pizza_1, drink_1, burger_2,burger_1, pizza_1, drink_1, burger_2])
    restaurant.add_order(order_1)
    user_1.TopUP(100000)
    restaurant.receive_payment(order_1, user_1)
    
    # user_2 = Customer("Ayesha", "ayesha@domain.com", "01798765432", 1500)
    # order_2 = order(user_2, [pizza_2, drink_2,burger_1, pizza_1, drink_1, burger_2])
    # restaurant.add_order(order_2)
    # user_2.TopUP(50000)
    # restaurant.receive_payment(order_2, user_2)
    
    # user_3 = Customer("Rahim", "rahim@domain.com", "01712349876", 2000)
    # order_3 = order(user_3, [pizza_3, burger_1, drink_3,pizza_3, burger_1, drink_3])
    # restaurant.add_order(order_3)
    # user_3.TopUP(100000)
    # restaurant.receive_payment(order_3, user_3)
    
    restaurant.pay_salary(manager)
    restaurant.pay_expense(restaurant.rent,"rent")
    print(restaurant.balance)
    # restaurant.show_employee_list()
    # menu.show_menu()
    
    
if __name__ == '__main__':
    main()