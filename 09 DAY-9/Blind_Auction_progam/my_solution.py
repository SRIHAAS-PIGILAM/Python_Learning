# Blind Auction
# The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

import art
import os
# Clearing the Screen
os.system('cls')
# HINT: You can call clear() to clear the output in the consle
# Import logo and print it
print(art.logo)
print("Welcome to Blind Auction program!!!")

# ask for Name input
Name = input("Please Tell your name: ")

# Ask for Bid price:
bid_price = int(input("What's your bid: $"))

# add Name and Bid into a dictionary as the key and value
dict = {}
dict[Name] = bid_price

# Ask if there are other users who want to bid:
any_bidders = input(
    'Are there any other bidders??? Type "yes" or "no" ').lower()
while any_bidders == "yes":
    # Clearing the Screen
    os.system('cls')
    # ask for Name input
    Name = input("Please Tell your name: ").upper()

    # Ask for Bid price
    bid_price = int(input("What's your bid: $"))

    # add Name and Bid into a dictionary as the key and value
    dict[Name] = bid_price
    # Ask if there are other users who want to bid
    any_bidders = input(
        'Are there any other bidders??? Type "yes" or "no" ').lower()

print(dict)

# find the highest bid in the dictionary and declare them as the winner
highest_bid = 0
winner = ""
for x in dict:
    bidder_amount = dict[x]
    if bidder_amount > highest_bid:
        highest_bid = bidder_amount
        winner = x

# Clearing the Screen:
os.system('cls')
print(art.logo)
print(f"The winner is {winner} with a bid of ${highest_bid}")
