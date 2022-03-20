# Write a Python Program which accepts the radius of a circle from the user and compute the area.
from math import pi
r = float(input ("Input the Radius of the Circle: "))
print("The Area of the Circle with Radius " + str(r) + " is: " + str(pi*r**2))