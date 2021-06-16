import random
from hangman_words import stages, words

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')



word = random.choice(words)
gword = list('_ ' * len(word))
cnt = len(stages) - 1

while True:
    letter = input("Guess a letter: ").lower()
    if not letter.isalpha():
        print("Type a letter!")
        exit(1)

    if letter in gword:
        print(''.join(gword))
        print(f"You've already guessed {letter}")
        print(stages[cnt])
        
    elif letter in word:
        idx = word.find(letter)
        while idx != -1:
            gword[idx*2] = letter
            idx = word.find(letter, idx + 1)
        print(''.join(gword))
        if '_' not in gword:
            print("You win. ^_^")
            print(stages[cnt])
            break
        print(stages[cnt])
    else:
        print(''.join(gword))
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        cnt -= 1
        if not cnt:
            print("You lose. ;_;")
            print(stages[cnt])
            break
        print(stages[cnt])

