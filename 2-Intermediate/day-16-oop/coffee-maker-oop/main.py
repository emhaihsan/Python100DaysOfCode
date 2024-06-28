from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
        print("Machine turned off.")
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
    else:
        print("Invalid choice. Please choose from espresso, latte, or cappuccino.")
