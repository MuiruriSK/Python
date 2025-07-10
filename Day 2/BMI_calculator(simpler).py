height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# height = float(height)
# weight = float(weight)
bmi = float(weight) / float(height) ** 2
print("Your BMI is: " + str(bmi))
# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"
print("You are classified as: " + category)
# This code calculates the Body Mass Index
#  (BMI) based on user input for weight and height
# and categorizes the BMI into underweight, normal weight, overweight, or obesity.
# The BMI is calculated using the formula: weight (kg) / (height (m)
# ** 2).