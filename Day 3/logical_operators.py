print("Welcome to the rollercoaster!")
height = (float(input("What is your height in cm?")))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5 
        print("Please pay 5$ for the ride.")  
    elif age <= 18:
        bill = 10
        print("Please pay 10$ for the ride.")
    elif age >=45 and age <=55:
        bill = 0
        print("You get a free ride due to your age!")
    else:
        bill = 15
        print("Please pay 15$ for the ride.") 
    # Ask if the user wants a photo taken
    wants_photo = input('Do you want a photo taken? Y or N: ').upper()
    if wants_photo == "Y":
        bill += 3
    print("Your final bill is: $" + str(bill))
    
else:
    print("Sorry bud, you have to grow taller before you can ride.")