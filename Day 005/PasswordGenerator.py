import random

sletters = "abcdefghijklmnopqrstuvwxyz"
cletters = sletters.upper()
letters = list(sletters + cletters)
numbers = list("0123456789")
symbols = list("*+!$%()#&")

try:
    nLetters = int(input("How many letters would you like in your password?\n"))
except ValueError:
    print("Enter a number!")
    exit(1)

try:
    nNumbers = int(input("How many numbers would you like?\n"))
except ValueError:
    print("Enter a number!")
    exit(1)

try:
    nSymbols = int(input("How many symbols would you like?\n"))
except ValueError:
    print("Enter a number!")
    exit(1)

password = random.choices(letters, k=nLetters) + \
            random.choices(numbers, k=nNumbers) + \
            random.choices(symbols, k=nSymbols)
random.shuffle(password)
print(f"Here is your password: {''.join(password)}")