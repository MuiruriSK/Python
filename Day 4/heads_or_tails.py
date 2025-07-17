#simple coin toss 1
import random
random_side = random.randint(0, 1)
if random_side == 0:
    print("Heads")
else:
    print("Tails")
         
#simple coin toss 2
import random
random_side = random.choice(['Heads', 'Tails'])
print(f"The coin landed on: {random_side}")

# simple coin toss with reproducibility
random.seed(42)  # Setting a seed for reproducibility
random_side = random.choice(['Heads', 'Tails'])
print(f"The coin landed on: {random_side}")
# The output will be consistent across runs due to the fixed seed

# simple coin toss with a loop
import random
for _ in range(5):  # Toss the coin 5 times
    random_side = random.choice(['Heads', 'Tails'])
    print(f"The coin landed on: {random_side}")

# simple coin toss with a loop and reproducibility
import random
random.seed(42)  # Setting a seed for reproducibility
for _ in range(5):  # Toss the coin 5 times
    random_side = random.choice(['Heads', 'Tails'])
    print(f"The coin landed on: {random_side}")