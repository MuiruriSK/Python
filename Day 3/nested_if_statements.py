print("Welcome to the rollercoaster!")
height = (float(input("What is your height in cm?")))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay 5$ for the ride.")
    elif age >= 12:
        print("Please pay 8$ for the ride.")  
    elif age >= 18:
        print("Please pay 12$ for the ride.")    
else:
    print("Sorry bud, you have to grow taller before you can ride.")