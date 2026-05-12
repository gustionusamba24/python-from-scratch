"""
    Calculate the area of rectangle, and the add it to the new variable
"""

rectangles = [
    {"height": 4, "width": 5,},
    {"height": 4, "width": 9,},
]

sum_of_all_area = 0
for rectangle in rectangles:
    area = rectangle["height"] * rectangle["width"]
    sum_of_all_area += area
print(sum_of_all_area)

