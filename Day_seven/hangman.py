import  random


word_list = ['ardvark', 'baboon', 'camel']
r = random.choice
choosen_word = random.choice(word_list)
print(choosen_word)
guess = input('Guess a letter: ').lower()
exist = ''
for i in choosen_word:
    exist = i
    if exist == guess:
        print('exist')
    else:
        print('lose')    