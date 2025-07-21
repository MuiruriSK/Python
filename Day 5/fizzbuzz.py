for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
# This code prints "Fizz" for multiples of 3, "Buzz" for multiples of 5,
# "FizzBuzz" for multiples of both 3 and 5, and the number itself if none of the conditions are met.
# The FizzBuzz problem is a common coding challenge used in interviews and assessments.
# It is often used to test a candidate's understanding of basic programming concepts, such as loops and conditionals.