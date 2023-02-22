from art import logo, vs
from game_data import data
import random

def format_account(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    #account_followers = account['followers']
    result = f"{account_name}, {account_description}, from {account_country}"
    return result

def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower and guess == 'a':
        return guess == "a"
    else:
        return guess == "b"    

        
is_game_over = False
score = 0
while not is_game_over:
    print(logo)

    account_a = random.choice(data)
    account_b = random.choice(data)
    

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")
    users_guess = input("Who has more followers, type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(users_guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right, current score: {score}")
    else:
        is_game_over = True
        print(f"Sorry, that's incorrect, final score: {score}")

