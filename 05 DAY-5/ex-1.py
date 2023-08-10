# Average Height
"""You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

Example Output
171

You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

Example Output
171

Remember to use the round() function to round the average height before you print it.
"""
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  # type: ignore
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_height = 0
for x in student_heights:
    total_height += x  # type: ignore

# print(total_height)
total_students = 0
for z in student_heights:
    total_students += 1

# print(total_students)

average_height = round(total_height/total_students)
print(average_height)
