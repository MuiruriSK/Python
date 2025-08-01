# Clear the console
from os import system, name
def clear():
    if system('cls' if name == 'nt' else 'clear') != 0:
        print("\n" * 100)

# Secret Auction Program
from art import logo
print(logo)

bids = {}
bids_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bids_finished:
    name = input("What is your name?")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if should_continue == "no":
        bids_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
        print("Next bidder please!")
