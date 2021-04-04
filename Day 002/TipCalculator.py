print("Welcome to My tip Calculator. ^_^")

try:
    bill = float(input("What's the total bill?\n$"))
except ValueError:
    print('Enter a number, please.')
    exit(ValueError)

try:
    tip = int(input('What percentage of tip would you like to give?\n'))
except ValueError:
    print('Enter a number, please.')
    exit(ValueError)


try:
    num = int(input('How many people to split the bill?\n'))
except ValueError:
    print('Enter a number, please.')
    exit(ValueError)

print(f"Each person should pay: ${round( ((1 + (tip/100)) * bill) / num, 2):.2f}")