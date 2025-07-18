# using random.choice to select a random name from a list
import random
names_string = input("Give me everybody's names separated by a comma: ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.choice(names)
print(f"{random_choice} is going to buy the meal today!")