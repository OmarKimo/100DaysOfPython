print(r'''

                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

''')


print('Welcome to My Treasure Island. ^_^')
print('Your mission is to find the treasure.')

direction = input("You're at cross road. Where do you want to go? \
Type \"left\" or \"right\"\n").lower()

if direction == "left":
    cmd = input("You come to a lake. There is an island in the middle of the lake. \
Type \"wait\" to wait for a boat. \
Type \"swim\" to swim across.\n").lower()
    if cmd == "wait":
        color = input("You arrive at the island unharmed. \
There is a house with 3 doors. One red, one yellow and one blue. \
Which colour do you choose?\n").lower()
        if color == "yellow":
            print("Congratulations. You found the treasure. ^_^")
        elif color == "blue":
            print("You enter a room of beasts. Game over!")
        elif color == "red":
            print("You enter a room of devils. Game over!")
        else:
            print("Type \"red\", \"yellow\" or \"blue\" only!")
            exit(1)
    elif cmd == "swim":
        print("You are eaten by a great carp. Game over!")
    else:
        print("Type \"wait\" or \"swim\" only!")
        exit(1)
elif direction == "right":
    print("You fell into a hole. Game over!")
else:
    print("Type \"left\" or \"right\" only!")
    exit(1)

