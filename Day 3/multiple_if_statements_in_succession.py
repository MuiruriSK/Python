print("Welcome to the rollercoaster!")
height = (float(input("What is your height in cm?")))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5 
        print("Please pay 5$ for the ride.")
    elif age >= 12:
        bill = 8
        print("Please pay 8$ for the ride.")  
    elif age >= 18:
        bill = 12
        print("Please pay 12$ for the ride.") 
    # Ask if the user wants a photo taken
    wants_photo = input('Do you want a photo taken? Y or N: ').upper()
    if wants_photo == "Y":
        bill += 3
    print("Your final bill is: $" + str(bill))
    
else:
    print("Sorry bud, you have to grow taller before you can ride.")
# This code checks if a person is tall enough to ride a rollercoaster.
# It prompts for the height in centimeters and compares it to the minimum height requirement.
# If the height is 120 cm or more, the person can ride; otherwise, they cannot.
# The code also checks the age of the person to determine the ride fee.
# Additionally, it asks if the user wants a photo taken, which adds to the total bill.