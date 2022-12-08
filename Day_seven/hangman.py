import  random


word_list = ['ardvark', 'baboon', 'camel']
choosen_word = random.choice(word_list)
print('The choosen word is ' +choosen_word)

word_lenght = len(word_list)
display = []
live = 6
for _ in range(word_lenght):
    display += '_ '
    #

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    for position in range(word_lenght):
        letter = choosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter : {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
    if "_ " not in display:
        end_of_game = True