
# ascii art
print('''
''')

while True:
    num1 = input("What's the first number? ")

    print("+\n-\n*\n/")
    while True:
        op = input("Pick an operation: ")
        if op not in ['*', '-', '+', '/']:
            print("Enter a valid operation! [* - / +]")
            exit(1)

        num2 = input("What's the next number? ")

        exp = f"{num1} {op} {num2}"
        try:
            num1 = eval(exp)
        except TypeError:
            print("Type valid operands, numbers only!")
            
        print(f"{exp} = {num1}")

        cont = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation: ")
        if cont != 'y':
            break
