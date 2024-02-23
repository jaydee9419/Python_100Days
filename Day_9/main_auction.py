import os

print("Welcome to Bid")

bids = {}

def clear_console():
    os.system('cls')

def find_heighest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and bid amount is ₹{highest_bid}.")
    

bidding_finished = False
while not bidding_finished:
    name = input("What is your name:")
    price = int(input("What is your bid?: ₹"))
    bids[name] = price
    
    should_continue = input("Are there any other bidders? (Yes/No)")
    if should_continue == 'no':
        bidding_finished = True
        clear_console()
        find_heighest_bidder(bids)
    elif should_continue == 'yes':
        clear_console()