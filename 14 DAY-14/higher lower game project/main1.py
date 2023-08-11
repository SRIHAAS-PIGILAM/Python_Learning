# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
# Get follower count.
# If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.

import random
import os
import art
import game_data

# clearing screen
os.system('cls')

print(art.logo)
print(f"Welcome to the number guessing game!!!!\U0001F60E")

score = 0
flag = 0

# Generating data from random account
a = random.choice(game_data.data)
# print(a)
b = random.choice(game_data.data)
# print(b)

while flag == 0:
    a = b
    b = random.choice(game_data.data)
    """
    FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

    Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)"""

    while a == b:
        b = random.choice(game_data.data)

    # print(f'{name}: {account["follower_count"]}')
    print(
        f"Compare A \U0001F9D0: {a.get('name')}, {a.get('description')}, {a.get('country')}  ")

    print(art.vs)

    print(
        f"Against B \U0001F916: {b.get('name')}, {b.get('description')}, {b.get('country')}  ")

    guess = input(
        f"Who has more followers\U0001F914? Type 'A' or 'B'\U0001F920 : ").upper()

    """Checks followers against user's guess and returns True if they got it right.
        Or False if they got it wrong."""

    if {a.get('follower_count')} > {b.get('follower_count')}:
        guess = True
    else:
        guess = False

    # clearing the screen
    os.system('cls')

    # Printing the logo
    print(art.logo)

    # validating the score
    if guess:
        score += 1
        print(f"You're right! Current score\U0001F973 : {score}.")
    else:
        flag = 1
        print(f"Sorry, that's wrong \U0001F613. Final score : {score}")


"""
    if guess == "A":
        if {a.get('follower_count')} > {b.get('follower_count')}:
            score += 1
        else:
            score = 0
"""
