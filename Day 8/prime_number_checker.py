
def prime_checker(number):
    for i in range(2, number):
        is_prime = True
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

number = int(input("Check this number: "))
prime_checker(number)