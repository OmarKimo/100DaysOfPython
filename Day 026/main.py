import pandas
alpha = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for _, row in alpha.iterrows()}

word = input("Enter a word: ")

while not word.isalpha():
    print("Sorry, only letters in the alphabet please.") 
    word = input("Enter a word: ")

print([nato_dict[char.upper()] for char in word])
