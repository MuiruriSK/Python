import math

def paint_calc(height, width, cover):
    """Calculate the number of cans of paint needed to paint a wall."""
    area = height * width
    num_cans = math.ceil(area / cover)
    print(f"You will need {num_cans} cans of paint.")
test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)