import random

choices = [
# Rock
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
# Paper
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
# Scissors
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

print("Welcome to My Rock, Paper, Scissors game.")

try:
    chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
except ValueError:
    print("Type 0, 1 or 2 only!")
    exit(1)

if chose in [0,1,2]:
    print("You chose:")
    print(choices[chose])
    print("Computer chose:")
    cchose = random.choice([0,1,2])
    print(choices[cchose])
    if chose == cchose:
        print("It's a draw. -_-")
    elif chose-1 == cchose or chose == cchose%2:
        print("Congratulations. You win. ^_^")
    else:
        print("You lose. ;_;")
else:
    print("Type 0, 1 or 2 only!")
    exit(1)