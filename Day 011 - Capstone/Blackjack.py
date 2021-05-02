import random
import os 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    # ascii art
    print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
''')
    
    user_cards = random.choices(cards, k = 2)
    com_cards = random.choices(cards, k = 2)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {com_cards[0]}")
    while input("Type 'y' to get another card, or 'n' to pass: ").lower() == 'y': 
        user_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {com_cards[0]}")
        if sum(user_cards) > 21:
            break
    while sum(com_cards) < 17:
        com_cards.append(random.choice(cards))
    
    s1 = sum(user_cards)
    s2 = sum(com_cards)
    print(f"Your final hand: {user_cards}, final score: {s1}")
    print(f"Computer's final hand: {com_cards}, final score: {s2}")
    
    if s1 > 21:
        print("You went over. You lose. ;_;")
    elif s1 == s2:
        print("It's a draw. -_-")
    elif s1 < s2:
        print("You lose. ;_;")
    else:
        print("You win. ^_^")
    
print("Goodbye.")