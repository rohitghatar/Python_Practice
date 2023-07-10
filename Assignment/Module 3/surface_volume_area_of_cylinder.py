'''Write a Python program to calculate surface volume and area of a
cylinder '''

# Surface Area = 2 * π * r * (r + h)
# Volume = π * r^2 * h

#---------- 1st method ----------------------

radius = 3
height = 5

surface_area = 2 * 3.14159 * radius * (radius + height)
print("Surface Area of the cylinder:", surface_area)

volume = 3.14159 * radius ** 2 * height
print("Volume of the cylinder:", volume)


#--------- 2nd Method -------------------

import math

surface_area = 2 * math.pi * radius * (radius + height)
print("Surface Area of the cylinder:", surface_area)

volume = math.pi * radius ** 2 * height
print("Volume of the cylinder:", volume)
