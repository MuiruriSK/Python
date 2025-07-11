year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
# This code checks if a given year is a leap year.
# A year is a leap year if it is divisible by 4, but not divisible by
# 100, unless it is also divisible by 400.
# It uses nested if statements to determine the leap year status and prints the result.        