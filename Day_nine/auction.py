logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidders in bidding_record:
        bid_amount = bidding_record[bidders]
        if int(bid_amount) > highest_bid:
            highest_bid = bid_amount
            winner = bidders

    print(f"The winner is {winner} with the bid amount of {highest_bid}")        






while not bidding_finished:
    name = input("What is your name? ")
    bidding_price = int(input("What is your bidding price? $"))

    bids[name] = bidding_price

    should_continue  = input('Are there other bidders? type "yes" or "no" ').lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # clear the screen 
        print("on to the next")
