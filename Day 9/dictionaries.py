programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A block of code that performs a specific task.",
}
# Retrieving items from the dictionary
print(programming_dictionary["Bug"])

# Adding new items to the dictionary
programming_dictionary["Loop"] = "A construct that allows code to be executed repeatedly."

print(programming_dictionary)

# Adding more items to the dictionary
programming_dictionary["Conditional"] = "A statement  that executes code based on a condition." 
print(programming_dictionary)

# Creating an empty dictionary
empty_dictionary = {}

# Wiping an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Editing an item in the dictionary
programming_dictionary["Bug"] = "A moth or other insect found in the computer."
print(programming_dictionary)

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])