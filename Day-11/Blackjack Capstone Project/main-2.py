# BLACKJACK CAPSTONE PROJECT
############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import os
import random
import art

# Clearing the Screen
os.system('cls')
choice_by_player1 = "y"

i, j, k, l, list1, list2, player_score, computer_score = 0, 0, 0, 0, [], [], 0, 0


def deck_cards():
    global cards, i, j, k, l, list1, list2, player_score, computer_score
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    i = random.choice(cards)
    j = random.choice(cards)
    list1 = [i, j]
    player_score = sum(list1)
    print(f"Your cards: {list1}, current score: {player_score}")
    k = random.choice(cards)
    l = random.choice(cards)
    list2 = [k, l]
    computer_score = sum(list2)
    print(f"Computer's first card is: {list2[0]}")
    if (list1[0] == 11 or list1[1] == 11) and (list1[0] == 10 or list1[1] == 10):
        print("You won!!")
        choice_by_player1 = "n"
    elif (list2[0] == 11 or list2[1] == 11) and (list2[0] == 10 or list2[1] == 10):
        print("You lost!!")
        choice_by_player1 = "n"
    else:
        print("\n")


game_start = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()

if game_start == "y":
    while choice_by_player1 == "y":
        os.system('cls')
        print(art.logo)

        deck_cards()

        if player_score > 21:
            for x in list1:
                if x == 11:
                    x = 1
                    player_score = player_score - x
                    if player_score > 21:
                        print("You lost")
                        choice_by_player1 = "n"
                else:
                    print("Yo lost!@")
                    choice_by_player1 = "n"
        else:
            print("")

        choice_by_player = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice_by_player == "y":
            player_score = sum(list1)
            while player_score < 17:
                extra_cards = random.choice(cards)
                list1.append(extra_cards)
                player_score = sum(list1)

            print(f"Your final hand: {list1}, final score is {player_score}")
            computer_score = sum(list2)
            print(
                f"Computer final hand: {list2}, final score is {computer_score}")

            if player_score > 21:
                print("You lost")
            elif computer_score < player_score < 21:
                print("You win!!")
            elif player_score < computer_score < 21:
                print("You lost!!@")
            elif computer_score == player_score:
                print("Draw!!")
            elif computer_score > 21:
                print("You Won!!")

        else:
            player_score = sum(list1)
            print(f"Your final hand: {list1}, final score is {player_score}")
            computer_score = sum(list2)
            while computer_score < 17:
                extra_cards = random.choice(cards)
                list2.append(extra_cards)
                computer_score = sum(list2)
            print(
                f"Computer final hand: {list2}, final score is {computer_score}")

            if player_score > 21:
                print("You lost")
            elif computer_score < player_score < 21:
                print("You win!!")
            elif player_score < computer_score < 21:
                print("You lost!!@")
            elif computer_score == player_score:
                print("Draw!!")
            elif computer_score > 21:
                print("You Won!!")

        choice_by_player1 = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()

    os.system('cls')
    print(art.logo)
    print("Have a good day, come back later!!!")
else:
    print("Have a good day, come back later!!!")
