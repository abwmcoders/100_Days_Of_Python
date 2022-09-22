import random
print('Welcome to our rock paper scissors game')

player_choice = int(input('please select your choice, 0 for rock, 1 for paper, 2 for scissors: '))
computer_choice = random.randint(0, 2)
print(player_choice)
print(computer_choice)
if player_choice == computer_choice:
    print('Its a tie')
elif player_choice == 0:
    if computer_choice == 1:
        print('Paper covers rock, you lose')   
    else:
        print('Rock smashes scissors, you win')  
elif player_choice == 1:
    if computer_choice == 0:
        print('paper covers rock, you win')  
    else:
        print('Scissors cuts paper, you lose')
elif player_choice == 2:
    if computer_choice == 0:
        print('rock smashes scissors, you lose')
    else:
        print('Scissors cuts paper, you win')                         