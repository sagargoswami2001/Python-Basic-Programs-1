# Write a Python Program to Calculate Body Mass Index.

height = float(input("Input Your Height in Meters: "))
weight = float(input("Input Your Weight in Kilogram: "))
print("Your Body Mass Index is: ", round(weight / (height * height), 2))