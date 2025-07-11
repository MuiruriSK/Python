print("Welcome to the best Pizza delivery service!")
print("We have the following pizzas available:")
print("1. Margherita small - $8")
print("2. Margherita medium - $13")
print("3. Margherita large - $18")
print("4. Pepperoni small - $10")
print("5. Pepperoni medium - $15")
print("6. Pepperoni large - $20")
print("7. BBQ Chicken small - $12")
print("8. BBQ Chicken medium - $17")
print("9. BBQ Chicken large - $22")
pizza_choice = int(input("Please enter the number of your pizza choice: "))
if pizza_choice == 1:
    pizza_name = "Margherita small"
    pizza_price = 8
elif pizza_choice == 2:
    pizza_name = "Margherita medium"
    pizza_price = 13
elif pizza_choice == 3:
    pizza_name = "Margherita large"
    pizza_price = 18
elif pizza_choice == 4:
    pizza_name = "Pepperoni small"
    pizza_price = 10
elif pizza_choice == 5:
    pizza_name = "Pepperoni medium"
    pizza_price = 15
elif pizza_choice == 6:
    pizza_name = "Pepperoni large"
    pizza_price = 20
elif pizza_choice == 7:
    pizza_name = "BBQ Chicken small"
    pizza_price = 12
elif pizza_choice == 8:
    pizza_name = "BBQ Chicken medium"
    pizza_price = 17
elif pizza_choice == 9:
    pizza_name = "BBQ Chicken large"
    pizza_price = 22
else:
    print("Invalid choice. Please restart the program.")
    exit()
quantity = int(input(f"How many {pizza_name} pizzas would you like to order? "))
total_price = pizza_price * quantity
print(f"You have ordered {quantity} {pizza_name} pizza(s).")
print(f"Total price: ${total_price}")
delivery_address = input("Please enter your delivery address: ")
print(f"Your {pizza_name} pizza(s) will be delivered to {delivery_address}.")
print("Thank you for your order! Enjoy your pizza!")
# This code simulates a pizza delivery service.
# It allows the user to choose a pizza type, specify the quantity, and enter a delivery address.
# The total price is calculated based on the pizza type and quantity.
# The program then confirms the order and provides delivery details.
# It uses conditional statements to handle different pizza choices and validate user input.