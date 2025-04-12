
#note Class for Restaurant

class Restaurant():
    def __init__(self,name,rent,menu = []):
        self.name = name 
        self.rent = rent
        self.menu = menu 
        self.Server = []
        self.Manager = []
        self.customers = []
        self.Orders = []
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0
        
    def add_Employee(self,role,employee):
        if role.upper() == "SERVER":
            self.Server.append(employee)
        elif role.upper() == "MANAGER":
            self.Manager.append(employee) 
        else:
            print("Wrong role please enter real role!")

    def add_order(self,order):
        self.Orders.append(order)
        
    def pay_expense(self,amount,Description):
        if amount <= self.balance:
            self.expense+=amount
            self.balance-=amount
            print(f"Your Expense is {amount} for {Description}")
        else:
            print(f"You dont have Enough money for pay this:{amount} Expense!")
    
    def pay_salary(self,Employee):
        if Employee.salary < self.balance:
            print(f"Pay salary for :{Employee.name}\nSalary Amount is :{Employee.salary}")
            self.balance-=Employee.salary
            self.expense+=Employee.salary
            Employee.receive_salary()
        else:
            print(f"Dont have money for pay this {Employee.salary}")  

    def add_customer(self,customer):
        self.customers.append(customer)
    
    def show_employee_list(self):
        if len(self.Server) > 0 and len(self.Manager) > 0:
            for i in self.Manager:
                print(f"Manager Name: {i.name} Email: {i.email} Salary: {i.salary}")
                
            for i in self.Server:
                print(f"Server Name: {i.name} Email: {i.email} Salary: {i.salary}")
            
    def receive_payment(self,order,customer):
        if order.bill < customer.wallet:
            self.balance += order.bill
            self.revenue += order.bill
            customer.wallet -= order.bill
            print("Your Order payment Successful!")
            print(f"You have only {customer.wallet} balance in your account")
        else:
            print(f"You are so poor!\ndont have money for pay:{order.bill} taka\nplease topUp your account !")
    
            