import random
import os
from data import data

def printData(dic):
    return f"{dic['name']}, {'an' if dic['description'][0] in ['a', 'e', 'o', 'i', 'u', 'y'] else 'a'} \
{dic['description']}, from {dic['country']}."

# ascii art
logo = '''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/   
'''
vsart = '''
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
'''


cnt = 0
c2 = None
over = False
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    if over:
        print(f"Sorry, that's wrong. Final score: {cnt}")
        break
    elif c2:
        print(f"You're right! Current score: {cnt}")
    c1 = c2
    if not c1:
        c1 = random.choice(data)
    c2 = random.choice(list(filter(lambda k : k != c1, data)))
    print(f"Compare A: {printData(c1)}")
    print(vsart)
    print(f"Against B: {printData(c2)}")
    ans = input("Who has more followers? Type 'A' or 'B': ").upper()
    if ans == "A":
        if c1['follower_count'] > c2['follower_count']:
            cnt += 1
        else:
            over = True
    elif ans == "B":
        if c1['follower_count'] < c2['follower_count']:
            cnt += 1
        else:
            over = True
    else:
        print("Type 'A' or 'B' only!")
        exit(1)
