import os

# ascii art
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

print("Welcome to My secret auction program.")

dic = {}
while True:
    name = input("What is your name? ")
    try:
        bid = int(input("What is your bid? $"))
    except ValueError:
        print("Type bid as numbers only!")
        exit(1)
    dic[name] = bid
    cont = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    if cont != 'yes':
        break

winner = sorted(dic.items(), key = lambda item: item[1], reverse = True)[0]
print(f"The winner is {winner[0]} with a bid of ${winner[1]}. ^_^")
