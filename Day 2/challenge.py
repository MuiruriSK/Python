# This code takes a two-digit number as input, extracts the first and second digits,
# converts them to integers, and then calculates the sum of these two digits.
# It then prints the result in a formatted string.
two_digit_number = input("Enter a two-digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print("The sum of the digits is: " +  str(result))
# Output: The sum of the digits is: X (where X is the sum of the
# two digits entered by the user)
# Example input: 34
# Example output: The sum of the digits is: 7
# Output: The sum of the digits is: 7