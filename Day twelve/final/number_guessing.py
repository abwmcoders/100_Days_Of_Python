logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)
import random

print("Welcome to number guessing game !!!")
print("I'm thinking of a number between 1 to 100")
level = input("Choose a difficulty level: type 'easy' or 'hard' ").lower()
guess_limit = 5
number = random.choice(range(0, 101))
is_game_over = False



if level == 'easy':
    guess_limit = 10
    print(f"You have {guess_limit} attempts remaining to guess the number")
    guessed_number = int(input("Make a guess: "))
    while not is_game_over:
        guess_limit -= 1
        if guess_limit == 0:
            is_game_over = True
            print("You have run out of guesses, You lose")
        elif guessed_number > number:
            print("Too high")
            print(
                f"You have {guess_limit} attempts remaining to guess the number")
            guessed_number = int(input("Guess again: "))
        elif guessed_number < number:
            print("Too low")
            print(f"You have {guess_limit} attempts remaining to guess the number")
            guessed_number = int(input("Guess again: "))
        elif guessed_number == number:
            print("You win")   
            is_game_over = True  
else:
    guess_limit = 5
    print(f"You have {guess_limit} attempts remaining to guess the number")
    guessed_number = int(input("Make a guess: "))
    while not is_game_over:
        guess_limit -= 1
        if guess_limit == 0:
            is_game_over = True
        elif guessed_number > number:
            print("Too high")
            print(
                f"You have {guess_limit} attempts remaining to guess the number")
            guessed_number = int(input("Guess again: "))
        elif guessed_number < number:
            print("Too low")
            print(
                f"You have {guess_limit} attempts remaining to guess the number")
            guessed_number = int(input("Guess again: "))
        elif guessed_number == number:
            print("You win")
            is_game_over = True



