import random

names_string = input("Give me everybody's names seperated by a comma.")
names = names_string.split(",")

num_items = len(names)
random.randint(0, num_items - 1)
random_choice = random.choice(names)

print(f"{random_choice} is going to buy the meal today!")