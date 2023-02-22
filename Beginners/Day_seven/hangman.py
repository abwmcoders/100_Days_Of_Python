import  random
from words import word_list

# ARt

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)

#word_list = ["aardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)
word_lenght = len(choosen_word)
display = []
end_of_game = False
live = 6

for _ in range(word_lenght):
    display += '_'
print(display)

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f"You've already guess {guess}")


    for position in range(word_lenght):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in choosen_word:
        print("You've guess {guess} that's not in the world, you lose a life")
        live -=1
        if live == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")


    if '_' not in display:
        end_of_game = True
        print("You win.")


    print(stages[live])    
    
        


