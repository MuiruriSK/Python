row1 = ["😂","😂","😂"]
row2 = ["😂","😂","😂"]
row3 = ["😂","😂","😂"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")  # Printing the initial map
position = input("Where do you want to put the treasure?")

row = int(position[0])
column = int(position[1])

print(map[row -1][column - 1])  # Printing the current value at the specified position
map[row - 1][column - 1] = "X"  # Marking the treasure position with "X"
print(f"{row1}\n{row2}\n{row3}")  # Printing the updated map with the treasure marked
