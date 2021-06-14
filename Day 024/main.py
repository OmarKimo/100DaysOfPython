#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

starting_letter = open('Day 024/Input/Letters/starting_letter.txt', 'r').read()

with open('Day 024/Input/Names/invited_names.txt', 'r') as f:
    for name in f:
        name = name.strip()
        final_letter = starting_letter.replace('[name]', name)
        open(f'Day 024/Output/ReadyToSend/{name}.txt', 'w').write(final_letter)

