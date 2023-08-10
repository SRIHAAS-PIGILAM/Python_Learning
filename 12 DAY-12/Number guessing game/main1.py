# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art
import os
# Clearing the Screen
os.system('cls')
print(art.logo)

print("Welcome to the Number Guessing game!\U0001F60E")
print("UMMMM!!!!! Thinking of a number between 1 and 100.!!!\U0001F971")

# generating a random number to guess
guess_number = random.randint(1, 101)
print(guess_number)
difficulty = input(
    f"Choose the difficulty level\U0001F914 , Type 'easy'  or 'hard' ").lower()
oho = ""
if difficulty == "easy":
    guess = 10
    print(
        f"You have {guess} attempts to guess the number correctly\U0001F920.")
    initial_guess = int(input("make a guess: "))

    while (guess != 0):
        if guess_number - initial_guess >= 10:
            print("Too High!!")
            print("guess again")
            guess -= 1
            print(
                f"You have {guess} attempts to guess the number correctly\U0001F920.")
            guess_again = int(input("guess:"))
            initial_guess = guess_again
            oho = "All guess are completed you lost!!!"
        elif 0 < guess_number - initial_guess < 10:
            print("too low")
            print("guess again")
            guess -= 1
            print(
                f"You have {guess} attempts to guess the number correctly\U0001F920.")
            guess_again = int(input("guess:"))
            initial_guess = guess_again
            oho = "All guess are completed you lost!!!"
        elif guess_number-initial_guess == 0:
            oho = "Hoorraahh!!! You guessed it correct"
            guess = 0
            art.lost = art.won

    print(f"Hahaa {oho}")
    print(art.lost)

else:
    guess = 5
    print(
        f"You have {guess} attempts remaining to guess the number correctly\U0001F62C")
    initial_guess = int(input("make a guess: "))

    while (guess != 0):
        if guess_number - initial_guess >= 5:
            print("Too High!!")
            print("guess again")
            guess -= 1
            print(
                f"You have {guess} attempts to guess the number correctly\U0001F920.")
            guess_again = int(input("guess:"))
            initial_guess = guess_again
            oho = "All guess are completed you lost!!!"
        elif 0 < guess_number - initial_guess < 5:
            print("too low")
            print("guess again")
            guess -= 1
            print(
                f"You have {guess} attempts to guess the number correctly\U0001F920.")
            guess_again = int(input("guess:"))
            initial_guess = guess_again
            oho = "All guess are completed you lost!!!"
        elif guess_number-initial_guess == 0:
            oho = "Hoorraahh!!! You guessed it correct"
            guess = 0
            art.lost = art.won

    print(f"{oho}")
    print(art.lost)


# initial_guess = int(input("make a guess: "))
# cant justify to both the levels by using just the below one after if and else block above,so we put the below code in both if and else block
"""
while (guess != 0):
    if guess_number - initial_guess >= 10:
        print("Too High!!")
        print("guess again")
        guess -= 1
        print(
            f"You have {guess} attempts to guess the number correctly\U0001F920.")
        guess_again = int(input("guess:"))
        initial_guess = guess_again
    elif 0 < guess_number - initial_guess < 10:
        print("too low")
        print("guess again")
        guess -= 1
        print(
            f"You have {guess} attempts to guess the number correctly\U0001F920.")
        guess_again = int(input("guess:"))
        initial_guess = guess_again
    elif guess_number-initial_guess == 0:
        print("Hoorraahh!!! You guessed it correct")
        guess = 0

print(guess_number)
"""
