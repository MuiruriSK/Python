student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    # Converting each score from string to integer
    student_scores[n] = int(student_scores[n])
print(student_scores)  # Printing the list of student scores

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score  # Updating the highest score if the current score is greater
print(f"The highest score in the class is: {highest_score}")  # Printing the highest score
# The highest score is determined by iterating through the list of scores and comparing each score