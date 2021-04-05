letters = "abcdefghijklmnopqrstuvwxyz"
LETTERS = letters.upper()

def caesar(msg, shift, direction):
    shift %= len(letters)
    rmsg = ""
    for let in msg:
        if not let.isalpha():
            rmsg += let
        # small
        elif let >= 'a':
            rmsg += letters[(letters.index(let) + direction*shift + len(letters))%len(letters)]
        # capital
        else:
            rmsg += LETTERS[(LETTERS.index(let) + direction*shift + len(letters))%len(letters)]
    return rmsg

# ascii art
print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')


while True:
    cmd = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()

    if cmd == 'encode':
        msg = input("Type your message: \n")
        try:
            shift = int(input("Type the shift number: \n"))
        except ValueError:
            print("Type the shift as numbers only!")
            exit(1)

        print(f"Here's the encoded result: {caesar(msg, shift, 1)}")

    elif cmd == 'decode':
        msg = input("Type your message: \n")
        try:
            shift = int(input("Type the shift number: \n"))
        except ValueError:
            print("Type the shift as numbers only!")
            exit(1)

        print(f"Here's the decoded result: {caesar(msg, shift, -1)}")

    else:
        print("Type 'encode' or 'decode' only!")
        exit(1)

    cont = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if cont != 'yes':
        break

print("Goodbye. ^_^")