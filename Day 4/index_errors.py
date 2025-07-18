import lists
num_of_states = len(lists.States_of_America)
# print(lists.States_of_America[num_of_states])
# This code snippet is used to demonstrate how to access the last state in the list
# but it will raise an IndexError because the index is out of range.        
# Uncommenting the line below will raise an IndexError

# The correct way to access the last state is to use a negative index
print(lists.States_of_America[-1])  # This will correctly print the last state
# The above code demonstrates how to access the last element of a list using negative indexing.
