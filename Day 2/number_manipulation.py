score = 0
score += 1
print("Your score is: " + str(score))
# round_function
print(round(8 / 3, 2))  # Output: 2.67
# round_function with negative digits
print(round(-8 / 3, 2))  # Output: -2.67
# round_function with no digits
print(round(8 / 3))  # Output: 3
# round_function with negative no digits
print(round(-8 / 3))  # Output: -3
# round_function with no digits and negative value
print(round(-8 / 3, 0))  # Output: -3.0
# round_function with no digits and positive value
print(round(8 / 3, 0))  # Output: 3.0
# round_function with no digits and negative value
print(round(-8 / 3, 0))  # Output: -3.0
# round_function with no digits and positive value

#f-Strings
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")  # Output: Hello, my name is Alice and I am 30 years old.
# f-Strings with expressions
print(f"In 5 years, I will be {age + 5} years old.")
score = 0
height = 1.75
isWinning = True
print(f"Score: {score}, Height: {height}, Winning: {isWinning}")  # Output: Score: 0, Height: 1.75, Winning: True