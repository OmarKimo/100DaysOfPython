from data import report, MENU, getOrder, can

while True:
    cmd = input("What would you like? (espresso / latte / cappuccino) [or 'report']: ").lower()
    if cmd == 'off':
        print("Goodbye!")
        break
    if cmd == 'report':
        report()
    elif cmd in MENU.keys():
        result = can(MENU[cmd])
        if result:
            print(f"Sorry there is not enough {result.lower()}.")
            continue
        money = 0
        print("Please insert coins.")
        try:
            money += int(input("How many quarters? ")) * 0.25
            money += int(input("How many dimes? ")) * 0.1
            money += int(input("How many nickles? ")) * 0.05
            money += int(input("How many pennies? ")) * 0.01
        except ValueError:
            print("Enter numbers only!")
            exit(1)
        
        if money >= MENU[cmd]['Money']:
            money = getOrder(MENU[cmd], money)
            print(f"Here is ${round(money,2)} in change.")
            print(f"Here is your {cmd}. Enjoy! ^_^")
        else:
            print("Sorry that's not enough money. Money refunded.")

    else:
        print("Enter one of those drinks (espresso / latte / cappuccino) or 'report' if you want.")
        exit(1)
