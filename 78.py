# Write a Python Program to Calculate the Hypotenuse of a Right Angled Triangle.

from math import sqrt
print("Input Lenghts of Shorter Triangle Sides:")
a = float(input("A: "))
b = float(input("B: "))

c = sqrt(a**2 + b**2)
print("The Length of the Hypotenuse is",c)