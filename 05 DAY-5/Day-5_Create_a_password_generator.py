# Day 5 Project: Create a Password Generator
# https://replit.com/@appbrewery/password-generator-start?v=1
"""Coding Rooms is very handy for our exercises. However, the end-of-day projects are more free-form. You can experiment and play with this project. Customize it. Get as creative as you like. There is no exact output for you to match. There are no tests for you to pass. These assignments are not graded."""


# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy Level - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""
for i in range(1, nr_letters+1):
    random_char = random.choice(letters)
    easy_password += random_char

for i in range(1, nr_symbols+1):
    random_char = random.choice(numbers)
    easy_password += random_char

for i in range(1, nr_numbers+1):
    random_char = random.choice(symbols)
    easy_password += random_char


print(f"Easy password is {easy_password}")


# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = []
for i in range(1, nr_letters+1):
    random_char = random.choice(letters)
    hard_password += random_char

for i in range(1, nr_symbols+1):
    random_char = random.choice(numbers)
    hard_password += random_char

for i in range(1, nr_numbers+1):
    random_char = random.choice(symbols)
    hard_password += random_char


# print(hard_password)
random.shuffle(hard_password)
# print(hard_password)

password = ""
for char in hard_password:
    password += char

print(f"Hard password is {password}")
