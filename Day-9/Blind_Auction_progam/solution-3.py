import art
import os
# Clearing the Screen
os.system('cls')

print(art.logo)
print("Welcome to the Blind Auction program!!!")

# Create an empty dictionary to store bids
bids = {}

# Function to find the highest bidder


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Collect bids


def collect_bids():
    while True:
        name = input("Please tell us your name: ")
        bid_price = int(input("What's your bid: $"))
        bids[name] = bid_price
        os.system('cls')
        more_bidders = input(
            "Are there any other bidders? Type 'yes' or 'no': ").lower()
        if more_bidders != "yes":
            break


# Execute the auction:
collect_bids()
print(bids)
find_highest_bidder(bids)
