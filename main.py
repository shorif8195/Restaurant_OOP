from menu import Menu,Pizza,Burger,Drinks
from restaurant import Restaurant
from users import Chef,Customer,Server,Manager
from order import Order

def main():
    menue = Menu()

    pizza1 = Pizza('shutki pizza',500,'Large',['shutki','onion'])
    menue.add_menu_item('pizza',pizza1)
    pizza2 = Pizza("alu pizza",800,"large",['Poteto','onion','pepper'])
    menue.add_menu_item("pizza",pizza2)

    #burger adding

    burger1 = Burger("Naga Burger",1000,'Chicken',['bread','chili'])
    menue.add_menu_item('burger',burger1)
    burger2 = Burger("beef Burger",1000,'beef',['bread','beef'])
    menue.add_menu_item('burger',burger2)


    #add drinks

    coke1 = Drinks('coke',59,True)
    menue.add_menu_item('drinks',coke1)

   # menue.show_menu()


    restro = Restaurant("Sai baba restraurant",200,menue)
    #add employees

    manager = Manager('kalachan baburchi',555555,'Kala@gmail.ocm','kaliyapur',5000,'jan 1 2020','core')
    restro.add_employee('manager',manager)

    chef = Chef('Rustom baburchi',520394,'Rustom','rustom nagar',555,'feb 2 2020','chef','everything')
    restro.add_employee('chef',chef)

    serv = Server('chutu server',25530,'cutu@gamil.com','keranigange',3453,'2 aug 2020','server')
    restro.add_employee('server',serv)

    #restro.show_employee()

    #customer

    customer_1 = Customer("shakib khan",7343,"shakib@gmail.com",'banani',50000)
    order_1 = Order(customer_1,[pizza1,burger1])

    customer_1.place_order(order_1)
    restro.add_order(order_1)

    #customer 1 paying for order 1

    restro.recieve_payment(order_1,2007,customer_1)

    print(restro.revenue, restro.balance)


    #customer2

    customer_2 = Customer("shakib All hasan",7343,"shakib@gmail.com",'banani',50000)
    order_2 = Order(customer_2,[pizza2,burger2])

    customer_1.place_order(order_2)
    restro.add_order(order_2)

    #customer 1 paying for order 1

    restro.recieve_payment(order_2,20343,customer_2)

    print(restro.revenue,restro.balance)


    #pay rent
    restro.pay_expense(restro.rent,'rent')
    print(restro.revenue,restro.balance,restro.expense)



main()