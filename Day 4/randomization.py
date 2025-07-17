# simple randomization example
import random
random_integer = random.randint(1, 100)
print(random_integer)

random_float_number = random.random()
print(random_float_number)
random_float_multiplied = random.random() * 10
print(random_float_multiplied)

random_float = random.uniform(1.0, 10.0)
print(random_float)

random_choice = random.choice(['apple', 'banana', 'cherry'])
print(random_choice)

random_sample = random.sample(range(1, 100), 5)
print(random_sample)

random.shuffle(random_sample)
print(random_sample)

love_score = random.randint(1, 100)
print(f"Your love score is: {love_score}")


# simple randomization example with reproducibility
import random
random.seed(42)  # Setting a seed for reproducibility
random_integer = random.randint(1, 100)
print(random_integer)

random_float_number = random.random()
print(random_float_number)

random_float_multiplied = random.random() * 10
print(random_float_multiplied)

random_float = random.uniform(1.0, 10.0)
print(random_float)

random_choice = random.choice(['apple', 'banana', 'cherry'])
print(random_choice)

random_sample = random.sample(range(1, 100), 5)
print(random_sample)

random.shuffle(random_sample)
print(random_sample)
# The output will be consistent across runs due to the fixed seed
