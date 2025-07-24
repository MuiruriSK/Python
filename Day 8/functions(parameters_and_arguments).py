def greet():
    print("Hello!")
    print("How are you today?")
    print("It's nice to meet you!")

greet()

# Functions that allow for parameters and arguments
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")

greet_with_name("Solomon")

# Functions with more than one parameter
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with("Solomon", "London")

# Functions with default/keyword parameters
def greet_with_default(name="User", location="Earth"):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with_default()