# Write a Python program to convert degree to radian 

#--------- 1st method --------------------------------

degree_value = 70
pi = 3.141592653589793
radians = degree_value * (pi / 180)

print(f"{degree_value} degrees is equal to {radians} radians.")


#------ 2nd Method -------------------------


import math

degree_value = 70
radians = math.radians(degree_value)

print(f"{degree_value} degrees is equal to {radians} radians.")
