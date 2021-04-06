def game(attempts):
    import random

    number = random.randint(1,100)
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            num = int(input("Make a guess: "))
        except ValueError:
            print("Type numbers only!")
            exit(1)
        if num > number:
            print("Too high.\nGuess again.")
        elif num < number:
            print("Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {num}. ^_^")
            return
        attempts -= 1
    print("You've run out of guesses, you lose. ;_;")
    print(f"The number was {number}.")

print("Welcome to My Number Guessing game.")

# ascii art
print('''
''')

print("I'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if diff == 'easy': game(10)
elif diff == 'hard': game(5)
else:
    print("Type 'easy' or 'hard' only!")
    exit(1)

