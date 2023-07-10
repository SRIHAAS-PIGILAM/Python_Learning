# Life in Weeks
"""Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
# You have 12410 days, 1768 weeks, and 408 months left."""

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
k_age_left = 90-int(age)
Z_months = k_age_left*12
y_weeks = k_age_left*52
x_days = k_age_left*365
print(f"You have {x_days} days, {y_weeks} weeks, and {Z_months} months left.")
