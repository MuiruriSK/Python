States_of_America = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                        "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
                        "Virginia", "New York", "North Carolina", "Rhode Island",
                        "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
                        "Indiana", "Mississippi", "Illinois", "Alabama", "Maine"]


print(States_of_America[9])  # Accessing the 10th state (index 9)
print(States_of_America[-1])  # Accessing the last state
print(States_of_America[0:5])  # Slicing the first 5 states
print(States_of_America[5:10])  # Slicing states from index 5 to 9
print(States_of_America[5:])  # Slicing from index 5 to the end
print(States_of_America[:5])  # Slicing from the start to index 4
print(States_of_America[-5:])  # Slicing the last 5 states
print(States_of_America[::2])  # Slicing every second state
print(States_of_America[::-1])  # Reversing the list
print(States_of_America[-1::-1])  # Reversing the list using negative indexing
print(States_of_America[-1:0:-1])  # Reversing the list from the last to the first state
print(States_of_America[-1:0:-2])  # Reversing the list with a step of 2
print(States_of_America[-1:0:-3])  # Reversing the list with a step of 3
print(States_of_America[-1:0:-4])  # Reversing the list with a step of 4
print(States_of_America[-1:0:-5])  # Reversing the list with a step of 5
print(States_of_America[-1:0:-6])  # Reversing the list with a step of 6
print(States_of_America[-1:0:-7])  # Reversing the list with a step of 7
print(States_of_America[-1:0:-8])  # Reversing the list with a step of 8
print(States_of_America[-1:0:-9])  # Reversing the list with a step of 9
print(States_of_America[-1:0:-10])  # Reversing the list with a step of 10
print(States_of_America[-1:0:-11])  # Reversing the list with a step of 11

States_of_America[2] = "Pencilvania"  # Changing the third state to "Pencilvania"

# Adding a new state to the list
States_of_America.append("California")
# Removing a state from the list
States_of_America.remove("Georgia")
# Inserting a state at a specific position
States_of_America.insert(3, "Florida")
print(States_of_America)  # Printing the modified list
print (f"Total number of states: {len(States_of_America)}")  # Printing the total number of states