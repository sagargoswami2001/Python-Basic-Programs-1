# Write a Python Program to Sort Three Integers Without Using Conditional Statements and Loops.

x = int(input("Input First Number: "))
y = int(input("Input Second Number: "))
z = int(input("Input Third Number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in Sorted Order: ",a1,a2,a3)