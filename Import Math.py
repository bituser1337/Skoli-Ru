# calculate the area and circumference of a circle from its radius
# Step 1: prompt for a radius
# Step 2: apply the area formula
# Step 3: Prin out the result

import math 

radius_str = input("Enter the radius of your circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print ("the circumference is:",circumference, \
        ", and the area is :",area)
