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


# Code Starting

import art  # importing art
import os  # importing os module
import random  # importing random module

# Clearing the Screen
os.system('cls')
game_start = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()
# Initialize variables
choice_by_player1 = "y"
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
i, j, k, l, list1, list2, player_score, computer_score = 0, 0, 0, 0, [], [], 0, 0

# 1.Generates two random cards , 2.Finds the users and computers total score


def deck_cards():
    global i, j, k, l, list1, list2, player_score, computer_score, cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # 2 random cards choose for user
    i = random.choice(cards)
    j = random.choice(cards)
    list1 = [i, j]
    player_score = sum(list1)  # player score after selection of 2 cards
    print(f"Your cards: {list1}, current score: {player_score}")
    # 2 random cards choose for computer
    k = random.choice(cards)
    l = random.choice(cards)
    list2 = [k, l]
    # computer score after selection of computer cards
    computer_score = sum(list2)
    # only one card is shown and the other is hidden according to the game rules
    print(f"Computer's first card is : {list2[0]}")

    # Checks whether the drawn random cards has an ace or not
    if (list1[0] == 11 or list1[1] == 11) and (list1[0] == 10 or list1[1] == 10):
        print("You won!!\U0001F60A")
        choice_by_player1 = "n"
    elif (list2[0] == 11 or list2[1] == 11) and (list2[0] == 10 or list2[1] == 10):
        print("You lost!!\U0001F622")
        choice_by_player1 = "n"
    else:
        print("")


if game_start == "y":  # game start
    while choice_by_player1 == "y":
        # Clearing the Screen
        os.system('cls')
        print(art.logo)  # displaying the logo

        deck_cards()  # Function call

# checks if users score is over 21 or not
        if player_score > 21:  # if greater than 21
            for x in list1:  # checks whether it has a ace or not
                if x == 11:  # if present
                    x = 1  # value changed to one and checked if the score is still greater than 21 or not
                    player_score = player_score - x
                    if player_score > 21:  # if greater then the player is lost or else the loop is exited and continues further below code from choice_by_player
                        print("You lost\U0001F622")
                        choice_by_player1 = "n"  # flag for while loop
                else:  # if not present user is declared as lost
                    print("You lost!@\U0001F44E")
                    choice_by_player1 = "n"
        else:
            print("")  # continues further below code after this condition execution

        choice_by_player = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()  # if wanted to draw another card
        if choice_by_player == "y":  # if wanted to draw
            player_score = sum(list1)
            while player_score < 17:
                extra_cards = random.choice(cards)
                list1.append(extra_cards)
                player_score = sum(list1)

            print(f"Your final hand: {list1}, final score is {player_score}")
            computer_score = sum(list2)
            print(
                f"Computer final hand: {list2}, final score is {computer_score}")

# Comparing the users and computers score and declaring the winner
            if player_score > 21:
                print("You lost\U0001F622")
            elif computer_score < player_score < 21:
                print("You win!!\U0001F525")
            elif player_score < computer_score < 21:
                print("You lost!!@\U0001F44E")
            elif computer_score == player_score:
                print("Draw!!")
            elif computer_score > 21:
                print("You Won!!\U0001F525")

        # if don't want to draw an another card , below code block is executed
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

# Comparing the users and computers score and declaring the winner
            if player_score > 21:
                print("You lost\U0001F622")
            elif computer_score < player_score < 21:
                print("You win!!\U0001F525")
            elif player_score < computer_score < 21:
                print("You lost!!@\U0001F44E")
            elif computer_score == player_score:
                print("Draw!!")
            elif computer_score > 21:
                print("You Won!!\U0001F44D")

        # Want to play the game again
        choice_by_player1 = input(
            "do you want to play a game of blackjack? Type 'y' or 'n' : ").lower()  # Exit of while loop

    # Out of while loop

    # Clearing the Screen
    os.system('cls')
    print(art.logo)
    print("Have a good day, comeback later!!!\U0001F44D")
else:
    print("Have a good day, comeback later!!!\U00002615")  # game end

# Code end
