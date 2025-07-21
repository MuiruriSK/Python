for number in range(1, 10):
    print(number)  # Printing numbers from 1 to 9
    print(number * 2)  # Printing double of each number

# We can specify a step in the range function
for number in range(1, 10, 2):
    print(number)  # Printing odd numbers from 1 to 9
    print(number * 2)  # Printing double of each odd number

# Using range to iterate through a list
numbers = [10, 20, 30, 40, 50]
for index in range(len(numbers)):
    print(f"Index: {index}, Value: {numbers[index]}")  # Printing index and value of each element in the list
    print(numbers[index] + 5)  # Adding 5 to each number in the list

# Adding numbers from 1 to 100 using a for loop
total = 0
for number in range(1, 101):
    total += number  # Summing numbers from 1 to 100
print(f"Total sum from 1 to 100 is: {total}")  # Printing

# Adding even numbers from 1 to 100
even_total = 0
for number in range(2, 101, 2):
    even_total += number  # Summing even numbers from 1 to 100
print(f"Total sum of even numbers from 1 to 100 is: {even_total}")

# Adding even numbers using modulus operator
even_total = 0
for number in range(1, 101):
    if number % 2 == 0:
        even_total += number  # Summing even numbers from 1 to 100
print(f"Total sum of even numbers from 1 to 100 using modulus is: {even_total}")
(f"Total sum of even numbers from 1 to 100 is: {even_total}")  # Printing the total sum of even numbers
# The total is calculated by iterating through the range and summing each number
