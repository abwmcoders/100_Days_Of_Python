from art import logo
import os

print(logo)

clear = lambda: os.system('clear') 
bid_list = {}
def get_bid_member(member_name, price_tag):
    bid_list[member_name] = price_tag

should_continue = True

while should_continue:
    name = input("What's your name: ")
    bid_amount = int(input("What's your bid: $"))

    get_bid_member(member_name= name, price_tag= bid_amount)    

    print(bid_list)

    cont = input("Are there any other bidders, if yes type 'yes' else 'no': ").lower()

    

    if cont == 'no':
        highest_bid = 0
        should_continue = False
        for bid in bid_list:
            price_of_bid = bid_list[bid]
            if highest_bid < price_of_bid:
                highest_bid = price_of_bid
        print(f'The winner is {name} with ${highest_bid} bid')        
    else:
        clear()
            



