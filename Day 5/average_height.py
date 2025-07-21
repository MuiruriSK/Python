student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    # Converting each height from string to integer
    student_heights[n] = int(student_heights[n])
print(student_heights)  # Printing the list of student heights 

total_height = 0
for height in student_heights:
    total_height += height
average_height = round(total_height / len(student_heights))
print(average_height)
# Printing the average height of the students
# The average height is calculated by summing all heights and dividing by the number of students
print(f"The average height is: {average_height}")