class Restaurant:
    def __init__(self,name,rent, menu = []) -> None:
        self.name = name
        self.rent = rent
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.expense = 0
        self.menu = menu
        self.revenue = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self,employee_type,employee):
        if employee_type== "chef":
            self.chef = employee
        elif employee_type=='server':
            self.server = employee

        elif employee_type == 'manager':
            self.manager = employee

    def add_order(self,order):
        self.orders.append(order)

    def recieve_payment(self,order,amount,customer):
        if amount > order.bill:
            self.revenue += amount
            self.balance += amount 
            customer.due_amount = 0
            return amount - order.bill
        
        else :
            print("not enough money pay more.")
        
    def pay_expense(self,amount,description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount

            print(f'Expence {amount} for {description}')

        else:
            print(f'not enough money to expense {amount}')

    def pay_salary(self,employee):
        if employee.salary <self.balance:
            employee.recieve_salary()

    def show_employee(self):
        print(f'============ showing Employees================')
        if self.chef is not None:
            print(f'chef {self.chef.name} is working now with salary:{self.chef.salary}. ')

        if self.manager is not None:
            print(f'Manager {self.manager.name} is working with salary : {self.manager.salary}')

        if self.server is not None:
            print(f'Server {self.server.name} is still working with salary {self.server.salary}')
        