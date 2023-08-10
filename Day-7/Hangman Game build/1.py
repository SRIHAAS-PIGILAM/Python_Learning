"""#Step 1 :

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
"""

# Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# print(f"Generate a random Word \n{chosen_word}")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter!! ").lower()
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for y in chosen_word:
    if y == guess:
        print("yes it is present")
    else:
        print("It is not present")
