# Rock Paper Scissors

# Write your code below this line 👇
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game_icons = [rock, paper, scissors]
print("Welcome!! To Rock Paper Scissors Game...$$\n\n")
print("Let us play the game!!..\n")
choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors  "))
if choice >= 3 or choice < 0:
    print("You type a invalid number!!!")
else:
    print(game_icons[choice])

    computer_choice = random.randint(0, 2)
    print(f"{computer_choice} is computer choice")
    print(game_icons[computer_choice])

    if choice == 0 and computer_choice == 2:
        print("You Won!")
    elif choice == 1 and computer_choice == 0:
        print("Yow Won!!")
    elif choice == 2 and computer_choice == 1:
        print("You Won!")
    elif choice == computer_choice:
        print("It's a draw!!")
    elif computer_choice > choice:
        print("You Loose!!!!")
    else:
        print("!!")
