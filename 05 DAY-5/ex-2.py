# High Score
"""You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91"""

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])  # type: ignore
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
highest_score = student_scores[0]
for x in student_scores:
    if x > highest_score:
        highest_score = x
    else:
        continue

print(f"The highest score in the class is: {highest_score}")

# for lowest in the class
"""
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = student_scores[0]
for x in student_scores:
    if highest_score > x :
        highest_score = x
    else:
        continue

print(f"The highest score in the class is: {highest_score}")
"""
