from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

CoffeMakerObj = CoffeeMaker()
MoneyMachineObj = MoneyMachine()
MenuObj = Menu()

while True:
    cmd = input(f"What would you like? ({MenuObj.get_items()}) [or 'report']: ").lower()
    if cmd == 'off':
        print("Goodbye!")
        break
    if cmd == 'report':
        CoffeMakerObj.report()
        MoneyMachineObj.report()
    else:
        drink = MenuObj.find_drink(cmd)
        if not drink:
            continue
        if not CoffeMakerObj.is_resource_sufficient(drink):
            continue
        if not MoneyMachineObj.make_payment(drink.cost):
            continue
        CoffeMakerObj.make_coffee(drink)
        
