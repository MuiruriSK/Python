number = (int(input("Enter a number to check if it's odd or even:")))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")   
# This code checks if a number is odd or even and prints the result.
# It uses the modulus operator to determine if the number is divisible by 2.
# If the remainder is 0, it's even; otherwise, it's odd. 